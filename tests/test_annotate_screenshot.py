from pathlib import Path
import sys
import tempfile
import unittest

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from annotate_screenshot import annotate


class ScreenshotAnnotationTest(unittest.TestCase):
    def test_annotation_writes_label_and_preserves_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.png"
            output = Path(tmp) / "annotated.png"
            Image.new("RGB", (300, 200), "white").save(source)
            original = source.read_bytes()

            annotate(source, output, ["result:40,50,80,60"], seed="test", font_size=18)

            self.assertEqual(source.read_bytes(), original)
            with Image.open(output) as result:
                self.assertEqual(result.size, (300, 200))
                label = result.crop((130, 40, 280, 100))
                self.assertIsNotNone(ImageChops.difference(label, Image.new("RGB", label.size, "white")).getbbox())


if __name__ == "__main__":
    unittest.main()
