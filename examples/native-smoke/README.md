# Native compiler smoke fixtures

These small synthetic documents test Chinese text, tables, equations, internal references and included source files. They are not academic report templates or a Quarto/Pandoc comparison. Both explicitly use macOS Songti SC; on other hosts configure an available Chinese font before running. Windows is not validated by these fixtures.

From the repository root, using a configured Python interpreter:

```sh
python scripts/route_report_output.py --format latex --source examples/native-smoke/report.tex --project-root examples/native-smoke --output output/latex-smoke.pdf
python scripts/route_report_output.py --format typst --source examples/native-smoke/report.typ --project-root examples/native-smoke --output output/typst-smoke.pdf
```

Outputs must not already exist unless `--force` is intended. Each successful run retains a unique source snapshot and compiler log next to the PDF. Re-run using the printed snapshot path and a different output directory to check source delivery. Review the PDF pages and logs; process success alone is insufficient.
