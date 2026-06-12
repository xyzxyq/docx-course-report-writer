from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageChops, ImageDraw


@dataclass(frozen=True)
class PageReport:
    path: Path
    page_number: int
    ink_ratio: float
    bbox: tuple[int, int, int, int] | None
    is_blank: bool


def render_pdf_pages(
    pdf_path: Path,
    output_dir: Path,
    *,
    dpi: int = 150,
    poppler_path: str | None = None,
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        from pdf2image import convert_from_path

        pages = convert_from_path(
            str(pdf_path),
            dpi=dpi,
            fmt="png",
            poppler_path=poppler_path,
        )
        rendered: list[Path] = []
        for index, image in enumerate(pages, 1):
            out = output_dir / f"page-{index:02d}.png"
            image.save(out)
            rendered.append(out)
        return rendered
    except Exception as pdf2image_error:
        try:
            import pypdfium2 as pdfium
        except Exception as import_error:
            raise RuntimeError(
                "PDF rendering failed. Install/configure pdf2image+Poppler or pypdfium2."
            ) from import_error

        pdf = pdfium.PdfDocument(str(pdf_path))
        rendered = []
        scale = dpi / 72
        try:
            for index in range(len(pdf)):
                page = pdf[index]
                bitmap = page.render(scale=scale)
                image = bitmap.to_pil()
                out = output_dir / f"page-{index + 1:02d}.png"
                image.save(out)
                rendered.append(out)
        except Exception as pdfium_error:
            raise RuntimeError("PDF rendering failed with both pdf2image and pypdfium2.") from pdfium_error

        if not rendered:
            raise RuntimeError(f"No pages rendered from {pdf_path}") from pdf2image_error
        return rendered


def make_contact_sheets(
    image_paths: Iterable[Path],
    output_dir: Path,
    *,
    pages_per_sheet: int = 4,
    columns: int = 2,
    page_reports: Iterable[PageReport] | None = None,
) -> list[Path]:
    pages = [Path(path) for path in image_paths]
    if not pages:
        return []
    if pages_per_sheet < 1:
        raise ValueError("pages_per_sheet must be >= 1")
    if columns < 1:
        raise ValueError("columns must be >= 1")

    output_dir.mkdir(parents=True, exist_ok=True)
    rows = math.ceil(pages_per_sheet / columns)
    sheet_paths: list[Path] = []
    reports_by_path = {report.path.resolve(): report for report in page_reports or []}

    for sheet_index, start in enumerate(range(0, len(pages), pages_per_sheet), 1):
        chunk = pages[start : start + pages_per_sheet]
        with Image.open(chunk[0]) as first:
            page_width, page_height = first.size

        sheet = Image.new("RGB", (columns * page_width, rows * page_height), "white")
        for offset, image_path in enumerate(chunk):
            with Image.open(image_path) as image:
                page = image.convert("RGB")
                if page.size != (page_width, page_height):
                    page = page.resize((page_width, page_height), Image.LANCZOS)
                report = reports_by_path.get(image_path.resolve())
                draw = ImageDraw.Draw(page)
                label = f"page {start + offset + 1:02d}"
                if report and report.is_blank:
                    label += " BLANK"
                    draw.rectangle((0, 0, page.width - 1, page.height - 1), outline="red", width=8)
                draw.rectangle((8, 8, 190, 38), fill="white", outline="black")
                draw.text((16, 14), label, fill="red" if report and report.is_blank else "black")
                x = (offset % columns) * page_width
                y = (offset // columns) * page_height
                sheet.paste(page, (x, y))

        out = output_dir / f"review-sheet-{sheet_index:02d}.png"
        sheet.save(out)
        sheet_paths.append(out)

    return sheet_paths


def analyze_pages(image_paths: Iterable[Path], *, blank_threshold: float = 0.003) -> list[PageReport]:
    reports: list[PageReport] = []
    for index, path in enumerate(image_paths, 1):
        image_path = Path(path)
        with Image.open(image_path) as image:
            gray = image.convert("L")
            histogram = gray.histogram()
            pixels = gray.width * gray.height
            ink_pixels = sum(histogram[:245])
            ink_ratio = ink_pixels / pixels if pixels else 0.0
            bbox = ImageChops.difference(gray, Image.new("L", gray.size, 255)).getbbox()
        reports.append(
            PageReport(
                path=image_path,
                page_number=index,
                ink_ratio=ink_ratio,
                bbox=bbox,
                is_blank=ink_ratio < blank_threshold,
            )
        )
    return reports


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render final PDF pages to PNG and combine every four pages into review sheets."
    )
    parser.add_argument("--pdf", type=Path, help="Final PDF exported after Word field update.")
    parser.add_argument("--pages-dir", type=Path, help="Directory for rendered page PNG files.")
    parser.add_argument("--from-pages-dir", type=Path, help="Use existing page-*.png files instead of rendering a PDF.")
    parser.add_argument("--sheets-dir", required=True, type=Path, help="Directory for four-page review sheets.")
    parser.add_argument("--dpi", type=int, default=150)
    parser.add_argument("--poppler-path", default=None)
    parser.add_argument("--pages-per-sheet", type=int, default=4)
    parser.add_argument("--blank-threshold", type=float, default=0.003)
    parser.add_argument("--allow-blank-pages", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.from_pages_dir:
        pages = sorted(args.from_pages_dir.glob("page-*.png"))
        if not pages:
            raise SystemExit(f"No page-*.png files found in {args.from_pages_dir}")
    else:
        if not args.pdf or not args.pages_dir:
            raise SystemExit("--pdf and --pages-dir are required unless --from-pages-dir is used")
        pages = render_pdf_pages(args.pdf, args.pages_dir, dpi=args.dpi, poppler_path=args.poppler_path)

    reports = analyze_pages(pages, blank_threshold=args.blank_threshold)
    sheets = make_contact_sheets(pages, args.sheets_dir, pages_per_sheet=args.pages_per_sheet, page_reports=reports)
    print(f"Rendered pages: {len(pages)}")
    print(f"Review sheets: {len(sheets)}")
    for report in reports:
        status = "BLANK_PAGE" if report.is_blank else "PAGE_OK"
        print(f"{status} page={report.page_number:02d} ink_ratio={report.ink_ratio:.6f} file={report.path}")
    for path in sheets:
        print(path)
    blank_pages = [report for report in reports if report.is_blank]
    if blank_pages and not args.allow_blank_pages:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
