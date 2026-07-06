#!/usr/bin/env python3
"""Generate a static HTML report comparing search-strategy eval results.

Usage:
    python scripts/generate_search_report.py \
        --inputs eval/results_search_v0.json eval/results_search_v1.json eval/results_search_v2.json \
        [--out eval/report_search_compare.html]

Inputs are the files produced by scripts/run_search_eval.py.
Rendering logic lives in eval/report_render.py.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from eval.report_render import build_html  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inputs", nargs="+", required=True, help="results_search_*.json files (order = display order)")
    ap.add_argument("--out", default=str(REPO / "eval" / "report_search_compare.html"))
    args = ap.parse_args()

    results: dict[str, dict] = {}
    for p in args.inputs:
        path = Path(p)
        data = json.loads(path.read_text(encoding="utf-8"))
        name = path.stem.replace("results_search_", "")
        results[name] = data
    out = Path(args.out)
    out.write_text(build_html(results), encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
