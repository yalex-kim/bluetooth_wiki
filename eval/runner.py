"""Shared eval-suite runner: drives agent strategies over dataset questions.

Used by scripts/run_search_eval.py (CLI) and server/jobs.py (background job).
"""

from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from typing import Callable

from .judge import DATASET_PATH, aggregate, judge, normalize_verdict, raw_total

REPO = Path(__file__).resolve().parent.parent
OUT_TEMPLATE = "results_search_{strategy}.json"


def load_questions(ids: list[str] | None, limit: int | None) -> tuple[dict, list[dict]]:
    dataset = json.loads(DATASET_PATH.read_text(encoding="utf-8"))
    questions = dataset["questions"]
    if ids:
        wanted = set(ids)
        questions = [q for q in questions if q["id"] in wanted]
        missing = wanted - {q["id"] for q in questions}
        if missing:
            raise ValueError(f"Unknown question ids: {sorted(missing)}")
    if limit:
        questions = questions[:limit]
    return dataset, questions


async def eval_question(agent, q: dict, sem: asyncio.Semaphore, *, verbose: bool = True) -> dict:
    """Ask + judge one question; a failed question scores 0 instead of
    aborting the suite."""
    async with sem:
        t0 = time.perf_counter()
        try:
            response = await agent.ask(q["question"])
            ask_time = time.perf_counter() - t0
            verdict = normalize_verdict(await judge(q, response.answer))
            entry_scores = verdict["scores"]
            raw = raw_total(verdict)
            error = None
        except Exception as exc:
            ask_time = time.perf_counter() - t0
            response = None
            verdict = {"scores": {}, "rationales": {}, "key_facts_missing": q.get("key_facts", [])}
            entry_scores = {k: 0 for k in ("accuracy", "completeness", "citation", "hallucination_penalty", "usability")}
            raw = 0
            error = f"{type(exc).__name__}: {exc}"

    entry = {
        "id": q["id"],
        "category": q["category"],
        "difficulty": q["difficulty"],
        "question": q["question"],
        "scores": entry_scores,
        "raw_total": raw,
        "rationales": verdict.get("rationales", {}),
        "key_facts_missing": verdict.get("key_facts_missing", []),
        "answer": response.answer if response else "",
        "citations": response.citations if response else [],
        "latency_sec": round(ask_time, 2),
        "cost_usd": response.total_cost_usd if response else None,
        "tool_calls": response.tool_calls if response else None,
        "num_turns": response.num_turns if response else None,
        "tools_used": response.tools_used if response else None,
        "stop_reason": response.stop_reason if response else None,
        "error": error,
    }
    if verbose:
        status = f"raw {raw}/11" if error is None else f"ERROR {error[:80]}"
        print(f"  [{q['id']}] {status}  ({ask_time:.1f}s)")
    return entry


async def run_strategy(
    strategy: str,
    questions: list[dict],
    dataset: dict,
    concurrency: int,
    *,
    note: str = "",
    on_question_done: Callable[[], None] | None = None,
    verbose: bool = True,
) -> Path:
    """Run one strategy over the questions; write eval/results_search_<s>.json."""
    from agent.agent import BluetoothWikiAgent

    agent = BluetoothWikiAgent(search_strategy=strategy)
    sem = asyncio.Semaphore(concurrency)

    async def _one(q):
        entry = await eval_question(agent, q, sem, verbose=verbose)
        if on_question_done:
            on_question_done()
        return entry

    entries = sorted(await asyncio.gather(*(_one(q) for q in questions)), key=lambda e: e["id"])
    results = aggregate(
        dataset,
        entries,
        system_name=f"Agent (search {strategy})",
        note=note or f"search strategy {strategy}",
    )
    out = REPO / "eval" / OUT_TEMPLATE.format(strategy=strategy)
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    return out
