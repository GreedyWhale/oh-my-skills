# General AI Coding Rules

> Status: Active. Personal general rules for AI-assisted development. Reusable baseline: 1.0.0.

At the start of work in a project, read this document and the neighboring [project-specific rules](project-specific-rules.md) in full, including all applicability states and task triggers. Reuse that reading while its content and task context remain current; reread changed sections when either changes. Then read the task-relevant references required by the project-specific rules before the corresponding operations. This discovers project-only obligations without requiring every linked document to be read for every task. Project-specific rules supplement these general requirements; they do not replace them.

`AGENTS.md`, `CLAUDE.md`, and other tool entry files reference this entire document. Only loading mechanisms may differ between tools; do not maintain separate rule bodies. When adopting these rules in another project, keep the general requirements here and provide that project's bindings in the neighboring `project-specific-rules.md`.

Maintain the rule documents in English. Use Chinese for explanations and rule reviews with the user.

## 0. Adoption, Applicability, and Rule Maintenance

### 0.1 Resolve Project Bindings Without Inventing Requirements

These are the user's cross-project working preferences and quality requirements, not claims that every technique is universally optimal. Apply each requirement when its stated condition is met. A project does not need every technology, platform, or document mentioned as an example.

For every project binding required by this document, keep its section or linked register entry discoverable and record one of these states, scoped to the relevant component or operation:

| State | Meaning and required action |
|---|---|
| Configured | The applicable command, constraint, reference, or ownership decision is identified from evidence or an explicit agreement. Read it before acting. This is configuration evidence, not proof that verification has passed. Record capability gaps separately. |
| Not applicable | The triggering capability or operation is absent from the current scope, with a concrete reason. Skip only that conditional binding. Reassess when the capability, task, or project scope changes. |
| Unconfigured | Applicability is unknown, or a required command, owner, reference, or protection is missing. Inspect existing project evidence and resolve what can be established within authorization. Ask only for decisions that cannot be inferred. |

A missing file, section, blank entry, broken reference, or unsupported tool is Unconfigured, not Not applicable. A module's absence does not waive unrelated general requirements. Do not invent commands, approval, historical test results, documentation, or project constraints to fill a template.

An Unconfigured binding blocks only the operation that needs it and any verification or acceptance claim depending on that operation. Continue independent authorized work. Do not run tests without the required execution protections, commit without applicable checks, perform destructive migrations without the required data-preservation basis, or bypass established network prerequisites. Missing optional topic documentation alone does not block analysis or implementation when Section 1.4's approved-requirements fallback supplies the necessary behavior. Before a functional change is ready to commit, designate or create the minimal handover required by Section 4 within the authorized documentation scope.

### 0.2 Map Verification to the Actual Project

Each independently executed test family needs a compatible controlled entry point; a common protection contract does not require one framework-specific executable for every language. Project bindings must name the component, invocation and working directory, budgets, failure signals, cleanup, applicable regression scope, and known limitations. Missing tooling is a capability gap, not an exemption from Section 2.

In Section 3, release build verification means the project's production-artifact build or its explicitly designated equivalent readiness check. Projects without a compilation or packaging step record that fact and the relevant checks; they must not fabricate a Release command. Manual UI verification uses the actual target environment, such as a browser, simulator, or physical device. Projects without UI have no UI-specific verification obligation. These mappings do not weaken applicable tests, static analysis, device evidence, or data protection.

### 0.3 Maintain One Owner for Each Requirement

Keep the user's expressly adopted cross-project collaboration preferences and quality floors here. Keep requirements depending on a project's business, architecture, stack, scale, or environment in project-specific rules. Keep detailed behavior and design with their authoritative topic owners; project-specific rules state triggers, obligations, and references rather than duplicating entire topics.

Add or update a project binding when new evidence or approved work changes it. Record its scope and basis, remove superseded requirements, and review dependent references. Do not promote a local workaround into a cross-project mandate or relax a general rule to make one project fit. A proposed general-policy change requires explicit authorization for that cross-project change. When sources conflict, identify the conflicting requirements and resolve them using their ownership and explicit user decisions; do not silently choose the easier rule.

Projects adopt an identified general-rules release and maintain their own bindings. A template is a distribution snapshot, not an additional live rule owner. Upgrades require reviewing the general-rule diff, preserving project bindings and valid local instructions, and checking affected references and applicability states. Do not overwrite other projects or auto-synchronize them merely because one copy changes. An approved new general release must update its packaged snapshot and release identifier together; retain historical approval records as history rather than rewriting their locks.

## 1. Task Execution Workflow

### 1.1 Prepare and Obtain Implementation Authorization

The agent may first read materials, investigate problems, and analyze possible approaches. Before modifying code, explain the plan, scope, and validation approach, and obtain explicit authorization to implement. Explicit instructions such as "Start" or "Proceed with the plan" count as authorization.

### 1.2 Organize Implementation According to Complexity

Work toward the user's explicit objective and the approved plan. Use the current requirements and behavior documents designated by the project. Historical materials explain background; they do not override current rules. Divide complex tasks into work units with clear objectives and verifiable outcomes, and explain their dependencies and implementation order. Complete small tasks with clear boundaries directly; do not require phases for every task.

### 1.3 Continue Within the Authorized Scope and Track Approved Changes

Once a task is authorized, proceed continuously within the approved scope until the overall objective is complete, without requesting confirmation at every step or phase. Align with the user again before changing the objective or expanding the scope. After a change is approved, update the existing plan and retain the change, its reason, and the approval basis. Use existing approval and commit records for traceability; recording a timestamp to the second and the person or model for every deviation is not a general requirement. Follow any applicable specialized diagnostic rules for precise records.

### 1.4 Check Alignment and Verify Incrementally

Before key decisions and commits, check that the actual work matches the approved objective, scope, and plan. After each commit, confirm the actual result. Complete the necessary verification for each work unit before proceeding to work that depends on it. Testing follows Section 2; commit checks and build timing follow Section 3. Avoid unnecessary repeated verification.

Before changing domain logic, read the project's existing designated current behavior references and any applicable change checklist, and inspect the relevant implementation paths. If no such reference exists, use the approved requirements to establish the intended behavior; this rule does not require creating a new document or checklist. After changes, verify the affected shared rules and related paths, not only the directly modified path. Read the [Domain Logic Changes section of the project-specific rules](project-specific-rules.md#domain-logic-changes) for the project's required references and change checks.

### 1.5 Record the Current State and Commit the Corresponding Change

When a functional change or bug fix is ready to commit, update the handover and include it in the same commit as the corresponding change, following Section 4. Commit checks and the one-bug-per-commit requirement follow Section 3. Section 4 alone defines the handover's content, information ownership, deletion safeguards, and verification-status accuracy.

## 2. Test Value, Suite Growth, and Execution Safety

### 2.1 Tests Protect Actual Behavior and Prevent Regressions

TDD is not mandatory. Do not judge code quality by the number of tests. Tests should verify business rules, data flow, and final outcomes. Avoid tests that merely mirror implementation details, pursue coverage numbers, or are added mechanically for low-risk changes.

### 2.2 New Tests Must Address an Identified Coverage Gap

Before adding tests, inspect existing coverage and explain which behavior or historical defect needs protection and why existing tests are insufficient. Prefer extending existing tests, using parameterized data or state matrices for related scenarios. Maintain each defect family together rather than creating a separate suite for every recurrence. As functionality changes, consolidate duplicate tests and remove obsolete tests. Do not remove effective regression protection merely to reduce test counts or make a failing suite pass.

### 2.3 Verify Business Logic Without Simulating UI Operations

Do not write automated tests that click buttons, wait for dialogs, operate pickers, wait for animations, or assert visual presentation. To verify the logic behind an operation, call the corresponding logic entry point directly from code and check state, data changes, and navigation or dialog requests. For example, call deletion logic directly and verify its result instead of simulating a delete-button tap and interacting with a confirmation dialog. Verify actual visual presentation and tap behavior manually on a simulator or physical device.

### 2.4 All Automated Tests Must Use a Controlled Entry Point with Failure Detection, Hard Deadlines, and Process Cleanup

Before execution, define time budgets for individual tests, the entire run, and any necessary execution phases. Detect failures through reliable signals such as test results and exit status. Do not infer a hang solely from the presence or absence of log output.

Supervision must run independently of the process under test. On failure, timeout, or unresponsiveness, end the run within the defined limits, clean up its child processes, and report a clear failure reason. Do not rely solely on the test framework's internal timeout or on the agent remembering to stop waiting.

Each project must specify its execution entry point and protection parameters. The agent must not bypass that entry point, disable protections, or relax deadlines without authorization. Explicitly report any gaps in supervision capabilities.

Before writing, modifying, or running tests, read the Testing Execution section of the project-specific rules at [docs/engineering/project-specific-rules.md](project-specific-rules.md#testing-execution) for the execution entry point, time budgets, framework constraints, and required regression scope. Those project-specific details supplement the general requirements in this section.

### 2.5 Limit Repeated Runs and Report Problems Accurately

During iteration, prioritize affected tests. Run full regression suites as required by commit or release gates. Once a scope has passed, do not rerun it without new changes, new failures, or unresolved concerns. After failure or timeout, immediately report the reason, elapsed time, and last observed progress. Diagnose before deciding the next step; do not blindly retry, relax deadlines without authorization, or skip failures.

### 2.6 Protect the Working Tree When Verifying Regression Detection

When verifying whether tests can detect regressions, use an isolated copy to run an earlier revision or a controlled mutation by default. Do not temporarily modify, roll back, or stash the current working tree for that verification. If the user explicitly requests using the current working tree, first agree on how to preserve the changes, restore the working tree, and handle interruptions. After execution finishes or is interrupted, verify the working tree and the restoration result; do not blindly run restoration commands. Test execution remains subject to Sections 2.4 and 2.5.

## 3. Commit Checks and Release Build Timing

### 3.1 Determine Required Checks from the Actual Changes

Determine required checks from the actual change scope, not the commit label or development phase. Each project must define the changes that trigger its application commit checks, the commands to run, and their acceptance criteria in its project-specific rules.

Changes that do not affect application build inputs or behavior, such as documentation-only changes or an independent website, require the checks relevant to their actual impact.

Before committing or building, read the [Commit and Build Checks section of the project-specific rules](project-specific-rules.md#commit-and-build-checks).

### 3.2 Keep One Bug per Commit and Retain Test and Analysis Requirements

Keep one bug per commit. Before each commit that triggers application checks, the project's required full regression suite and static analysis must pass under its defined acceptance criteria. No development phase or bug batch exempts these requirements.

During iteration, affected tests may run first, but they do not replace the full suite before a triggering commit. Test execution and failure handling follow Section 2. Results must cover the final code and test content to be committed. A required test or static-analysis check that fails, times out, or has not been executed blocks the commit.

### 3.3 Trigger Release Builds by User Request, Compilation Risk, or Acceptance Milestones

An ordinary bug-fix commit does not require a Release build every time. Run the project's designated build verification when any of the following applies:

- The user explicitly requests a build.
- Changes involve compilation or platform-integration risk, including dependencies, generated code, native projects, plugin integration, or build configuration, or repair a historical compilation failure. The agent must initiate the build without waiting for a user reminder.
- A concentrated round of fixes is complete and the application is entering overall acceptance or release preparation. Build the final application content before acceptance or release.

At the start of a concentrated round of fixes, state the planned build checkpoints. The end of a conversation turn or an individual bug commit does not automatically constitute an overall acceptance milestone. The risk examples above are not an exhaustive guarantee that other changes cannot cause compilation failures; the final acceptance or release build remains required.

For application changes whose Release build has not been verified, explicitly report that Release build verification is pending. Do not claim that all checks have passed. A failed build blocks acceptance or release. A build does not replace the required tests and static analysis.

### 3.4 Reuse Build Evidence Only for Unchanged Inputs and Environment

A build result covers only the build inputs and environment actually verified. Reuse a successful result only while those inputs and that environment remain unchanged. Later application changes are not covered by an earlier successful build.

### 3.5 Preserve Release Versions During Routine Work

Follow the project's policy for ownership and changes of release versions and build numbers. Routine development, bug fixing, commits, or build validation do not by themselves authorize changing them. Explicit authorization may come from a user instruction or an approved release workflow that includes the change. Before running a script or command that changes these values, check its relevant side effects and verify that they are covered by existing authorization. A tutorial's command recommendation does not grant authorization. Read the [Release Version Control section of the project-specific rules](project-specific-rules.md#release-version-control) for the project's version sources, ownership, and script behavior.

### 3.6 Write Clear Commit Messages

Follow an established project commit-message convention when one exists; otherwise use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) with `<type>[optional scope][!]: <description>`. Choose a type that matches the actual change: `fix` for bug fixes, `feat` for new features, and other appropriate types for other changes. Keep the subject concise and specific. Add a body only when needed to explain the reason or material effects, separated from the subject by a blank line. Under Conventional Commits, mark breaking changes with `!` or a `BREAKING CHANGE:` footer. Use the language agreed for the project or with the user.

## 4. Current-State Documents and Handover Maintenance

The requirements to read the entire document, classify content, replace outdated state, record verification accurately, protect valid information, and review changes apply to the handover and other documents explicitly designated by the project to maintain the current work state. This scope does not require updating every document for every task.

Before updating current-state documents, read the [Current-State Documents and Information Ownership section of the project-specific rules](project-specific-rules.md#current-state-documents-and-information-ownership).

### 4.1 Update the Handover Together with the Corresponding Change

When a functional change or bug fix is complete and ready to commit, update the project's designated handover in place and include that update in the same commit as the corresponding change. When a phase transition or batch completion changes the current work state, update the handover accordingly. Commit checks and the one-bug-per-commit requirement follow Section 3.

### 4.2 Maintain Only the Current Work State

The handover contains the overall goal, current state, still-active risks or blockers, outstanding validation, next steps, required reading, and at most one concise validation baseline. Change the overall goal only when the project direction actually changes.

### 4.3 Read the Entire Document and Update It as a State Transition

Before editing, read the entire document and classify affected content as a long-term goal, current state, next action, risk, validation baseline, or history. Replace outdated state. When work is completed, remove items that no longer affect the current work in the same edit.

### 4.4 Store Durable Information with Its Owner

Keep current behavior, closed defects and their evidence, durable regression scope, and documentation-organization evidence with their project-designated authoritative owners. Keep only necessary summaries and references in the handover.

### 4.5 Record Verification Status Accurately

Distinguish actual passes, failures, and checks not executed. If an application change has not yet been built under Section 3, retain its pending Release build verification status. A commit does not establish that all verification is complete.

### 4.6 Protect Valid Information and Review the Complete Diff

Before deleting content, confirm that it is obsolete, superseded, or preserved by the correct owning document. Keep content that remains active or whose ownership is uncertain. Before committing, review the complete diff for accidental deletion, duplication, and outdated state.

### 4.7 Control Document Growth

Do not append per-feature histories, explanations of closed defects, completed phase reports, accumulating test logs, or conversational history to current-state documents. Do not record conversations, step-by-step execution logs, or commit history as current project state. Retain user decisions, scope constraints, open questions, and next actions that still affect the handoff, linking to their basis when needed.

Approved implementation plans may retain necessary implementation steps and the basis for approved changes. Do not delete valid information solely because it contains steps or originated in user instructions.

Automated documentation checks must enforce only stable structural invariants; they must not hard-code current versions, bug identifiers, test counts, or tasks.

## 5. Code and References in Documentation

### 5.1 Keep Implementation Code in Code or Script Files

When describing the current implementation, explain its behavior, constraints, or structure and reference the actual file paths. Do not copy project implementation code into documentation or maintain duplicate functions, classes, or business implementations there. Store complete implementations in code or script files and reference their paths from documentation. Do not maintain a separate complete implementation in documentation that requires synchronized updates.

### 5.2 Allow Necessary Commands and Minimal Configuration Examples

Tutorials and engineering documentation may use code blocks for necessary operating commands and minimal configuration examples. Explain their purpose, execution prerequisites, and which parameters must be replaced.

### 5.3 Keep References and Examples Accurate

Referenced file paths must be valid. Update documentation references when files are moved or renamed. Clearly label example configurations as examples so readers do not mistake them for the project's current configuration.

### 5.4 Explain Behavior in Plain Language for Nontechnical Readers

For documents or sections intended for nontechnical readers, use everyday language to explain user-observable behavior, rules, and limitations. Do not substitute internal field names, function names, or fix history for an explanation. Use concrete scenarios for complex boundaries and specific dates for time-related rules. Prefer comparison tables when multiple cases need to be compared. These expression requirements apply to content intended for nontechnical readers; engineering explanations and defect histories should retain the detail appropriate to their purposes.

## 6. Recurring Defects

### 6.1 Define Recurrence

A defect is recurring when the same user-visible failure persists or reappears after a targeted fix has been implemented, or when a new change violates a key rule that an earlier fix stated it would protect. Repeatedly reproducing the same issue during diagnosis, before any fix has been implemented, does not by itself make the defect recurring.

### 6.2 Diagnose Recurrence Before Patching Production Code

For a recurring defect under Section 6.1, complete the following diagnosis before changing production code for the repair:

- Review the related fix history, historical reproductions, and the outcomes earlier fixes claimed to protect.
- State the stable user-visible expectation shared by the occurrences in terms of observable behavior, without implementation names or details.
- Explain the failure mechanism and why earlier fixes or verification did not prevent recurrence, using evidence. Distinguish confirmed facts from hypotheses still needing validation, and explicitly identify missing evidence rather than presenting assumptions as conclusions.
- Do not accept labels such as "conflicting fixes" as a root cause. Explain the concrete causal path from the relevant implementation decisions to the failure of the shared expectation.

### 6.3 Unify Responsibility and Repair the Demonstrated Recurrence Mechanism

For the shared expectation identified under Section 6.2:

- Trace all relevant paths that produce, transform, or consume the affected information, and designate one module as the authority for decisions about that expectation. Prefer an existing module that can fulfill this responsibility.
- Require affected callers to use the authoritative result rather than independently re-deciding the same rule. Remove duplicated or conflicting decisions and caller-specific fallbacks that re-decide it. Presentation adaptations and defined recovery behavior must remain within the result contract.
- Repair the demonstrated recurrence mechanism through shared decisions, state constraints, or interface contracts that make invalid or contradictory outcomes harder to represent. Strengthen the existing authority where appropriate, and determine the scope of structural changes from the diagnosed cause. A special case for the latest reproduction alone does not address the recurrence mechanism.
- Make the authoritative module's result contract cover its valid inputs and distinguish valid absence, intentional filtering, and processing failure. Failures must yield explicit errors or contract-defined safe outcomes; do not silently turn them into missing output, skipped work, or success.

### 6.4 Verify Recurrence at the Final Result Boundary

Ensure the following coverage for recurring defects, reusing existing verification and filling identified gaps under Section 2:

- Verify the shared expectation at the application-controlled final result boundary rather than relying solely on intermediate helpers. Automated checks use direct logic entry points and assert state, data, or action requests in accordance with Section 2.3. Scenarios requiring actual UI interaction receive manual verification under that section.
- Cover all historical reproductions that remain applicable in the defect-family verification set organized under Section 2.2. If a reproduction is obsolete under approved current behavior, record the reason for excluding it.
- Where the failure depends on state combinations, apply Section 2.2's matrix approach to representative states and identified risks rather than mechanically enumerating every combination. Where omission or duplication is possible, check the relevant collection invariants at the final result boundary.

### 6.5 Demonstrate Regression Failure Detection

For shared expectations covered by Section 6.4 that can be verified by automated logic checks permitted under Section 2.3:

- Confirm that the same relevant protective checks pass on the corrected version and fail on a known-bad revision or a targeted controlled mutation because the protected expectation is violated. Mere observation of passing checks does not establish failure-detection capability.
- Use failures of the target result assertions or checks explicitly tied to the protected contract as evidence. Setup or compilation failures and unrelated timeouts do not count. If the protected expectation is bounded completion, use a failure of a deadline check directed at that expectation.
- Use the smallest necessary defect-family regression scope that establishes this evidence. Execution supervision, failure handling, and workspace protection follow Sections 2.4 through 2.6; normal commit and release checks still follow Section 3.
- Reuse existing detection evidence only while the protected expectation, assertions, covered scenarios, relevant tested paths, and environment affecting the evidence remain unchanged. Re-establish evidence for affected protection when these change, and record incomplete or ineffective verification as an outstanding gap.

Behavior requiring manual verification continues to follow Section 6.4.

### 6.6 Close Recurring Defects Only with Complete Applicable Evidence

Declare a recurring defect resolved only after all applicable conditions below are met:

- The shared user-visible expectation from Section 6.2 and the authoritative owner from Section 6.3 are documented. The repair satisfies Section 6.3, including removal of the relevant duplicated or conflicting decisions and silent failure paths.
- Verification required by Section 6.4 has passed, including all still-applicable historical reproductions. Regression failure-detection capability has been demonstrated where Section 6.5 applies.
- The regression tests, static analysis, and build checks required at the current stage have passed under Sections 2 and 3.
- Any actual UI, device, or system behavior necessary to establish the repair has been verified in an environment capable of establishing that result, following Sections 2.3 and 6.4 and the project's acceptance requirements. Automated logic checks alone do not prove actual system behavior.

If an applicable condition fails, has not been executed, or lacks sufficient evidence, retain the outstanding verification gap and do not declare the defect resolved. A commit alone does not establish defect closure, overall acceptance, or release readiness.

Build timing remains governed by Section 3. Closing an individual defect does not by itself trigger a Release build. Release build verification that is not yet due remains explicitly pending under that section; overall acceptance and release requirements remain unchanged.

### 6.7 Preserve Recurrence Evidence Without Fixing the Protocol to Current Cases

1. Preserve the root cause of recurrence, gaps in earlier fixes or verification, and repair and closure evidence under Sections 6.2 through 6.6. Reuse, extend, or reference existing records rather than maintaining duplicate copies.
2. Store and maintain these records, durable regression scope, and current work state separately under the information ownership defined in Section 4 and the project-specific rules.
3. Keep this protocol as durable general requirements rather than fixing its scope to the current defect family, identifiers, or individual reproductions. Keep actual cases and reproductions in the corresponding defect records and regression assets.

### 6.8 Apply Recurrence and Performance Protections Together

1. For recurring defects defined in Section 6.1, the requirements of this recurring-defect protocol take precedence over the ordinary bug-fix workflow, bug-batch arrangements, and requests for a quick local patch. Such arrangements or requests do not automatically waive the protocol.
2. Recurrence repairs must also comply with performance protections. Do not introduce nonterminating or uncontrolled computation or data updates to establish correctness, and do not use performance or efficiency as a reason to bypass the diagnosed recurrence mechanism.
3. Task authorization and scope, test-execution protections, commit checks, build timing, and information ownership remain governed by Sections 1 through 4. If the requirements cannot be met together, explain the specific conflict, risks, and verification gaps, and follow the existing rules for plan changes. Do not declare the issue resolved without the applicable closure evidence required by Section 6.6.

## 7. Network and File-Creation Failures

1. When a network request or file-creation operation fails, inspect the actual error and directly relevant prerequisites first. Address confirmed causes within the available capabilities and authorized scope; do not conceal failures.
2. Set an attempt limit or overall time budget before retrying. Retry within that limit only after correcting the cause or when evidence supports a transient failure. Do not repeat the same failed operation with unchanged conditions and no new basis.
3. If the blocker cannot be removed within the available capabilities and authorized scope, report the confirmed cause or remaining uncertainty, checks already performed, and outstanding actions. Ask only for necessary assistance when user participation is required to proceed; continue independent authorized work where possible.

Test-execution failures remain subject to Section 2. This section does not provide an exception for bypassing the test entry point, relaxing deadlines, or blindly retrying tests.

## 8. Confirm and Follow Project Network Requirements

1. When a project first requires network access, check existing network agreements. If the requirements remain unclear, proactively ask the user whether there are requirements for proxies, package mirrors, access restrictions, or a specific connection method. Follow established agreements or user responses without asking again.
2. Do not assume the project has network problems or requires a proxy. If the user explicitly confirms that no special requirements apply, use the current environment's normal connection method. An unanswered question does not establish that no requirements apply. Continue independent authorized work while awaiting clarification.
3. Where the project has specific network requirements, record them in the [Network Access section of the project-specific rules](project-specific-rules.md#network-access). Read and satisfy those requirements in the actual execution environment before the relevant operations; do not assume configuration from another terminal or session automatically applies. If required configuration cannot be enabled or confirmed, handle the blocker under Section 7 rather than bypassing the prerequisite.

## 9. Dependency Diagnosis and Change Compatibility

1. When encountering third-party dependency API mismatches, type errors, deprecated APIs, or compatibility diagnostics, check the actual resolved versions, project version constraints, and relevant SDK and dependency compatibility information before modifying the implementation. Determine the cause from the actual error; do not assume that every error involving a third-party package is a version problem. Reuse confirmed information that has not changed.
2. Choose a compatible version adjustment or a code or configuration repair based on the cause. When adjusting versions, prefer a stable version that addresses the identified problem and complies with the project's compatibility constraints. Do not treat the latest version as the default repair or another dependency's version lock as the only condition permitting code changes.
3. Before adding or upgrading dependencies, check the relevant compatibility requirements between candidate versions and the current SDK, direct and transitive dependencies, generation tools, and target platforms. Before committing, validate the final selected dependency combination through the project's dependency-resolution process and the relevant checks under Sections 2 and 3. Version diagnostics or successful resolution alone do not establish code and platform compatibility. Resolve constraint conflicts rather than bypassing them with unverified forced versions. Before execution, read the [Dependency Change Compatibility section of the project-specific rules](project-specific-rules.md#dependency-change-compatibility).
4. Use version constraints, a lockfile, or an equivalent mechanism appropriate to the project type to preserve verified dependency combinations and prevent unreviewed version drift. An allowed version range does not establish that every version or combination within it has been verified. Do not delete or regenerate lockfiles, relax compatibility pins, or broadly upgrade dependencies merely to remove unrelated diagnostics. When the baseline must change, stay within the authorized scope and validate the final combination under item 3 of this section. Before these operations, read the [Dependency Version Baseline section of the project-specific rules](project-specific-rules.md#dependency-version-baseline).

Before diagnosis, read the [Dependency Diagnostics section of the project-specific rules](project-specific-rules.md#dependency-diagnostics) for actual version sources and diagnostic commands. Network operations follow Section 8, implementation authorization and scope follow Section 1, and verification follows Sections 2 and 3.

## 10. Repair Real Compilation Errors Without Concealing Them

1. For confirmed real compilation errors, repair the cause in code, dependencies, or configuration. Do not use ignore directives, exclude the affected scope, disable checks, or downgrade diagnostic severity to conceal errors or manufacture passing results.
2. Distinguish compilation errors from non-error diagnostics. This rule does not prohibit all ignore directives; handle non-error diagnostics under the project's standards without weakening existing check requirements. A diagnostic disappearing does not establish that the error has been repaired; complete the applicable verification under Section 3.

## 11. Performance Protection

### 11.1 Give Performance Protection Highest Priority Throughout the Project

1. Give performance protection highest priority across feature development, data processing, refactoring, and both ordinary and recurring defect repairs. Do not introduce nonterminating or uncontrolled recursion, loops, or data updates within an individual operation. Do not turn local changes into unnecessary high-frequency full recomputation, unrelated bulk data updates, or broad refreshes.
2. If an approach would regress performance, first seek an approach that meets both correctness and performance requirements. Prefer event-driven processing, boundary triggers, and incremental work. Necessary batch processing must have an explicit scope, a termination condition, and a cost rationale that considers data volume and execution frequency; performance protection does not prohibit all batch operations.
3. Preserve approved behavior and correctness requirements. If these requirements cannot be met together within the authorized scope, explain the specific conflict, impact, risks, and alternatives, and follow Section 1 for plan changes. Do not unilaterally relax performance protection or violate approved behavior merely to improve speed.

Before changing high-frequency processing, read the [Performance Constraints section of the project-specific rules](project-specific-rules.md#performance-constraints).

## 12. Preserve Existing Data During Storage Changes

1. Before changing persisted data structures, storage formats, or migration logic, identify the affected existing data and applicable compatibility requirements. Preserve the data required by approved behavior. Do not discard that data to bypass a migration or a failed repair; intentional data loss must be explicitly covered by authorization.
2. When migration is involved, validate the existing-data upgrade paths affected by the change and the required data preservation. Successful creation of an empty store or new data alone does not establish migration correctness. Test scope and execution follow Section 2; commit and build checks follow Section 3.

Before these changes, read the [Persisted Data and Migrations section of the project-specific rules](project-specific-rules.md#persisted-data-and-migrations).
