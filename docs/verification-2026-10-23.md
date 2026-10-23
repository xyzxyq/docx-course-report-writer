# Skill optimization verification — 2026-10-23

## Initial optimization scope and result

Updated the current working tree without resetting pre-existing modifications. Retained the skill identifier and legacy DOCX builder. Reused the already-present native router/environment probe instead of adding another conversion backend.

- Entry `SKILL.md`: 27,408 → 7,764 Unicode characters (71.7% shorter than the working-tree version at task start). This measures instruction size, **not actual end-to-end token savings**.
- Default review: one main-agent artifact review, at most two focused repair rounds. Independent review is requested-only; no forced reviewer model or Superpowers chain. Format-specific and historical references load only when relevant.
- Explicit format selection is required unless the user already specified it. Router `--format` is now required; direct `build_report.py` remains DOCX-only and backward compatible.
- Added native LaTeX and Typst projects based on the default Word structure, with editable cover fields, automatic TOC, body page 1, chapter/section and figure/table numbering, equations, cross-references and GB/T 7714-2015 references. No general DOCX/Markdown-to-native converter was added.
- Added macOS font candidates to screenshot annotation and documented OS-specific finalization.

## Executed checks

Use a Python environment with `python-docx`, Pillow and `pypdfium2` (the macOS system interpreter lacked Pillow; the bundled document runtime was used for the suite):

```sh
python -m unittest discover -s tests -p 'test_*.py' -q
python scripts/check_environment.py --json
python scripts/route_report_output.py --format latex --source skill-assets/latex/main.tex --output output/template-validation/latex.pdf
python scripts/route_report_output.py --format typst --source skill-assets/typst/main.typ --output output/template-validation/typst.pdf
```

Full suite: **40 tests passed**. After final native-template adjustments, both real native integration tests passed again. They compile in a path containing Chinese and spaces; check A4, six pages, cover/TOC/body numbering, raised bracketed citations, figures/tables, cross-chapter references and bibliography; remove the original source directory and rebuild from the published source snapshot.

Compiler versions: latexmk 4.88, XeTeX/TeX Live 2026, Typst 0.15.1. Both PDFs were rendered and all six pages of each inspected. No clipped/missing content was observed. Typst emitted no warnings. LaTeX resolves its first-pass undefined references during latexmk convergence; remaining Computer Modern math-size substitutions are nonblocking but are not claimed warning-free.

The sparse native template's TOC, discussion and reference pages trigger the ink-ratio near-blank heuristic. Those pages intentionally contain short instructional samples and were visually inspected; this is a **template-only exception**, not permission to accept an empty finished report. The source includes cover placeholders and sample prose deliberately; users must replace them for a real report.

`git diff --check` and all local Markdown link-target checks passed. YAML frontmatter parsed successfully with Ruby's standard YAML parser. The skill-creator `quick_validate.py` was attempted but could not run because the available Python environments lacked PyYAML; its success is not claimed. No dependency was installed solely to run that validator.

## macOS DOCX boundary

Built the existing sample via `build_report.py` and exported using the available LibreOffice headless runtime. PDF creation succeeded, but page 2 retained the unupdated TOC placeholder, confirmed by page inspection. This is **pending field finalization**, not a successful end-to-end DOCX acceptance test. The export did not update cached fields inside the DOCX. Use the target Word/WPS application to update/save fields and recheck before submission; LibreOffice appearance cannot establish Word/WPS fidelity.

## Not verified / not changed

No Windows execution, Word/WPS desktop finalization, real user-report behavioral benchmark, or measured token A/B experiment. No new report research/experiment was run. No backend migration, arbitrary-template converter, global skill installation sync, commit or push was performed. Earlier uncommitted work remains in the working tree. Generated preview PDFs/source snapshots are under ignored `output/template-validation/` and are not committed assets.

## Follow-up: companion skills and PPT reconstruction intake

Added a one-time, task-relevant installed-skill assessment; user-facing format advantages/limitations; and a conditional AI-enabled follow-up for count and editable PPT reconstruction. Updated direct-raster rules to explicitly permit the selected native-object reconstruction route. Added `references/ppt-figure-reconstruction.md` with PPTX/PDF deliverables, raster/vector distinctions and Word insertion limits; no new converter or DOCX vector-insertion implementation was added.

This follow-up changes instructions and routing only. It does not claim a real AI-image → PPT → PDF → Word end-to-end run. The earlier character-count reduction refers to the initial optimization snapshot, before these additional user-requested rules.

Follow-up checks: 21 existing policy tests passed; YAML frontmatter parsed; local Markdown links resolved; `git diff --check` passed. Reviewed the explicit branches for preselected format, AI disabled, AI enabled with unresolved PPT preference, and selected native-object reconstruction. This is an instruction-consistency review, not an agent behavior benchmark or an end-to-end vector-insertion test.

## Transformer vector figure end-to-end run

This later run implements and exercises the previously missing PDF/SVG-to-DOCX path. The user requested a more complex Transformer architecture example; the earlier four-card AI image was replaced for this test.

`build_report.py` now routes PDF/SVG figures to `vector_figure.py`. PDFs must be unencrypted and single-page; PDF text is converted to vector glyph outlines. Static SVG is embedded unchanged. DOCX contains an Office `asvg:svgBlip` relationship to the SVG and a PNG compatibility preview. Invalid/active/external SVG resources are rejected before rendering. Raster-only report builds retain their existing dependency path. The environment probe reports the optional PyMuPDF module separately from basic DOCX generation.

The actual chain was **built-in image generation → native editable PPTX → LibreOffice figure PDF → SVG → DOCX → LibreOffice report PDF**. The diagram follows [Vaswani et al., Figure 1](https://arxiv.org/abs/1706.03762); AI residual wiring was corrected, rather than treated as evidence. The source image, native reconstruction script, report draft and check script are retained under ignored `output/vector-e2e/`.

| Artifact/check | Observed result |
|---|---|
| PPTX slide XML | 52 native shapes/text boxes + 25 native connectors, 34 text runs, 0 pictures |
| Actual edit test | Changed `Encoder` to `Encoder QA` and one module's fill in a separate copy; saved, reopened and rendered successfully; original retained |
| Figure PDF | 1 page, 75 vector drawing objects, 432 text characters, 0 raster instances |
| Embedded SVG | 169,282 bytes, SVG part and relationship present, no `<image>` element; both DOCX routes contain the same SVG bytes |
| PDF-input DOCX export | 1 page, 444 vector drawing objects, 0 raster instances |
| SVG-input DOCX export | 1 page, 444 vector drawing objects, 0 raster instances |
| Visual review | Reconstructed figure, edited test copy and complete Chinese report inspected; readable labels, intact arrows, no clipped figure |

Counts are evidence of representation, not a scientific validation metric. Text outlines increase the report's path count. Native editing is supplied by PPTX; no native Word-shape editing is claimed. PNG previews in the DOCX package are expected, but the tested report exports contain no drawn raster instances.

Environment: macOS arm64; Python 3.12 based on the Codex bundled runtime with task-local optional packages; PyMuPDF 2.0; LibreOfficeDev `26.8.0.0.alpha0`, build `2c87e51eeaa2b413ff4ae097b2705eea1995d8e5`. The first PPT export inherited rasterized theme shadows; these were removed in the authoritative reconstruction script. Encoder residual routes were adjusted for renderer compatibility. The first report export lacked CJK glyphs because the bundled headless renderer did not find system fonts. The accepted report uses the installed `Songti SC` font and an export-process-only `FONTCONFIG_FILE=/opt/homebrew/etc/fonts/fonts.conf`; no global font configuration changed.

Companion-skill boundary: `nature-image2ppt` was inspected and its doctor eventually passed after missing packages were installed in the task environment. Its current manifest builder does not expose the required elbow route adjustments. The reconstruction therefore used the installed `python-pptx` library and the retained `build_transformer.py`; **no Image2PPT page/final QA pass is claimed**. It was not silently replaced by a picture-only presentation.

Reproduce from this checkout (use the interpreter/environment recorded in `output/vector-e2e/validation.json`; `python` below denotes an environment with python-docx, python-pptx and PyMuPDF):

```sh
python output/vector-e2e/build_transformer.py
soffice --headless --convert-to pdf --outdir output/vector-e2e/figure-export output/vector-e2e/transformer-editable.pptx
```

Derive the SVG through the same helper before `python output/vector-e2e/build_demo.py`:

```python
import sys
from pathlib import Path
sys.path.insert(0, "scripts")
from vector_figure import vector_assets
root = Path("output/vector-e2e")
svg, _ = vector_assets(root / "figure-export/transformer-editable.pdf")
(root / "transformer.svg").write_bytes(svg)
```

Export the DOCX to a fresh folder using the available renderer and real font configuration. `check_deliverables.py` checks the retained final artifacts and the disposable edit test, including native arrow ownership, DOCX relationships, matching SVG bytes and PDF raster instances. It is an evidence check, not an automatic recreation of the original AI image.

Deliverables: `output/vector-e2e/Transformer矢量插图验证.docx`, its checked `.pdf`, `transformer-editable.pptx`, `transformer-figure.pdf`, `transformer.svg`, `validation.json` and `provenance.json`. The figure source and verification scripts remain beside them. The duplicate SVG-input DOCX/PDF and edit-check PPT/PDF are retained as supporting evidence.

Validation: **46 tests passed**, including six new vector tests (relationships/PNG fallback, repeated images, direct PDF build, multipage failure preserving an existing report, static SVG boundaries and missing-dependency error). The skill-creator validator now passes in the prepared environment. Microsoft Word and WPS desktop rendering/editing remain unverified: WPS UI access returned a blank/offscreen dialog and then a ScreenCaptureKit error; no connected document session was available. No Windows execution, installed-skill sync, commit or push was performed. The one-page sample deliberately omits cover/TOC fields and does not supersede their earlier finalization caveats.

## Follow-up: writing quality and configurable subagents

This later policy supersedes the initial requested-only independent-review policy above. Substantial reports now use useful bounded specialists and one independent final review when enabled, available and permitted; small edits stay local. Defaults are centralized in `references/multi-agent-workflow.md`: `gpt-6.1-sol / medium` for evidence or bounded tasks, `gpt-6.1-sol / high` for independent review, at most two active workers and three worker tasks per report request. These are configurable starting settings, not benchmark-derived optima. First-use disclosure, preference reuse, capability checks and requested-versus-observed runtime settings are explicit. One full review and the shared two-repair limit remain in force; no nested delegation or duplicate main-agent full review.

Writing now follows assignment requirements and grading criteria, with main-agent integration of argument, terminology, numbers and citations. Central claims require passage/raw-result support and derived numbers require recalculation. QA distinguishes PASS, NEEDS_FIXES and UNVERIFIED on a specific build; missing checks cannot inflate completion. Measurement reuses the existing run record and does not equate claim coverage with report accuracy or promise a teacher's grade. Existing intake, review, format, figure and README instructions were reconciled with this policy; no new runtime dependency, model dispatcher or global configuration was added.

### Read-only forward scenarios

Two fresh-context subagents received the updated skill, only task-relevant references and synthetic cases, without repository history, expected answers or earlier review conclusions. They were forbidden from external actions, report generation and nested delegation. Both inherited the parent settings; actual runtime model/effort was not exposed. The parent assessed the returned actions against the user requirements and given evidence. These are policy simulations, not executed report workflows or a model-quality benchmark.

| Case and supplied condition | Observed response |
|---|---|
| A1: First 15-page review request with a Word template, unspecified format/AI; host supports default settings | Asked format with trade-offs and AI enablement; disclosed model/effort/cap; did not infer DOCX or begin drafting |
| A2: Typst, no AI, no subagents, two-paragraph polish | Reused all explicit choices; local edit and affected-content review only |
| A3: Existing explicit high-effort, concurrency-one preference; continued LaTeX report | Reused preference/disclosure and cumulative budgets; planned independent review after build |
| A4: Explicit final reviewer `gpt-6-astra / ultra`, unavailable on test host | Reported unavailability and supported alternatives; kept required review pending while continuing permitted evidence work |
| A5: Host permits inherited settings only and exposes neither value | Disclosed unknown settings; did not silently substitute or launch; self-review distinguished from independence |
| A6: Defaults disclosed, no adjustment; launch accepts requested settings without runtime confirmation | Used disclosed defaults without inventing explicit consent; recorded requested settings separately from unknown observed settings |
| E1: Verified source metadata, abstract reports association; draft asserts universal causation | Rejected causal/generalized claim, limited wording to the available evidence and identified missing methods/results |
| E2: 800 versus 840 correct out of the same 1,000 tests | Recomputed 4 percentage points and 5% relative improvement; removed unsupported cross-task generalization |
| E3: Native PPT/vector PDF/SVG-in-DOCX verified only through LibreOffice; Word required | Kept Word rendering/export gates UNVERIFIED; did not generalize LibreOffice results |
| E4: Three workers and two repairs exhausted, required citation unresolved, user requests delivery | Delivered only as pending/defective, with unresolved citation identified; no new worker or reset budget |
| E5: Four of six mandatory gates and nine of twelve key claims verified; no timing/token baseline | Reported 4/6 and 9/12 coverage; rejected 95% accuracy and doubled-speed claims |
| E6: Independent review passed OLD; table changed and NEW regenerated without checks | Required focused checks on NEW and downstream effects before calling it verified; did not reuse OLD's pass |

All 12 responses matched the targeted routing/evidence constraints in this single exercise. No real report, model-override dispatch, speed, token-use or acceptance-rate comparison was exercised. A defensible improvement claim still needs comparable reports and a recorded baseline.

The initial regression run found 45 passes and one obsolete assertion requiring the literal `Actor/Critic text review` label in the entrypoint. That assertion was removed; all semantic figure checks were retained, the affected nine tests passed, and the final full suite passed **46/46 tests**. Skill frontmatter validation, local links in all 23 maintained Markdown files (excluding macOS metadata sidecars) and `git diff --check` also passed. Final suite output is retained under `output/quality-and-subagents-2026-10-23/regression-tests.txt`.

Only the project working tree was updated; installed-skill synchronization, commit and push were not performed. Earlier uncommitted changes and previous vector artifacts were preserved.

## Release preparation — 2026-10-24

Before publishing the accumulated updates, code review found two font paths accidentally inserted into `label_position()`'s coordinate candidates. An actual annotation regression test reproduced `ValueError: too many values to unpack`. Removing those two entries preserves the macOS font candidates in `load_font()` while restoring label placement. The regression verifies that an annotated image contains the label and that the original image is unchanged.

The full suite now passes **47/47 tests** in the prepared macOS Python environment, including native LaTeX/Typst compilation and PDF/SVG-to-DOCX integration. This supersedes the earlier 46-test suite count without extending the platform or target-application claims. The 12 policy scenarios above were not rerun because their rules did not change.

Both READMEs now expose the three formats, configurable subagent defaults, installation/update guidance, platform-specific finalization and current verification limits. Shared Python examples no longer require PowerShell syntax. The existing skill identifier is retained. Historical September design notes are explicitly labeled as superseded; the original records remain intact. AppleDouble metadata is excluded through `.gitignore`.

Skill frontmatter validation, local links in 37 documentation files (excluding literal code examples and report-template placeholders), and `git diff --check` pass. Publishable text files were scanned for common credential patterns with no matches; this is a limited scan, not a security audit. Generated outputs and virtual environments remain excluded from publication. Project test output is retained locally at `output/release-2026-10-24/project-tests.txt`.
