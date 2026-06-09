# Chinese DOCX Style

Use the template or user-polished report as the source of truth. Use these defaults only when the template does not clearly define a stronger standard.

## Body Text

- Chinese font: 宋体
- Size: 小四 / 10.5 pt
- First-line indent: 2 Chinese characters
- Line spacing: 1.25
- Paragraph spacing: modest, usually 0 pt before and about 6 pt after
- English and numbers: Times New Roman or another template-consistent Latin font
- Technical inline tokens: use consistent Latin/code font without disrupting Chinese body rhythm

## Page Setup

- A4 paper unless the template or assignment says otherwise.
- Typical margins: top/bottom 2.54 cm, left 3.0 cm, right 2.6 cm.
- Preserve template section breaks, page numbers, headers, and footers when they are useful.
- Avoid unnecessary blank pages after rebuilding from a prior report.

## Headings

- Use real Word `Heading 1`, `Heading 2`, and `Heading 3` styles so the automatic TOC works.
- Heading 1: bold Chinese heading font such as 黑体, chapter-level spacing, centered if the template uses chapter-style headings.
- Heading 2/3: bold, left aligned unless the template says otherwise.
- Keep spacing stable: headings should not collide with previous body text or float alone at the bottom of a page.
- Typical spacing: Heading 1 has about 12 pt before and 6 pt after; Heading 2 has about 10 pt before and 4 pt after.

## Table Of Contents

- The TOC must be an automatic Word field, not hand-typed text.
- TOC page title should be centered, bold, and visually separated from entries.
- TOC entries must show a clear hierarchy:
  - level 1: no left indent, larger/bolder than sublevels
  - level 2: modest left indent
  - level 3: deeper left indent and slightly smaller font
- Use dot leaders and right-aligned page numbers when Word supports them.
- Avoid cramped TOC pages: line spacing should be about 1.15-1.25, with enough paragraph spacing that entries scan cleanly.
- After Word field update, inspect the exported PDF TOC page. A TOC that is technically automatic but visually cluttered, flat, over-dense, or hard to scan fails QA.
- If the template's TOC styling is weak, override Word `TOC 1`, `TOC 2`, and `TOC 3` styles before field update.

## Captions

- Figure caption format: `图X ...`
- Table caption format: `表X ...`
- Captions should be centered and close to the figure/table they describe.
- Avoid isolated captions on a separate page from their figure/table.

## Tables

- Use a restrained academic style.
- Center the table on the page.
- Set table width deliberately; do not leave arbitrary default widths.
- Header cells: bold, centered, vertically centered.
- Header fill: avoid decoration by default, but light blue-gray or neutral gray is acceptable when the template uses it, the user asks for prettier tables, or dense tables need clearer scanning.
- Body cells: vertically centered.
- Short identifier columns, command columns, file-name columns, and status columns: center aligned.
- Long explanation/result columns: left aligned.
- Prefer several focused tables over one oversized table:
  - requirement-to-implementation mapping
  - environment summary
  - file responsibility table
  - protocol/API format table
  - normal test cases
  - abnormal/error test cases
- Review column widths in the exported PDF. Long Chinese cells should wrap cleanly without squeezing key command names or labels.

## Code Blocks

- Font: Consolas for code, with Chinese fallback when needed.
- Size: about 9.5-10.5 pt.
- Background: light gray such as `F5F5F5`.
- Preserve indentation.
- Keep snippets short and tied to report claims.
- Avoid dumping full source files unless the assignment explicitly requires it.
- Add a short lead-in sentence before code blocks so the reader knows why the snippet matters.

## Images

- Center figures.
- Size them for readability in exported PDF, not only in Word editing view.
- Leave stable spacing before/after images and captions.
- For terminal screenshots, crop enough to focus the output but keep command/result context.

## Visual QA

Always inspect the exported PDF or rendered pages for:

- clipped text
- table overflow
- unreadable screenshots
- awkward page breaks
- isolated captions
- excessive blank space
- old template images or topic residue
