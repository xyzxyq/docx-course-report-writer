# Superpowers Adapter

Use this adapter whenever `docx-course-report-writer` is active and the current environment has the Superpowers plugin or any `superpowers:*` skills installed.

## Invocation Gate

Before doing report work, check the available skills/tooling:

1. If `superpowers:using-superpowers` is installed, invoke it first or follow the platform's skill activation mechanism.
2. If a mapped Superpowers skill is installed and the trigger applies, invoke it before acting.
3. If Superpowers is unavailable, use the fallback process in this file and record `Superpowers: unavailable` in the run record.

Do not treat this as optional. The installed Superpowers skills are workflow gates, not background reading.

## Task Mode Routing

| DOCX report situation | Required Superpowers skill when installed | DOCX fallback when unavailable |
|---|---|---|
| Rough idea, unclear assignment, uncertain scope, or user wants a plan | `superpowers:brainstorming` or `superpowers:writing-plans` | Scope lock, requirement-to-evidence checklist, and a bite-sized report plan |
| User provided requirements/template and wants artifact creation | `superpowers:writing-plans` before file writes when the task is multi-step | Write a report plan with phases, files, evidence, figures, commands, and QA |
| Existing written plan should be executed | `superpowers:subagent-driven-development` when real subagents are available; otherwise `superpowers:executing-plans` | Execute the plan task-by-task with Actor/Critic checkpoints |
| Code, experiment scripts, report generators, or bug fixes are being implemented | `superpowers:test-driven-development` when tests are feasible | Create a minimal failing check or reproducible command before implementation |
| User reports a defect, failed QA, broken DOCX/PDF, bad diagram, missing TOC, stale facts, or unexpected behavior | `superpowers:systematic-debugging` | Four-phase root-cause repair: investigate, compare, hypothesize, fix source |
| Completing major report work or a repair | `superpowers:verification-before-completion` | Fresh verification commands/checks before claiming completion |
| Substantial generated scripts or package changes need review | `superpowers:requesting-code-review` when subagents/review tooling are available | Critic review against assignment, plan, source files, and rendered artifact |

## Planning Pattern For Reports

Adapt Superpowers planning to report work:

1. **Scope lock:** report type, rubric, template, deliverables, file names, evidence, AI-image decision, PDF requirement.
2. **File map:** list source draft, scripts, logs, screenshots, figure sources, DOCX, PDF, citations, and attribution files.
3. **Bite-sized phases:** each phase should take a small, reviewable step such as "extract rubric", "run experiment", "draft result table", "render TikZ figure", "update fields", or "inspect PDF page".
4. **Verification per phase:** every phase includes the exact command/check and expected evidence.
5. **No placeholders:** do not write `TBD`, "add analysis later", "insert screenshots", or "verify manually" without specifying source, method, and pass condition.
6. **Self-review:** after the plan, check requirement coverage, stale-template risks, figure needs, TOC/field path, and final QA route.

## Execution Pattern For Reports

Adapt Superpowers execution to DOCX work:

1. Load and critically review the plan before writing files.
2. Create a task list from the plan and mark exactly one active phase at a time.
3. For each phase, run Actor work, then Critic review. Keep at least the global two Actor -> Critic cycles required by the main skill.
4. Do not skip verification commands because the artifact "looks fine".
5. Stop and ask only for blockers that cannot be resolved from local evidence, assignment files, or user-provided constraints.
6. Continue through final DOCX/PDF generation and verification when the user asked for execution, not just planning.

## Systematic Debugging For Report Defects

When repairing a reported defect, do not patch blindly.

1. **Root cause investigation:** inspect the actual DOCX/PDF/source script/log/image source. Reproduce or locate the defect.
2. **Pattern comparison:** compare with a working report, template, field-update script, figure source, or previous passing artifact.
3. **Single hypothesis:** state the suspected root cause, then test the smallest change or inspection that confirms it.
4. **Source-level fix:** fix the generator, draft, figure source, screenshot process, or Word automation path before regenerating.
5. **Verification:** rerun the focused check that would have caught the defect, then run affected final gates.

If three fix attempts fail or each fix creates a new unrelated problem, stop and question the report generation architecture instead of stacking more patches.

## Completion Gate

Before any final response:

- Freshly verify the final artifact state.
- Read the verification output, not only the command exit status.
- State what was verified and any limitation.
- Do not claim DOCX/PDF layout is verified unless the rendered PDF/pages were inspected.
