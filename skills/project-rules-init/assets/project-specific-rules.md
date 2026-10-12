# Project-Specific Rules

> General rules baseline: 1.0.0.
> Binding status: initialization scaffold; complete from project evidence before dependent operations.

Read this file in full with [the general rules](project-rules.md) at project startup. Maintain project-only triggers here. The general rules' Section 0 defines Configured, Not applicable, and Unconfigured; a missing section is Unconfigured and does not disable a general requirement. Replace scaffold statements with evidence-based bindings as the project is inspected. These states describe configuration, not successful verification.

## Testing Execution

**Unconfigured.** Inventory each independently executed test family and its compatible supervised entry, working directory, individual/run/necessary phase budgets, failure signals, process cleanup, regression scope, and capability gaps. Do not run an unprotected command or borrow another framework's runner. If there are no tests for the current scope, record that fact and its verification implications; do not claim application behavior is verified.

## Commit and Build Checks

**Unconfigured.** Establish actual change triggers, required full regression and static-analysis commands, acceptance criteria, and the production build or designated equivalent. No compiler or packaging step may be recorded as Not applicable with its reason and remaining relevant checks. Lack of a working build environment is a gap, not inapplicability. Documentation-only initialization can use link, scope, and diff checks without inventing application gates; code-changing commits require their actual bindings.

## Current-State Documents and Information Ownership

**Configured for startup handover only.** Read `docs/project/handover.md` at task start; reuse the reading while still current. This is the initializer's minimal fallback. During project discovery, prefer an existing designated handover, change this binding to its actual path, and preserve its content.

**Unconfigured for other owners.** Locate existing current requirements, behavior topics, defect evidence, regression scope, and documentation index as needed. Do not generate empty owner documents. When a functional change is ready to commit, resolve its handover and durable information ownership under general Section 4.

## Network Access

**Unconfigured.** Check existing agreements. Before the first operation needing network access, ask only if requirements remain unknown. Record an explicit agreement that no special requirements apply as Configured with normal access; do not infer it from silence or copy a proxy command from another project.

## Dependency Diagnostics

**Unconfigured.** Inspect manifests, lockfiles and actual SDK/toolchain sources before a dependency diagnosis. Record Not applicable only for a scope confirmed to have no dependency management.

### Dependency Change Compatibility

**Unconfigured.** Before changing dependencies, identify the resolution command, compatibility constraints, target environments and required validation. Successful resolution alone is not compatibility evidence.

### Dependency Version Baseline

**Unconfigured.** Identify the project's reproducibility mechanism and existing pins. Preserve verified constraints and lockfiles; no broad upgrade is authorized by initialization.

## Domain Logic Changes

**Unconfigured.** Identify approved requirements and existing current behavior references before a domain change. If no topic document exists, general Section 1.4 permits using approved requirements directly. This does not require creating a topic or checklist. Add project-specific reading triggers for relevant implementation paths.

## Release Version Control

**Unconfigured.** Before release or version-writing operations, identify version sources, their owner and script side effects. Do not change release versions as a side effect of initialization. Record Not applicable if this project has no release/versioning operation in scope, with its reason.

## Performance Constraints

**Unconfigured for project-specific limits.** General Section 11 remains active. Inspect the actual workload and any existing limits before changing high-frequency processing. If no additional limits apply, record that evidence-based decision; do not copy UI, event-timer, or algorithm limits from another project.

## Persisted Data and Migrations

**Unconfigured.** Determine whether affected persisted data or formats exist before storage changes. No persistence in the current project can justify Not applicable; no migration documentation cannot. Before an applicable change, identify data preservation, compatibility, upgrade paths and their verification under general Section 12.

## Project-Only Triggers

No project-only triggers have yet been established by this scaffold. During discovery, add applicable requirements for such matters as generated code, localization, UI design, deployment, security boundaries, or platform support. Use actual project evidence and user decisions; this list does not require every project to implement these capabilities.
