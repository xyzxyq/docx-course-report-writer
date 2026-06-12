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
            "No report drafting may start until",
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

    def test_run_record_contains_reference_ledger_and_final_reference_gates(self) -> None:
        text = (ROOT / "references" / "intake-and-run-record.md").read_text(encoding="utf-8")

        required_phrases = [
            "Reference Metadata Ledger",
            "GB/T 7714-2015 format source",
            "Verified DOI or canonical URL",
            "In-text citation style",
            "Reference hallucination audit",
            "Reference typography audit",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_actor_critic_and_qa_check_reference_content_and_format(self) -> None:
        actor_critic = (ROOT / "references" / "actor-critic-loop.md").read_text(encoding="utf-8")
        qa = (ROOT / "references" / "report-qa-checklist.md").read_text(encoding="utf-8")

        for phrase in [
            "reference hallucination",
            "GB/T 7714-2015",
            "superscript bracketed numeric citations",
            "reference list typography",
        ]:
            with self.subTest(file="actor-critic-loop.md", phrase=phrase):
                self.assertIn(phrase, actor_critic)
            with self.subTest(file="report-qa-checklist.md", phrase=phrase):
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
