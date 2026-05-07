"""Run one eval question through BluetoothWikiAgent + LLM-as-Judge.

Usage:
    .venv/bin/python scripts/eval_one.py Q001
    .venv/bin/python scripts/eval_one.py Q001 --save     # also append to eval/results_agent.json
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path

from anthropic import AsyncAnthropic

from agent import BluetoothWikiAgent

REPO = Path(__file__).resolve().parent.parent
DATASET_PATH = REPO / "eval" / "dataset.json"
RESULTS_PATH = REPO / "eval" / "results_agent.json"
JUDGE_MODEL = "claude-sonnet-4-5"

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


def _load_question(qid: str) -> dict:
    data = json.loads(DATASET_PATH.read_text(encoding="utf-8"))
    for q in data["questions"]:
        if q["id"] == qid:
            return q
    raise SystemExit(f"Question {qid} not found in dataset")


def _extract_json(text: str) -> dict:
    start = text.find("{")
    if start == -1:
        raise ValueError("Judge response had no JSON object")
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
                return json.loads(text[start : i + 1])
    raise ValueError("Unbalanced JSON braces in judge response")


async def judge(question: dict, system_answer: str) -> dict:
    client = AsyncAnthropic()
    user = JUDGE_USER_TEMPLATE.format(
        question=question["question"],
        reference=question["reference_answer"],
        key_facts="\n".join(f"- {f}" for f in question["key_facts"]),
        expected_citations=", ".join(question["expected_citations"]),
        system_answer=system_answer,
    )
    msg = await client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=2048,
        system=JUDGE_SYSTEM,
        messages=[{"role": "user", "content": user}],
    )
    text = "".join(b.text for b in msg.content if hasattr(b, "text"))
    return _extract_json(text)


def _print_result(qid: str, question: dict, response, verdict: dict) -> int:
    s = verdict["scores"]
    # Some judges return 'hallucination' instead of 'hallucination_penalty'.
    halluc = s.get("hallucination_penalty", s.get("hallucination", 0))
    s["hallucination_penalty"] = halluc
    raw = s["accuracy"] + s["completeness"] + s["citation"] + halluc + s["usability"]
    rationales = verdict.get("rationales", {})
    halluc_rat = rationales.get(
        "hallucination_penalty", rationales.get("hallucination", "")
    )
    rationales["hallucination_penalty"] = halluc_rat
    print(f"\n══════ {qid} ({question['category']}, {question['difficulty']}) ══════")
    print(f"Q: {question['question']}\n")
    print("──── ANSWER (first 500 chars) ────")
    print(response.answer[:500] + ("…" if len(response.answer) > 500 else ""))
    print(f"\nCitations: {len(response.citations)}")
    print("\n──── SCORES ────")
    print(f"  accuracy:              {s['accuracy']}/3   — {verdict['rationales']['accuracy']}")
    print(f"  completeness:          {s['completeness']}/3   — {verdict['rationales']['completeness']}")
    print(f"  citation:              {s['citation']}/3   — {verdict['rationales']['citation']}")
    print(f"  hallucination_penalty: {halluc}/0  — {halluc_rat}")
    print(f"  usability:             {s['usability']}/2   — {verdict['rationales']['usability']}")
    print(f"  ───────────────────")
    print(f"  RAW TOTAL:             {raw}/11")
    if verdict.get("key_facts_missing"):
        print(f"\nKey facts MISSING: {verdict['key_facts_missing']}")
    return raw


async def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("qid")
    p.add_argument("--save", action="store_true")
    args = p.parse_args()

    question = _load_question(args.qid)
    agent = BluetoothWikiAgent()
    t0 = time.perf_counter()
    response = await agent.ask(question["question"])
    ask_time = time.perf_counter() - t0
    t1 = time.perf_counter()
    verdict = await judge(question, response.answer)
    judge_time = time.perf_counter() - t1
    raw = _print_result(args.qid, question, response, verdict)
    print(f"\n──── LOOP ────")
    print(f"  num_turns:    {response.num_turns}")
    print(f"  tool_calls:   {response.tool_calls}  ({response.tools_used or {}})")
    print(f"  stop_reason:  {response.stop_reason}")
    if response.total_cost_usd is not None:
        print(f"  cost_usd:     ${response.total_cost_usd:.4f}")
    if response.usage:
        u = response.usage
        in_tok = u.get("input_tokens", 0)
        out_tok = u.get("output_tokens", 0)
        cache_r = u.get("cache_read_input_tokens", 0)
        cache_c = u.get("cache_creation_input_tokens", 0)
        print(f"  tokens:       in={in_tok} out={out_tok} cache_read={cache_r} cache_create={cache_c}")
    print(f"\n──── TIMING ────")
    print(f"  agent.ask:        {ask_time:6.2f}s  (api {response.duration_api_ms/1000:.2f}s, total {response.duration_ms/1000:.2f}s)")
    print(f"  judge:            {judge_time:6.2f}s")
    print(f"  total:            {ask_time + judge_time:6.2f}s")

    if args.save:
        if RESULTS_PATH.exists():
            results = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
        else:
            results = {"per_question": {}}
        results["per_question"][args.qid] = {
            "scores": verdict["scores"],
            "raw_total": raw,
            "rationales": verdict["rationales"],
            "key_facts_missing": verdict.get("key_facts_missing", []),
            "answer": response.answer,
            "citations": response.citations,
            "raw_response": response.raw,
            "reasoning": response.reasoning,
            "timing_sec": {
                "agent_ask": round(ask_time, 2),
                "judge": round(judge_time, 2),
                "total": round(ask_time + judge_time, 2),
            },
            "loop": {
                "num_turns": response.num_turns,
                "tool_calls": response.tool_calls,
                "tools_used": response.tools_used,
                "stop_reason": response.stop_reason,
                "total_cost_usd": response.total_cost_usd,
                "usage": response.usage,
            },
        }
        RESULTS_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False))
        print(f"\nSaved → {RESULTS_PATH.relative_to(REPO)}")

    return 0 if raw >= 10 else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
