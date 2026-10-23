from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import check_environment as env
import route_report_output as router


class OutputRoutesTest(unittest.TestCase):
    def call(self, *args):
        with patch.object(sys, 'argv', ['router', *map(str, args)]), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            router.main()

    def fake_compile(self, cmd, cwd=None, **kwargs):
        if 'compile' in cmd:
            target = Path(cmd[-1])
            if not target.is_absolute():
                target = Path(cwd) / target
        else:
            target = Path(next(x.split('=', 1)[1] for x in cmd if x.startswith('-outdir='))) / (Path(cmd[-1]).stem + '.pdf')
        target.write_bytes(b'%PDF-1.7\nnew artifact\n%%EOF')

    def test_missing_format_does_not_default_to_docx(self):
        with patch.object(router, "build_docx") as build:
            with self.assertRaises(SystemExit):
                self.call("--output", "report.docx")
            build.assert_not_called()

    def test_existing_source_named_output_folder_is_never_deleted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'source'
            source.mkdir()
            (source / 'main.typ').write_text('hello')
            out = root / 'output'
            precious = out / 'source'
            precious.mkdir(parents=True)
            (precious / 'user.txt').write_text('keep')
            with patch.object(router.shutil, 'which', return_value='/fake/typst'), patch.object(router, '_run', side_effect=self.fake_compile):
                self.call('--format', 'typst', '--source', source / 'main.typ', '--output', out / 'report.pdf')
            self.assertEqual('keep', (precious / 'user.txt').read_text())
            self.assertTrue((out / 'report.pdf').is_file())

    def test_failure_preserves_existing_pdf_and_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / 'main.typ'
            src.write_text('hello')
            out = root / 'report.pdf'
            out.write_bytes(b'previous approved report')
            with patch.object(router.shutil, 'which', return_value='/fake/typst'), patch.object(router, '_run', side_effect=RuntimeError('compile failed')):
                with self.assertRaises((SystemExit, RuntimeError)):
                    self.call('--format', 'typst', '--source', src, '--output', out, '--force')
            self.assertEqual(b'previous approved report', out.read_bytes())
            self.assertEqual('hello', src.read_text())

    def test_zero_exit_without_pdf_is_failure_even_with_stale_pdf(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / 'main.typ'
            src.write_text('hello')
            out = root / 'report.pdf'
            out.write_bytes(b'%PDF-1.7\nold')
            with patch.object(router.shutil, 'which', return_value='/fake/typst'), patch.object(router, '_run'):
                with self.assertRaises((SystemExit, RuntimeError)):
                    self.call('--format', 'typst', '--source', src, '--output', out, '--force')
            self.assertEqual(b'%PDF-1.7\nold', out.read_bytes())

    def test_nested_output_and_explicit_project_root_preserve_assets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'chapters').mkdir()
            (root / 'asset.txt').write_text('asset')
            src = root / 'chapters' / 'main.typ'
            src.write_text('hello')
            out = root / 'output' / '中文 report.pdf'
            with patch.object(router.shutil, 'which', return_value='/fake/typst'), patch.object(router, '_run', side_effect=self.fake_compile):
                self.call('--format', 'typst', '--source', src, '--project-root', root, '--output', out)
            bundles = [p for p in out.parent.glob('*-sources-*') if p.is_dir()]
            self.assertEqual(1, len(bundles))
            self.assertEqual('asset', (bundles[0] / 'asset.txt').read_text())
            self.assertFalse((bundles[0] / 'output').exists())
            self.assertTrue(out.is_file())

    def test_existing_pdf_requires_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / 'main.typ'
            src.write_text('hello')
            out = root / 'report.pdf'
            out.write_bytes(b'keep')
            with patch.object(router, '_run') as run, patch.object(router.shutil, 'which', return_value='/fake/typst'):
                with self.assertRaises(SystemExit):
                    self.call('--format', 'typst', '--source', src, '--output', out)
                run.assert_not_called()

    def test_output_suffix_is_not_silently_rewritten(self):
        with self.assertRaises(SystemExit):
            self.call('--format', 'typst', '--source', 'main.typ', '--output', 'report.docx')

    def test_bad_compiler_output_does_not_replace_previous_pdf(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / 'main.typ'
            src.write_text('hello')
            out = root / 'report.pdf'
            out.write_bytes(b'keep')
            def bad_compile(cmd, **kwargs):
                Path(cmd[-1]).write_text('not a pdf at all')
            with patch.object(router.shutil, 'which', return_value='/fake/typst'), patch.object(router, '_run', side_effect=bad_compile):
                with self.assertRaises(SystemExit):
                    self.call('--format', 'typst', '--source', src, '--output', out, '--force')
            self.assertEqual(b'keep', out.read_bytes())

    def test_latex_never_silently_falls_back_to_pdflatex(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / 'main.tex'
            src.write_text('hello')
            with patch.object(router.shutil, 'which', side_effect=lambda cmd: '/fake/pdflatex' if cmd == 'pdflatex' else None), patch.object(router, '_run') as run:
                with self.assertRaises(SystemExit):
                    self.call('--format', 'latex', '--source', src, '--output', root / 'report.pdf')
                run.assert_not_called()

    def test_explicit_pdflatex_uses_latexmk_pdf_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / 'main.tex'
            src.write_text('hello')
            with patch.object(router.shutil, 'which', return_value='/fake/engine'), patch.object(router, '_run', side_effect=self.fake_compile) as run:
                self.call('--format', 'latex', '--source', src, '--output', root / 'result.pdf', '--latex-engine', 'pdflatex')
                self.assertIn('-pdf', run.call_args.args[0])
                self.assertNotIn('-pdflatex', run.call_args.args[0])

    def test_failed_version_probe_is_unavailable(self):
        failure = subprocess.CompletedProcess(['typst'], 1, '', 'broken')
        with patch.object(env, '_which', return_value='/fake/typst'), patch.object(env.subprocess, 'run', return_value=failure):
            self.assertFalse(env._run_version('typst')[0])

    def test_timed_out_version_probe_is_unavailable(self):
        with patch.object(env, '_which', return_value='/fake/typst'), patch.object(env.subprocess, 'run', side_effect=subprocess.TimeoutExpired('typst', 5)):
            self.assertFalse(env._run_version('typst')[0])

    def test_selected_format_only_and_json_stays_parseable(self):
        stdout = io.StringIO()
        with patch.object(sys, 'argv', ['probe', '--format', 'docx', '--json', '--summary']), patch.object(env, '_check_docx_route', return_value={'available': True, 'status': 'ok'}), patch.object(env, '_check_typst_route') as typst, patch.object(env, '_check_latex_route') as latex, contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(0, env.main())
        self.assertEqual(['docx'], list(json.loads(stdout.getvalue())['routes']))
        typst.assert_not_called()
        latex.assert_not_called()


if __name__ == '__main__':
    unittest.main()
