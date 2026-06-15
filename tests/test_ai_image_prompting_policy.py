from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AIImagePromptingPolicyTest(unittest.TestCase):
    def test_prompting_reference_requires_information_architecture_before_style(self) -> None:
        text = (ROOT / "references" / "ai-image-prompting.md").read_text(encoding="utf-8")

        required_phrases = [
            "information architecture first, visual style second",
            "knowledge-structure-driven",
            "one core question",
            "specific knowledge point",
            "named modules",
            "required knowledge modules",
            "directional relationships",
            "labels, arrows, legend, and layering",
            "decorative element must have a semantic function",
            "Generic tech aesthetic words are insufficient",
            "teaching information graphic",
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
            "Reject or regenerate when visible text is unreadable",
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

    def test_prompting_reference_rejects_empty_ai_tech_poster_style(self) -> None:
        text = (ROOT / "references" / "ai-image-prompting.md").read_text(encoding="utf-8")

        required_phrases = [
            "not a technology poster",
            "Do not use futuristic AI artwork",
            "Do not add meaningless glowing lines",
            "Do not add random servers",
            "Do not add random cubes",
            "Do not pile up abstract neural-network decoration",
            "Every visible element must map to a named concept",
            "paper overview figure",
            "system pipeline figure",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_prompting_reference_contains_training_flow_template(self) -> None:
        text = (ROOT / "references" / "ai-image-prompting.md").read_text(encoding="utf-8")

        required_modules = [
            "Training Data",
            "Preprocessing",
            "Neural Network",
            "Forward Pass",
            "Prediction",
            "Label",
            "Loss Function",
            "Backpropagation",
            "Optimizer / Update Weights",
            "Inference Output",
        ]

        for module in required_modules:
            with self.subTest(module=module):
                self.assertIn(module, text)

    def test_prompting_reference_uses_text_review_not_whitelist(self) -> None:
        text = (ROOT / "references" / "ai-image-prompting.md").read_text(encoding="utf-8")

        required_phrases = [
            "Visible text plan",
            "not a strict whitelist",
            "reasonable extra text",
            "Actor/Critic text review",
            "readable, accurate, relevant, and non-garbled",
            "Do not reject a figure only because it contains useful text outside the initial plan",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

        forbidden_phrases = [
            "exact whitelist",
            "text whitelist",
            "Visible text whitelist",
            "Allowed visible text",
            "match the whitelist",
            "must render only those labels",
        ]

        for phrase in forbidden_phrases:
            with self.subTest(forbidden=phrase):
                self.assertNotIn(phrase, text)

    def test_main_skill_blocks_empty_ai_concept_art(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("information architecture", text)
        self.assertIn("knowledge-structure-driven", text)
        self.assertIn("named modules", text)
        self.assertIn("directional relationships", text)
        self.assertIn("readable final text labels", text)
        self.assertIn("one-pass text-to-image", text)
        self.assertIn("must be regenerated", text)
        self.assertIn("visible text plan", text)
        self.assertIn("Actor/Critic text review", text)
        self.assertNotIn("text whitelist", text)

    def test_deterministic_diagrams_prioritize_tikz_before_python(self) -> None:
        text = (ROOT / "references" / "figures-and-diagrams.md").read_text(encoding="utf-8")

        required_phrases = [
            "LaTeX TikZ > Python",
            "prefer LaTeX TikZ before Python",
            "Use Python only when TikZ is unsuitable",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_report_ai_images_must_use_user_top_level_imagegen_not_system_skill(self) -> None:
        combined_text = "\n".join(
            [
                (ROOT / "SKILL.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "figures-and-diagrams.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "workflow.md").read_text(encoding="utf-8"),
            ]
        )

        required_phrases = [
            "$CODEX_HOME/skills/imagegen/SKILL.md",
            "$CODEX_HOME/skills/.system/imagegen/SKILL.md",
            "two different skills",
            "does not require `OPENAI_API_KEY`",
            "Do not check `OPENAI_API_KEY`",
            "Never route report text-to-image work through `.system/imagegen`",
            "unless the user explicitly requests `.system/imagegen`",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined_text)

    def test_skill_docs_do_not_hardcode_user_home_paths(self) -> None:
        docs = [
            ROOT / "SKILL.md",
            ROOT / "references" / "figures-and-diagrams.md",
            ROOT / "references" / "workflow.md",
            ROOT / "references" / "template-fidelity.md",
            ROOT / "references" / "tooling-recipes.md",
            ROOT / "references" / "windows-word-fields.md",
        ]
        forbidden = "C:" + "\\Users" + "\\20795"

        for doc in docs:
            text = doc.read_text(encoding="utf-8")
            with self.subTest(doc=doc.relative_to(ROOT)):
                self.assertNotIn(forbidden, text)

    def test_tikz_figure_is_mandatory_for_nontrivial_reports(self) -> None:
        combined_text = "\n".join(
            [
                (ROOT / "SKILL.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "figures-and-diagrams.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "intake-and-run-record.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "report-qa-checklist.md").read_text(encoding="utf-8"),
            ]
        )

        required_phrases = [
            "at least one LaTeX TikZ figure",
            "mandatory unless the user explicitly forbids TikZ",
            "Minimum LaTeX TikZ figures to insert: 1",
            "TikZ minimum gate",
            "A nontrivial report with zero TikZ figures fails this gate",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined_text)

    def test_windows_chinese_encoding_fix_is_documented(self) -> None:
        text = (ROOT / "references" / "figures-and-diagrams.md").read_text(encoding="utf-8")

        required_phrases = [
            "Chinese text on Windows",
            "Chinese labels inside figures",
            "PowerShell pipeline",
            "mojibake",
            "write a UTF-8 source file",
            "do not pipe Chinese source code",
            "XeLaTeX",
            "CJK font",
            "inspect the rendered figure",
        ]

        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
