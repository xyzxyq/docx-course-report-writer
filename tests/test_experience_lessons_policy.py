from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExperienceLessonsPolicyTest(unittest.TestCase):
    def test_main_skill_routes_to_history_derived_experience_lessons(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("references/experience-lessons.md", text)
        self.assertIn("history-derived experience", text)

    def test_experience_lessons_capture_recent_practice_failures(self) -> None:
        text = (ROOT / "references" / "experience-lessons.md").read_text(encoding="utf-8")

        required_phrases = [
            "History-Derived Experience Lessons",
            "35 task-level samples",
            "PDF page renders",
            "contact sheets are an index, not the proof",
            "blank or near-blank page",
            "user feedback becomes a failed QA test",
            "copy-first template editing",
            "GB/T 7714-2015",
            "TikZ",
            "WSL",
            "top-level imagegen",
            "one-pass text-to-image",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_visual_qa_requires_individual_page_review_not_only_contact_sheets(self) -> None:
        qa_text = (ROOT / "references" / "report-qa-checklist.md").read_text(encoding="utf-8")
        tooling_text = (ROOT / "references" / "tooling-recipes.md").read_text(encoding="utf-8")

        for text in (qa_text, tooling_text):
            self.assertIn("every rendered page", text)
            self.assertIn("contact sheets are an index, not the proof", text)
            self.assertIn("blank or near-blank page", text)

    def test_pdf_review_renderer_script_has_help(self) -> None:
        script = ROOT / "scripts" / "render_pdf_review_pages.py"
        result = subprocess.run(
            [sys.executable, str(script), "--help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("render PDF pages to PNG", result.stdout)
        self.assertIn("--contact-sheet-cols", result.stdout)
        self.assertIn("--blank-threshold", result.stdout)


if __name__ == "__main__":
    unittest.main()
