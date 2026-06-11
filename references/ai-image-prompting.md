# AI Image Prompting For Course Reports

Use this reference whenever text-to-image figures are enabled. The goal is not to make decorative images; the goal is to create dense, purposeful, report-grade visual assets.

## Root Cause From Failed Runs

Poor AI figures usually come from underspecified prompts:

- The prompt says the topic but not the visual job.
- It asks for a broad "concept illustration" without a concrete focal object, foreground/midground/background, or information density.
- It forbids text even when the requested artifact is a diagram that needs labels.
- It lacks a negative prompt/avoid list, so the model fills space with empty gradients, vague nodes, random icons, or stock-art decoration.
- The Critic only checks "no watermark/no text", not whether the image actually improves the report.
- It assumes labels can be fixed later, which violates one-pass text-to-image delivery.

Treat any mostly empty, generic, or stock-looking AI image as a failed artifact, even if it is technically clean.

## Information Architecture Gate

For AI figures in academic reports, use information architecture first, visual style second. Generic tech aesthetic words are insufficient: do not rely on "deep learning, neural network, futuristic, glowing lines, transparent glass, advanced rendering" as the core prompt.

Before any visual style words, specify:

- the specific knowledge point the figure must explain
- the named modules that must be visible
- the directional relationships between modules
- the labels, arrows, legend, and layering plan
- the semantic function of every decorative element

A decorative element must have a semantic function. Cables mean data flow, stacked blocks mean layers or repeated modules, chips mean compute, colors mean categories, dotted boxes mean optional/auxiliary paths, and background grids mean coordinate/layer alignment. If an element has no meaning, remove it from the prompt.

Use top-conference architecture figures as the reference style: clean module boxes, readable labels, arrows with a clear direction, compact legends, grouped layers, and minimal decoration. The reader should be able to answer "what mechanism is this explaining?" without relying on the caption.

Architecture, schematic, flowchart, pipeline, and model-structure figures must have readable final text labels in the generated image itself. For text-to-image figures, one-pass text-to-image is mandatory: the accepted PNG/JPEG must already contain the labels, arrows, and legend. No post-generation label overlay, manual text repair, Photoshop-style editing, Pillow/SVG/TikZ/PowerPoint label insertion, or other after-the-fact semantic correction is allowed. Final text labels are required. If generated text is wrong, reject and regenerate with a narrower prompt.

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
- Knowledge point explained:
- Why AI is better than self-drawn/TikZ/screenshot/paper crop:
- Visual density target: low / medium / high
- Focal subject:
- Named modules:
- Directional relationships:
- Label/arrow/legend/layer plan:
- Semantic decoration rule:
- Foreground:
- Midground:
- Background:
- Composition: e.g. centered hero, left-to-right process, radial hub, split comparison
- Lighting/color/material:
- Camera/framing/aspect ratio:
- Allowed visible text: exact whitelist; required for architecture/schematic/flowchart/pipeline/model-structure figures
- One-pass text-to-image plan: how the prompt will make the generated image itself contain the labels/arrows/legend
- Regeneration trigger: exact text, arrow, legend, or layout errors that force a new generation
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
Knowledge point: <CNN feature hierarchy / Transformer self-attention / MoE routing / training loop / deployment dataflow / loss optimization>.
Subject: <specific focal object or system>.
Scene: <concrete academic/technical visual environment>.
Composition: <layout, visual hierarchy, focal point, amount of negative space>.
Information density: <medium/high; specify number of modules/regions/paths>.
Named modules: <module names that should appear as boxes/panels/layers>.
Directional relationships: <A -> B -> C, skip connection, feedback loop, branching router, aggregation>.
Label plan: <exact visible text whitelist, placement, font style, and legend placement in the generated image>.
Layer plan: <lanes, stages, grouped blocks, hierarchy, legend categories>.
Semantic decoration: <each non-structural object and what it means>.
Visual elements: <specific components, relationships, materials, icon families tied to meaning>.
Style: <restrained scientific editorial / clean technical illustration / realistic lab photo>.
Lighting and color: <palette and contrast>.
Format: <landscape 16:9 or page-friendly ratio>.
Text policy: exact visible text whitelist; the image model must render these labels directly; no post-generation label overlay.
Constraints: <must include/must preserve>.
Avoid: blank space, generic glowing network, random icons, stock illustration, decorative gradients, fake UI, fake logos, watermark, unreadable text, clutter, distorted anatomy, irrelevant objects.
```

## Density Requirements

For DOCX course reports, an AI figure must pass at least one density rule:

- It has a strong central subject plus at least three meaningful supporting regions.
- It shows a concrete process with at least four visually distinct stages.
- It contrasts two or more technical ideas with clear spatial separation.
- It explains one named mechanism with at least four named modules, three directional links, and one legend or layer grouping.
- It provides a rich, inspectable scene relevant to the assignment.

Reject a figure if more than one third of the usable image area is empty without a layout reason, or if the page would be equally understandable after deleting the image.

## Text And Label Policy

For architecture, schematic, flowchart, pipeline, and model-structure figures, readable final labels are mandatory.

Use this sequence:

1. Write a short exact whitelist of visible labels before generation.
2. Ask the image model to render only those labels, arrows, and legend directly in the image.
3. Inspect the generated image at report scale.
4. If any required label, arrow, legend, or module relationship is wrong, unreadable, missing, or hallucinated, reject the image and regenerate from text-to-image. Do not repair it after generation.

Short English labels are often more reliable than long Chinese labels. If Chinese labels are required, keep them short and include a strict rejection rule for malformed characters.

For chapter-opening mood images that are not diagrams, no final labels may be acceptable only if the prompt card explicitly says the image is a non-diagram concept background and the nearby caption/prose carries the explanation.

## Critic Acceptance Gate

The Critic must inspect the actual generated image and answer:

- Does it answer the reader question from the prompt card?
- Can a reader identify the specific knowledge point without the caption?
- Are the named modules visible in the intended locations?
- Are the directional relationships, arrows, lanes, or flows clear?
- Are labels, arrows, legend, and layering present in the generated image itself, with readable text at report scale?
- Does every decorative element have a semantic function recorded in the prompt card?
- Is the focal subject clear within three seconds?
- Is the visual density appropriate for a course report?
- Is there any accidental text, logo, watermark, fake metric, fake UI, or irrelevant symbol?
- Does it look like a purposeful academic figure rather than a generic stock background?
- Would a self-drawn diagram be more informative? If yes, replace the AI figure with a non-AI deterministic diagram instead of repairing the AI image.

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
