# Optional AI image → editable PPT → PDF → report

Load only when the user selects PPT reconstruction or explicitly requests image-to-PPT work. This is an authorized alternative to direct AI-raster insertion, not a requirement for every report. Reuse the answer and share SKILL.md's repair budget; do not create an extra review loop.

## Preflight

Use the installed skill catalog to select an available reconstruction skill, such as `nature-image2ppt`, and read its instructions only now. Check the actual runtime/tool availability; a skill name in the catalog does not prove its dependencies work. Follow the selected skill's own artifact/QA contracts without inventing a second implementation or state ledger. If unavailable, use a suitable existing native-slide authoring tool when it can meet the same requirement; otherwise report the missing capability. Do not silently substitute an image-only PPT for editable reconstruction.

Confirm the chosen report format and target application, available PPT authoring/export tools and vector insertion route before committing to the figure workflow. No automatic skill/software installation. For complex photos, textures or artwork, identify parts that would remain raster; if that conflicts with the requested full-vector outcome, resolve it before production.

## Production

1. Generate or obtain the AI illustration as a composition reference, retaining its original file and provenance. For planned reconstruction, prompts may prioritize layout/structure; final verified labels and connectors will be authored natively. Do not regenerate solely for an AI spelling defect that will be replaced during reconstruction. Verify the scientific content independently.
2. Reconstruct each report figure as a tightly framed slide, using native editable text, shapes, connectors and appropriate equations/charts. Rebuild semantic elements rather than putting labels over a flattened full-slide bitmap. Correct factual or arrow errors from verified report content; do not faithfully reproduce an AI hallucination. Record any remaining raster subparts and keep them separate from editable diagram elements.
3. Save the editable `.pptx`, export the figure/slide to PDF using an available verified slide renderer, and inspect the exported result. Native objects should remain paths/text; export effects or retained raster assets can produce mixed content. Inspect object structure and the PDF, not merely the file extension or a zoomed screenshot. Preserve both PPTX and PDF.
4. Insert the figure through a vector-preserving route supported by the selected report application, then check the final report and its exported PDF. Keep formal captions in the report and PPT/AI provenance in the figure ledger. Edits return to the PPT source, then re-export and reinsert.

## Word insertion boundary

The requested route is editable PPT → exported PDF → Word figure. Do not promise that inserting a PDF object in Word makes the illustration native editable Word shapes or preserves all vector content: the stored object, displayed preview and exported report PDF can differ. Verify the actual target version of Word/WPS on Windows/macOS.

When direct PDF insertion cannot preserve the intended appearance/vector content, retain the PDF as the master export and derive a vector SVG from it (or export SVG from the same PPT source), then insert that SVG using a supported Office application/tool. Microsoft documents [SVG insertion/editing in Microsoft 365, including Mac](https://support.microsoft.com/en-us/office/graphics-visuals/edit-svg-images-in-microsoft-365); it also notes that [PDF conversion can lose document structure](https://support.microsoft.com/en-us/word/opening-pdfs-in-word). These do not establish WPS support or the behavior of a particular installed version.

`build_report.py` now accepts PDF/SVG in the existing Markdown figure syntax. It delegates these two formats to `scripts/vector_figure.py`; ordinary raster insertion is unchanged. The optional dependency is **PyMuPDF**, installed into the same Python environment that runs the builder. `check_environment.py` reports whether that dependency can be found; it does not prove rendering fidelity.

```sh
python -m pip install PyMuPDF
python scripts/build_report.py --draft report-draft.md --refs references.md --root . --output output/report.docx --title "Report title"
```

Use either input in the draft, with the usual caption and width rules:

```markdown
![Transformer architecture](figures/transformer.pdf)
图片宽度：15cm

![Transformer architecture](figures/transformer.svg)
图片宽度：15cm
```

The PDF must be an unencrypted **single-page** figure; export the desired slide separately. PDF paths remain paths and text becomes SVG glyph outlines to avoid receiving-machine font substitution. An SVG input is retained as supplied. Inputs must be self-contained static SVG: scripts, event handlers, DTDs, external file/network references, CSS imports and animated content are rejected. Use outlined text for portable SVG fonts. Embedded raster subparts remain raster; the converter does not trace them or certify vector purity. Complex SVG effects still need visual comparison.

The DOCX contains a normal PNG preview plus a separate `image/svg+xml` part referenced by Office's `asvg:svgBlip` extension. This is a vector picture, not an attached PDF object and not native editable Word shapes. Older or incompatible clients may use the PNG preview. A PNG in `word/media/` is therefore expected; its presence alone does not prove a rasterized report. Inspect the SVG relationship and, crucially, the **actual report export**. Rebuild from the original PDF/SVG path so later report builds retain the figure automatically.

## Verify the complete route

1. Inspect PPTX slide XML: text in `p:sp`, arrows in `p:cxnSp`, and no full-slide picture standing in for those objects. Modify a text run or shape in a disposable copy, save, reopen and render it. Preserve the unmodified source. Application selection/editing is an additional check when available.
2. Export the PPT to a fresh PDF location. Inspect the rendered page and PDF paths/text versus images. Remove unwanted shadows/glows if they create raster effects. With PyMuPDF, `page.get_drawings()`, `page.get_text()` and `page.get_image_info()` provide evidence about drawn content; counts alone do not prove semantic correctness.
3. Build the DOCX from that PDF, export the DOCX using the target application, and check its pages. For a pure-vector figure, visible content in the figure region must include paths/text and no raster image instances. For mixed figures, record precisely which subparts remain raster. Keep a render to verify labels/arrows were not lost or clipped.
4. Record the application/version, source hashes and result. LibreOffice proves its own export behavior; it does not prove Microsoft Word or WPS behavior. Deliver the PPTX, figure PDF, any SVG derivative, DOCX and checked report PDF together. See [the recorded Transformer run](../docs/verification-2026-10-23.md#transformer-vector-figure-end-to-end-run) for the actual tested scope.

If a chosen companion reconstruction tool cannot express required connector geometry, use an available native-slide library within the user's authorized scope and record that fallback. Do not report the companion tool's QA gates as passed. Preserve one reproducible source for the chosen route; do not patch only the final deck.

For LaTeX, use the verified PDF figure in the native project. For Typst, use a supported vector input such as SVG and verify the installed compiler's behavior; do not assume direct PDF-image support. Preserve the same PPTX/PDF source deliverables.

## Acceptance and delivery

- **Editable source:** diagram text/shapes/connectors can be selected and edited in PPT; an entire screenshot on a slide fails this criterion. Inspect the package/object structure and, when available, the target desktop application.
- **Vector preservation:** inspect the exported figure PDF and final report PDF for paths/text versus rasterized regions. A PDF/SVG wrapper around a bitmap is not vectorization. State any mixed vector/raster result precisely.
- **Appearance/content:** compare the reconstructed slide, figure PDF and inserted report figure for correct labels/arrows, Chinese fonts, clipping, cropping and insertion-size readability. Library/LibreOffice checks alone do not establish WPS/PowerPoint appearance.
- **Deliverables:** report, editable PPTX, exported figure PDF, insertion SVG if used, and source/provenance. Explain that editability is provided by the PPTX; do not imply object-level editing inside Word was verified unless it was.
