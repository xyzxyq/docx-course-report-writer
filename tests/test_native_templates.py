"""Real native-template builds; skipped when the selected compilers/PDF reader are absent."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

try:
    import pypdfium2 as pdfium
except ImportError:
    pdfium = None

ROOT = Path(__file__).resolve().parents[1]


class NativeTemplatesTest(unittest.TestCase):
    def check_template(self, fmt, extension):
        if pdfium is None:
            self.skipTest('pypdfium2 is required to inspect generated PDFs')
        tools = ['typst'] if fmt == 'typst' else ['latexmk', 'xelatex']
        if not all(shutil.which(tool) for tool in tools):
            self.skipTest('missing ' + '/'.join(tools))
        with tempfile.TemporaryDirectory(prefix='course-template-') as tmp:
            root = Path(tmp)
            project = root / '中文 project'
            shutil.copytree(ROOT / 'skill-assets' / fmt, project)
            src = project / ('main.' + extension)
            src.write_text(src.read_text(encoding='utf-8').replace('提交日期', '2026-10-23'), encoding='utf-8')
            output = root / 'output' / '课程 report.pdf'
            def build(source, target):
                result = subprocess.run([
                    sys.executable, str(ROOT / 'scripts/route_report_output.py'),
                    '--format', fmt, '--source', str(source), '--output', str(target),
                ], capture_output=True, text=True, timeout=120)
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            build(src, output)
            with pdfium.PdfDocument(output) as doc:
                self.assertEqual(6, len(doc), 'cover / TOC / three chapters / bibliography')
                texts = []
                for page in doc:
                    tp = page.get_textpage()
                    texts.append(re.sub(r'\s+', '', tp.get_text_range()))
                    tp.close()
                    self.assertAlmostEqual(595.28, page.get_width(), delta=1)
                    self.assertAlmostEqual(841.89, page.get_height(), delta=1)
                self.assertIn('课程报告', texts[0])
                self.assertTrue(texts[0].endswith('2026-10-23'), 'no body page number on cover')
                self.assertIn('目录', texts[1])
                self.assertIn('第一章研究目的', texts[2])
                self.assertTrue(texts[2].endswith('1'), 'body must restart at page 1')
                self.assertIn('[1]', texts[2])
                self.assertNotIn('?', ''.join(texts))
                self.assertIn('图2.1', texts[3])
                self.assertIn('表2.1', texts[3])
                self.assertIn('表2.1仅展示记录结构', texts[4], 'cross-chapter references must retain the target chapter')
                self.assertIn('参考文献', texts[5])
                self.assertIn('typst.app', texts[5])
                # The citation must be raised relative to its preceding Chinese character.
                page = doc[2]
                tp = page.get_textpage()
                text = tp.get_text_range()
                index = text.index('[1]')
                left, bottom, right, top = tp.get_charbox(index)
                _, body_bottom, _, body_top = tp.get_charbox(index - 1)
                self.assertGreater(bottom, body_bottom + 1)
                self.assertLess(top - bottom, body_top - body_bottom)
                tp.close()
            log = next(output.parent.glob('*-sources-*.log')).read_text(encoding='utf-8')
            self.assertNotIn('unknown font family', log.lower())
            self.assertNotIn('Missing character:', log)
            # A handed-off source snapshot must rebuild, without the original project.
            bundle = next(p for p in output.parent.glob('*-sources-*') if p.is_dir())
            shutil.rmtree(project)
            build(bundle / src.name, root / 'rebuilt' / 'report.pdf')

    def test_latex_template(self):
        self.check_template('latex', 'tex')

    def test_typst_template(self):
        self.check_template('typst', 'typ')


if __name__ == '__main__':
    unittest.main()
