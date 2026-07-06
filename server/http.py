"""FastAPI test server — the `bluetooth-wiki-agent-http` entry point.

Routes:
    GET  /                          static test UI (server/static/index.html)
    GET  /api/health                liveness
    POST /api/compare               run a question through selected strategies concurrently
    POST /api/eval/run              start a background eval job → {job_id}
    GET  /api/eval/status/{job_id}  poll job progress
    GET  /api/eval/report/{job_id}  the finished job's comparison report (HTML)
    GET  /reports/{filename}        generated report files (eval/report_search_compare*.html)

Run:  bluetooth-wiki-agent-http   (or: uvicorn server.http:app --port 8080)
"""

from __future__ import annotations

import asyncio
import time
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse

from agent.config import HTTP_HOST, HTTP_PORT

from . import jobs
from .schemas import (
    VALID_STRATEGIES,
    CompareRequest,
    CompareResponse,
    EvalRunRequest,
    EvalRunResponse,
    JobStatus,
    StrategyAnswer,
)

REPO = Path(__file__).resolve().parent.parent
STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="Bluetooth Wiki — Search Strategy Test Server", version="0.1.0")


def _check_strategies(strategies: list[str]) -> list[str]:
    bad = [s for s in strategies if s not in VALID_STRATEGIES]
    if bad:
        raise HTTPException(status_code=422, detail=f"unknown strategies {bad}; valid: {list(VALID_STRATEGIES)}")
    if not strategies:
        raise HTTPException(status_code=422, detail="at least one strategy required")
    return list(dict.fromkeys(strategies))  # dedupe, keep order


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    return HTMLResponse((STATIC_DIR / "index.html").read_text(encoding="utf-8"))


@app.get("/api/health")
async def health() -> dict:
    return {"status": "ok"}


async def _ask_one(strategy: str, question: str) -> StrategyAnswer:
    from agent.agent import BluetoothWikiAgent

    t0 = time.perf_counter()
    try:
        agent = BluetoothWikiAgent(search_strategy=strategy)
        resp = await agent.ask(question)
        return StrategyAnswer(
            strategy=strategy,
            answer=resp.answer,
            citations=resp.citations,
            reasoning=resp.reasoning,
            wall_time_sec=round(time.perf_counter() - t0, 2),
            num_turns=resp.num_turns,
            tool_calls=resp.tool_calls,
            tools_used=resp.tools_used,
            total_cost_usd=resp.total_cost_usd,
            stop_reason=resp.stop_reason,
        )
    except Exception as exc:
        return StrategyAnswer(
            strategy=strategy,
            answer="",
            citations=[],
            reasoning="",
            wall_time_sec=round(time.perf_counter() - t0, 2),
            num_turns=0,
            tool_calls=0,
            tools_used=None,
            total_cost_usd=None,
            stop_reason=None,
            error=f"{type(exc).__name__}: {exc}",
        )


@app.post("/api/compare", response_model=CompareResponse)
async def compare(req: CompareRequest) -> CompareResponse:
    strategies = _check_strategies(req.strategies)
    answers = await asyncio.gather(*(_ask_one(s, req.question) for s in strategies))
    return CompareResponse(question=req.question, results={a.strategy: a for a in answers})


@app.post("/api/eval/run", response_model=EvalRunResponse, status_code=202)
async def eval_run(req: EvalRunRequest) -> EvalRunResponse:
    strategies = _check_strategies(req.strategies)
    job = jobs.create_job()
    asyncio.create_task(jobs.run_eval_job(job, strategies, req.limit, req.question_ids, req.concurrency))
    return EvalRunResponse(job_id=job.job_id)


@app.get("/api/eval/status/{job_id}", response_model=JobStatus)
async def eval_status(job_id: str) -> JobStatus:
    job = jobs.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="unknown job_id")
    return JobStatus(
        job_id=job.job_id,
        state=job.state,
        progress={"completed": job.completed, "total": job.total},
        result_paths=job.result_paths or None,
        report_url=f"/api/eval/report/{job.job_id}" if job.report_path else None,
        error=job.error,
    )


@app.get("/api/eval/report/{job_id}", response_class=HTMLResponse)
async def eval_report(job_id: str) -> HTMLResponse:
    job = jobs.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="unknown job_id")
    if job.state != "done" or not job.report_path:
        raise HTTPException(status_code=409, detail=f"job is {job.state}")
    return HTMLResponse((REPO / job.report_path).read_text(encoding="utf-8"))


@app.get("/reports/{filename}")
async def report_file(filename: str) -> FileResponse:
    # Only serve generated comparison reports, no path traversal.
    if "/" in filename or ".." in filename or not filename.startswith("report_search_compare"):
        raise HTTPException(status_code=404)
    path = REPO / "eval" / filename
    if not path.is_file():
        raise HTTPException(status_code=404)
    return FileResponse(path)


def main() -> None:
    import uvicorn

    uvicorn.run("server.http:app", host=HTTP_HOST, port=HTTP_PORT, reload=False)


if __name__ == "__main__":
    main()
