#!/usr/bin/env python3
"""Environment probe for DOCX/Latex/Typst report output routes."""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


def _which(cmd: str) -> str | None:
    return shutil.which(cmd)


def _has_wsl() -> bool:
    return platform.system() == "Windows" and bool(_which("wsl"))


def _run_version(cmd: str) -> tuple[bool, str]:
    exe = _which(cmd)
    if not exe:
        return False, "missing"
    try:
        out = subprocess.run([exe, "--version"], capture_output=True, text=True, check=False, timeout=5)
        lines = (out.stdout or out.stderr or "").strip().splitlines()
        return out.returncode == 0, (lines[0][:140] if lines else f"exit={out.returncode}, no version text")
    except Exception as exc:  # pragma: no cover - defensive for platform/runtime failures
        return False, f"present: {exe} (version query failed: {exc})"


def _is_docx_ready() -> tuple[bool, str]:
    try:
        __import__("docx")
        return True, "python-docx available"
    except Exception as exc:
        return False, f"python-docx not importable: {exc}"


def _check_docx_route() -> dict[str, Any]:
    available, detail = _is_docx_ready()
    return {
        "available": available,
        "status": detail,
        "scope": "generation dependency only; no field/layout verification",
        "finalization_verified": False,
        "optional_pdf_svg_dependency_found": importlib.util.find_spec("pymupdf") is not None,
        "commands": {
            "python": sys.executable,
            "python-docx": available,
        },
    }


def _check_latex_route() -> dict[str, Any]:
    latexmk_ok, latexmk_info = _run_version("latexmk")
    xelatex_ok, xelatex_info = _run_version("xelatex")

    core_ok = latexmk_ok and xelatex_ok

    return {
        "available": core_ok,
        "status": (
            "commands respond; template/fonts/build not verified" if core_ok else "latex toolchain incomplete"
        ),
        "commands": {
            "latexmk": latexmk_ok,
            "xelatex": xelatex_ok,
        },
        "details": {
            "latexmk": latexmk_info,
            "xelatex": xelatex_info,
        },
    }


def _check_typst_route() -> dict[str, Any]:
    typst_ok, typst_info = _run_version("typst")
    return {
        "available": typst_ok,
        "status": "command responds; template/fonts/build not verified" if typst_ok else "typst not available",
        "commands": {
            "typst": typst_ok,
        },
        "details": {
            "typst": typst_info,
        },
    }


@dataclass
class EnvironmentReport:
    platform: str
    release: str
    host: str
    has_wsl: bool
    routes: dict[str, dict[str, Any]]

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)


def build_report(formats: list[str]) -> EnvironmentReport:
    route_checks = {
        "docx": _check_docx_route,
        "latex": _check_latex_route,
        "typst": _check_typst_route,
    }

    routes: dict[str, dict[str, Any]] = {}
    for fmt in formats:
        checker = route_checks.get(fmt)
        if checker is None:
            routes[fmt] = {"available": False, "status": "unsupported format"}
        else:
            routes[fmt] = checker()

    return EnvironmentReport(
        platform=platform.system(),
        release=platform.platform(),
        host=platform.node(),
        has_wsl=bool(_has_wsl()),
        routes=routes,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe local capabilities for report output routes.")
    parser.add_argument(
        "--format",
        action="append",
        dest="formats",
        default=None,
        choices=["docx", "latex", "typst"],
        help="Format route to probe: docx, latex, typst. Repeatable.",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON only.")
    parser.add_argument(
        "--require",
        action="append",
        dest="require",
        choices=["docx", "latex", "typst"],
        default=[],
        help="Fail if any listed format route is unavailable.",
    )
    parser.add_argument("--strict", action="store_true", help="Equivalent to --require docx --require latex --require typst")
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print concise one-line summary after JSON or text output.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional path to write JSON report.",
    )
    args = parser.parse_args()

    required = set(args.require)
    if args.strict:
        required.update({"docx", "latex", "typst"})
    formats = sorted(set(args.formats or required or ["docx", "latex", "typst"]) | required)
    report = build_report(formats)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report.to_json(), encoding="utf-8")

    if args.json:
        print(report.to_json())
    else:
        print(f"platform: {report.platform}")
        print(f"release: {report.release}")
        print(f"host: {report.host}")
        print(f"has_wsl: {report.has_wsl}")
        for fmt, detail in report.routes.items():
            print(f"{fmt}: {detail['status']} ({detail['available']})")

    required = set(args.require)
    if args.strict:
        required.update({"docx", "latex", "typst"})

    missing = [fmt for fmt in sorted(required) if not report.routes.get(fmt, {}).get("available")]
    if args.summary:
        can_docx = report.routes.get("docx", {}).get("available", False)
        can_latex = report.routes.get("latex", {}).get("available", False)
        can_typst = report.routes.get("typst", {}).get("available", False)
        print(f"summary: docx={can_docx} latex={can_latex} typst={can_typst}", file=sys.stderr if args.json else sys.stdout)

    return 0 if not missing else 3


if __name__ == "__main__":
    raise SystemExit(main())
