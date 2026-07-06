"""Shared JSON-payload extraction for LLM responses.

Single source of truth for the fenced-block + brace-balancing parse that was
previously duplicated across agent/agent.py, scripts/eval_one.py, and now the
search sufficiency judge.
"""

from __future__ import annotations

import json
import re

_FENCED_JSON_RE = re.compile(r"```json\s*\n(?P<body>.*?)\n```", re.DOTALL)


def extract_json_payload(text: str) -> dict | None:
    """Extract the first JSON object from LLM output.

    Tries (in order):
      1. ``` ```json ... ``` ``` fenced block
      2. The first top-level JSON object in the text via brace-balancing
    Returns the parsed dict on success, else None.
    """
    m = _FENCED_JSON_RE.search(text)
    if m:
        try:
            return json.loads(m.group("body"))
        except json.JSONDecodeError:
            pass
    start = text.find("{")
    while start != -1:
        depth = 0
        in_str = False
        esc = False
        for i in range(start, len(text)):
            ch = text[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    candidate = text[start : i + 1]
                    try:
                        return json.loads(candidate)
                    except json.JSONDecodeError:
                        break
        start = text.find("{", start + 1)
    return None
