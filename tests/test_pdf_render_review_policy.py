from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render_pdf_review_pages.py"


def load_render_module():
    spec = importlib.util.spec_from_file_location("render_pdf_review_pages", SCRIPT)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class PdfRenderReviewPolicyTest(unittest.TestCase):
    def test_skill_documents_word_pdf_render_contact_sheet_review(self) -> None:
        files = [
            ROOT / "SKILL.md",
            ROOT / "references" / "windows-word-fields.md",
            ROOT / "references" / "tooling-recipes.md",
            ROOT / "references" / "report-qa-checklist.md",
            ROOT / "references" / "failure-patterns.md",
        ]
        combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

        required_phrases = [
            "Word COM update/export must happen before PDF page rendering",
            "render the final PDF pages to PNG",
            "four pages per contact sheet",
            "PDF page render images are not screenshots",
            "near-blank page",
            "blank-page detection",
            "scripts/render_pdf_review_pages.py",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_contact_sheet_groups_four_pages_without_resizing_layout(self) -> None:
        module = load_render_module()

        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            pages = []
            colors = ["red", "green", "blue", "yellow", "purple"]
            for index, color in enumerate(colors, 1):
                page = work / f"page-{index:02d}.png"
                Image.new("RGB", (120, 160), color=color).save(page)
                pages.append(page)

            sheets = module.make_contact_sheets(pages, work / "sheets", pages_per_sheet=4)

            self.assertEqual(2, len(sheets))
            with Image.open(sheets[0]) as first:
                self.assertEqual((240, 320), first.size)
            with Image.open(sheets[1]) as second:
                self.assertEqual((240, 320), second.size)
            self.assertEqual("review-sheet-01.png", sheets[0].name)
            self.assertEqual("review-sheet-02.png", sheets[1].name)

    def test_detects_near_blank_pages_before_contact_sheet_labels(self) -> None:
        module = load_render_module()

        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            blank = work / "page-01.png"
            content = work / "page-02.png"

            blank_image = Image.new("RGB", (300, 400), "white")
            ImageDraw.Draw(blank_image).text((150, 380), "2", fill="black")
            blank_image.save(blank)

            content_image = Image.new("RGB", (300, 400), "white")
            draw = ImageDraw.Draw(content_image)
            for y in range(50, 300, 20):
                draw.rectangle((40, y, 260, y + 8), fill="black")
            content_image.save(content)

            reports = module.analyze_pages([blank, content], blank_threshold=0.003)

            self.assertTrue(reports[0].is_blank)
            self.assertFalse(reports[1].is_blank)
            self.assertLess(reports[0].ink_ratio, 0.003)
            self.assertGreater(reports[1].ink_ratio, 0.003)

    def test_cli_fails_on_near_blank_pages_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            pages_dir = work / "pages"
            sheets_dir = work / "sheets"
            pages_dir.mkdir()

            blank = Image.new("RGB", (300, 400), "white")
            ImageDraw.Draw(blank).text((150, 380), "2", fill="black")
            blank.save(pages_dir / "page-01.png")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--from-pages-dir",
                    str(pages_dir),
                    "--sheets-dir",
                    str(sheets_dir),
                    "--blank-threshold",
                    "0.003",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertNotEqual(0, result.returncode)
            self.assertIn("BLANK_PAGE", result.stdout)


if __name__ == "__main__":
    unittest.main()
