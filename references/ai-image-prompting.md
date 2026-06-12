# AI Image Prompting For Course Reports

Use this reference whenever text-to-image figures are enabled. The goal is not to make decorative images. The goal is to create dense, purposeful, report-grade visual assets that explain a concrete knowledge structure.

## Root Cause From Failed Runs

Poor AI figures usually come from a theme-driven prompt:

```text
Draw an advanced technology image about deep learning.
```

That prompt produces a technology poster: glowing networks, chips, servers, data streams, transparent cubes, and dramatic lighting. The result may look complex, but the information is hollow. The reader can only say "this is related to AI"; they cannot explain which mechanism, workflow, model architecture, or system relation the image teaches.

The corrected approach is knowledge-structure-driven:

```text
Draw a teaching information graphic that explains one core question.
List the required knowledge modules, arrange them in a real data or gradient flow, and make every visible element correspond to a named concept.
```

Treat any mostly empty, generic, or stock-looking AI image as a failed artifact, even if it is visually polished.

## Information Architecture Gate

For AI figures in academic reports, use information architecture first, visual style second. Generic tech aesthetic words are insufficient: do not rely on "deep learning, neural network, futuristic, glowing lines, transparent glass, advanced rendering" as the core prompt.

Before any visual style words, specify:

- the one core question the figure answers
- the specific knowledge point the figure explains
- the required knowledge modules that must be visible
- the named modules and likely labels
- the directional relationships between modules
- the labels, arrows, legend, and layering plan
- the semantic function of every decorative element
- the rejection criteria for empty AI-tech-poster output

A decorative element must have a semantic function. Cables mean data flow, stacked blocks mean layers or repeated modules, chips mean compute, colors mean categories, dotted boxes mean optional/auxiliary paths, and background grids mean coordinate/layer alignment. If an element has no meaning, remove it from the prompt.

Every visible element must map to a named concept. If the element cannot be explained in the caption or nearby prose, it should not appear.

Use top-conference architecture figures as the reference style: clean module boxes, readable labels, arrows with a clear direction, compact legends, grouped layers, and minimal decoration. The target style is a textbook figure, course handout diagram, paper overview figure, mechanism explanation figure, architecture diagram, or system pipeline figure, not a technology poster.

## Anti-Poster Style Rules

Do not use futuristic AI artwork as the style target for report diagrams.

Do not add meaningless glowing lines.
Do not add random servers.
Do not add random cubes.
Do not add random chips unless compute is a named module.
Do not add floating neural-network nodes unless they represent a specific layer, token relation, attention graph, or model state.
Do not pile up abstract neural-network decoration.
Do not fill the background with generic data streams, glass panels, holograms, or blue sci-fi haze.
Do not let every region look visually busy while no region has a clear teaching role.

Allowed visual density must be semantic density: more labeled stages, clearer grouping, better arrows, useful comparison lanes, or a legend that explains color and line types.

## Mandatory Prompt Card

Before generating each AI figure, write a prompt card in the run record or `image-attributions.md`:

```markdown
### AI Figure Prompt Card: <figure id>
- Report section:
- Figure role: concept-enhancement / explanatory
- Reader question answered:
- Knowledge point explained:
- Why AI is better than self-drawn/TikZ/screenshot/paper crop:
- One core question:
- Required knowledge modules:
- Visual density target: low / medium / high:
- Focal subject:
- Named modules:
- Directional relationships:
- Label/arrow/legend/layer plan:
- Semantic decoration rule:
- Forbidden decoration:
- Foreground:
- Midground:
- Background:
- Composition: e.g. left-to-right process, two-lane comparison, layered architecture, radial hub
- Reference style: textbook figure / course handout / paper overview figure / mechanism explanation figure / system pipeline figure
- Lighting/color/material:
- Camera/framing/aspect ratio:
- Visible text plan: expected core labels and useful explanatory text; this is not a strict whitelist
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
One core question: <only one mechanism/workflow/comparison>.
Knowledge point: <CNN feature hierarchy / Transformer self-attention / MoE routing / training loop / deployment dataflow / loss optimization>.
Required knowledge modules: <complete module inventory>.
Named modules: <module names that should appear as boxes/panels/layers>.
Directional relationships: <A -> B -> C, skip connection, feedback loop, branching router, aggregation>.
Label plan: <expected core labels, optional explanatory text, placement, font style, and legend placement in the generated image>.
Layer plan: <lanes, stages, grouped blocks, hierarchy, legend categories>.
Semantic decoration: <each non-structural object and what it means>.
Composition: <layout, visual hierarchy, focal point, amount of negative space>.
Information density: <medium/high; specify number of modules/regions/paths>.
Reference style: teaching information graphic, textbook figure, course handout, paper overview figure, or system pipeline figure.
Visual elements: <specific components, relationships, materials, icon families tied to meaning>.
Lighting and color: <clean white background, restrained blue/gray, limited orange/red emphasis for loss/gradient/error>.
Format: <landscape 16:9 or document-friendly ratio>.
Avoid: <technology poster, futuristic AI artwork, random servers, random cubes, meaningless glowing lines, abstract neural-network decoration, unlabelled chips, empty gradients, stock-art style>.
Rejection criteria: <wrong labels, missing modules, unclear arrows, decorative filler, low semantic density>.
```

## Training Flow Prompt Template

Use this template when the figure must explain how a deep learning model learns from data.

```text
Create a 16:9 landscape teaching information graphic for an academic course report.
Topic: Deep learning model training workflow.
Reader question: How does a model learn from data and then produce an inference output?
One core question: the training loop from data input to weight update and final inference.

Required knowledge modules, arranged left to right:
1. Training Data: image, text, and audio samples.
2. Preprocessing: normalization, tokenization/encoding, batching.
3. Neural Network: input layer, hidden layers, output layer.
4. Forward Pass: arrow from processed input to prediction.
5. Prediction and Label: side-by-side comparison panel.
6. Loss Function: loss box or small loss curve.
7. Backpropagation: reverse arrow from loss to model parameters.
8. Optimizer / Update Weights: gradient descent update step.
9. Iteration Loop: circular arrow showing repeated training epochs.
10. Inference Output: trained model produces classification, generation, or prediction result.

Visible text plan:
Core labels should include Training Data, Preprocessing, Neural Network, Forward Pass, Prediction, Label, Loss Function, Backpropagation, Optimizer / Update Weights, Inference Output, and Epoch Loop. Reasonable extra text is allowed when it clarifies a module, legend, axis, or flow direction.

Visual style:
teaching information graphic, textbook figure, course handout, paper overview figure, clean white background, module boxes, clear arrows, compact legend, high semantic density, restrained blue and gray with orange emphasis for loss and gradient.

Negative prompt:
not a technology poster, no futuristic AI artwork, no sci-fi data center, no meaningless glowing lines, no random servers, no random cubes, no abstract neural-network decoration, no empty gradient background, no decorative chips unless they represent compute.

Acceptance criteria:
Every visible element must map to a named concept. All listed modules must be present. Arrows must express data flow or gradient flow. Visible text must be readable, accurate, relevant, and non-garbled.
```

## One-Pass Text-To-Image Label Policy

Architecture, schematic, flowchart, pipeline, and model-structure figures must have readable final text labels in the generated image itself. For text-to-image figures, one-pass text-to-image is mandatory: the accepted PNG/JPEG must already contain the labels, arrows, and legend.

No post-generation label overlay is allowed for AI diagram semantics. Final text labels are required.

Do not create an unlabeled AI background and then repair the semantics later. The visible text plan guides generation and review, but it is not a strict whitelist. Do not reject a figure only because it contains useful text outside the initial plan. Reject or regenerate when visible text is unreadable, garbled, factually wrong, misleading, irrelevant, or visually disruptive. If repeated generations fail, reject the AI figure and use TikZ/self-drawn/vector output as a separate non-AI figure.

For text-heavy report diagrams, prefer short English labels in AI generation when the report can explain them in Chinese nearby. Use Chinese labels in AI generation only if the model reliably renders them and the rendered figure is inspected at final size.

## Actor/Critic Text Review

Use Actor/Critic text review after generation instead of enforcing a closed vocabulary. The Actor records the intended visible text plan before generation. The Critic then reviews all visible text in the generated image and classifies it:

- `required and correct`: core labels that support the figure's knowledge structure
- `useful extra text`: reasonable extra text that clarifies a module, legend, axis, or flow direction
- `harmless extra text`: minor text that does not affect meaning or professionalism
- `blocking text defect`: unreadable, misspelled, garbled, hallucinated, irrelevant, misleading, or visually disruptive text

Accepted AI figures may contain reasonable extra text when it improves explanation. Blocking text defects require regeneration, replacement with a deterministic diagram, or removal of the AI figure from the report.

## Density Requirements

Choose visual density based on the job:

- `low`: only for cover-style conceptual orientation; not acceptable for mechanism diagrams.
- `medium`: 4 to 7 named modules, 3 to 6 arrows, one legend or lane grouping.
- `high`: 8 to 12 named modules, multiple lanes, feedback loops, or grouped submodules.

A report-grade AI diagram should usually be `medium` or `high`. Sparse atmospheric output fails unless the user explicitly asked for a cover illustration.

## Critic Acceptance Gate

The Critic must inspect the generated image and answer:

- What is the one core question this figure answers?
- Which required knowledge modules are visible?
- Is visible text readable, accurate, relevant, and non-garbled?
- Does any reasonable extra text improve explanation rather than create noise?
- Do arrows encode true data flow, control flow, gradient flow, comparison, or hierarchy?
- Does each non-structural visual element have a semantic purpose?
- Is the figure a teaching information graphic rather than a technology poster?
- Would the reader understand the mechanism without the caption?
- Is there any meaningless glowing line, random server, random cube, or abstract decoration?
- Does the figure remain readable after DOCX/PDF scaling?

Reject the image if any required module is missing, any important label is wrong, any arrow is ambiguous, or the image relies on atmosphere rather than structure.

## Attribution Requirements

Every accepted AI image must be recorded in `image-attributions.md` or the run ledger with:

- final file path
- prompt card
- generation date
- whether it is concept-enhancement or explanatory
- note that it is not evidence
- Critic acceptance notes
- any rejected attempts and why they failed

Do not place raw provenance lines below figures in the report body unless the assignment or user explicitly requires visible provenance.
