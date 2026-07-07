"""Run one eval question through BluetoothWikiAgent + LLM-as-Judge.

Usage:
    .venv/bin/python scripts/eval_one.py Q001
    .venv/bin/python scripts/eval_one.py Q001 --save          # append to eval/results_agent.json
    .venv/bin/python scripts/eval_one.py Q001 --strategy v2   # pick a search strategy

Judge prompts/scoring live in eval/judge.py (shared with run_search_eval.py).
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from agent import BluetoothWikiAgent  # noqa: E402
from agent.config import SEARCH_STRATEGY  # noqa: E402
from eval.judge import DATASET_PATH, judge, normalize_verdict, raw_total  # noqa: E402

RESULTS_PATH = REPO / "eval" / "results_agent.json"


def _load_question(qid: str) -> dict:
    data = json.loads(DATASET_PATH.read_text(encoding="utf-8"))
    for q in data["questions"]:
        if q["id"] == qid:
            return q
    raise SystemExit(f"Question {qid} not found in dataset")


def _print_result(qid: str, question: dict, response, verdict: dict) -> int:
    verdict = normalize_verdict(verdict)
    s = verdict["scores"]
    raw = raw_total(verdict)
    rationales = verdict["rationales"]
    print(f"\n══════ {qid} ({question['category']}, {question['difficulty']}) ══════")
    print(f"Q: {question['question']}\n")
    print("──── ANSWER (first 500 chars) ────")
    print(response.answer[:500] + ("…" if len(response.answer) > 500 else ""))
    print(f"\nCitations: {len(response.citations)}")
    print("\n──── SCORES ────")
    print(f"  accuracy:              {s['accuracy']}/3   — {rationales.get('accuracy', '')}")
    print(f"  completeness:          {s['completeness']}/3   — {rationales.get('completeness', '')}")
    print(f"  citation:              {s['citation']}/3   — {rationales.get('citation', '')}")
    print(f"  hallucination_penalty: {s['hallucination_penalty']}/0  — {rationales.get('hallucination_penalty', '')}")
    print(f"  usability:             {s['usability']}/2   — {rationales.get('usability', '')}")
    print("  ───────────────────")
    print(f"  RAW TOTAL:             {raw}/11")
    if verdict.get("key_facts_missing"):
        print(f"\nKey facts MISSING: {verdict['key_facts_missing']}")
    return raw


async def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("qid")
    p.add_argument("--save", action="store_true")
    p.add_argument("--strategy", default=SEARCH_STRATEGY, choices=("v0", "v1", "v2"), help="search strategy (default from BT_AGENT_SEARCH_STRATEGY)")
    args = p.parse_args()

    question = _load_question(args.qid)
    agent = BluetoothWikiAgent(search_strategy=args.strategy)
    t0 = time.perf_counter()
    response = await agent.ask(question["question"])
    ask_time = time.perf_counter() - t0
    t1 = time.perf_counter()
    verdict = await judge(question, response.answer)
    judge_time = time.perf_counter() - t1
    raw = _print_result(args.qid, question, response, verdict)
    print("\n──── LOOP ────")
    print(f"  strategy:     {args.strategy}")
    print(f"  num_turns:    {response.num_turns}")
    print(f"  tool_calls:   {response.tool_calls}  ({response.tools_used or {}})")
    print(f"  stop_reason:  {response.stop_reason}")
    if response.total_cost_usd is not None:
        print(f"  cost_usd:     ${response.total_cost_usd:.4f}")
    if response.usage:
        u = response.usage
        print(f"  tokens:       in={u.get('prompt_tokens', 0)} out={u.get('completion_tokens', 0)}")
    print("\n──── TIMING ────")
    print(f"  agent.ask:        {ask_time:6.2f}s  (total {response.duration_ms/1000:.2f}s)")
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
            "search_strategy": args.strategy,
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
