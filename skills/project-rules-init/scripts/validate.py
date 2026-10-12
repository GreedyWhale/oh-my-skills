#!/usr/bin/env python3
"""Validate the package with isolated, independently bounded behavioral checks."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time


PACKAGE = Path(__file__).resolve().parents[1]
RUN_BUDGET = 60
COMMAND_BUDGET = 10
CLEANUP_BUDGET = 2


def invoke(root: Path, *options: str, package: Path = PACKAGE, expected: int = 0):
    result = subprocess.run(
        [sys.executable, "-I", str(package / "scripts/initialize.py"), "--root", str(root), *options],
        capture_output=True, text=True, timeout=COMMAND_BUDGET,
    )
    if result.returncode != expected:
        raise AssertionError(f"Expected exit {expected}, got {result.returncode}: {result.stdout}{result.stderr}")
    return result


def snapshot(root: Path) -> dict[str, bytes]:
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def check_links(path: Path, boundary: Path):
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if "://" in target:
            continue
        name, _, anchor = target.partition("#")
        resolved = (path.parent / name).resolve() if name else path.resolve()
        if not resolved.is_relative_to(boundary.resolve()) or not resolved.exists():
            raise AssertionError(f"Broken or escaping reference in {path}: {target}")
        if anchor:
            headings = re.findall(r"^#{1,6}\s+(.+)$", resolved.read_text(encoding="utf-8"), re.M)
            anchors = {re.sub(r"[^\w -]", "", h.lower()).replace(" ", "-") for h in headings}
            if anchor not in anchors:
                raise AssertionError(f"Missing heading in {path}: {target}")


def check_package(source_general: Path | None):
    release = json.loads((PACKAGE / "assets/release.json").read_text(encoding="utf-8"))
    for name, expected in release["sha256"].items():
        actual = hashlib.sha256((PACKAGE / "assets" / name).read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError(f"Stale release hash: {name}")
    if source_general and source_general.read_bytes() != (PACKAGE / "assets/project-rules.md").read_bytes():
        raise AssertionError("Packaged general rules differ from the supplied canonical source")
    skill = PACKAGE / "SKILL.md"
    body = skill.read_text(encoding="utf-8")
    if not body.startswith("---\nname: project-rules-init\ndescription:"):
        raise AssertionError("Skill frontmatter is missing or has the wrong identity")
    check_links(skill, PACKAGE)
    check_links(PACKAGE / "references/bindings.md", PACKAGE)
    print("PASS release integrity, skill references, and optional source comparison", flush=True)


def worker(source_general: Path | None):
    check_package(source_general)
    with tempfile.TemporaryDirectory(prefix="project-rules-validation-") as directory:
        base = Path(directory)
        fresh = base / "project with spaces"
        fresh.mkdir()
        invoke(fresh, "--dry-run")
        assert snapshot(fresh) == {}, "Dry run mutated the project"
        invoke(fresh)
        initial = snapshot(fresh)
        assert len(initial) == 5, initial.keys()
        assert initial["AGENTS.md"] == initial["CLAUDE.md"]
        for path in fresh.rglob("*.md"):
            check_links(path, fresh)
        print("PASS fresh non-Git project, paths with spaces, dry run, and generated links", flush=True)

        specific = fresh / "docs/engineering/project-specific-rules.md"
        specific.write_text(specific.read_text() + "\n## Local Constraint\n\nKeep the user's real constraint.\n")
        handover = fresh / "docs/project/handover.md"
        handover.write_text("# Existing State\n\nUser-owned unfinished work.\n")
        (fresh / "user-code.txt").write_text("untouched")
        before = snapshot(fresh)
        invoke(fresh)
        assert snapshot(fresh) == before, "Rerun overwrote customization or work state"
        print("PASS repeated initialization preserves project bindings, handover, and unrelated files", flush=True)

        for relative in ("AGENTS.md", "CLAUDE.md", "docs/engineering/project-rules.md", "docs/engineering/project-specific-rules.md"):
            conflict = base / ("conflict-" + relative.replace("/", "-"))
            destination = conflict / relative
            destination.parent.mkdir(parents=True)
            destination.write_text("# Existing rules\nDo not erase.\n")
            before = snapshot(conflict)
            invoke(conflict, expected=2)
            assert snapshot(conflict) == before, "Collision produced partial output"
        print("PASS conflicts preserve all original bytes and create no partial rule pair", flush=True)

        existing = base / "existing-handover"
        destination = existing / "docs/project/handover.md"
        destination.parent.mkdir(parents=True)
        destination.write_text("Preserved state")
        invoke(existing)
        assert destination.read_text() == "Preserved state"
        print("PASS first adoption preserves an existing handover", flush=True)

        outside = base / "outside"
        outside.mkdir()
        sentinel = outside / "sentinel.md"
        sentinel.write_text("keep")
        for index, relative in enumerate(("docs", "AGENTS.md", "CLAUDE.md")):
            linked = base / f"symlink-{index}"
            linked.mkdir()
            (linked / relative).symlink_to(outside if relative == "docs" else sentinel)
            invoke(linked, expected=2)
            assert not (linked / "docs/engineering/project-rules.md").exists()
            assert sentinel.read_text() == "keep"
        broken = base / "broken-symlink"
        broken.mkdir()
        (broken / "AGENTS.md").symlink_to(base / "missing-target")
        invoke(broken, expected=2)
        assert not (base / "missing-target").exists()
        print("PASS parent, file, and dangling symlinks cannot redirect writes", flush=True)

        obstructed = base / "file-parent"
        obstructed.mkdir()
        (obstructed / "docs").write_text("not a directory")
        invoke(obstructed, expected=2)
        assert snapshot(obstructed) == {"docs": b"not a directory"}
        invoke(base / "missing-root", expected=2)
        print("PASS invalid parent and missing project root fail without mutation", flush=True)

        damaged = base / "damaged-package"
        shutil.copytree(PACKAGE, damaged)
        (damaged / "assets/project-rules.md").write_text("unreviewed change")
        target = base / "damaged-target"
        target.mkdir()
        invoke(target, package=damaged, expected=2)
        assert snapshot(target) == {}, "Tampered release was installed"
        print("PASS altered release assets are rejected before writing", flush=True)


def terminate_group(process: subprocess.Popen):
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    deadline = time.monotonic() + CLEANUP_BUDGET
    while time.monotonic() < deadline:
        process.poll()
        try:
            os.killpg(process.pid, 0)
        except ProcessLookupError:
            return
        time.sleep(0.05)
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    try:
        process.wait(timeout=0.5)
    except subprocess.TimeoutExpired:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-general", type=Path)
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        worker(args.source_general)
        return 0
    if os.name != "posix":
        print("Validation needs a POSIX process-group supervisor; configure a host equivalent first.", file=sys.stderr)
        return 2
    command = [sys.executable, "-I", "-B", str(Path(__file__).resolve()), "--worker"]
    if args.source_general:
        command += ["--source-general", str(args.source_general.resolve())]
    started = time.monotonic()
    process = subprocess.Popen(command, start_new_session=True)

    def interrupted(_number, _frame):
        raise KeyboardInterrupt

    previous = signal.signal(signal.SIGTERM, interrupted)
    try:
        result = process.wait(timeout=RUN_BUDGET - CLEANUP_BUDGET - 0.5)
    except subprocess.TimeoutExpired:
        print("FAIL validation exceeded its 60-second total budget", file=sys.stderr)
        result = 124
    except KeyboardInterrupt:
        print("FAIL validation interrupted; cleaning up worker group", file=sys.stderr)
        result = 130
    finally:
        terminate_group(process)
        signal.signal(signal.SIGTERM, previous)
    print(f"Validation exit={result}; elapsed={time.monotonic() - started:.2f}s", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
