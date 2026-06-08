# Tooling Recipes

Use these command patterns as starting points. Adjust paths, executable names, and ports to the actual assignment.

## Unicode And Long-Output Hygiene

On this Windows machine, Chinese paths plus long PowerShell output can corrupt paths or trigger stdout failures. Prefer small, structured reads:

```powershell
$env:PYTHONIOENCODING='utf-8'
@'
from pathlib import Path
p = Path(r"C:\path\to\file.md")
for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
    if 1 <= i <= 120:
        print(f"{i:03}: {line}")
'@ | python -
```

Rules:

- Do not dump very large profiles, skills, PDFs, or generated logs to the terminal at once.
- Use UTF-8 output for Python subprocesses that print Chinese paths or JSON.
- Use absolute paths and PowerShell `-LiteralPath`.
- If a tool returns `????` paths, stop and rerun with a Unicode-safe path strategy before opening DOCX/PDF files.
- For Word COM and PDF export in Chinese paths, prefer the existing `-UseAsciiTemp` fallback.

## WSL Runtime Evidence

Use WSL for Linux/POSIX/socket/file-system experiments on Windows unless the user asks for native Windows.

Recommended evidence commands:

```powershell
wsl.exe -d Ubuntu-24.04 -- bash -lc 'cd /mnt/c/path/to/project && uname -a && gcc --version | head -1 && make --version | head -1'
wsl.exe -d Ubuntu-24.04 -- bash -lc 'cd /mnt/c/path/to/project && make clean && make'
wsl.exe -d Ubuntu-24.04 -- bash -lc 'cd /mnt/c/path/to/project && ./run_tests.sh'
```

Record:

- WSL distribution
- compiler/runtime versions
- exact project path
- build command
- run/test command
- raw log path

## Real Terminal Screenshots

When the user asks for real screenshots:

- Run the command in an actual visible terminal/application window.
- Capture the real window region after the command has produced the result.
- Keep raw screenshots and produce annotated copies.
- Do not use log-rendered images as screenshots.

For server/client workflows:

- capture build output
- capture server listening state
- capture client command/result session
- capture verification command such as `diff`, checksum, or test summary

## Annotating Screenshots

Use `scripts/annotate_screenshot.py` for repeatable red-box annotations:

```powershell
python C:\Users\20795\.codex\skills\docx-course-report-writer\scripts\annotate_screenshot.py `
  --input raw.png `
  --output annotated.png `
  --box "编译成功:40,120,620,80" `
  --box "异常处理:60,420,700,120"
```

Labels:

- red text
- transparent background
- no more than 10 Chinese characters
- fully inside the image bounds
- not covering the proof text

## Word Fields And PDF Export

Use Word COM when available:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
  -File C:\Users\20795\.codex\skills\docx-course-report-writer\scripts\update_word_fields.ps1 `
  -DocxPath report.docx `
  -ExportPdf `
  -UseAsciiTemp
```

Use `-KillExistingWord` only when stale Word processes block automation and it is safe to close them.

Always inspect the rendered TOC page after export. If it still contains placeholder text such as "please update in Word", rerun field updates before exporting and patch the report generator so future reruns update fields automatically.

## LaTeX To DOCX Conversion

When converting a LaTeX course report into a template DOCX:

1. Inspect custom macros and environments before conversion.
2. Map custom chapter/section/cite/ref/equation macros into a stable intermediate representation.
3. Convert PDF figures into DOCX-friendly PNGs only after confirming the referenced files exist.
4. Preserve the Word template's cover, page setup, heading styles, and automatic TOC field.
5. Remove sample body text, sample TOC entries, and previous report media.
6. Update Word fields and export PDF for visual QA.
7. Scan DOCX/PDF text for LaTeX residue: `\ref`, `\cite`, `\begin`, `\end`, unresolved labels, and stale template text.

If Pandoc or subprocess output fails with a `gbk`/Unicode encode/decode error, rerun with UTF-8 environment variables and avoid printing converted long text directly to PowerShell.

## Build Report Script Template Behavior

`scripts/build_report.py` uses this template precedence:

1. `--template path\to\user-template.docx` when the user supplied a template.
2. `skill-assets/default-course-report-template.docx` when the user did not supply one.
3. A blank Word document only when `--no-default-template` is explicitly passed.

By default, the script clears template body content and keeps the template as a style/page-setup source. This prevents old static TOC entries, sample chapters, and placeholders from leaking into the new report.

Use these flags only when intentional:

- `--preserve-cover-paragraphs N`: keep the first `N` template paragraphs, then remove the rest.
- `--keep-template-body`: keep all template body content. Use only for controlled repair work where the template body is the intended source, then run a stale-term scan.
- `--no-default-template`: ignore the integrated default template and build from a blank document.

## DOCX QA

Use `scripts/qa_docx_report.py` after generating the DOCX:

```powershell
python C:\Users\20795\.codex\skills\docx-course-report-writer\scripts\qa_docx_report.py `
  --docx report.docx `
  --require-toc `
  --min-images 4 `
  --min-tables 3 `
  --stale-term 实验五 `
  --stale-term 日志渲染
```

This is a gate, not a replacement for visual inspection. Still inspect exported PDF or rendered pages.

## PDF/Page Visual QA

Render or inspect pages around:

- TOC
- large figures
- result screenshots
- tables
- code blocks

Typical checks:

- no missing images
- no unreadable screenshots
- no table overflow
- no clipped text
- no isolated captions
