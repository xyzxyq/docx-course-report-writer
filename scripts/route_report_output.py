#!/usr/bin/env python3
"""Route report generation to DOCX, LaTeX PDF, or Typst PDF workflows."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def _run(cmd: list[str], cwd: Path | None = None, timeout: int = 300) -> str:
    try:
        proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"Build timed out after {timeout}s: {cmd[0]}") from exc
    if proc.returncode:
        raise RuntimeError(f"Build failed ({proc.returncode}): {cmd[0]}\n{proc.stdout}\n{proc.stderr}")
    return proc.stdout + "\n" + proc.stderr


def _publish(candidate: Path, output: Path, force: bool) -> None:
    # Stage on the destination filesystem; failed builds never touch the old report.
    fd, name = tempfile.mkstemp(prefix=".report-", suffix=output.suffix, dir=output.parent)
    os.close(fd)
    staged = Path(name)
    try:
        shutil.copyfile(candidate, staged)
        if not force and output.exists():
            raise RuntimeError(f"Output already exists: {output}; use --force to replace")
        staged.replace(output)
    finally:
        staged.unlink(missing_ok=True)


def _generate_docx(args: argparse.Namespace) -> None:
    cmd = [
        sys.executable,
        str(Path(__file__).resolve().parent / "build_report.py"),
        "--draft", str(args.draft),
        "--refs", str(args.refs),
        "--output", str(args.output),
    ]
    if args.template:
        cmd.extend(["--template", str(args.template)])
    if args.no_default_template:
        cmd.append("--no-default-template")
    if args.no_toc:
        cmd.append("--no-toc")
    if args.drop_template_body:
        cmd.append("--drop-template-body")
    if args.title:
        cmd.extend(["--title", args.title])
    if args.course:
        cmd.extend(["--course", args.course])
    if args.college:
        cmd.extend(["--college", args.college])
    if args.major:
        cmd.extend(["--major", args.major])
    if args.student_name:
        cmd.extend(["--student-name", args.student_name])
    if args.student_id:
        cmd.extend(["--student-id", args.student_id])
    if args.teacher:
        cmd.extend(["--teacher", args.teacher])
    if args.date:
        cmd.extend(["--date", args.date])
    if args.root:
        cmd.extend(["--root", str(args.root)])
    if args.no_number_headings:
        cmd.append("--no-heading-numbering")
    if args.no_figure_numbering:
        cmd.append("--no-figure-numbering")
    if args.include_image_source_lines:
        cmd.append("--include-image-source-lines")

    _run(cmd, timeout=args.timeout)


def build_docx(args: argparse.Namespace) -> None:
    with tempfile.TemporaryDirectory(prefix="report-build-") as tmp:
        candidate = Path(tmp) / args.output.name
        staged_args = argparse.Namespace(**vars(args))
        staged_args.output = candidate
        _generate_docx(staged_args)
        if not candidate.is_file():
            raise RuntimeError("DOCX builder did not produce an artifact")
        _publish(candidate, args.output, args.force)
    print(f"DOCX generated (fields/layout not finalized): {args.output}")


def build_native(args: argparse.Namespace) -> None:
    source = args.source.resolve()
    root = (args.project_root or source.parent).resolve()
    if not root.is_dir() or not source.is_relative_to(root):
        raise RuntimeError("--source must be inside --project-root")
    engine = "typst" if args.format == "typst" else "latexmk"
    executable = shutil.which(engine)
    if not executable:
        raise RuntimeError(f"Required command not found: {engine}")
    if args.format == "latex" and not shutil.which(args.latex_engine):
        raise RuntimeError(f"Required LaTeX engine not found: {args.latex_engine}")

    output = args.output
    # Copy to a fresh workspace, never to a user-owned source-named directory.
    with tempfile.TemporaryDirectory(prefix="report-build-") as tmp:
        staging = Path(tmp).resolve()
        if staging.is_relative_to(root):
            raise RuntimeError("Project root includes the temporary workspace; select a narrower project root")
        project = staging / "project"
        artifacts = staging / "artifacts"
        artifacts.mkdir()

        def ignore(directory, names):
            directory = Path(directory)
            excluded = []
            for name in names:
                path = directory / name
                if (name in {".git", "__pycache__"} or name.startswith("._")
                        or path == output or name.startswith(output.stem + "-sources-")
                        or (output.parent != root and output.parent.is_relative_to(root)
                            and path == output.parent)):
                    excluded.append(name)
                elif path.is_symlink():
                    raise RuntimeError(f"Symlink in project: {path}; use a self-contained source project")
            return excluded

        shutil.copytree(root, project, ignore=ignore)
        work = project / source.relative_to(root)
        if not work.is_file():
            raise RuntimeError("Output directory contains the source; choose a separate output directory")
        if args.format == "typst":
            candidate = artifacts / "report.pdf"
            build_log = _run([executable, "compile", "--root", str(project), str(work), str(candidate)],
                 cwd=work.parent, timeout=args.timeout)
        else:
            candidate = artifacts / (work.stem + ".pdf")
            engine_flag = {"xelatex": "-xelatex", "lualatex": "-lualatex", "pdflatex": "-pdf"}[args.latex_engine]
            build_log = _run([executable, engine_flag, "-g", "-interaction=nonstopmode",
                  "-halt-on-error", "-file-line-error", "-outdir=" + str(artifacts), "./" + work.name],
                 cwd=work.parent, timeout=args.timeout)
        if not candidate.is_file() or candidate.stat().st_size < 8:
            raise RuntimeError("Compiler produced no fresh PDF")
        with candidate.open("rb") as pdf:
            if pdf.read(5) != b"%PDF-":
                raise RuntimeError("Compiler output is not a PDF")
        bundle = Path(tempfile.mkdtemp(prefix=output.stem + "-sources-", dir=output.parent))
        try:
            shutil.copytree(project, bundle, dirs_exist_ok=True)
            log_path = bundle.with_name(bundle.name + ".log")
            log_path.write_text(build_log or "", encoding="utf-8")
            _publish(candidate, output, args.force)
        except Exception:
            # Only this invocation's newly created bundle is safe to remove.
            shutil.rmtree(bundle)
            bundle.with_name(bundle.name + ".log").unlink(missing_ok=True)
            raise
    print(f"Source snapshot: {bundle / source.relative_to(root)}")
    print(f"PDF generated (content/layout review still required): {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Route report output by requested format.")
    parser.add_argument("--format", choices=["docx", "latex", "typst"], required=True)
    parser.add_argument("--draft", type=Path, help="Markdown draft for DOCX route")
    parser.add_argument("--refs", type=Path, help="Reference list for DOCX route")
    parser.add_argument("--output", type=Path, required=True, help="Primary output path")
    parser.add_argument("--source", type=Path, help="LaTeX (.tex) or Typst (.typ) source for non-DOCX routes")
    parser.add_argument("--template", type=Path)
    parser.add_argument("--no-default-template", action="store_true")
    parser.add_argument("--no-toc", action="store_true")
    parser.add_argument("--drop-template-body", action="store_true")
    parser.add_argument("--title", default="")
    parser.add_argument("--course", default="")
    parser.add_argument("--college", default="")
    parser.add_argument("--major", default="")
    parser.add_argument("--student-name", default="")
    parser.add_argument("--student-id", default="")
    parser.add_argument("--teacher", default="")
    parser.add_argument("--date", default="")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--include-image-source-lines", action="store_true")
    parser.add_argument("--no-heading-numbering", dest="no_number_headings", action="store_true")
    parser.add_argument("--no-figure-numbering", dest="no_figure_numbering", action="store_true")
    parser.add_argument("--project-root", type=Path, help="Native project root; defaults to source parent")
    parser.add_argument("--latex-engine", choices=["xelatex", "lualatex", "pdflatex"], default="xelatex")
    parser.add_argument("--timeout", type=int, default=300, help="Build timeout in seconds")
    parser.add_argument("--force", action="store_true", help="Replace an existing output file only after a successful build")
    args = parser.parse_args()

    expected_suffix = ".docx" if args.format == "docx" else ".pdf"
    if args.output.suffix.lower() != expected_suffix:
        parser.error(f"--output must end in {expected_suffix}; the path is never silently rewritten")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    # Reject symlinks before resolve(), which would hide the destination identity.
    if args.output.is_symlink():
        parser.error("--output must not be a symlink")
    args.output = args.output.resolve()
    if args.output.exists() and (not args.output.is_file() or not args.force):
        parser.error("Output exists; --force permits replacing a file, never a directory")
    if args.format == "docx":
        if not args.draft or not args.refs or not args.draft.is_file() or not args.refs.is_file():
            parser.error("DOCX requires existing --draft and --refs files")
        if args.output in {args.draft.resolve(), args.refs.resolve(),
                           (args.template or Path(__file__).resolve().parent.parent / "skill-assets/default-course-report-template.docx").resolve()}:
            parser.error("Output must not overwrite an input or template")
    elif not args.source or not args.source.is_file() or args.source.suffix.lower() != {"latex": ".tex", "typst": ".typ"}[args.format]:
        parser.error("Native route requires an existing --source with the selected format's extension")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        if args.format == "docx":
            build_docx(args)
        else:
            build_native(args)
    except (OSError, RuntimeError) as exc:
        raise SystemExit(str(exc)) from exc


if __name__ == "__main__":
    main()
