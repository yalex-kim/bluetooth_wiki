"""Thin subprocess wrapper around ripgrep (``rg``).

All lexical search in v1/v2 goes through here. ripgrep is an OS binary, not a
Python dependency — if it is missing we raise immediately with an actionable
message instead of silently degrading.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

_RG_TIMEOUT_SEC = 30


@dataclass
class RgMatch:
    path: Path
    line_number: int  # 1-based
    line_text: str


def _rg_bin() -> str:
    rg = shutil.which("rg")
    if rg is None:
        raise RuntimeError(
            "ripgrep ('rg') was not found on PATH. Install it (e.g. `apt install ripgrep` "
            "or https://github.com/BurntSushi/ripgrep#installation) — the v1/v2 search "
            "strategies require it."
        )
    return rg


def rg_search(
    pattern: str,
    roots: list[Path],
    *,
    fixed_string: bool = True,
    case_insensitive: bool = True,
    glob: str = "*.md",
    max_count_per_file: int = 50,
    max_total_matches: int = 4000,
) -> list[RgMatch]:
    """Run one ripgrep query and return structured matches.

    Returns an empty list on no-match (rg exit code 1). Raises on real errors.
    """
    roots = [r for r in roots if r.exists()]
    if not roots or not pattern:
        return []
    cmd = [_rg_bin(), "--json", "--glob", glob, "--max-count", str(max_count_per_file)]
    if fixed_string:
        cmd.append("--fixed-strings")
    if case_insensitive:
        cmd.append("--ignore-case")
    cmd.append("--")
    cmd.append(pattern)
    cmd.extend(str(r) for r in roots)

    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=_RG_TIMEOUT_SEC)
    if proc.returncode not in (0, 1):  # 1 = no matches
        raise RuntimeError(f"ripgrep failed (exit {proc.returncode}): {proc.stderr.strip()[:500]}")

    matches: list[RgMatch] = []
    for line in proc.stdout.splitlines():
        if len(matches) >= max_total_matches:
            break
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if obj.get("type") != "match":
            continue
        data = obj["data"]
        text = data["lines"].get("text", "")
        matches.append(
            RgMatch(
                path=Path(data["path"]["text"]),
                line_number=data["line_number"],
                line_text=text.rstrip("\n"),
            )
        )
    return matches
