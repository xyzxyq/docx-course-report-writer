# Multi-Agent Workflow

Use this reference for Chinese DOCX course or experiment reports when specialist delegation is useful. The main agent remains the Orchestrator and owns final integration.

## Core Rule

Every use of `docx-course-report-writer` must create/activate the baseline Actor and Critic agents or roles and run the mandatory Actor/Critic loop in `references/actor-critic-loop.md`: at least two complete cycles, no maximum iteration count, continue until no blocking defects remain.

Subagents improve reliability only when their work is bounded. Delegate independent analysis, evidence gathering, implementation slices, or QA. Keep final DOCX assembly, final field update, final PDF QA, and user-facing delivery under the Orchestrator unless a worker has explicit file ownership.

If real subagent tooling is unavailable or prohibited by the current platform, do not skip the loop. The Orchestrator must run the Actor and Critic as two separated local roles and keep their notes/checks distinct.

For ready-to-copy specialist prompts, read `references/specialist-prompts.md`.

## Roles

### Orchestrator

Owns:

- scope, assumptions, and final deliverables
- work partitioning and file ownership
- integration of all specialist outputs
- final DOCX/PDF generation, or explicit supervision of it
- final QA decision and final response

Do locally:

- resolve contradictory specialist advice
- update the final report artifact
- run the last text, TOC, field, and PDF visual checks
- decide whether defects are blocking

### Materials Analyst

Use early, often in parallel with runtime setup.

Inputs:

- assignment sheet
- prior report/template
- user constraints
- available source files and reference materials

Outputs:

- metadata to preserve or change
- required chapter structure
- stale-content risk list
- requirement-to-evidence checklist
- template style observations for headings, tables, captions, and code blocks

Do not modify files unless explicitly assigned.

### Runtime And Evidence Engineer

Use when the report depends on real program behavior.

Inputs:

- assignment requirements
- current source tree
- required runtime environment

Outputs:

- runnable implementation or missing-work diagnosis
- exact build/run/test commands
- WSL or local environment facts
- host OS, Linux/WSL availability, and WSL install-permission outcome when relevant
- raw logs and verification results
- list of proof points that need screenshots

Rules:

- For Linux/POSIX/socket/file-system assignments, first check whether the host is Linux. On Windows, verify WSL. If WSL is missing, ask before installing/enabling it.
- Do not invent results. Run the program and preserve commands/logs.
- If implementing code, own only the experiment source/test files assigned by the Orchestrator.

### Evidence Curator

Use after the runtime proof points are known.

Outputs:

- raw real screenshots when required
- cropped screenshots that retain enough context
- annotated screenshots
- image attribution records
- browser screenshot URL/content checks
- terminal screenshot command/result context checks

Rules:

- Real screenshot means actual visible terminal/application capture, not a log-rendered image.
- Browser screenshots must show the intended content, not a login, CAPTCHA, 403, blank page, or error page.
- Terminal screenshots must include enough command/result context to prove what was run.
- Keep raw screenshots alongside annotated versions when possible.
- Use red boxes for key experiment results.
- Labels must be red text, transparent background, inside image bounds, no more than 10 Chinese characters, and must not cover the evidence.
- When a hand-marked look is requested, add mild deterministic jitter to box position, padding, and line width.

### Report Writer And Layout Engineer

Use after structure and evidence are stable.

Outputs:

- report draft/source
- DOCX assembly updates
- requirement mapping tables
- file/protocol/test tables
- code snippets and captions

Rules:

- Preserve useful template metadata and page setup.
- Remove stale topic text, old screenshots, old TOC entries, and irrelevant figures.
- Use real Word heading styles and an automatic TOC field.
- Match template or user-polished table, caption, paragraph, and code-block styles.

### Word Automation Engineer

Use when TOC, fields, page numbers, or PDF export are fragile.

Outputs:

- updated DOCX fields and TOC
- exported PDF
- automation log or error summary

Rules:

- Prefer Word COM on Windows.
- If Chinese paths cause hangs or failures, copy the DOCX to an ASCII-only temp directory, update/export there, then copy results back.
- Close stale Word processes only when needed and safe for the current task.

### QA Critic

Use after a draft DOCX/PDF exists. This role should be independent when possible.

Outputs:

- blocking issues first
- exact file/page/section references when available
- pass/fail verdict for deliverability
- minimal fix list

Check:

- assignment coverage
- old-topic residues and placeholders
- evidence authenticity and visibility
- screenshot labels and red-box quality
- automatic TOC field and updated page numbers
- paragraph/table/code formatting
- PDF-rendered pages for visual defects

## Suggested Parallelization

Initial wave:

- Materials Analyst inspects assignment/template.
- Runtime And Evidence Engineer verifies or builds the experiment.

Second wave:

- Evidence Curator prepares screenshots from confirmed proof points.
- Report Writer drafts structure and tables using Materials Analyst output.

Final wave:

- Word Automation Engineer updates fields and exports PDF.
- QA Critic audits the generated DOCX/PDF.

The Orchestrator can work locally during every wave on non-overlapping integration tasks.

## Orchestrator-Only Decisions

Keep these decisions local to the Orchestrator:

- final scope and deliverable naming
- whether user-provided evidence is sufficient
- final file ownership and merge/integration
- whether a defect blocks delivery
- final response to the user

Do not ask specialists to decide whether to deliver the final report.

## Stage Gates

Gate 1: Materials Ready

- Assignment understood.
- Template preservation strategy clear.
- Required evidence list known.
- Metadata final or marked pending.

Gate 2: Runtime Evidence Ready

- Program builds/runs in the intended environment.
- Required commands have real outputs.
- Linux/POSIX work used native Linux or verified WSL, or the missing-runtime limitation is documented.
- Raw logs or raw screenshots exist.
- Verification commands prove key claims.

Gate 3: Report Draft Ready

- Chapter structure complete.
- Required evidence appears in the report.
- Tables and code snippets support evaluation.
- Old report content is removed.

Gate 4: Word Fields Ready

- Heading styles are real Word headings.
- Automatic TOC field exists.
- TOC and fields have been updated.
- PDF export exists when required.

Gate 5: Visual QA Ready

- PDF/page renders were inspected.
- Screenshots are readable and correctly annotated.
- Tables fit the page.
- No blocking residue, placeholder, or layout defect remains.

## Rework Triggers

Restart the relevant specialist stage when any of these occur:

- a screenshot is rendered from logs but described as real
- runtime results cannot be reproduced
- an automatic TOC is replaced by static text
- Word field update fails and no fallback was attempted
- red boxes are too mechanical after a hand-marked style was requested
- labels have filled backgrounds when transparent red text was requested
- labels exceed 10 Chinese characters, leave the image bounds, or cover key output
- the report has thin analysis and relies mainly on screenshots
- old experiment/topic text remains after generation
- PDF visual QA reveals clipped text, broken tables, missing images, or isolated captions
- either mandatory Actor/Critic cycle was skipped, collapsed into one pass, or run only on the plan instead of the actual artifact

## Rework Routing

- Assignment/template mismatch -> Materials Analyst.
- Runtime cannot be reproduced -> Runtime And Evidence Engineer.
- Screenshot authenticity or annotation defect -> Evidence Curator.
- Thin content, weak analysis, or poor tables -> Report Writer And Layout Engineer.
- TOC, page numbers, fields, or PDF export failure -> Word Automation Engineer.
- Multiple unresolved blocking issues -> Orchestrator performs a new scope and ownership pass before delegating again.

## File Ownership Pattern

Use explicit ownership before delegating write tasks:

- Runtime worker: experiment source, Makefile/scripts, raw logs.
- Evidence worker: screenshot files and image attribution entries.
- Report writer: markdown draft or assigned generated DOCX source.
- Orchestrator: final DOCX, final PDF, final integration scripts.

If ownership is unclear, keep the write task local to the Orchestrator.
