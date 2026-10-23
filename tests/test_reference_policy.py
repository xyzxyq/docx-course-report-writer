from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReferencePolicyTest(unittest.TestCase):
    def test_main_skill_requires_gbt7714_verified_references_before_drafting(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        required_phrases = [
            "GB/T 7714-2015",
            "Reference Metadata Ledger",
            "before drafting",
            "Do not invent reference metadata",
            "DOI",
            "superscript bracketed numeric citations",
            "reference list typography",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_source_quality_locks_reference_metadata_and_forbids_hallucinations(self) -> None:
        text = (ROOT / "references" / "source-quality.md").read_text(encoding="utf-8")

        required_phrases = [
            "Reference Metadata Lock",
            "before drafting claims that cite it",
            "Do not invent",
            "DOI resolver",
            "Crossref",
            "publisher page",
            "GB/T 7714-2015",
            "reference type marker",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_review_and_record_route_to_shared_reference_checks(self) -> None:
        for name in ["actor-critic-loop.md", "intake-and-run-record.md"]:
            text = (ROOT / "references" / name).read_text(encoding="utf-8")
            self.assertIn("report-qa-checklist.md", text)
        qa = (ROOT / "references" / "report-qa-checklist.md").read_text(encoding="utf-8")
        for phrase in ["reference hallucination", "GB/T 7714-2015",
                       "superscript bracketed numeric citations", "reference list typography"]:
            self.assertIn(phrase, qa)

    def test_reference_template_requires_verified_metadata_fields(self) -> None:
        text = (ROOT / "skill-assets" / "references-template.md").read_text(encoding="utf-8")

        required_phrases = [
            "GB/T 7714-2015",
            "Verified metadata source",
            "DOI",
            "Do not cite",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
