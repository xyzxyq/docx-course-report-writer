from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render_pdf_review_pages.py"


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
            "scripts/render_pdf_review_pages.py",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_contact_sheet_groups_four_pages_without_resizing_layout(self) -> None:
        spec = importlib.util.spec_from_file_location("render_pdf_review_pages", SCRIPT)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

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


if __name__ == "__main__":
    unittest.main()
