#!/usr/bin/env python3
"""Install a versioned rule scaffold without overwriting project content."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


PACKAGE = Path(__file__).resolve().parents[1]
OUTPUTS = {
    "docs/engineering/project-rules.md": "project-rules.md",
    "docs/engineering/project-specific-rules.md": "project-specific-rules.md",
    "docs/project/handover.md": "handover.md",
    "AGENTS.md": "entry.md",
    "CLAUDE.md": "entry.md",
}
CUSTOMIZABLE = {
    "docs/engineering/project-specific-rules.md",
    "docs/project/handover.md",
}


def load_assets() -> tuple[str, dict[str, bytes]]:
    assets = PACKAGE / "assets"
    release = json.loads((assets / "release.json").read_text(encoding="utf-8"))
    result = {}
    for source in set(OUTPUTS.values()):
        content = (assets / source).read_bytes()
        if hashlib.sha256(content).hexdigest() != release["sha256"][source]:
            raise ValueError(f"Release asset changed without a reviewed manifest: {source}")
        result[source] = content
    version = release["version"]
    if f"Reusable baseline: {version}.".encode() not in result["project-rules.md"]:
        raise ValueError("General-rules baseline and release version disagree")
    if f"> General rules baseline: {version}.".encode() not in result["project-specific-rules.md"]:
        raise ValueError("Specific-rule template and release version disagree")
    return version, result


def check_path(root: Path, relative: str) -> Path:
    destination = root / relative
    current = root
    for part in Path(relative).parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"Refusing symlink in output path: {current}")
        if current.exists():
            if current == destination and not current.is_file():
                raise ValueError(f"Output is not a regular file: {current}")
            if current != destination and not current.is_dir():
                raise ValueError(f"Output parent is not a directory: {current}")
    return destination


def initialize(root: Path, dry_run: bool = False) -> list[str]:
    if not root.is_dir():
        raise ValueError("The project root must already exist and be a directory.")
    # Resolve only the caller-selected root. Never follow symlinks below it.
    root = root.resolve()
    version, assets = load_assets()
    general = root / "docs/engineering/project-rules.md"
    specific = root / "docs/engineering/project-specific-rules.md"
    for relative in OUTPUTS:
        check_path(root, relative)
    # Existing project-specific content is recognized only as part of this pair.
    adopted = (
        general.is_file()
        and general.read_bytes() == assets["project-rules.md"]
        and specific.is_file()
        and f"> General rules baseline: {version}.".encode() in specific.read_bytes()
    )
    pending = []
    messages = []
    conflicts = []
    for relative, source in OUTPUTS.items():
        destination = root / relative
        if destination.exists():
            identical = destination.read_bytes() == assets[source]
            # A handover is user state, never replace it even on first adoption.
            preserve = relative == "docs/project/handover.md" or (
                adopted and relative in CUSTOMIZABLE
            )
            if not identical and not preserve:
                conflicts.append(relative)
            else:
                messages.append(f"KEEP {relative}")
        else:
            pending.append((relative, assets[source]))
            messages.append(f"{'WOULD CREATE' if dry_run else 'CREATE'} {relative}")
    if conflicts:
        raise ValueError(
            "Existing rules need a reviewed migration; no files written: "
            + ", ".join(conflicts)
        )
    if not dry_run:
        for relative, content in pending:
            destination = check_path(root, relative)
            destination.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation also protects a concurrently created file.
            with destination.open("xb") as stream:
                stream.write(content)
    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        for message in initialize(args.root, args.dry_run):
            print(message)
    except (OSError, ValueError, KeyError) as error:
        print(f"Initialization stopped: {error}", file=sys.stderr)
        return 2
    print("Rule files only; inspect and configure applicable bindings before dependent operations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
