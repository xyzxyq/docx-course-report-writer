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

## Linux And WSL Runtime Evidence

Use this whenever the report depends on Linux/POSIX behavior: sockets, fork/processes, signals, shared memory, semaphores, file permissions, shell scripts, Makefiles, GCC/Clang, Linux-only packages, or teacher-provided Linux commands.

### Runtime Selection Order

1. Check whether the user host is already Linux. If yes, use native Linux and record `uname -a`.
2. If the host is not Linux, check for local Linux runtimes. On Windows, check WSL first.
3. If a suitable WSL distribution exists, use it unless the user explicitly asks for native Windows.
4. If no suitable Linux runtime exists, ask the user whether to install WSL. Do not install, enable features, change default distributions, or run admin-level setup before explicit user permission.
5. If installation is approved but requires admin rights, reboot, Store login, or network access, report that limitation and continue only after the environment is usable.

### Windows Host Checks

```powershell
$PSVersionTable.PSEdition
[System.Runtime.InteropServices.RuntimeInformation]::OSDescription
where.exe wsl
wsl.exe --status
wsl.exe -l -v
```

If `wsl.exe -l -v` lists a distribution, verify it:

```powershell
wsl.exe -d Ubuntu-24.04 -- bash -lc 'uname -a; printf "PWD=%s\n" "$PWD"; command -v gcc || true; command -v make || true'
```

Use the actual distribution name from `wsl.exe -l -v`; do not assume `Ubuntu-24.04`.

### WSL Install Gate

Ask a concise permission question before installing:

```text
该任务需要 Linux/POSIX 环境。当前未检测到可用 WSL。是否允许我安装/启用 WSL？安装可能需要管理员权限、联网和重启。
```

After approval, use the platform's normal WSL setup path, then verify again:

```powershell
wsl.exe --install
wsl.exe --status
wsl.exe -l -v
```

If a distribution must be selected, prefer a current Ubuntu distribution available on the machine. Record the exact command and any reboot/admin limitation.

### Running Projects In WSL

Convert Windows paths to WSL mount paths:

```powershell
$win = "$env:USERPROFILE\Documents\project"
$wsl = $win -replace '^C:', '/mnt/c' -replace '\\', '/'
wsl.exe -d Ubuntu-24.04 -- bash -lc "cd '$wsl' && pwd && uname -a"
```

Recommended evidence commands:

```powershell
wsl.exe -d Ubuntu-24.04 -- bash -lc 'cd /mnt/c/path/to/project && uname -a && gcc --version | head -1 && make --version | head -1'
wsl.exe -d Ubuntu-24.04 -- bash -lc 'cd /mnt/c/path/to/project && make clean && make'
wsl.exe -d Ubuntu-24.04 -- bash -lc 'cd /mnt/c/path/to/project && ./run_tests.sh'
```

Record:

- host OS and whether native Linux or WSL was used
- WSL distribution and version
- Linux kernel and compiler/runtime versions
- exact Windows path and WSL path
- build/run/test commands
- raw log paths and screenshot paths
- missing packages and installation commands, if any

## Screenshot Evidence

Treat screenshots as planned evidence, not decoration. Use them when visual proof helps the report: browser output, UI state, terminal build/test result, server/client interaction, external source page, or required proof of execution.

### Browser Page Screenshots

- Navigate to the intended page and wait for the relevant content, not just network idle.
- Capture full page or a focused region according to the report need.
- Inspect the screenshot content before using it.
- Reject or relabel screenshots that show 403, CAPTCHA, login wall, cookie blocker, blank page, loading spinner, wrong tab, or error page.
- Record URL, capture time, raw screenshot path, and any cropped/annotated path.

### Real Terminal Screenshots

When the user or assignment needs real terminal screenshots:

- Run the command in an actual visible terminal/application window.
- Capture after the command has produced the result.
- Include enough context: prompt/current directory, command, result summary, and key verification lines.
- Keep raw screenshots and produce annotated copies when helpful.
- Do not use log-rendered images as screenshots. If a log-rendered image is used, label it as a rendered log.

For server/client workflows:

- capture build output
- capture server listening state
- capture client command/result session
- capture verification command such as `diff`, checksum, or test summary

### Screenshot Quality Checks

- Text is readable at final DOCX/PDF scale.
- Crop focuses the evidence but keeps enough context to prove what was run.
- Annotations do not cover proof text.
- Raw and annotated versions are not confused.
- Caption states what the screenshot proves.

## Annotating Screenshots

Use `scripts/annotate_screenshot.py` for repeatable red-box annotations:

```powershell
python "$env:CODEX_HOME\skills\docx-course-report-writer\scripts\annotate_screenshot.py" `
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
  -File "$env:CODEX_HOME\skills\docx-course-report-writer\scripts\update_word_fields.ps1" `
  -DocxPath report.docx `
  -ExportPdf `
  -UseAsciiTemp
```

Use `-KillExistingWord` only when stale Word processes block automation and it is safe to close them.

Always inspect the rendered TOC page after export. Word COM update/export must happen before PDF page rendering so the reviewed pages reflect Word's real TOC, fields, and page numbers. If the rendered TOC still contains placeholder text such as "please update in Word", rerun field updates before exporting and patch the report generator so future reruns update fields automatically.

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

By default, when the integrated default template is used, the script preserves the visible default cover and page setup, then removes sample body content and stale static TOC entries before inserting a fresh automatic TOC field and report body. The body starts in a new Word section with page numbering restarted at 1, and front matter footers do not display the body `PAGE` field, so cover and TOC pages are front matter rather than body-page count. This prevents a plain white document while still avoiding old sample chapters and placeholders.

The default cover must fit entirely on page 1. If rendered PDF page 2 contains only a cover date, blank cover residue, or other cover metadata, fix the cover spacing/source template and regenerate before delivery.

Use these flags only when intentional:

- `--preserve-cover-paragraphs N`: keep the first `N` template paragraphs, then remove the rest.
- `--keep-template-body`: keep all template body content. Use only for controlled repair work where the template body is the intended source, then run a stale-term scan.
- `--no-default-template`: ignore the integrated default template and build from a blank document.
- `--drop-template-cover`: use the integrated default template only as a style/page-setup source and discard its visible cover. Use only when the user explicitly asks for no cover.
- `{{PAGEBREAK}}` in `report-draft.md`: insert a Word page break, useful before full-page figures or appendices.

## DOCX QA

Use `scripts/qa_docx_report.py` after generating the DOCX:

```powershell
python "$env:CODEX_HOME\skills\docx-course-report-writer\scripts\qa_docx_report.py" `
  --docx report.docx `
  --require-toc `
  --require-cover `
  --require-body-page-start-1 `
  --min-images 4 `
  --min-tables 3 `
  --require-formal-figure-captions `
  --forbid-image-source-lines `
  --stale-term 实验五 `
  --stale-term 日志渲染
```

This is a gate, not a replacement for visual inspection. Still inspect exported PDF or rendered pages.

If AI text-to-image was enabled during intake, set `--min-images` high enough to include the generated AI figure plus other required figures, then verify `image-attributions.md` marks the AI figure as `explanatory` or `concept-enhancement`.

## PDF/Page Visual QA

Preferred sequence:

1. Run `scripts/update_word_fields.ps1 -ExportPdf -UseAsciiTemp` or equivalent Word COM automation.
2. Render every PDF page to PNG.
3. Generate contact sheets for navigation.
4. Inspect every rendered page PNG; contact sheets are an index, not the proof.
5. Treat any blank or near-blank page as blocking unless explicitly allowed by the template or assignment and documented in the run record.

```powershell
python "$env:CODEX_HOME\skills\docx-course-report-writer\scripts\render_pdf_review_pages.py" `
  --pdf report.pdf `
  --pages-dir build\pdf-pages `
  --sheets-dir build\pdf-review-sheets `
  --dpi 150
```

Or use the compact equivalent:

```powershell
python "$env:CODEX_HOME\skills\docx-course-report-writer\scripts\render_pdf_review_pages.py" `
  --pdf report.pdf `
  --out-dir report-rendered-pages `
  --contact-sheet-cols 2 `
  --contact-sheet-rows 2 `
  --fail-on-blank
```

The review sheets combine four pages per contact sheet to reduce repeated image opening, but contact sheets are an index, not the proof. The script also runs blank-page detection before drawing page labels. PDF page render images are not screenshots; do not call them terminal/browser screenshots or use them as execution evidence.

If a template deliberately contains a blank separator page, rerun with `--allow-blank-pages` only after recording the page number and reason in the run record.

Render or inspect pages around:

- TOC
- large figures
- result screenshots
- tables
- code blocks
- references
- every rendered page that looks blank, sparse, or suspicious in the contact sheet

Typical checks:

- TOC page numbers share a single right edge and dot leaders reach that edge
- the first visible page number 1 is on the first body/chapter page after cover/TOC front matter
- figure captions use formal `图x.x` numbering
- raw `图片来源：` provenance lines did not leak into the report body
- no missing images
- no unreadable screenshots
- no table overflow
- no clipped text
- no isolated captions
- no blank or near-blank page is missed because only the contact sheet was skimmed
