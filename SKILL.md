---
name: docx-course-report-writer
description: Use when Codex handles Chinese coursework/report DOCX deliverables, including experiment reports, course papers, literature reviews, reading reports, report conversion, report repair, figure-heavy Word reports, and submission-ready report packages.
---

# DOCX Course Report Writer

## Start Here

Use this skill to create, repair, polish, or verify Chinese academic `.docx` reports. Read this file first, then open only the routed references needed for the current task.

The Orchestrator owns scope, file ownership, final integration, DOCX/PDF verification, and the final response. For nontrivial runs, treat `references/experience-lessons.md` as history-derived experience: it summarizes real failures and prevention checks from prior uses of this skill.

## Mandatory Run Contract

These rules apply every time this skill is active:

0. **Invoke Superpowers when installed.** If the environment has the Superpowers plugin or any `superpowers:*` skills installed, call the relevant Superpowers skill before acting. Start with `superpowers:using-superpowers` when available, then route through `superpowers:writing-plans`, `superpowers:subagent-driven-development`, `superpowers:executing-plans`, `superpowers:systematic-debugging`, `superpowers:test-driven-development`, or `superpowers:verification-before-completion` as the task requires. If Superpowers is unavailable, use `references/superpowers-adapter.md` as the fallback and record that limitation.
1. **Create Actor and Critic roles first.** Every run must create or activate two independent agents or clearly separated local roles: `Actor` and `Critic`. Use real subagents when available; otherwise run separated local notes and checkpoints.
2. **Run at least two full Actor -> Critic cycles.** Minimum: `Actor cycle 1`, `Critic cycle 1`, `Actor cycle 2`, `Critic cycle 2`. There is no maximum iteration count. Continue until the Critic finds no blocking defects or only documented acceptable limitations remain.
3. **AI-image intake is a blocking question.** Before writing the report body, generating figures, or assembling DOCX/PDF, ask whether to enable text-to-image figures and exactly how many may be generated/inserted. Do not silently default to `off`. Proceed only when the user has explicitly answered, unless the current request already states both enablement and count. If the user enables AI images without a count, ask for the count instead of assuming. For nontrivial creation reports where AI images are enabled, generate and insert at least one academically appropriate conceptual/explanatory AI figure in a suitable section.
3a. **Report AI images must use the user top-level imagegen skill.** There are two different skills named `imagegen`: the user-installed report asset skill at `$CODEX_HOME/skills/imagegen/SKILL.md` and the bundled/internal system skill at `$CODEX_HOME/skills/.system/imagegen/SKILL.md`. They are two different skills. For report text-to-image work, use the top-level `$CODEX_HOME/skills/imagegen/SKILL.md` skill or the platform-equivalent user skills root. Never route report text-to-image work through `.system/imagegen`, `$CODEX_HOME/skills/.system/imagegen/SKILL.md`, or any bundled/internal image-generation fallback unless the user explicitly requests `.system/imagegen`. The user top-level `imagegen` skill does not require `OPENAI_API_KEY` in this Codex environment. Do not check `OPENAI_API_KEY`, do not block on a missing API key, and do not replace allowed AI figures with deterministic figures merely because `OPENAI_API_KEY` is absent.
4. **AI images require prompt-card QA and knowledge-structure-driven information architecture.** Before each text-to-image call, load `references/ai-image-prompting.md` and write a full prompt card: figure role, reader question, one core question, knowledge point, required knowledge modules, named modules, directional relationships, labels/arrows/legend/layering plan, semantic decoration rule, forbidden decoration, focal subject, composition, visual density target, positive prompt, negative/avoid prompt, visible text plan, one-pass text-to-image plan, Actor/Critic text review criteria, and rejection criteria. The prompt must target a teaching information graphic, textbook figure, course handout, paper overview figure, mechanism explanation figure, architecture diagram, or system pipeline figure, not a technology poster. Architecture, schematic, flowchart, pipeline, and model-structure figures must have readable final text labels directly in the generated image. Do not add or repair labels/arrows/legends after generation; a flawed AI figure must be regenerated or replaced with a non-AI deterministic diagram. A generic, mostly empty, or style-only AI figure is a blocking defect even if it has no watermark or accidental text.
5. **Treat generated images as non-evidence.** AI-generated images must not replace real experiment results, real data plots, required screenshots, or item-by-item proof. Factual labels and other visible text in generated images require a pre-generation visible text plan and post-generation Actor/Critic text review. The plan is not a closed vocabulary: useful extra text is acceptable when it is readable, accurate, relevant, and non-garbled.
6. **Lock references before drafting.** If the report uses citations, create a `Reference Metadata Ledger` before drafting the report body. The ledger must record the GB/T 7714-2015 source type, authors, title, venue/source, year/date, volume/issue/pages when applicable, publisher or official host, DOI or canonical URL, metadata verification source, and intended citation number. Do not invent reference metadata. Drafting may start only after each intended reference is verified against DOI, DOI resolver/Crossref, publisher page, official paper page, library/standard metadata, or another authoritative source; if a required field cannot be verified, do not cite it or mark it as missing and ask/replace it.
6a. **Use GB/T 7714-2015 citation typography.** Course-report citations default to GB/T 7714-2015 sequential numeric style. In-text citations must be superscript bracketed numeric citations such as `[1]`, `[2-3]`, or `[1,3]`, not plain body-sized text. The final `参考文献` list must follow GB/T 7714-2015 order, punctuation, reference type marker, DOI/URL rules, and reference list typography: bracketed sequence number and reference information use template-consistent Song/Times fonts at about 10 pt, with hanging indent unless the user template imposes a stricter style.
7. **Use source-first evidence.** Do not invent results. Run programs, collect logs, capture real screenshots, or clearly document missing evidence before writing final claims.
8. **Route Linux work through a verified Linux runtime.** When the assignment needs Linux/POSIX behavior, first check whether the user host is already Linux. If not, check for available local Linux runtimes, especially WSL on Windows. If no suitable Linux runtime exists, ask whether the user wants WSL installed and do not install it until the user explicitly permits it. When permission is granted, install/enable WSL using the platform's normal mechanism, then verify the distribution, kernel, path mapping, compilers, and commands before using results in the report.
9. **Plan screenshots as first-class evidence.** When a browser page, terminal, GUI, or external source should be visually proven, decide the screenshot target during intake, capture the real visible page/window when required, keep raw screenshots, create annotated copies when useful, and inspect the image content before treating it as evidence. Browser screenshots must show the intended page, not a login, 403, CAPTCHA, blank page, or error page. Terminal screenshots must show enough command/result context.
10. **Use real Word mechanisms.** Use Word heading styles and automatic TOC fields when a TOC is expected. Cover and TOC pages are front matter and must not count as body pages: the body must start in a new Word section with page numbering restarted at 1, and front matter must not display the body `PAGE` field, so the first visible page number 1 belongs to chapter/body content rather than the TOC page. On Windows, prefer Word COM for field update, TOC update, save, and PDF export; use an ASCII temp path fallback for path/encoding failures.
11. **Use the correct report template visibly.** If the user provides a DOCX template, use the user's template. If the user does not provide one, use the integrated default template at `skill-assets/default-course-report-template.docx`. The default template is not merely a style source: preserve its visible cover/page setup/heading/table/TOC styling unless the user explicitly requests a blank document or no cover. Remove sample body content, stale static TOC entries, old screenshots, and placeholders without discarding the default cover.
11a. **User-provided templates are authoritative layout artifacts.** When the user names or attaches a DOCX template, treat "use this template" as a strict formatting requirement, not as writing-style inspiration. First copy the template to the target report path and edit the copy. Do not create a blank document, clear the entire body, or rebuild an approximate cover/headings/tables from memory unless the user explicitly says the template is only a reference or accepts a fallback after being told what fidelity cannot be preserved.
11b. **Extract a Template Fidelity Contract before writing.** For every user-provided template, inspect and record the cover layout, page setup, section breaks, margins, headers/footers, page numbers, TOC mechanism/style, heading style names/outline levels, body/table/caption styles, placeholder text/content controls, sample body regions to replace, and media that must be preserved or removed. Prefer Word COM or OOXML inspection plus PDF/page render screenshots. The Actor must write into identified placeholder/body regions in the copied template; the Critic must compare the final render against the extracted contract.
11c. **Default DOCX builder must produce formal report structure.** When using `scripts/build_report.py` with the integrated default template, populate the cover metadata instead of leaving `放置`, `校徽`, `《XXXX》`, `实验题目`, or similar placeholders; the visible cover must fit on exactly the first page, with no cover-only date or blank spillover page; use real Word heading styles with chapter numbering such as `第一章` and section numbering such as `1.1`; keep the automatic TOC visually hierarchical and right-align page numbers with dot leaders; restart page numbering at 1 in the body section after the cover and TOC; and put `参考文献` on a new page before inserting references.
12. **Prefer deterministic structure diagrams before illustrative fallbacks.** For formal flowcharts, timelines, model architecture diagrams, module graphs, and pipeline figures, follow `references/figures-and-diagrams.md`: LaTeX TikZ > Python. For every nontrivial report creation run, insert at least one LaTeX TikZ figure; this is mandatory unless the user explicitly forbids TikZ or the assignment explicitly forbids self-drawn/LaTeX figures. Use Python only when TikZ is unsuitable, such as data-driven plots, heatmaps, charts, or image montages. When Chinese labels inside figures are needed on Windows, write UTF-8 source files, use XeLaTeX/CJK-capable fonts for TikZ or explicit Chinese fonts for Python, and inspect the rendered figure for mojibake before insertion.
13. **Review And Revise every diagram.** Every flowchart, pipeline, architecture diagram, timeline, mechanism diagram, TikZ drawing, self-drawn figure, or similar visual must enter a final `Review And Revise` stage after rendering. Focus especially on arrows and text layout: no arrow may be crossed, hidden, clipped, ambiguous, pointed at the wrong target, or overlapped with text/modules; no label may collide with a box, border, arrow, legend, caption, or another label in a way that weakens readability or aesthetics.
14. **Use formal figure captions, not body source labels or production-process claims.** Every inserted image must have a formal caption immediately below the image, using chapter-scoped numbering such as `图2.1 概念图：从早期网络到现代基础模型的架构演化`. The numbering must match the current chapter and figure order. Do not render `图片来源：...`, `AI-generated, non-evidence`, or similar provenance/source lines in the report body by default; keep provenance, AI-generation status, prompt cards, and evidence boundaries in `image-attributions.md`, a figure ledger, or nearby prose when academically necessary. Do not place implementation/process statements inside report-visible images, captions, or body prose, including claims about source encoding, rendering engines, drawing tools, prompt mechanics, or QA mechanics. A report page or image that says a module is clear because of a particular file encoding, drawing language, compiler, renderer, image model, or QA script fails this gate; move that information to the run record or sidecar attribution file.
15. **Audit the actual artifact.** Final QA must inspect the generated DOCX text/package and the rendered PDF or pages when layout matters. Word COM update/export must happen before PDF page rendering so TOC, fields, and page numbers reflect Word's real layout. Prefer `scripts/render_pdf_review_pages.py` to render the final PDF pages to PNG, run blank-page detection for every page, and combine four pages per contact sheet for fast visual review. Inspect every rendered page; contact sheets are an index, not the proof. A blank or near-blank page is blocking unless the template/assignment explicitly requires it and the run record names the page and reason. PDF page render images are not screenshots; label them as rendered PDF pages. User feedback after delivery becomes a failed QA test and must be fixed at the source of truth before regeneration.

## Run Card

Follow this compact sequence unless the user explicitly limits the task to analysis only:

1. **Scope and intake**
   Check and invoke applicable Superpowers skills. Read the assignment, template/prior report, source files, user constraints, and required deliverables. If a user-provided DOCX template exists, run the template extraction workflow and lock a Template Fidelity Contract before drafting or assembling. Ask the mandatory AI-image question and wait for the user's answer before artifact creation. Determine whether Linux/WSL or real screenshots are required. Create a run record using `references/intake-and-run-record.md`.
2. **Evidence plan**
   Build a requirement-to-evidence checklist, runtime plan, screenshot plan, fact ledger for scores, filenames, dataset sizes, model names, dates, source boundaries, and final-vs-intermediate claims, plus the `Reference Metadata Ledger` when citations will be used. Resolve and verify references before drafting prose that cites them.
3. **Actor cycle 1**
   Draft, repair, assemble, run experiments, collect screenshots, create figures, or update DOCX sources.
4. **Critic cycle 1**
   Audit the current work against the assignment, evidence ledger, source files, and rendered artifacts where available. Record blocking issues.
5. **Actor cycle 2**
   Fix Critic findings at the source of truth, regenerate affected DOCX/PDF/assets, and update the run record.
6. **Critic cycle 2**
   Re-audit the regenerated artifact. If blocking issues remain, keep iterating without an artificial cap.
7. **Final gates**
   Update fields/TOC, export PDF when useful or required, render the final PDF pages to PNG, inspect every rendered page and use contact sheets only as an index, run focused QA scripts when helpful, and document any unavoidable limitation.

## Reference Routing

Open these only when needed:

- Mandatory run record and intake template: `references/intake-and-run-record.md`
- Superpowers invocation, planning, execution, debugging, and verification adapter: `references/superpowers-adapter.md`
- Actor/Critic protocol: `references/actor-critic-loop.md`
- Multi-agent role contracts and delegation gates: `references/multi-agent-workflow.md`
- Ready-to-copy specialist prompts: `references/specialist-prompts.md`
- End-to-end source-first workflow: `references/workflow.md`
- History-derived experience and regression lessons: `references/experience-lessons.md`
- User-provided DOCX template fidelity workflow: `references/template-fidelity.md`
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
   Heading styles are real Word headings. TOC is automatic. TOC styles are readable, hierarchical, and visually checked in the exported PDF. Page numbers in the TOC must share a common right edge and use dot leaders or an equivalent formal alignment. Cover and TOC pages are not counted as body pages and must not show the body page-number field; the first visible page number 1 must be on the body/chapter page after Word field update/export. Fields/page numbers are updated through Word COM or an equivalent documented process.
   Default-template reports must use formal chapter/section heading text such as `第一章` and `1.1`, not only unnumbered Markdown headings.
4a. **User-template fidelity gate**
   When the user provides a DOCX template, the final DOCX/PDF must be produced by editing a copy of that template unless a documented and user-approved fallback was required. The final render must preserve the template's cover layout, page geometry, section/header/footer/page-number behavior, TOC styling, heading/table/caption styles, and visible brand/layout elements except where the contract says to replace sample content. A generic white document, hand-recreated cover, lost header/footer, changed title hierarchy, reset table style, or missing template media fails this gate even if the text is complete.
5. **Fact ledger gate**
   Numeric results, scores, dataset sizes, filenames, class names, model names, dates, and final-vs-intermediate claims match the latest approved evidence across DOCX text, PDF text, figure sources, captions, tables, and image specs.
5a. **Reference integrity gate**
   Every in-text citation maps to a verified `Reference Metadata Ledger` entry, every reference list entry is cited in order, no uncited or dangling references remain unless explicitly allowed, and no reference hallucination is present. The reference list follows GB/T 7714-2015 and the PDF/DOCX render shows superscript bracketed numeric citations and correct reference list typography.
6. **Linux runtime gate**
   Linux/POSIX claims were produced in native Linux or a verified local Linux runtime such as WSL. If no Linux runtime was available, the run records the missing environment and the user's install decision. WSL installation or distribution changes were never attempted without explicit user permission.
7. **Figure semantics gate**
   Every self-drawn/TikZ/AI figure has correct semantics, readable labels, clean spacing, completed `Review And Revise`, and a formal caption like `图x.x 标题`. Arrow audit must pass after final scaling/rendering. AI figures must also pass the prompt-card density and non-generic visual gate from `references/ai-image-prompting.md`. Figure provenance is tracked outside the body unless the assignment explicitly requires visible source notes. Report-visible figures, captions, and body prose must not contain production-process claims about how the figure was made, encoded, rendered, generated, or QA-checked; keep those details in sidecar records.
8. **Screenshot evidence gate**
   Browser/source screenshots show the intended content. Terminal screenshots show enough command/result context. A 403 page, CAPTCHA, login wall, cookie blocker, blank page, error page, or log-rendered substitute is not real screenshot evidence unless explicitly labeled as such.
9. **Analysis depth gate**
   Experiment/project reports include result analysis, interpretation, failure causes, limitations, and personal understanding, not only implementation description.
10. **Rendered visual QA gate**
   PDF or page renders were checked around TOC pages, figure pages, table-heavy pages, code-block pages, references, and every suspect page before claiming layout is verified. The preferred route is Word COM update/export -> render final PDF pages to PNG -> inspect every rendered page PNG; contact sheets are an index, not the proof. Blank-page detection must pass, and any allowed near-blank page must be explicitly documented.
11. **Default-template visual gate**
   When no user template is supplied, the generated DOCX/PDF preserves the integrated default template's visible cover and professional report styling. The cover must occupy page 1 only; page 2 should begin the TOC or body, not a cover date or blank cover residue. A plain white document with only generic margins/headings fails this gate unless the user explicitly requested a blank document.
12. **References pagination gate**
   The `参考文献` section must start on a new page. If `{{REFERENCES}}` is used, the builder should insert the page break and `参考文献` heading automatically unless an immediately preceding reference heading already exists.

## Working Defaults

- Prefer a reproducible source-first workspace: `report-draft.md`, `references.md`, `image-attributions.md`, helper scripts, raw logs, raw screenshots, annotated screenshots, figure sources, final DOCX, and final PDF.
- If Linux behavior matters, prefer native Linux on Linux hosts; on Windows, prefer verified WSL. Record distro, kernel, package/compiler versions, commands, logs, and path mapping.
- Treat browser and terminal screenshots as planned evidence assets. Keep raw captures separate from cropped or annotated copies.
- Template precedence is strict: user-provided template first; otherwise `skill-assets/default-course-report-template.docx`; use `--no-default-template` only when the user explicitly requests a blank Word document.
- Template editing default is copy-first: duplicate the chosen template to the target report path, then replace placeholders/sample regions in that copy while preserving sections, styles, headers/footers, page numbers, media, and fields.
- Preserve useful template page setup, visible cover style, table style, heading hierarchy, TOC styling, captions, and metadata. For user templates, preserve them strictly, not approximately.
- Remove stale body content, old screenshots, old captions, old TOC entries, and irrelevant media before assembly.
- For nontrivial report creation, include at least one figure. If the user enables text-to-image, at least one inserted figure should be AI-generated conceptual/explanatory art unless a stricter assignment forbids it.
- Put proof inside the report body when the assignment requires proof, not only in side folders.
- Use `scripts/qa_docx_report.py` for DOCX text/package checks when useful.
- Use `scripts/update_word_fields.ps1` or Word COM for TOC/field/PDF workflows.
- Use `scripts/render_pdf_review_pages.py` to render final PDF pages to PNG, create contact sheets, and detect blank or near-blank pages when visual QA matters.
- Use `scripts/annotate_screenshot.py` for repeatable red-box annotations when coordinates are known.

## Companion Skills And Tools

- Use `doc` / `documents` for low-level DOCX editing, rendering, and OOXML details.
- Use `pdf` when PDF rendering or page-level visual QA matters.
- Use the user-installed top-level `imagegen` skill for explanatory or conceptual figures that are not evidence, after the blocking AI-image intake and recorded count. Resolve this by skill name or by the portable skills-root location such as `$CODEX_HOME/skills/imagegen/SKILL.md` or the platform-equivalent user skills directory. Never route report text-to-image work through `.system/imagegen` or `$CODEX_HOME/skills/.system/imagegen/SKILL.md` unless the user explicitly requests `.system/imagegen`. The top-level report `imagegen` skill does not require `OPENAI_API_KEY`; do not check or block on that environment variable for this workflow.
- Use Browser/Playwright/browser tools for web-page screenshot evidence when available; use Computer Use or visible terminal capture for real terminal screenshots when required by the assignment.
- On Windows, prefer Word COM for Word-specific fidelity.
- For Linux/POSIX/socket/file-system assignments on Windows, verify and use WSL unless the user asks for native Windows. If WSL is missing, ask before installing or enabling it.

## Scope Boundaries

In scope: Chinese course reports, experiment reports, course papers, literature reviews, reading reports, figure-heavy academic DOCX workflows, and repair of weak report drafts.

Out of scope: legal drafting, tracked-change review pipelines, forms/content controls, and arbitrary OOXML surgery unrelated to report writing. Use generic `doc` / `documents` skills for those tasks.
