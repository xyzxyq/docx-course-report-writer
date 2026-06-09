# Workflow

## End-To-End Flow

1. Check for installed Superpowers plugin/skills. Invoke applicable `superpowers:*` skills before acting; otherwise follow `superpowers-adapter.md` as fallback.
2. Read assignment, template/prior report, source files, and user constraints. If the user did not provide a template, select `skill-assets/default-course-report-template.docx` as the default template.
3. Create or update the run record from `intake-and-run-record.md`.
4. Lock report archetype, deliverables, metadata, naming, chapter structure, required evidence, Linux/WSL need, screenshot targets, and AI-image permission/count.
5. Create or activate the mandatory Actor and Critic roles.
6. Build a requirement-to-evidence checklist before writing long prose.
7. Verify or create real runtime evidence when the report depends on program behavior. If Linux/POSIX behavior matters, use native Linux or verified WSL and record the environment facts.
8. Run a Figure Decision Pass chapter by chapter.
9. Create working source files:
   - `report-draft.md`
   - `references.md`
   - `image-attributions.md`
   - helper scripts, raw logs, raw screenshots, annotated screenshots as needed
10. Complete Actor -> Critic cycle 1 on the current draft/source/artifacts.
11. Complete Actor -> Critic cycle 2 after source-level fixes and regeneration.
12. Continue extra cycles while the Critic finds blocking defects.
13. Generate or update the DOCX.
14. Update TOC and fields in Word when available.
15. Export PDF or render page images for QA.
16. Fix blocking defects at the source of truth and regenerate.
17. Use `superpowers:verification-before-completion` when installed, or run the equivalent fresh verification gate.
18. Deliver final DOCX/PDF plus reusable source files unless the user asked for only the final artifact.

## Why Source-First Matters

- It keeps revisions reproducible.
- It prevents citation and attribution drift.
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

Do not jump to AI image generation just because a page feels visually sparse.

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

Use this branch only when AI generation is genuinely the best medium and the image is not evidence.

0. Confirm the mandatory intake record says AI text-to-image is enabled and records a maximum count. If the user enabled AI images without a count, use at most 3.
1. Identify the image goal.
2. Write a prompt summary:
   - what the image explains
   - figure role
   - why AI is the right medium
3. Build a structured prompt:
   - use case
   - asset type
   - primary request
   - scene/backdrop
   - style/medium
   - composition/framing
   - constraints
   - avoid
4. Use the system `imagegen` skill.
5. Validate the result:
   - academically appropriate
   - no watermark
   - no accidental text
   - not over-stylized
6. Record attribution metadata.
7. Insert with caption and nearby explanatory prose.
8. Re-check the exported PDF after insertion.

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
- If the template is good, adapt it instead of rebuilding it, but clear stale body content unless the user explicitly asks to preserve it.
- If the assignment is strict, create a visible requirement-to-evidence mapping inside the report.
- If a result is required item-by-item, the report itself must show direct evidence.
- If source code or runtime evidence is missing, make the experiment runnable before writing final results.
- If the TOC looks blank in a renderer, verify the field in DOCX XML, Word, or exported PDF before declaring failure.
- If the run record does not show two Actor -> Critic cycles, the report is not ready.
- If a diagram arrow audit is not recorded, the report is not ready.
- If a diagram label-overlap audit is not recorded, the report is not ready.
- If fresh completion verification has not run, the report is not ready.
