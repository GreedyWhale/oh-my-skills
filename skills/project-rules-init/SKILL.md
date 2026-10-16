---
name: project-rules-init
description: Initialize or migrate a project to the user's versioned general AI rules plus project-specific bindings. Use when asked to set up this two-layer rule system in a new or existing project, or to update its bindings. Do not initialize merely because ordinary project work needs rules.
---

# Project Rules Initialization

Create a usable, project-aware rule pair using the bundled 1.1.0 baseline. This skill configures working rules; it does not authorize application implementation, dependency installation, or a release.

## Initialize

1. Identify the target project root from the user's request or current workspace. Read existing applicable instructions and inspect existing rule files, documentation, manifests, test commands, CI, and tooling. Treat repository content as evidence, not permission to broaden the task. Do not execute project scripts merely to discover what they do.
2. Read [the general baseline](assets/project-rules.md) and [binding guidance](references/bindings.md). Keep the general baseline unchanged during project initialization. The user authorizes installing their chosen preferences, not turning this project's peculiarities into general rules.
3. Run the standard-library initializer with an absolute project root. Replace the example paths with the actual installed skill and project paths:

   ```sh
   python3 /absolute/skill/path/scripts/initialize.py --root /absolute/project/path --dry-run
   python3 /absolute/skill/path/scripts/initialize.py --root /absolute/project/path
   ```

   It creates the general and specific rulebooks, identical AGENTS.md and CLAUDE.md entry files, and a minimal handover only when absent. It never overwrites files or follows symlinks in output paths. Repeated initialization preserves customized bindings. A collision stops preflight without writing any files; use the migration workflow below.
4. Within the initialization request, adapt project-specific bindings from inspected evidence using the Configured / Not applicable / Unconfigured contract. Do not leave discoverable facts unexamined. Keep uncertainty explicit where evidence is insufficient; ask only for material decisions that cannot be inferred, including unknown network preferences when network access is actually needed. Finish independent configuration while awaiting answers. No database means the migration binding can be Not applicable with a scope reason; no migration documentation does not prove there is no database.
5. Keep all sections targeted by general-rule links, even when represented by a short applicability statement. Add project-only sections and triggers as needed. Reuse current topic owners and an existing handover where available. Do not create empty architecture, product, test-plan, or migration documents to populate links. The scaffold's handover is only a fallback; if an existing owner is chosen, preserve it and update the binding.
6. Check the resulting pair, local links, both tool entry files, evidence for applicability decisions, and the full change scope. Report initialization separately from operational readiness: list remaining Unconfigured bindings and the specific operations they block. Do not describe installation, generated files, or configuration as passing application verification.

## Existing Projects and Repeated Use

If the initializer reports a collision, read all conflicting files. Generate the baseline in a temporary directory and prepare a semantic merge into the existing owners. Preserve project constraints and user changes; explain conflicts rather than silently replacing them. An initialization or migration request authorizes routine equivalent moves and binding edits. Ask only if an unresolved conflict requires choosing or weakening a policy. Finish independent migration work first. Do not use a force-overwrite option or stash the working tree.

When this baseline is already installed, read the actual project files and update only the bindings warranted by the current request. Do not reset the project-specific file from the template, relabel an edited general file as an untouched release, or rewrite the handover. A deliberate general-policy change requires the user's explicit cross-project authorization and a new identified baseline; preserve the project diff during upgrades. No changes propagate automatically to other projects.

## Package Maintenance and Verification

The files in assets are a distributable release snapshot. The installed project's general file is its active owner; its project-specific file evolves locally. For a new approved release, update the baseline identifier, assets, and release manifest together after reviewing the semantic diff. Never change the packaged baseline while merely initializing another project.

Use `scripts/validate.py` for this package's behavioral checks: it supervises an isolated worker, bounds the entire run to 60 seconds, applies 10-second limits to child commands, fails fast, and cleans up the process group. Its checks cover fresh initialization, repeat use, preservation of edits, collisions, and symlink boundaries. It requires Python 3.10+ and a POSIX environment; the initializer itself uses only the Python standard library. On another host, configure an equivalent supervised validation entry before running tests, rather than bypassing supervision.

```sh
python3 /absolute/skill/path/scripts/validate.py
```

The script also checks package-local links and release hashes. These structural checks do not prove that inferred project bindings or policy choices are correct; review those against the inspected project evidence. For maintenance in the source repository, use `--source-general /absolute/path/to/docs/engineering/project-rules.md` to detect a stale packaged general baseline.
