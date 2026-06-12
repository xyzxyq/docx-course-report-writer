# History-Derived Experience Lessons

This reference compresses the reviewed Codex history for `docx-course-report-writer` into reusable checks. The review filtered local session logs to 35 task-level samples where the skill was explicitly requested, loaded, or used to complete Chinese DOCX/course-report work. Use this file when starting a nontrivial report run, after user feedback, or before changing the skill.

## Sample Map

The samples cluster into these recurring work types:

| Period | Representative work | Main lesson |
|---|---|---|
| 2026-05 early report runs | brain-cognition and neural-network lab reports | Rich reports need verified references, formal captions, and enough analysis; a structurally complete report can still feel thin. |
| 2026-05 Linux/network labs | socket/process reports on Windows | Linux/POSIX claims must run in WSL or native Linux, with command logs and real terminal screenshots. |
| 2026-05 template reviews | user template and multi-agent workflow planning | A DOCX template is a layout artifact. Use copy-first template editing, not "make a similar document." |
| 2026-05/06 research reports | brain-cognition literature/report tasks | Use authoritative images and verified metadata; too many self-drawn figures can weaken rigor. |
| 2026-06 model/project reports | final neural-network project report and README demo | Distinguish final model, baselines, intermediate probes, and official submission claims through a fact ledger. |
| 2026-06 skill practice TEST5-TEST8 | deep-learning architecture reports | AI images, TikZ, references, PDF page renders, and README examples exposed the highest-value failure tests. |

## Required Prevention Checks

| Historical symptom | Root cause | Required next-run behavior |
|---|---|---|
| The user said the report was too thin even though the structure was complete | The Actor treated headings as completion and did not expand theory, method, result analysis, failure causes, and personal understanding | Plan content density per chapter. A report is not ready until the Analysis depth gate confirms interpretation, limitations, and personal reflection. |
| The user asked for recent authoritative references after a draft | Citation work started as an afterthought | Build the Reference Metadata Ledger before drafting. Use GB/T 7714-2015 from the start, not as a final formatting pass. |
| Linux/socket/process reports were planned on Windows without immediate evidence | POSIX behavior was described before verifying WSL/native Linux | Route Linux work through WSL or native Linux first. Record distro, kernel, compiler, commands, logs, and screenshots before writing claims. |
| The user said a supplied template was not actually followed | The builder treated the template as inspiration or style source | Use copy-first template editing. Extract a Template Fidelity Contract, edit the copy, preserve cover/sections/styles/TOC/header/footer, and compare rendered pages. |
| A final report used too many self-drawn figures and looked less rigorous | Figure source choice was based on convenience | Prefer authoritative paper/website figures when rigor matters. Use self-drawn/TikZ to explain the agent's interpretation, not to replace authoritative evidence. |
| AI figures looked complex but empty | Prompt was theme-driven: "deep learning, futuristic, glowing, neural network" | Use one-pass text-to-image only after the prompt card defines one core question, named modules, directional relationships, labels, legend, semantic decoration, and rejection criteria. |
| AI architecture/flow figures had no readable text | The agent accepted an atmospheric image and planned to explain it in the caption | Architecture, schematic, flowchart, pipeline, and model-structure AI figures need readable labels/arrows/legend in the generated image itself. Do not overlay labels after generation; regenerate or switch to TikZ. |
| Text-to-image silently used the wrong imagegen skill and failed due to API key expectations | Two `imagegen` skills existed and the internal `.system` one was selected | Use the user-installed top-level imagegen skill, resolved by skill name or portable skills-root path. Do not use `.system/imagegen` for report figures unless the user explicitly asks. |
| TikZ/Python figures with Chinese labels rendered as boxes, question marks, or mojibake | Chinese source was piped through PowerShell or rendered without CJK-capable fonts | Write UTF-8 source files, compile TikZ with XeLaTeX and explicit CJK fonts, set Chinese fonts for Python plots, then inspect the rendered figure before insertion. |
| README/demo images contained process declarations inside the visible figure or body | QA allowed "this figure was made with..." statements to leak into public/report artifacts | Formal report/README visuals must not contain meta-process declarations such as "labels rendered by UTF-8 TikZ/XeLaTeX" unless the assignment is about that process. Keep provenance in sidecar notes. |
| The agent said a contact sheet looked fine but missed a blank second page | The Critic inspected a combined contact sheet as if it were proof and did not open individual pages | Render every PDF page to PNG and inspect every rendered page; contact sheets are an index, not the proof. A blank or near-blank page is blocking unless the template/assignment explicitly requires it and the run record names why. |
| User feedback after delivery was fixed only in the final DOCX | The source-first loop was abandoned under pressure | user feedback becomes a failed QA test. Fix the source of truth, regenerate DOCX/PDF/assets, rerun focused QA, and add the failure to the run record or failure patterns. |
| GitHub README/demo drifted from the actual skill rules | Demo artifacts were updated without checking bilingual README consistency and repo state | When publishing the skill, verify README.md, README.en.md, examples/docs assets, installed copy expectations, git status, and remote ref after push. |

## Runbook Additions

1. Before drafting, classify the run against the sample map above and open the relevant references.
2. When the user gives feedback, copy the exact defect into the run record under `Failed QA from user feedback`.
3. Convert the defect into one source-level fix and one prevention check.
4. Regenerate derived artifacts instead of hand-patching final output.
5. Run focused verification after the latest regeneration.
6. If the fix changes skill behavior, add or update a test before editing the skill.

## Visual QA Rule From TEST7

The reliable route is:

1. Update Word fields and export the final PDF through Word COM or an equivalent Word-rendering path.
2. Render every PDF page to PNG.
3. Generate contact sheets, usually four pages per image, only for fast navigation.
4. Inspect every rendered page PNG, especially cover, TOC, blank-looking pages, figure pages, table pages, code pages, and references.
5. Treat blank or near-blank pages as blocking unless explicitly allowed and documented.

Contact sheets help find suspect pages quickly, but they can hide a page-level failure. contact sheets are an index, not the proof.
