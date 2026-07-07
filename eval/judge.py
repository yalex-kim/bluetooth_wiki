"""Shared LLM-as-Judge scoring — single source of truth.

Extracted from scripts/eval_one.py (which previously inlined near-verbatim
copies of the prompts documented in eval/judge_prompt.md). Used by both the
single-question harness (scripts/eval_one.py) and the multi-strategy suite
runner (scripts/run_search_eval.py).
"""

from __future__ import annotations

import statistics
from pathlib import Path

from agent.json_extract import extract_json_payload
from agent.config import JUDGE_MODEL
from agent.llm import get_client

REPO = Path(__file__).resolve().parent.parent
DATASET_PATH = REPO / "eval" / "dataset.json"

DIFFICULTY_WEIGHTS = {"easy": 1.0, "medium": 1.5, "hard": 2.0, "expert": 2.5}
RAW_MAX = 11  # accuracy 3 + completeness 3 + citation 3 + usability 2 (hallucination ≤ 0)

DIMENSION_MAX = {
    "accuracy": 3,
    "completeness": 3,
    "citation": 3,
    "hallucination_penalty": 0,
    "usability": 2,
}

JUDGE_SYSTEM = (
    "You are an expert evaluator for Bluetooth specification knowledge systems.\n"
    "Your job is to score a system's answer against a reference answer using a strict rubric.\n"
    "You must return valid JSON only — no explanation outside the JSON block.\n"
    "Be strict: only mark a fact as correct if it explicitly matches the reference.\n"
    "Do not reward plausible-sounding but unverifiable claims."
)

JUDGE_USER_TEMPLATE = """## Question
{question}

## Reference Answer
{reference}

## Key Facts (must be present for full Completeness score)
{key_facts}

## Expected Citations
{expected_citations}

## System Answer to Evaluate
{system_answer}

---

Score the System Answer on these 5 dimensions. Return ONLY a JSON object.

Dimensions:
1. accuracy (0-3): Are all stated facts correct? Penalize any factual error.
2. completeness (0-3): What fraction of Key Facts appear in the answer? (≥90%=3, 60-89%=2, 30-59%=1, <30%=0)
3. citation (0-3): Is the spec version + section correctly cited? (version+section=3, version only=2, vague=1, none=0)
4. hallucination_penalty (0 to -3): Did the answer fabricate any facts not in the reference? (none=0, minor=-1, significant=-2, substantially fabricated=-3)
5. usability (0-2): Is the answer clearly structured and actionable for an engineer?

Return ONLY this exact JSON structure (no prose around it):
{{
  "scores": {{
    "accuracy": <int>,
    "completeness": <int>,
    "citation": <int>,
    "hallucination_penalty": <int>,
    "usability": <int>
  }},
  "rationales": {{
    "accuracy": "<one sentence>",
    "completeness": "<one sentence>",
    "citation": "<one sentence>",
    "hallucination_penalty": "<one sentence>",
    "usability": "<one sentence>"
  }},
  "raw_total": <sum of all 5 scores including the negative hallucination penalty>,
  "key_facts_found": [<key facts that were present>],
  "key_facts_missing": [<key facts absent>]
}}
"""


def extract_json(text: str) -> dict:
    data = extract_json_payload(text)
    if data is None:
        raise ValueError("Judge response had no parseable JSON object")
    return data


def normalize_verdict(verdict: dict) -> dict:
    """Canonicalize judge output in place (some judges emit 'hallucination'
    instead of 'hallucination_penalty'); returns the same dict."""
    s = verdict.setdefault("scores", {})
    s["hallucination_penalty"] = s.get("hallucination_penalty", s.get("hallucination", 0))
    r = verdict.setdefault("rationales", {})
    r["hallucination_penalty"] = r.get("hallucination_penalty", r.get("hallucination", ""))
    return verdict


def raw_total(verdict: dict) -> int:
    s = normalize_verdict(verdict)["scores"]
    return (
        s.get("accuracy", 0)
        + s.get("completeness", 0)
        + s.get("citation", 0)
        + s.get("hallucination_penalty", 0)
        + s.get("usability", 0)
    )


async def judge(question: dict, system_answer: str, *, model: str = JUDGE_MODEL) -> dict:
    """Score one answer. Returns the normalized judge verdict dict."""
    client = get_client()
    user = JUDGE_USER_TEMPLATE.format(
        question=question["question"],
        reference=question["reference_answer"],
        key_facts="\n".join(f"- {f}" for f in question["key_facts"]),
        expected_citations=", ".join(question["expected_citations"]),
        system_answer=system_answer,
    )
    resp = await client.chat.completions.create(
        model=model,
        max_tokens=2048,
        messages=[{"role": "system", "content": JUDGE_SYSTEM}, {"role": "user", "content": user}],
    )
    text = resp.choices[0].message.content or ""
    return normalize_verdict(extract_json(text))


def aggregate(dataset: dict, entries: list[dict], *, system_name: str, note: str = "") -> dict:
    """Aggregate per-question entries into the results_wiki.json shape
    (meta / by_category / dimension_averages / per_question) plus telemetry.

    Each entry must carry: id, category, difficulty, scores{...}, raw_total,
    and optionally latency_sec / cost_usd / tool_calls / num_turns / search_meta.
    """
    from datetime import date

    by_cat: dict[str, dict] = {}
    dims: dict[str, list[float]] = {d: [] for d in DIMENSION_MAX}
    total_weighted = 0.0
    total_max = 0.0

    for e in entries:
        w = DIFFICULTY_WEIGHTS.get(e["difficulty"], 1.0)
        weighted = e["raw_total"] * w
        max_weighted = RAW_MAX * w
        total_weighted += weighted
        total_max += max_weighted
        cat = by_cat.setdefault(e["category"], {"weighted": 0.0, "max": 0.0, "questions": []})
        cat["weighted"] += weighted
        cat["max"] += max_weighted
        cat["questions"].append(e["id"])
        for d in dims:
            dims[d].append(e["scores"].get(d, 0))

    for cat in by_cat.values():
        cat["weighted"] = round(cat["weighted"], 1)
        cat["max"] = round(cat["max"], 1)
        cat["pct"] = round(100.0 * cat["weighted"] / cat["max"], 1) if cat["max"] else 0.0

    dimension_averages = {}
    for d, vals in dims.items():
        avg = statistics.mean(vals) if vals else 0.0
        mx = DIMENSION_MAX[d]
        dimension_averages[d] = {
            "avg": round(avg, 2),
            "max": mx,
            "pct": round(100.0 * avg / mx, 1) if mx else None,
        }

    latencies = sorted(e["latency_sec"] for e in entries if e.get("latency_sec") is not None)
    costs = [e["cost_usd"] for e in entries if e.get("cost_usd") is not None]

    def _pctl(vals: list[float], p: float) -> float | None:
        if not vals:
            return None
        i = min(len(vals) - 1, int(round(p * (len(vals) - 1))))
        return round(vals[i], 2)

    telemetry = {
        "avg_latency_sec": round(statistics.mean(latencies), 2) if latencies else None,
        "p50_latency_sec": _pctl(latencies, 0.5),
        "p95_latency_sec": _pctl(latencies, 0.95),
        "avg_cost_usd": round(statistics.mean(costs), 4) if costs else None,
        "total_cost_usd": round(sum(costs), 4) if costs else None,
        "avg_tool_calls": round(statistics.mean([e["tool_calls"] for e in entries if e.get("tool_calls") is not None]), 1)
        if any(e.get("tool_calls") is not None for e in entries)
        else None,
        "avg_num_turns": round(statistics.mean([e["num_turns"] for e in entries if e.get("num_turns") is not None]), 1)
        if any(e.get("num_turns") is not None for e in entries)
        else None,
    }

    return {
        "meta": {
            "system": system_name,
            "evaluator": f"LLM-as-Judge ({JUDGE_MODEL})",
            "date": date.today().isoformat(),
            "overall_pct": round(100.0 * total_weighted / total_max, 1) if total_max else 0.0,
            "total_weighted": round(total_weighted, 1),
            "total_max_weighted": round(total_max, 1),
            "num_questions": len(entries),
            "note": note,
        },
        "telemetry": telemetry,
        "by_category": by_cat,
        "dimension_averages": dimension_averages,
        "per_question": entries,
    }
