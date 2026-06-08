# Figures And Diagrams

## Start With Figure Role, Not Figure Count

Prefer adding a figure when the report needs to explain:

- a multi-step workflow
- a method pipeline
- a system structure
- a concept-to-implementation mapping
- a comparison that is hard to follow in prose
- a required result or deliverable that must be visible in the report

Do not add figures only to make the report look busy.

## Figure Role Categories

- `evidence`: real outputs, results, measurements, screenshots, or required proof
- `explanatory`: workflows, structures, processes, method blocks, relationship maps
- `concept-enhancement`: chapter-opening orientation, high-level contrast, abstract intuition

These roles are not interchangeable.

## Priority Matrix

Choose the production method by what the figure must do:

- real result, chart, or proof -> local experiment output
- rigorous flow, structure, or pipeline -> TikZ or self-drawn figure
- authoritative method illustration -> paper figure crop
- interface context -> screenshot
- abstract orientation or concept reinforcement -> AI-generated image may be appropriate
- empty-looking page only -> do not add a figure

## Real Experiment Screenshot Rules

Use these rules when screenshots are evidence:

- Run the program or command for real before capturing.
- If the user asks for real screenshots, capture an actual visible terminal/application window. Do not substitute a log-rendered image or screenshot-like render.
- Save raw logs or terminal output separately.
- Keep raw screenshots when possible, then create annotated copies for the report.
- Crop to the useful area but retain enough command/result context to prove what was run.
- If a server and client are both part of the proof, capture each role separately when needed.
- Log-rendered images may be used only when acceptable for the task, and must be labeled as rendered logs, not screenshots.

## Red Box Annotation Rules

For highlighted experiment results:

- Use red boxes to mark key proof regions.
- Add a short red text label for each box.
- Keep each label within 10 Chinese characters.
- Use transparent label background unless the user explicitly requests a filled label.
- Keep labels inside image bounds and avoid covering the evidence text.
- If the user wants a human-marked look, use mild deterministic jitter: uneven padding, slight line movement, and small line-width variation.

## When AI Image Generation Is Appropriate

Before any AI text-to-image generation for the report, ask the user:

1. Whether to enable AI-generated images and insert them into the DOCX.
2. The maximum number of generated images to run/insert.

Default: if the user enables AI images but gives no count, generate/insert at most 3. If the user does not answer, keep AI image generation off and use deterministic diagrams, screenshots, paper crops, or data plots instead.

Use AI image generation only when:

- the figure materially improves reader understanding
- the figure is not required to serve as formal evidence
- a raster/illustrative image is better than TikZ, self-drawn structure, screenshot, or paper crop

Good use cases:

- chapter-opening concept figure
- architecture-like overview figure when a literal box diagram is too dry
- comparison-oriented concept graphic
- abstract system relation or feature-space intuition

Bad use cases:

- replacing required result curves
- replacing real data plots
- pretending a generated image is experimental proof
- adding decorative filler just because the page looks empty

## AI Figure Requirements

Before generating an AI figure, record:

- figure role
- prompt summary
- why AI is the right medium
- why experiment output / TikZ / screenshot / paper crop was not chosen instead
- allowed text, numbers, names, labels, and symbols
- forbidden text, wrong examples, hallucination risks, and source facts that must not appear
- a one-paragraph drawing plan covering layout, visual hierarchy, and where factual labels will appear

After generating it, ensure:

- it is labeled as `概念图`, `示意图`, or `概念架构图`
- it is visually restrained
- it contains no accidental text or watermark
- nearby prose explains what it helps the reader understand
- all visible text and numbers match the drawing spec exactly
- no unrelated school, company, logo, license plate, UI text, fake metric, or model name appears

If accurate text is important, prefer one of these safer patterns:

1. Generate a no-text or minimal-text visual background, then overlay all Chinese labels, numbers, and arrows with Python/Pillow, SVG, TikZ, or another deterministic renderer.
2. Use AI only for a conceptual image and pair it with a deterministic caption/table for the factual content.
3. Reject the AI figure and use TikZ/self-drawn/vector output when the task requires exact text.

## Recommended Source Choices

- Self-drawn:
  - workflows
  - pipelines
  - route maps
  - architecture skeletons
  - summary structures
- Paper figure crop:
  - authoritative method overview
  - important comparison figure the report directly analyzes
- Local experiment output:
  - intermediate evidence
  - final results
  - charts
  - overlays
  - montages
- Screenshot:
  - interface or page context, cropped tightly and deliberately
- AI-generated image:
  - concept-enhancement
  - some explanatory visuals where illustration is more effective than formal diagramming

## TikZ Guidance

TikZ is recommended for clean, reproducible diagrams when the report needs:

- flowcharts
- route maps
- architecture-like structures
- layered concept diagrams

If TikZ is used:

1. Keep the `.tex` source.
2. Render to `.pdf`.
3. Convert to a DOCX-friendly format such as `.png`.
4. Inspect the rendered image before insertion.
5. Inspect the final PDF after insertion.

For report-scale TikZ, also check:

- arrows use explicit anchors such as `node.east -- node.west`, `north`, `south`, or orthogonal routes instead of vague diagonal lines
- arrowheads remain visible after DOCX/PDF scaling
- node spacing is large enough that arrows do not hide behind boxes
- timeline arrows point to the intended event/card
- swimlanes, layers, and long pipelines are split or routed when a single dense diagram becomes confusing
- no factual label, score, or final-result statement in `.tex` is stale after the user corrects the report facts

User feedback such as "arrows are messy", "layout is confusing", or "the TOC/figure is gone" is a failed visual QA test. Fix the source generator or TikZ source, regenerate every derived asset, and inspect the final report page.

## Mandatory Review And Revise Stage

Every generated flowchart, pipeline, architecture diagram, timeline, mechanism figure, or process illustration must pass a final Review And Revise stage after rendering and before insertion or delivery. This applies to TikZ, Mermaid, SVG, Matplotlib annotations, AI-generated visuals with overlays, screenshots with arrows, and any other method used to draw process-like graphics.

Arrow audit checklist:

- each arrow starts from the intended source module and ends at the intended target module
- arrowheads are visible and not hidden by node borders, labels, or image cropping
- arrows do not cross through unrelated boxes, text, legends, captions, screenshots, or important evidence
- unavoidable crossings are rerouted, separated, labeled, or the diagram is split into smaller figures
- arrow direction is visually obvious after final DOCX/PDF scaling
- timeline arrows point to the matching time point/event card
- swimlane arrows stay in the correct lane unless an intentional cross-lane transition is clearly shown
- node spacing is increased when arrowheads or line segments become cramped

Revision rule: if any arrow weakens clarity or aesthetics, revise the source layout and regenerate. Do not deliver with a note saying the reader can infer the direction.

## Data Plot And Result Figure Rules

When improving experiment-result analysis:

- derive plots from real logs, CSVs, prediction files, submission records, or verified metrics
- save the extracted data table next to the plot when possible
- keep final, intermediate, probe/debug, and server-submission scores in separate series or clearly labeled rows
- do not invent confusion matrices or per-class accuracy when labels are unavailable
- scan plot titles, legends, CSV labels, captions, TikZ sources, DOCX text, and PDF text for obsolete scores
- if the user corrects a score, rebuild all dependent figures and rerun text scans for forbidden values

## External Source Screenshot Rules

Do not trust a web screenshot because the URL is authoritative. Inspect the visible content:

- If it shows the intended official page/article/table, it can be used with source attribution.
- If it shows 403, CAPTCHA, login prompts, cookie-blocking overlays, blank pages, or unrelated redirects, it is not valid evidence.
- When access is blocked, use a source-backed metadata card, DOI/PubMed/official-title table, or manually verified citation record instead of inserting the broken page.

## Paper Figure Crop Rules

- Prefer open-access PDF or high-quality publisher images when available.
- Keep enough surrounding context that labels and arrows still make sense.
- Remove unrelated surrounding body text where possible.
- Record:
  - source title
  - page number
  - DOI or canonical URL
  - whether the figure was cropped or otherwise prepared

Do not redraw a paper's method logic unless the user explicitly wants a simplified interpretation figure.

## Per-Figure QA

For every figure, check three stages:

1. Source-stage QA
   - Is the original asset readable?
   - Are key labels, arrows, or panels intact?
2. Pre-insertion QA
   - Is the crop or render clean?
   - Is the file sharp enough for DOCX?
   - Is the format appropriate?
3. Final-document QA
   - Is the figure large enough in PDF?
   - Are labels readable without excessive zoom?
   - Do caption and source lines remain visually associated?
   - Does the figure actually help in the chapter where it appears?
