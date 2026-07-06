"""In-memory background-job registry for eval runs.

Deliberately simple: a module-level dict of job states populated by tasks on
the FastAPI process's own event loop. Single-process only — jobs do not
survive a server restart and this is not suitable for multi-worker
deployments. Fine for the intended use: a local comparison/test UI.
"""

from __future__ import annotations

import json
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


@dataclass
class JobState:
    job_id: str
    state: str = "pending"  # pending | running | done | error
    completed: int = 0
    total: int = 0
    result_paths: list[str] = field(default_factory=list)
    report_path: str | None = None
    error: str | None = None
    started_at: float = field(default_factory=time.time)


JOBS: dict[str, JobState] = {}


def create_job() -> JobState:
    job = JobState(job_id=uuid.uuid4().hex[:12])
    JOBS[job.job_id] = job
    return job


def get_job(job_id: str) -> JobState | None:
    return JOBS.get(job_id)


async def run_eval_job(job: JobState, strategies: list[str], limit: int | None, question_ids: list[str] | None, concurrency: int) -> None:
    """Drive the same per-question logic as scripts/run_search_eval.py
    (shared implementation in eval/runner.py)."""
    from eval.report_render import build_html
    from eval.runner import load_questions, run_strategy

    job.state = "running"
    try:
        dataset, questions = load_questions(question_ids, limit)
        if not questions:
            raise ValueError("no questions selected")
        job.total = len(questions) * len(strategies)

        def _tick() -> None:
            job.completed += 1

        for strategy in strategies:
            out = await run_strategy(
                strategy,
                questions,
                dataset,
                concurrency,
                note=f"search strategy {strategy}; generated via server /api/eval/run job {job.job_id}",
                on_question_done=_tick,
                verbose=False,
            )
            job.result_paths.append(str(out.relative_to(REPO)))

        loaded = {}
        for rel in job.result_paths:
            p = REPO / rel
            loaded[p.stem.replace("results_search_", "")] = json.loads(p.read_text(encoding="utf-8"))
        report = REPO / "eval" / f"report_search_compare_{job.job_id}.html"
        report.write_text(build_html(loaded), encoding="utf-8")
        job.report_path = str(report.relative_to(REPO))
        job.state = "done"
    except Exception as exc:
        job.state = "error"
        job.error = f"{type(exc).__name__}: {exc}"
