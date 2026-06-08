---
name: docx-course-report-writer
description: Use when Codex handles Chinese coursework/report DOCX deliverables, including experiment reports, course papers, literature reviews, reading reports, report conversion, report repair, figure-heavy Word reports, and submission-ready report packages.
---

# DOCX Course Report Writer

## Start Here

Use this skill to create, repair, polish, or verify Chinese academic `.docx` reports. Read this file first, then open only the routed references needed for the current task.

The Orchestrator owns scope, file ownership, final integration, DOCX/PDF verification, and the final response.

## Mandatory Run Contract

These rules apply every time this skill is active:

0. **Invoke Superpowers when installed.** If the environment has the Superpowers plugin or any `superpowers:*` skills installed, call the relevant Superpowers skill before acting. Start with `superpowers:using-superpowers` when available, then route through `superpowers:writing-plans`, `superpowers:subagent-driven-development`, `superpowers:executing-plans`, `superpowers:systematic-debugging`, `superpowers:test-driven-development`, or `superpowers:verification-before-completion` as the task requires. If Superpowers is unavailable, use `references/superpowers-adapter.md` as the fallback and record that limitation.
1. **Create Actor and Critic roles first.** Every run must create or activate two independent agents or clearly separated local roles: `Actor` and `Critic`. Use real subagents when available; otherwise run separated local notes and checkpoints.
2. **Run at least two full Actor -> Critic cycles.** Minimum: `Actor cycle 1`, `Critic cycle 1`, `Actor cycle 2`, `Critic cycle 2`. There is no maximum iteration count. Continue until the Critic finds no blocking defects or only documented acceptable limitations remain.
3. **Ask the AI-image intake question before generation.** Ask whether to enable text-to-image figures and how many may be generated/inserted. Default maximum is 3 when enabled without a count. Do not generate or insert AI images until permission and count are recorded, unless the user already gave both in the current request.
4. **Treat generated images as non-evidence.** AI-generated images must not replace real experiment results, real data plots, required screenshots, or item-by-item proof. Factual labels in generated images require a pre-generation text whitelist and post-generation verification.
5. **Use source-first evidence.** Do not invent results. Run programs, collect logs, capture real screenshots, or clearly document missing evidence before writing final claims.
6. **Use real Word mechanisms.** Use Word heading styles and automatic TOC fields when a TOC is expected. On Windows, prefer Word COM for field update, TOC update, save, and PDF export; use an ASCII temp path fallback for path/encoding failures.
7. **Review And Revise every diagram.** Every flowchart, pipeline, architecture diagram, timeline, mechanism diagram, TikZ drawing, self-drawn figure, or similar visual must enter a final `Review And Revise` stage after rendering. Focus especially on arrows: no arrow may be crossed, hidden, clipped, ambiguous, pointed at the wrong target, or overlapped with text/modules in a way that weakens readability or aesthetics.
8. **Audit the actual artifact.** Final QA must inspect the generated DOCX text/package and the rendered PDF or pages when layout matters. User feedback after delivery becomes a failed QA test and must be fixed at the source of truth before regeneration.

## Run Card

Follow this compact sequence unless the user explicitly limits the task to analysis only:

1. **Scope and intake**
   Check and invoke applicable Superpowers skills. Read the assignment, template/prior report, source files, user constraints, and required deliverables. Ask the mandatory AI-image question. Create a run record using `references/intake-and-run-record.md`.
2. **Evidence plan**
   Build a requirement-to-evidence checklist and a fact ledger for scores, filenames, dataset sizes, model names, dates, source boundaries, and final-vs-intermediate claims.
3. **Actor cycle 1**
   Draft, repair, assemble, run experiments, collect screenshots, create figures, or update DOCX sources.
4. **Critic cycle 1**
   Audit the current work against the assignment, evidence ledger, source files, and rendered artifacts where available. Record blocking issues.
5. **Actor cycle 2**
   Fix Critic findings at the source of truth, regenerate affected DOCX/PDF/assets, and update the run record.
6. **Critic cycle 2**
   Re-audit the regenerated artifact. If blocking issues remain, keep iterating without an artificial cap.
7. **Final gates**
   Update fields/TOC, export PDF when useful or required, inspect rendered pages, run focused QA scripts when helpful, and document any unavoidable limitation.

## Reference Routing

Open these only when needed:

- Mandatory run record and intake template: `references/intake-and-run-record.md`
- Superpowers invocation, planning, execution, debugging, and verification adapter: `references/superpowers-adapter.md`
- Actor/Critic protocol: `references/actor-critic-loop.md`
- Multi-agent role contracts and delegation gates: `references/multi-agent-workflow.md`
- Ready-to-copy specialist prompts: `references/specialist-prompts.md`
- End-to-end source-first workflow: `references/workflow.md`
- Figure, screenshot, AI-image, TikZ, and arrow QA rules: `references/figures-and-diagrams.md`
- Past defects and required prevention checks: `references/failure-patterns.md`
- Chinese DOCX typography, tables, and code blocks: `references/chinese-docx-style.md`
- Word COM, TOC, fields, and PDF export: `references/windows-word-fields.md`
- WSL, screenshot, Word, PDF, and QA command recipes: `references/tooling-recipes.md`
- Source quality, citations, and attribution: `references/source-quality.md`
- Report-type defaults: `references/report-archetypes.md`

## Non-Negotiable Gates

Do not deliver until these gates pass or the limitation is explicitly stated:

1. **Evidence authenticity gate**
   Required experiment claims have real commands, logs, screenshots, data, or code evidence. Real screenshots are visible terminal/application captures, not log-rendered substitutes.
2. **File ownership gate**
   No concurrent worker overwrites the same final DOCX/PDF, main generation script, screenshot, or figure source. The Orchestrator owns final integration unless explicitly assigned otherwise.
3. **Template residue gate**
   No stale previous topic text, old screenshots, old TOC entries, placeholders, garbled update prompts, or unrelated template media remain.
4. **Word field and TOC gate**
   Heading styles are real Word headings. TOC is automatic. Fields/page numbers are updated through Word COM or an equivalent documented process.
5. **Fact ledger gate**
   Numeric results, scores, dataset sizes, filenames, class names, model names, dates, and final-vs-intermediate claims match the latest approved evidence across DOCX text, PDF text, figure sources, captions, tables, and image specs.
6. **Figure semantics gate**
   Every self-drawn/TikZ/AI figure has correct semantics, readable labels, clean spacing, and completed `Review And Revise`. Arrow audit must pass after final scaling/rendering.
7. **External screenshot gate**
   Website/source screenshots show the intended content. A 403 page, CAPTCHA, login wall, cookie blocker, or error page is not evidence.
8. **Analysis depth gate**
   Experiment/project reports include result analysis, interpretation, failure causes, limitations, and personal understanding, not only implementation description.
9. **Rendered visual QA gate**
   PDF or page renders were checked around TOC pages, figure pages, table-heavy pages, and code-block pages before claiming layout is verified.

## Working Defaults

- Prefer a reproducible source-first workspace: `report-draft.md`, `references.md`, `image-attributions.md`, helper scripts, raw logs, raw screenshots, annotated screenshots, figure sources, final DOCX, and final PDF.
- Preserve useful template page setup, cover style, table style, heading hierarchy, captions, and metadata.
- Remove stale body content, old screenshots, old captions, old TOC entries, and irrelevant media before assembly.
- Put proof inside the report body when the assignment requires proof, not only in side folders.
- Use `scripts/qa_docx_report.py` for DOCX text/package checks when useful.
- Use `scripts/update_word_fields.ps1` or Word COM for TOC/field/PDF workflows.
- Use `scripts/annotate_screenshot.py` for repeatable red-box annotations when coordinates are known.

## Companion Skills And Tools

- Use `doc` / `documents` for low-level DOCX editing, rendering, and OOXML details.
- Use `pdf` when PDF rendering or page-level visual QA matters.
- Use `imagegen` only for explanatory or conceptual figures that are not evidence, after the mandatory AI-image intake.
- On Windows, prefer Word COM for Word-specific fidelity.
- For Linux/POSIX/socket/file-system assignments on Windows, prefer the user's local WSL environment unless the user asks for native Windows.

## Scope Boundaries

In scope: Chinese course reports, experiment reports, course papers, literature reviews, reading reports, figure-heavy academic DOCX workflows, and repair of weak report drafts.

Out of scope: legal drafting, tracked-change review pipelines, forms/content controls, and arbitrary OOXML surgery unrelated to report writing. Use generic `doc` / `documents` skills for those tasks.
