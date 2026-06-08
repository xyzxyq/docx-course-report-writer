#!/usr/bin/env python3
"""Build a Chinese course-report DOCX from a lightweight markdown draft."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt


SOURCE_PREFIX = "图片来源："
WIDTH_PREFIX = "图片宽度："
DEFAULT_TEMPLATE_PATH = Path(__file__).resolve().parents[1] / "skill-assets" / "default-course-report-template.docx"


def set_run_font(
    run,
    east_asia: str = "宋体",
    latin: str = "Times New Roman",
    size: float = 10.5,
    bold: bool | None = None,
) -> None:
    run.font.name = latin
    run.font.size = Pt(size)
    if bold is not None:
        run.font.bold = bold
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    rfonts.set(qn("w:eastAsia"), east_asia)
    rfonts.set(qn("w:ascii"), latin)
    rfonts.set(qn("w:hAnsi"), latin)


def set_style_font(
    style,
    east_asia: str = "宋体",
    latin: str = "Times New Roman",
    size: float = 10.5,
    bold: bool | None = None,
) -> None:
    style.font.name = latin
    style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    rpr = style._element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    rfonts.set(qn("w:eastAsia"), east_asia)
    rfonts.set(qn("w:ascii"), latin)
    rfonts.set(qn("w:hAnsi"), latin)


def ensure_heading_styles(doc: Document) -> None:
    for level, size in ((1, 16), (2, 14), (3, 12)):
        name = f"Heading {level}"
        try:
            style = doc.styles[name]
        except KeyError:
            style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
            style.base_style = doc.styles["Normal"]
        set_style_font(style, east_asia="黑体", size=size, bold=True)
        ppr = style._element.get_or_add_pPr()
        outline = ppr.find(qn("w:outlineLvl"))
        if outline is None:
            outline = OxmlElement("w:outlineLvl")
            ppr.append(outline)
        outline.set(qn("w:val"), str(level - 1))


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_paragraph_shading(paragraph, fill: str) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    shd = p_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        p_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def configure_document(doc: Document) -> None:
    for section in doc.sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(2.6)

    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(10.5)
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")
    ensure_heading_styles(doc)


def parse_markdown_table(lines: list[str], start: int) -> tuple[list[str], list[list[str]], int]:
    rows: list[str] = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        rows.append(lines[i].strip())
        i += 1
    header = [c.strip() for c in rows[0].strip("|").split("|")]
    body = [[c.strip() for c in row.strip("|").split("|")] for row in rows[2:]]
    return header, body, i


def parse_width_cm(text: str) -> float:
    return float(text.replace("cm", "").strip())


def parse_tokens(text: str) -> list[tuple[str, Any]]:
    lines = text.splitlines()
    tokens: list[tuple[str, Any]] = []
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == "{{REFERENCES}}":
            tokens.append(("references", None))
            i += 1
            continue

        if stripped.startswith("```"):
            language = stripped.strip("`").strip()
            i += 1
            code_lines: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i].rstrip("\n"))
                i += 1
            if i < len(lines):
                i += 1
            tokens.append(("code", {"language": language, "text": "\n".join(code_lines)}))
            continue

        if stripped.startswith("# "):
            tokens.append(("h1", stripped[2:].strip()))
            i += 1
            continue

        if stripped.startswith("## "):
            tokens.append(("h2", stripped[3:].strip()))
            i += 1
            continue

        if stripped.startswith("### "):
            tokens.append(("h3", stripped[4:].strip()))
            i += 1
            continue

        if stripped.startswith("!["):
            match = re.match(r"!\[(.+?)\]\((.+?)\)", stripped)
            if not match:
                raise ValueError(f"Invalid figure markdown: {stripped}")

            caption, path = match.group(1), match.group(2)
            source = ""
            width_cm = 11.8

            if i + 1 < len(lines) and lines[i + 1].strip().startswith(SOURCE_PREFIX):
                source = lines[i + 1].strip()
                i += 1

            if i + 1 < len(lines) and lines[i + 1].strip().startswith(WIDTH_PREFIX):
                width_line = lines[i + 1].strip().split("：", 1)[1]
                width_cm = parse_width_cm(width_line)
                i += 1

            tokens.append(("figure", {"caption": caption, "path": path, "source": source, "width_cm": width_cm}))
            i += 1
            continue

        if stripped.startswith("|"):
            header, body, i = parse_markdown_table(lines, i)
            tokens.append(("table", {"header": header, "rows": body}))
            continue

        block = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt:
                i += 1
                break
            if nxt.startswith(("# ", "## ", "### ", "![", "|", "```")) or nxt == "{{REFERENCES}}":
                break
            block.append(nxt)
            i += 1
        tokens.append(("p", " ".join(block)))

    return tokens


def preserve_template_opening(doc: Document, keep_paragraphs: int) -> None:
    body = doc._element.body
    seen = 0
    for child in list(body):
        if child.tag.endswith("}sectPr"):
            continue
        if child.tag.endswith("}p"):
            seen += 1
            if seen <= keep_paragraphs:
                continue
        body.remove(child)


def clear_document_body(doc: Document) -> None:
    body = doc._element.body
    for child in list(body):
        if not child.tag.endswith("}sectPr"):
            body.remove(child)


def resolve_template(args: argparse.Namespace) -> tuple[Path | None, bool]:
    if args.template:
        return args.template, False
    if not args.no_default_template and DEFAULT_TEMPLATE_PATH.exists():
        return DEFAULT_TEMPLATE_PATH, True
    return None, False


def add_body_paragraph(doc: Document, text: str, indent: bool = True) -> None:
    paragraph = doc.add_paragraph(style="Normal")
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph.paragraph_format.line_spacing = 1.25
    paragraph.paragraph_format.space_after = Pt(6)
    if indent:
        paragraph.paragraph_format.first_line_indent = Pt(21)
    run = paragraph.add_run(text)
    set_run_font(run, size=10.5)


def add_heading(doc: Document, text: str, level: int) -> None:
    style = {1: "Heading 1", 2: "Heading 2", 3: "Heading 3"}[level]
    paragraph = doc.add_paragraph(style=style)
    if level == 1:
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.space_before = Pt({1: 12, 2: 10, 3: 8}[level])
    paragraph.paragraph_format.space_after = Pt({1: 6, 2: 4, 3: 4}[level])
    run = paragraph.add_run(text)
    set_run_font(run, east_asia="黑体", size={1: 16, 2: 14, 3: 12}[level], bold=True)


def add_toc_field(doc: Document) -> None:
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("目录")
    set_run_font(run, east_asia="黑体", size=16, bold=True)

    paragraph = doc.add_paragraph()
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), 'TOC \\o "1-3" \\h \\z \\u')
    run_el = OxmlElement("w:r")
    text_el = OxmlElement("w:t")
    text_el.text = "目录将在 Word 中更新。"
    run_el.append(text_el)
    fld.append(run_el)
    paragraph._p.append(fld)


def add_figure(doc: Document, payload: dict[str, Any], root: Path) -> None:
    fig_path = (root / str(payload["path"])).resolve()
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.space_before = Pt(6)
    paragraph.add_run().add_picture(str(fig_path), width=Cm(float(payload.get("width_cm", 11.8))))

    caption = doc.add_paragraph()
    caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
    caption.paragraph_format.space_after = Pt(6)
    run = caption.add_run(str(payload["caption"]))
    set_run_font(run, size=10.5)

    source = str(payload.get("source", "")).strip()
    if source:
        source_para = doc.add_paragraph()
        source_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        source_para.paragraph_format.space_after = Pt(6)
        run = source_para.add_run(source)
        set_run_font(run, size=9.5)


def add_table(doc: Document, payload: dict[str, Any]) -> None:
    rows = payload["rows"]
    header = payload["header"]
    table = doc.add_table(rows=len(rows) + 1, cols=len(header))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    for col, text in enumerate(header):
        cell = table.cell(0, col)
        cell.text = ""
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_cell_shading(cell, "D9EAF7")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        set_run_font(run, east_asia="宋体", size=10.5, bold=True)

    for row_i, row in enumerate(rows, start=1):
        for col, text in enumerate(row):
            cell = table.cell(row_i, col)
            cell.text = ""
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if len(str(text)) <= 18 else WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(str(text))
            set_run_font(run, size=10.5)

    doc.add_paragraph()


def add_code_block(doc: Document, payload: dict[str, str]) -> None:
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    set_cell_shading(cell, "F5F5F5")
    cell.text = ""
    paragraph = cell.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.space_before = Pt(4)
    paragraph.paragraph_format.space_after = Pt(4)
    run = paragraph.add_run(payload["text"])
    set_run_font(run, east_asia="宋体", latin="Consolas", size=9.5)
    doc.add_paragraph()


def add_references(doc: Document, refs_path: Path) -> None:
    if not refs_path.exists():
        return
    for line in refs_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            add_body_paragraph(doc, line.strip(), indent=False)


def build(args: argparse.Namespace) -> None:
    template_path, _used_default_template = resolve_template(args)
    if template_path:
        doc = Document(str(template_path))
        if args.keep_template_body:
            pass
        elif args.preserve_cover_paragraphs > 0:
            preserve_template_opening(doc, args.preserve_cover_paragraphs)
        else:
            clear_document_body(doc)
    else:
        doc = Document()

    configure_document(doc)

    if not args.no_toc:
        if template_path and (args.keep_template_body or args.preserve_cover_paragraphs > 0):
            doc.add_page_break()
        add_toc_field(doc)
        doc.add_page_break()

    tokens = parse_tokens(args.draft.read_text(encoding="utf-8"))
    for kind, payload in tokens:
        if kind == "h1":
            add_heading(doc, str(payload), 1)
        elif kind == "h2":
            add_heading(doc, str(payload), 2)
        elif kind == "h3":
            add_heading(doc, str(payload), 3)
        elif kind == "p":
            add_body_paragraph(doc, str(payload))
        elif kind == "figure":
            add_figure(doc, payload, args.root)
        elif kind == "table":
            add_table(doc, payload)
        elif kind == "code":
            add_code_block(doc, payload)
        elif kind == "references":
            add_references(doc, args.refs)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(args.output))


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a Chinese course-report DOCX.")
    parser.add_argument("--draft", type=Path, required=True)
    parser.add_argument("--refs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--template", type=Path)
    parser.add_argument("--no-default-template", action="store_true")
    parser.add_argument("--keep-template-body", action="store_true")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--preserve-cover-paragraphs", type=int, default=0)
    parser.add_argument("--no-toc", action="store_true")
    build(parser.parse_args())


if __name__ == "__main__":
    main()
