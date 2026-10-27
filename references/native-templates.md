# Native report templates

Copy the entire `skill-assets/latex/` or `skill-assets/typst/` directory into the user's report workspace before editing. Replace metadata, instructional sample chapters and sample bibliography with verified report content. Keep the reusable originals unchanged. Existing user-native projects take precedence.

## Mapping from the built-in DOCX

The Word asset's A4 page is approximately 210 × 297 mm with four 25.4 mm margins. Its visible cover contains course, title, college, major, name, student ID, teacher and date. The native templates preserve those fields, a separate automatic TOC, chapter/section hierarchy, figure/table captions, references on a new page and body page 1 after unnumbered front matter. The empty logo placeholder is omitted; add only a supplied/authorized logo.

The legacy Word file has inconsistent style metadata: body style 11 pt/1.25 spacing, normal style 10.5 pt, and instructional text claiming 小四/1.5 spacing. Native body defaults use 10.5 pt, two-character indent and 16/14/12 pt headings. Typst explicitly targets a 17 pt body baseline gap, matching the measured reading rhythm of the LaTeX report; numeric spacing settings are not interchangeable between engines. They are a normalized adaptation, not an exact page-for-page conversion. Long titles/names and font substitutions require fresh page review. A strict school template overrides these defaults.

## LaTeX

- Entry: `main.tex`; bibliography: `references.bib`.
- Requires latexmk, XeLaTeX, ctex, Fandol, gbt7714/BibTeX, geometry, caption, graphicx, booktabs, amsmath and hyperref (available in a full TeX Live installation). Do not install an entire distribution without checking the host first.
- CJK uses TeX Live's Fandol explicitly for portability; Latin uses Times New Roman when available, otherwise TeX Gyre Termes. These are declared substitutions from Word fonts, not a guarantee of identical glyph metrics.
- Change the `\Report...` metadata commands. Write native chapters/sections, `\label` / `\ref`, and `\cite{key}`. Use `\bibliographystyle{gbt7714-numerical}` once; that style selects superscript numeric citations. Avoid the obsolete `super` package option, which also inserts a bibliography-style command.
- latexmk handles internal passes for TOC/BibTeX/reference convergence. These are compiler passes, not extra agent review rounds. Do not manually invoke repeated identical builds after convergence.

## Typst

- Entry: `main.typ`; bibliography: `references.bib`.
- Requires Typst and installed CJK/Latin fonts. Run `typst fonts` once, then set the three font variables at the top. Defaults suit macOS: Songti SC, Heiti SC, Times New Roman. Windows commonly uses SimSun, SimHei, Times New Roman; Noto CJK is another explicit option if installed. Do not silently accept missing-font warnings.
- Readability defaults: 10.5 pt body, explicit text edges totaling 1 em plus 6.5 pt leading (17 pt baseline gap), 12.5 pt paragraph spacing, and heading block spacing of 24 pt above / 12 pt below. Bibliography uses 10 pt text with 4 pt leading and 10 pt paragraph spacing. Typst's [leading](https://typst.app/docs/reference/model/par/#parameters-leading) is the gap between text frames, not a line-spacing multiplier. Check actual PDF line distances and title/paragraph separation; fewer pages or absence of clipping does not establish readable density.
- Edit cover variables; use native headings, `@label` and `@bibliography-key`. The built-in `gb-7714-2015-numeric` CSL style provides the citation/bibliography format. Confirm actual typography against the assignment. See the [official bibliography documentation](https://typst.app/docs/reference/model/bibliography/).
- Figure/table counters reset per chapter. Cross-chapter references resolve the heading counter at the target location using the [counter location API](https://typst.app/docs/reference/introspection/counter/), so a table in chapter 2 remains table 2.1 when cited from chapter 3.

## Build and review

Use the commands in output-formats.md with the copied project's root. Deliver PDF plus source snapshot, bibliography and assets. Review compiler output and rendered pages for missing fonts, unresolved labels, cover spillover and citation placement. The included sample is for template validation only; it is not a completed student report or experimental evidence.
