# Binding the General Rules to a Project

Read this when initializing, migrating, or extending bindings. The general baseline's Section 0 owns the state contract and conflict handling; this file supplies discovery guidance, not a second rulebook.

## Evidence to Inspect

| Binding | Useful evidence | What to establish |
|---|---|---|
| Testing Execution | Test directories, manifests, CI, runner implementations | Separate test families, protected invocation and working directory, individual/run/phase budgets, failure signals, child cleanup, required scope, real gaps |
| Commit and Build Checks | Build scripts, CI, compiler/linter configuration | Scope triggers, required commands and success criteria, production artifact or designated equivalent; a framework's default script is not automatically a guarded entry |
| Current-State Documents and Information Ownership | Existing instructions, documentation index, active handover | Startup reading, handover, current behavior, defect evidence and regression owners; keep existing owners and avoid duplicate documents |
| Network Access | Existing project agreements and user decisions | Proxy/mirror/access requirements; absence of config is not agreement that none exist |
| Dependency Diagnostics / Change Compatibility / Version Baseline | Manifests, lockfiles, toolchains and package manager config | Actual version sources, compatible resolution process, reproducibility and approved pins; do not copy another project's constraints |
| Domain Logic Changes | Current requirements, topic owners, actual entry points | Relevant read/check triggers; use approved requirements if no behavior document exists |
| Release Version Control | Version files, release scripts and workflow | Ownership and mutations; do not infer permission to bump versions from script existence |
| Performance Constraints | Runtime paths, workload evidence, service objectives | Actual hot paths, scale, budgets and relevant owner; do not universalize O(1) or UI-specific limits |
| Persisted Data and Migrations | Database/file formats, schemas, production compatibility | Whether existing data exists, preservation requirements and upgrade paths; missing tests do not mean migration is inapplicable |

## Apply the Three States

- **Configured**: record the scope and actual evidence. An existing `npm test` can be recorded as an observed command while its missing supervision remains Unconfigured; do not label the full execution binding ready merely because a command exists.
- **Not applicable**: give a reason tied to the current project or task. An empty documentation-only repository may have no runtime build, database, dependencies, or UI. New capabilities reopen those decisions. A production web service can have migrations even without a local database file.
- **Unconfigured**: name the missing decision or capability and the operation it blocks. Inspect resolvable facts now; defer a user decision only when it is not needed for the current operation. Read-only investigation and independent authorized changes can continue.

For mixed repositories, assign states per component rather than forcing one status onto the entire repository. For example, a configured Dart runner does not cover Python helper tests or browser audits. A host missing its required compiler is Unconfigured for that build, not a project without build requirements.

If a project has no special performance limits, its binding may explicitly state that general Section 11 applies without extra limits; this is a configured decision, not a performance waiver. If no domain reference exists, identify the approved requirement source instead of inventing a document. Existing code supplies implementation evidence, not authorization to change behavior.

## Preserve the Boundary During Migration

Keep product truths and full checklists with their current owners. Move reusable collaboration preferences only with explicit cross-project authorization; project initialization does not grant it. Preserve every still-active requirement from old entry files before replacing their bodies with whole-document references. If old and new requirements disagree, describe the conflict and obtain only the missing policy decision.

Keep project-only triggers discoverable from the fully read specific rulebook. Do not build a parallel rule body in AGENTS.md or CLAUDE.md. Existing nested tool instructions remain effective in their scopes and must be included in conflict analysis, not removed by the root initializer.
