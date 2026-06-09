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
3. **AI-image intake is a blocking question.** Before writing the report body, generating figures, or assembling DOCX/PDF, ask whether to enable text-to-image figures and exactly how many may be generated/inserted. Do not silently default to `off`. Proceed only when the user has explicitly answered, unless the current request already states both enablement and count. If the user enables AI images without a count, ask for the count instead of assuming. For nontrivial creation reports where AI images are enabled, generate and insert at least one academically appropriate conceptual/explanatory AI figure in a suitable section.
4. **AI images require prompt-card QA.** Before each text-to-image call, load `references/ai-image-prompting.md` and write a full prompt card: figure role, reader question, focal subject, composition, visual density target, positive prompt, negative/avoid prompt, text policy, deterministic overlay plan, and rejection criteria. A generic or mostly empty AI figure is a blocking defect even if it has no watermark or text.
5. **Treat generated images as non-evidence.** AI-generated images must not replace real experiment results, real data plots, required screenshots, or item-by-item proof. Factual labels in generated images require a pre-generation text whitelist and post-generation verification.
6. **Use source-first evidence.** Do not invent results. Run programs, collect logs, capture real screenshots, or clearly document missing evidence before writing final claims.
7. **Route Linux work through a verified Linux runtime.** When the assignment needs Linux/POSIX behavior, first check whether the user host is already Linux. If not, check for available local Linux runtimes, especially WSL on Windows. If no suitable Linux runtime exists, ask whether the user wants WSL installed and do not install it until the user explicitly permits it. When permission is granted, install/enable WSL using the platform's normal mechanism, then verify the distribution, kernel, path mapping, compilers, and commands before using results in the report.
8. **Plan screenshots as first-class evidence.** When a browser page, terminal, GUI, or external source should be visually proven, decide the screenshot target during intake, capture the real visible page/window when required, keep raw screenshots, create annotated copies when useful, and inspect the image content before treating it as evidence. Browser screenshots must show the intended page, not a login, 403, CAPTCHA, blank page, or error page. Terminal screenshots must show enough command/result context.
9. **Use real Word mechanisms.** Use Word heading styles and automatic TOC fields when a TOC is expected. On Windows, prefer Word COM for field update, TOC update, save, and PDF export; use an ASCII temp path fallback for path/encoding failures.
10. **Use the correct report template visibly.** If the user provides a DOCX template, use the user's template. If the user does not provide one, use the integrated default template at `skill-assets/default-course-report-template.docx`. The default template is not merely a style source: preserve its visible cover/page setup/heading/table/TOC styling unless the user explicitly requests a blank document or no cover. Remove sample body content, stale static TOC entries, old screenshots, and placeholders without discarding the default cover.
10a. **Default DOCX builder must produce formal report structure.** When using `scripts/build_report.py` with the integrated default template, populate the cover metadata instead of leaving `放置`, `校徽`, `《XXXX》`, `实验题目`, or similar placeholders; use real Word heading styles with chapter numbering such as `第一章` and section numbering such as `1.1`; keep the automatic TOC visually hierarchical; and put `参考文献` on a new page before inserting references.
11. **Review And Revise every diagram.** Every flowchart, pipeline, architecture diagram, timeline, mechanism diagram, TikZ drawing, self-drawn figure, or similar visual must enter a final `Review And Revise` stage after rendering. Focus especially on arrows and text layout: no arrow may be crossed, hidden, clipped, ambiguous, pointed at the wrong target, or overlapped with text/modules; no label may collide with a box, border, arrow, legend, caption, or another label in a way that weakens readability or aesthetics.
12. **Audit the actual artifact.** Final QA must inspect the generated DOCX text/package and the rendered PDF or pages when layout matters. User feedback after delivery becomes a failed QA test and must be fixed at the source of truth before regeneration.

## Run Card

Follow this compact sequence unless the user explicitly limits the task to analysis only:

1. **Scope and intake**
   Check and invoke applicable Superpowers skills. Read the assignment, template/prior report, source files, user constraints, and required deliverables. Ask the mandatory AI-image question and wait for the user's answer before artifact creation. Determine whether Linux/WSL or real screenshots are required. Create a run record using `references/intake-and-run-record.md`.
2. **Evidence plan**
   Build a requirement-to-evidence checklist, runtime plan, screenshot plan, and fact ledger for scores, filenames, dataset sizes, model names, dates, source boundaries, and final-vs-intermediate claims.
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
- AI image prompt-card and rejection rules: `references/ai-image-prompting.md`
- Past defects and required prevention checks: `references/failure-patterns.md`
- Chinese DOCX typography, tables, and code blocks: `references/chinese-docx-style.md`
- Word COM, TOC, fields, and PDF export: `references/windows-word-fields.md`
- Linux/WSL runtime selection, screenshots, Word, PDF, and QA command recipes: `references/tooling-recipes.md`
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
   Heading styles are real Word headings. TOC is automatic. TOC styles are readable, hierarchical, and visually checked in the exported PDF. Fields/page numbers are updated through Word COM or an equivalent documented process.
   Default-template reports must use formal chapter/section heading text such as `第一章` and `1.1`, not only unnumbered Markdown headings.
5. **Fact ledger gate**
   Numeric results, scores, dataset sizes, filenames, class names, model names, dates, and final-vs-intermediate claims match the latest approved evidence across DOCX text, PDF text, figure sources, captions, tables, and image specs.
6. **Linux runtime gate**
   Linux/POSIX claims were produced in native Linux or a verified local Linux runtime such as WSL. If no Linux runtime was available, the run records the missing environment and the user's install decision. WSL installation or distribution changes were never attempted without explicit user permission.
7. **Figure semantics gate**
   Every self-drawn/TikZ/AI figure has correct semantics, readable labels, clean spacing, and completed `Review And Revise`. Arrow audit must pass after final scaling/rendering. AI figures must also pass the prompt-card density and non-generic visual gate from `references/ai-image-prompting.md`.
8. **Screenshot evidence gate**
   Browser/source screenshots show the intended content. Terminal screenshots show enough command/result context. A 403 page, CAPTCHA, login wall, cookie blocker, blank page, error page, or log-rendered substitute is not real screenshot evidence unless explicitly labeled as such.
9. **Analysis depth gate**
   Experiment/project reports include result analysis, interpretation, failure causes, limitations, and personal understanding, not only implementation description.
10. **Rendered visual QA gate**
   PDF or page renders were checked around TOC pages, figure pages, table-heavy pages, and code-block pages before claiming layout is verified.
11. **Default-template visual gate**
   When no user template is supplied, the generated DOCX/PDF preserves the integrated default template's visible cover and professional report styling. A plain white document with only generic margins/headings fails this gate unless the user explicitly requested a blank document.
12. **References pagination gate**
   The `参考文献` section must start on a new page. If `{{REFERENCES}}` is used, the builder should insert the page break and `参考文献` heading automatically unless an immediately preceding reference heading already exists.

## Working Defaults

- Prefer a reproducible source-first workspace: `report-draft.md`, `references.md`, `image-attributions.md`, helper scripts, raw logs, raw screenshots, annotated screenshots, figure sources, final DOCX, and final PDF.
- If Linux behavior matters, prefer native Linux on Linux hosts; on Windows, prefer verified WSL. Record distro, kernel, package/compiler versions, commands, logs, and path mapping.
- Treat browser and terminal screenshots as planned evidence assets. Keep raw captures separate from cropped or annotated copies.
- Template precedence is strict: user-provided template first; otherwise `skill-assets/default-course-report-template.docx`; use `--no-default-template` only when the user explicitly requests a blank Word document.
- Preserve useful template page setup, visible cover style, table style, heading hierarchy, TOC styling, captions, and metadata.
- Remove stale body content, old screenshots, old captions, old TOC entries, and irrelevant media before assembly.
- For nontrivial report creation, include at least one figure. If the user enables text-to-image, at least one inserted figure should be AI-generated conceptual/explanatory art unless a stricter assignment forbids it.
- Put proof inside the report body when the assignment requires proof, not only in side folders.
- Use `scripts/qa_docx_report.py` for DOCX text/package checks when useful.
- Use `scripts/update_word_fields.ps1` or Word COM for TOC/field/PDF workflows.
- Use `scripts/annotate_screenshot.py` for repeatable red-box annotations when coordinates are known.

## Companion Skills And Tools

- Use `doc` / `documents` for low-level DOCX editing, rendering, and OOXML details.
- Use `pdf` when PDF rendering or page-level visual QA matters.
- Use `imagegen` only for explanatory or conceptual figures that are not evidence, after the blocking AI-image intake and recorded count.
- Use Browser/Playwright/browser tools for web-page screenshot evidence when available; use Computer Use or visible terminal capture for real terminal screenshots when required by the assignment.
- On Windows, prefer Word COM for Word-specific fidelity.
- For Linux/POSIX/socket/file-system assignments on Windows, verify and use WSL unless the user asks for native Windows. If WSL is missing, ask before installing or enabling it.

## Scope Boundaries

In scope: Chinese course reports, experiment reports, course papers, literature reviews, reading reports, figure-heavy academic DOCX workflows, and repair of weak report drafts.

Out of scope: legal drafting, tracked-change review pipelines, forms/content controls, and arbitrary OOXML surgery unrelated to report writing. Use generic `doc` / `documents` skills for those tasks.
