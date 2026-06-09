# AI Image Prompting For Course Reports

Use this reference whenever text-to-image figures are enabled. The goal is not to make decorative images; the goal is to create dense, purposeful, report-grade visual assets.

## Root Cause From Failed Runs

Poor AI figures usually come from underspecified prompts:

- The prompt says the topic but not the visual job.
- It asks for a broad "concept illustration" without a concrete focal object, foreground/midground/background, or information density.
- It forbids text but does not say how labels will be handled deterministically.
- It lacks a negative prompt/avoid list, so the model fills space with empty gradients, vague nodes, random icons, or stock-art decoration.
- The Critic only checks "no watermark/no text", not whether the image actually improves the report.

Treat any mostly empty, generic, or stock-looking AI image as a failed artifact, even if it is technically clean.

## Patterns Borrowed From High-Star Prompting Projects

High-star image-generation projects and prompt collections converge on the same practical pattern:

- `AUTOMATIC1111/stable-diffusion-webui` popularized explicit negative prompts: say what must not appear, not only what should appear.
- `lllyasviel/Fooocus` emphasizes prompt-focused workflows and prompt processing rather than manual parameter tweaking; this supports writing a clear visual brief before generation.
- AI prompt collections use complete visual briefs: subject, environment, composition, lighting, style, camera/framing, quality details, restrictions, and intended use.

For this skill, convert those patterns into a mandatory report-figure prompt card.

## Mandatory Prompt Card

Before generating each AI figure, write a prompt card in the run record or `image-attributions.md`:

```markdown
### AI Figure Prompt Card: <figure id>
- Report section:
- Figure role: concept-enhancement / explanatory
- Reader question answered:
- Why AI is better than self-drawn/TikZ/screenshot/paper crop:
- Visual density target: low / medium / high
- Focal subject:
- Foreground:
- Midground:
- Background:
- Composition: e.g. centered hero, left-to-right process, radial hub, split comparison
- Lighting/color/material:
- Camera/framing/aspect ratio:
- Allowed visible text: none / exact whitelist
- Deterministic overlay plan: none / labels added after generation with Pillow/SVG/TikZ
- Positive prompt:
- Negative prompt / avoid:
- Rejection criteria:
```

## Report-Grade Prompt Formula

Use this structure for most course-report AI figures:

```text
Use case: academic course report figure.
Figure role: <concept-enhancement/explanatory>.
Reader question: <what the reader should understand after seeing it>.
Subject: <specific focal object or system>.
Scene: <concrete academic/technical visual environment>.
Composition: <layout, visual hierarchy, focal point, amount of negative space>.
Information density: <medium/high; specify number of modules/regions/paths>.
Visual elements: <specific components, relationships, materials, icon families>.
Style: <restrained scientific editorial / clean technical illustration / realistic lab photo>.
Lighting and color: <palette and contrast>.
Format: <landscape 16:9 or page-friendly ratio>.
Text policy: no generated text, no letters, no numbers; labels will be added separately if needed.
Constraints: <must include/must preserve>.
Avoid: blank space, generic glowing network, random icons, stock illustration, decorative gradients, fake UI, fake logos, watermark, unreadable text, clutter, distorted anatomy, irrelevant objects.
```

## Density Requirements

For DOCX course reports, an AI figure must pass at least one density rule:

- It has a strong central subject plus at least three meaningful supporting regions.
- It shows a concrete process with at least four visually distinct stages.
- It contrasts two or more technical ideas with clear spatial separation.
- It provides a rich, inspectable scene relevant to the assignment.

Reject a figure if more than one third of the usable image area is empty without a layout reason, or if the page would be equally understandable after deleting the image.

## Text And Label Policy

Default to no generated text. If labels are needed:

1. Generate a no-text background.
2. Add all labels, arrows, and factual values with deterministic tooling.
3. Inspect the final composited image at report scale.

Never ask the image model to render Chinese technical labels unless the user explicitly accepts OCR-like errors.

## Critic Acceptance Gate

The Critic must inspect the actual generated image and answer:

- Does it answer the reader question from the prompt card?
- Is the focal subject clear within three seconds?
- Is the visual density appropriate for a course report?
- Is there any accidental text, logo, watermark, fake metric, fake UI, or irrelevant symbol?
- Does it look like a purposeful academic figure rather than a generic stock background?
- Would a self-drawn diagram be more informative? If yes, replace the AI figure or use it only as a background with deterministic overlays.

If any answer fails, regenerate with a narrower prompt or replace the figure. Do not keep a weak AI figure just because the required count was met.

## Attribution Requirements

For every accepted AI image, record:

- final prompt card
- generation method/model/tool
- output file path
- original generated file path when copied
- accepted/rejected iteration notes
- explicit statement: `AI-generated, non-evidence`

Do not deliver a report with AI images whose final prompt and rejection criteria are missing.
