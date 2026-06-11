from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AIImagePromptingPolicyTest(unittest.TestCase):
    def test_prompting_reference_requires_information_architecture_before_style(self) -> None:
        text = (ROOT / "references" / "ai-image-prompting.md").read_text(encoding="utf-8")

        required_phrases = [
            "information architecture first, visual style second",
            "specific knowledge point",
            "named modules",
            "directional relationships",
            "labels, arrows, legend, and layering",
            "decorative element must have a semantic function",
            "Generic tech aesthetic words are insufficient",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_prompt_card_contains_semantic_diagram_fields(self) -> None:
        text = (ROOT / "references" / "ai-image-prompting.md").read_text(encoding="utf-8")

        required_fields = [
            "- Knowledge point explained:",
            "- Named modules:",
            "- Directional relationships:",
            "- Label/arrow/legend/layer plan:",
            "- Semantic decoration rule:",
        ]

        for field in required_fields:
            with self.subTest(field=field):
                self.assertIn(field, text)

    def test_architecture_figures_require_readable_final_labels(self) -> None:
        text = (ROOT / "references" / "ai-image-prompting.md").read_text(encoding="utf-8")

        required_phrases = [
            "Architecture, schematic, flowchart, pipeline, and model-structure figures must have readable final text labels",
            "one-pass text-to-image",
            "No post-generation label overlay",
            "Final text labels are required",
            "If generated text is wrong, reject and regenerate",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

        forbidden_phrases = [
            "deterministic overlay",
            "Add all labels, arrows, and factual values with deterministic tooling",
            "labels added after generation",
        ]

        for phrase in forbidden_phrases:
            with self.subTest(forbidden=phrase):
                self.assertNotIn(phrase, text)

    def test_main_skill_blocks_empty_ai_concept_art(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("information architecture", text)
        self.assertIn("named modules", text)
        self.assertIn("directional relationships", text)
        self.assertIn("readable final text labels", text)
        self.assertIn("one-pass text-to-image", text)
        self.assertIn("must be regenerated", text)


if __name__ == "__main__":
    unittest.main()
