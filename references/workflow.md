# Workflow

## End-To-End Flow

1. Check for installed Superpowers plugin/skills. Invoke applicable `superpowers:*` skills before acting; otherwise follow `superpowers-adapter.md` as fallback.
2. Read assignment, template/prior report, source files, and user constraints. If the user did not provide a template, select `skill-assets/default-course-report-template.docx` as the default template and preserve its visible cover/style by default.
3. Create or update the run record from `intake-and-run-record.md`.
4. Ask the blocking AI-image intake question and wait for the user answer unless enablement and count were already specified in the current request.
5. Lock report archetype, deliverables, metadata, naming, chapter structure, required evidence, Linux/WSL need, screenshot targets, and AI-image permission/count.
6. Create or activate the mandatory Actor and Critic roles.
7. Build a requirement-to-evidence checklist before writing long prose.
8. If citations are used, build and lock the `Reference Metadata Ledger` before drafting: verify DOI values or canonical URLs through DOI resolver/Crossref, publisher page, official paper page, library/standard metadata, or another authoritative source; then map each source to a GB/T 7714-2015 citation number.
9. Verify or create real runtime evidence when the report depends on program behavior. If Linux/POSIX behavior matters, use native Linux or verified WSL and record the environment facts.
10. Run a Figure Decision Pass chapter by chapter.
11. Create working source files:
   - `report-draft.md`
   - `references.md`
   - `image-attributions.md`
   - helper scripts, raw logs, raw screenshots, annotated screenshots as needed
12. Complete Actor -> Critic cycle 1 on the current draft/source/artifacts, including reference hallucination and GB/T 7714-2015 format review when citations exist.
13. Complete Actor -> Critic cycle 2 after source-level fixes and regeneration, including the same reference and typography audit on the current DOCX/PDF.
14. Continue extra cycles while the Critic finds blocking defects.
15. Generate or update the DOCX.
    When using `scripts/build_report.py` with the integrated default template, pass known cover metadata such as `--title`, `--course`, `--student-name`, `--student-id`, `--teacher`, and `--date`. The builder should produce a formal cover, automatic TOC, chapter numbering (`第一章`, `1.1`), body page numbering restarted at 1 after the cover/TOC front matter, and a new-page references section by default.
16. Update TOC and fields in Word when available.
17. Export PDF or render page images for QA.
    For layout-sensitive reports, render every PDF page to PNG and generate contact sheets only as an index. Inspect individual page renders before claiming visual QA passed.
18. Fix blocking defects at the source of truth and regenerate.
19. Use `superpowers:verification-before-completion` when installed, or run the equivalent fresh verification gate.
20. Deliver final DOCX/PDF plus reusable source files unless the user asked for only the final artifact.

## Why Source-First Matters

- It keeps revisions reproducible.
- It prevents citation and attribution drift by locking verified reference metadata before prose drafting.
- It makes DOCX regeneration cheap after content changes.
- It reduces stale template residue.
- It makes figure role tracking and AI image attribution manageable.

## Figure Decision Pass

For each major section, decide:

1. Does the section need a figure?
2. If yes, what is missing?
   - evidence
   - explanation
   - concept orientation
3. What is the figure's role?
   - `evidence`
   - `explanatory`
   - `concept-enhancement`
4. What is the best production method?
   - local experiment output
   - TikZ / self-drawn
   - paper crop
   - screenshot, including browser page, terminal, GUI, or external source capture
   - AI-generated image

For nontrivial creation reports, plan at least one figure. If AI text-to-image is enabled, at least one planned non-evidence concept/explanatory figure should be AI-generated unless the assignment forbids generated imagery.

For nontrivial creation reports, also plan at least one LaTeX TikZ figure. Minimum LaTeX TikZ figures to insert: 1. This TikZ minimum gate is mandatory unless the user explicitly forbids TikZ or the assignment explicitly forbids self-drawn/LaTeX figures. AI images, screenshots, paper crops, and Python plots do not satisfy the TikZ minimum.

## Linux/WSL Branch

Use this branch when the report depends on Linux-specific behavior.

1. Check whether the host is Linux. If yes, use native Linux and record OS/kernel facts.
2. If not Linux, check local Linux runtimes. On Windows, run WSL availability checks from `tooling-recipes.md`.
3. If WSL exists, verify the distribution, kernel, compiler/runtime, project path mapping, and build/run/test commands.
4. If WSL is missing, ask the user whether to install/enable WSL. Do not install until explicit permission is given.
5. If installation is blocked by admin rights, reboot, network, or policy, record the limitation and do not present Linux results as verified.

## Screenshot Branch

Use this branch when visual evidence improves or is required by the report.

1. Decide screenshot targets during intake: browser page, terminal, GUI, external source, server/client state, or PDF render.
2. Capture raw screenshots before cropping or annotation.
3. Inspect each screenshot for semantic correctness. Reject wrong tab, wrong page, blank/error/login/CAPTCHA/403 captures.
4. For terminal screenshots, include command and result context. Do not describe log-rendered images as real screenshots.
5. Add cropped or annotated copies only after preserving raw captures.

## AI Image Branch

Use this branch only after blocking intake is resolved. AI generation is for conceptual or explanatory enhancement, not evidence.

0. Confirm the mandatory intake record says AI text-to-image is enabled and records a maximum count. If the user enabled AI images without a count, stop and ask for the count. Do not infer `off` from silence.
1. Load `references/ai-image-prompting.md`.
2. Identify the reader question and why AI is the right medium instead of self-drawn/TikZ/screenshot/paper crop.
3. Write the full AI Figure Prompt Card, including visual density target, focal subject, foreground/midground/background, composition, positive prompt, negative/avoid prompt, and rejection criteria.
4. Use the user-installed top-level `imagegen` skill, resolved by skill name or by a portable skills-root path such as `$CODEX_HOME/skills/imagegen/SKILL.md` or the platform-equivalent user skills directory. The bundled/internal system skill is `$CODEX_HOME/skills/.system/imagegen/SKILL.md`. These are two different skills. Never route report text-to-image work through `.system/imagegen` unless the user explicitly requests `.system/imagegen`. The top-level report `imagegen` skill does not require `OPENAI_API_KEY` in this Codex environment, so do not check `OPENAI_API_KEY` and do not block on a missing API key.
5. Validate the result against the prompt card:
   - academically appropriate
   - no watermark
   - exact required visible text for diagrams, or no accidental text for non-diagram concept images
   - not over-stylized
   - not generic, sparse, or stock-like
   - enough purposeful visual density for the report section
6. If the result fails, regenerate with a narrower text-to-image prompt or replace it with a separate non-AI deterministic diagram; do not keep weak AI art to satisfy a count and do not repair AI labels after generation.
7. Record attribution metadata and accepted/rejected iteration notes.
8. Insert with caption and nearby explanatory prose.
9. Re-check the exported PDF after insertion.

## Diagram Review And Revise

Every TikZ, flowchart, pipeline, architecture diagram, timeline, mechanism diagram, or similar visual must pass this after rendering and again after DOCX/PDF insertion:

1. Inspect the rendered image/page at final scale.
2. Trace every arrow from source anchor to target anchor.
3. Inspect every text block: label text must stay inside its node, avoid touching borders, avoid arrow collisions, and remain readable at final report width.
4. Fix crossings, overlaps with modules/text, hidden arrowheads, clipped paths, wrong targets, ambiguous direction, cramped spacing, and label overflow.
5. Prefer explicit anchors, orthogonal routing, wider spacing, shorter labels, wrapped labels, larger nodes, and simpler graph structure over decorative density.
6. If one diagram cannot meet the standard after two source-level revisions, split it into smaller figures or replace it with a table plus simpler diagram.
7. Update the figure ledger with `Review And Revise` status before final delivery.

## Decision Rules

- If Superpowers is installed and a mapped Superpowers skill applies, invoke it before doing the DOCX work.
- If the report work is multi-step and not already planned, write a phase plan before artifact writes.
- If repairing a defect, complete root-cause investigation before changing files.
- If the user provides a template, use it. If not, use the integrated default template. Never silently fall back to an unrelated old report.
- If the template is good, adapt it instead of rebuilding it. For the integrated default template, preserve the visible cover by default and clear only sample body content, stale static TOC entries, old media, and placeholders. Use a blank/no-cover document only when explicitly requested.
- If using the integrated default template, unnumbered body headings and a references section that continues on the previous page are blocking defects.
- If the assignment is strict, create a visible requirement-to-evidence mapping inside the report.
- If a result is required item-by-item, the report itself must show direct evidence.
- If source code or runtime evidence is missing, make the experiment runnable before writing final results.
- If reference metadata is unverified, do not cite the source and do not draft the dependent claim.
- If body citations are not superscript bracketed numeric citations or the reference list is not GB/T 7714-2015 compliant, the report is not ready.
- If the TOC looks blank in a renderer, verify the field in DOCX XML, Word, or exported PDF before declaring failure.
- If the run record does not show two Actor -> Critic cycles, the report is not ready.
- If no user template was supplied and the rendered report does not show the integrated default cover/style, the report is not ready unless the user explicitly requested a blank document.
- If AI-image intake is missing, or AI images were enabled but no generated figure was inserted in a nontrivial creation report, the report is not ready unless the run record documents a user/assignment prohibition.
- If a diagram arrow audit is not recorded, the report is not ready.
- If a diagram label-overlap audit is not recorded, the report is not ready.
- If fresh completion verification has not run, the report is not ready.
- If user feedback exposed a defect, treat it as a failed QA test, fix the source of truth, regenerate derived artifacts, and record the prevention check before delivering again.
- If PDF/page visual QA used only a contact sheet and did not inspect every rendered page, the report is not ready.
