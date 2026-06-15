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
- rigorous flow, structure, or pipeline -> LaTeX TikZ > Python
- authoritative method illustration -> paper figure crop
- interface context -> screenshot
- abstract orientation or concept reinforcement -> AI-generated image may be appropriate
- empty-looking page only -> do not add a figure

For deterministic diagrams, the default priority is **LaTeX TikZ > Python**. In practice, prefer LaTeX TikZ before Python for formal flowcharts, timelines, model architecture diagrams, module graphs, and pipeline figures because TikZ keeps boxes, arrows, anchors, labels, and source-controlled layout explicit. Use Python only when TikZ is unsuitable, such as numeric charts, heatmaps, data-driven plots, image montages, or cases where the figure is primarily computed from data rather than laid out as a conceptual structure.

## Mandatory TikZ Minimum

For every nontrivial course-report creation task, plan, render, insert, and QA at least one LaTeX TikZ figure. This is mandatory unless the user explicitly forbids TikZ or the assignment explicitly forbids self-drawn/LaTeX figures. Minimum LaTeX TikZ figures to insert: 1.

The TikZ minimum gate is separate from the AI-image gate. AI figures may supplement the report, but they do not satisfy the required deterministic TikZ figure. A nontrivial report with zero TikZ figures fails this gate unless the run record documents the user's explicit TikZ prohibition.

## Real Experiment Screenshot Rules

Use these rules when screenshots are evidence:

- Run the program or command for real before capturing.
- If the user asks for real screenshots, capture an actual visible terminal/application window. Do not substitute a log-rendered image or screenshot-like render.
- Save raw logs or terminal output separately.
- Keep raw screenshots when possible, then create annotated copies for the report.
- Crop to the useful area but retain enough command/result context to prove what was run.
- For terminal screenshots, include visible command context: prompt/current directory when useful, exact command, key output, and verification line.
- For browser screenshots, capture the actual rendered page or target region after the intended content is visible, then inspect the screenshot before using it.
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

Before any report drafting, figure generation, or DOCX assembly, ask the user:

1. Whether to enable AI-generated images and insert them into the DOCX.
2. The exact maximum number of generated images to run/insert.

This is a blocking intake question. Do not treat silence as `off`. If the user enables AI images but gives no count, stop and ask for the count. For nontrivial creation reports where AI images are enabled, generate and insert at least one conceptual or explanatory AI figure unless the assignment or user forbids it.

After intake is resolved, load `references/ai-image-prompting.md` before every text-to-image call. The prompt-card workflow in that file is mandatory, not optional. For the actual text-to-image call, use the user-installed top-level `imagegen` skill, resolved by skill name or by a portable skills-root path such as `$CODEX_HOME/skills/imagegen/SKILL.md` or the platform-equivalent user skills directory. The bundled/internal system skill is `$CODEX_HOME/skills/.system/imagegen/SKILL.md`; these are two different skills. Never route report text-to-image work through `.system/imagegen` or `$CODEX_HOME/skills/.system/imagegen/SKILL.md` unless the user explicitly requests `.system/imagegen`. The user top-level report `imagegen` skill does not require `OPENAI_API_KEY` in this Codex environment. Do not check `OPENAI_API_KEY`, and do not block AI figure generation because that environment variable is absent.

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
- satisfying the requested image count with generic, sparse, stock-like concept art

## AI Figure Requirements

Before generating an AI figure, record:

- the full prompt card from `references/ai-image-prompting.md`
- figure role
- prompt summary
- the specific knowledge point being explained
- the named modules that must appear
- the directional relationships between modules
- the label, arrow, legend, and layer plan
- the semantic function of each decorative element
- why AI is the right medium
- why experiment output / TikZ / screenshot / paper crop was not chosen instead
- allowed text, numbers, names, labels, and symbols
- forbidden text, wrong examples, hallucination risks, and source facts that must not appear
- a one-paragraph drawing plan covering layout, visual hierarchy, and where factual labels will appear
- rejection criteria, including what counts as too empty, too generic, or insufficiently related to the report section

After generating it, ensure:

- it is labeled as `概念图`, `示意图`, or `概念架构图`
- it has a formal chapter-scoped caption in the report body, such as `图2.1 概念图：从早期网络到现代基础模型的架构演化`
- it is visually restrained
- it contains no accidental text or watermark
- nearby prose explains what it helps the reader understand
- all visible text and numbers match the drawing spec exactly
- architecture, schematic, flowchart, pipeline, and model-structure figures have readable final labels, arrows, and legends directly in the generated image
- no unrelated school, company, logo, license plate, UI text, fake metric, or model name appears
- the figure has enough purposeful visual density for a course report; mostly empty backgrounds and vague glowing networks fail
- the figure explains the intended knowledge point through modules, arrows, grouping, labels, and legend rather than only through atmosphere
- the Critic records accepted/rejected iteration notes, not only the final image path

If accurate text is important, use one of these patterns:

1. Keep the AI text whitelist short and require the text-to-image model to render the final labels directly.
2. If the generated text is wrong, regenerate with fewer labels or simpler wording.
3. If repeated generations fail, reject the AI figure and use TikZ/self-drawn/vector output as a separate non-AI figure. Do not repair the AI image by adding labels after generation.

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

## Captions And Provenance Placement

Every image inserted into the final report needs a formal figure caption immediately below the image. Use chapter-scoped numbering: `图<chapter>.<index> 标题`. Reset the second number when the chapter changes, and keep captions consistent with the chapter number after heading renumbering.

Do not place raw provenance lines such as `图片来源：Codex image tool 生成；AI-generated, non-evidence...` below figures in the report body by default. They make the report look like a draft and compete with the formal caption. Put source/provenance details in `image-attributions.md`, the figure ledger, or the references/evidence prose. Only render visible source lines when the user, template, publisher, or assignment explicitly requires them.

Also keep production-process claims out of report-visible content. A figure, caption, nearby paragraph, or table cell should not explain itself by naming source encoding, drawing languages, compilers, rendering engines, image-generation tools, prompt mechanics, screenshot scripts, or QA scripts. Those details are useful engineering evidence, but they belong in the run record, figure ledger, source comments, or attribution sidecar. The report-visible page should explain the subject matter, not the toolchain used to create the page.

## TikZ Guidance

TikZ is recommended for clean, reproducible diagrams when the report needs:

- flowcharts
- route maps
- architecture-like structures
- layered concept diagrams

For deterministic report diagrams, prefer LaTeX TikZ before Python unless the figure is a data plot or TikZ would make the output harder to maintain. Python remains appropriate for Matplotlib/Seaborn charts, image grids, confusion matrices from real data, or other data-derived figures.

If TikZ is used:

1. Keep the `.tex` source.
2. Render to `.pdf`.
3. Convert to a DOCX-friendly format such as `.png`.
4. Inspect the rendered image before insertion.
5. Inspect the final PDF after insertion.

## Windows Chinese Encoding For Figures

Chinese text on Windows can fail in two separate ways: Chinese paths may be decoded incorrectly, and Chinese labels inside figures may become mojibake even when the file path is ASCII-safe. Treat both as rendering defects.

When a TikZ, LaTeX, Python, SVG, or plotting source contains Chinese labels, titles, legends, captions, or node text:

- write a UTF-8 source file first, then execute the compiler or interpreter from that file
- do not pipe Chinese source code through a PowerShell pipeline, here-string, or command argument if the content will be parsed by LaTeX, Python, or another drawing tool
- use XeLaTeX for TikZ sources that contain Chinese text
- set an explicit CJK font, preferably a Windows font such as `Microsoft YaHei`, `SimSun`, or `Noto Sans CJK SC` when available
- for Python plots, set an explicit Chinese-capable font before drawing text
- keep Chinese labels short and manually wrapped
- inspect the rendered figure, not just the source, before inserting it into DOCX/PDF

If Chinese labels inside figures still render as boxes, question marks, missing glyphs, or mojibake, stop and fix the source encoding or font selection. Do not accept the figure and do not explain it away in the caption.

For report-scale TikZ, the default should be conservative and spacious:

- prefer one main reading direction: left-to-right or top-to-bottom
- use explicit node dimensions such as `text width`, `minimum width`, `minimum height`, `inner sep`, and `align=center`
- wrap long Chinese labels manually; avoid forcing paragraph-length text into a small node
- keep module names short and move explanations to captions or nearby prose
- use `node distance`, grid/layer alignment, or fixed coordinates so boxes do not drift into arrows
- prefer orthogonal routing with `|-`, `-|`, `out/in`, or named intermediate coordinates
- use `shorten >=` and `shorten <=` so arrowheads do not hide under node borders
- avoid diagonal arrows unless the relation cannot be shown orthogonally
- split dense pipelines, timelines, and multi-lane systems into multiple figures before arrows become tangled

For report-scale TikZ, also check:

- arrows use explicit anchors such as `node.east -- node.west`, `north`, `south`, or orthogonal routes instead of vague diagonal lines
- arrowheads remain visible after DOCX/PDF scaling
- node spacing is large enough that arrows do not hide behind boxes
- labels do not touch node borders, arrow shafts, arrowheads, legends, or captions
- labels remain fully inside their boxes after PDF/PNG conversion and DOCX scaling
- no text is clipped, squeezed, overprinted, or placed on top of another visual element
- every edge label, if used, has enough white space and does not sit directly on the arrow line
- timeline arrows point to the intended event/card
- swimlanes, layers, and long pipelines are split or routed when a single dense diagram becomes confusing
- no factual label, score, or final-result statement in `.tex` is stale after the user corrects the report facts

User feedback such as "arrows are messy", "layout is confusing", or "the TOC/figure is gone" is a failed visual QA test. Fix the source generator or TikZ source, regenerate every derived asset, and inspect the final report page.

## Strict TikZ And Diagram Acceptance Gate

A diagram is not acceptable if any of the following is true in the rendered image or final PDF page:

- an arrow crosses through a node, text label, caption, legend, or important evidence region
- an arrowhead is hidden by a node border, outside the crop, too small to see, or points to the wrong object
- two or more arrows overlap closely enough that the reader cannot distinguish their paths
- a text label touches or overlaps a box border, arrow, arrowhead, icon, legend, or another label
- a node contains too much text for its width and the line breaks look cramped or unbalanced
- a label is visually detached from the module it describes
- dense crossings make the graph look clever but harder to read
- the diagram only looks acceptable in the source editor but becomes cramped after DOCX/PDF scaling

Required repair order:

1. Increase whitespace: larger canvas, larger `node distance`, larger nodes, shorter labels.
2. Route arrows explicitly: anchors, orthogonal paths, intermediate coordinates, `shorten >=`, and `shorten <=`.
3. Move explanatory text out of nodes into captions, side notes, or a table.
4. Split the diagram by chapter, phase, lane, or abstraction level.
5. If two source-level revisions still fail, discard the crowded layout and rebuild a simpler diagram from scratch.

Do not accept a diagram by saying "the meaning is still understandable." The standard is readable, accurate, and visually clean at the final report size.

## Mandatory Review And Revise Stage

Every generated flowchart, pipeline, architecture diagram, timeline, mechanism figure, or process illustration must pass a final Review And Revise stage after rendering and before insertion or delivery. This applies to TikZ, Mermaid, SVG, Matplotlib annotations, one-pass AI-generated visuals, screenshots with arrows, and any other method used to draw process-like graphics.

Arrow audit checklist:

- each arrow starts from the intended source module and ends at the intended target module
- arrowheads are visible and not hidden by node borders, labels, or image cropping
- arrows do not cross through unrelated boxes, text, legends, captions, screenshots, or important evidence
- unavoidable crossings are rerouted, separated, labeled, or the diagram is split into smaller figures
- arrow direction is visually obvious after final DOCX/PDF scaling
- timeline arrows point to the matching time point/event card
- swimlane arrows stay in the correct lane unless an intentional cross-lane transition is clearly shown
- node spacing is increased when arrowheads or line segments become cramped

Text-layout audit checklist:

- every label stays inside its intended node or label area
- no label touches a node border unless the design intentionally uses a borderless label
- no label overlaps an arrow, icon, legend, figure border, caption, or another label
- Chinese labels are manually wrapped when needed and remain balanced
- font size is large enough after DOCX/PDF scaling
- node padding is large enough that text does not look squeezed
- explanatory prose is moved out of boxes when it makes the box crowded
- visible figure text does not contain production-process claims about encoding, drawing tools, generation tools, renderers, prompts, or QA mechanics

Revision rule: if any arrow or label weakens clarity or aesthetics, revise the source layout and regenerate. Do not deliver with a note saying the reader can infer the direction or tolerate the overlap.

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
- If it captures the wrong tab, stale browser state, loading skeleton, or an error overlay, retake it after navigating and waiting for the intended content.
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
