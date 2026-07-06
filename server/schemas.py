"""Pydantic request/response models for the HTTP test server."""

from __future__ import annotations

from pydantic import BaseModel, Field

VALID_STRATEGIES = ("v0", "v1", "v2")


class CompareRequest(BaseModel):
    question: str = Field(min_length=1)
    strategies: list[str] = Field(default=["v0", "v1", "v2"])


class StrategyAnswer(BaseModel):
    strategy: str
    answer: str
    citations: list[dict]
    reasoning: str
    wall_time_sec: float
    num_turns: int
    tool_calls: int
    tools_used: dict | None
    total_cost_usd: float | None
    stop_reason: str | None
    error: str | None = None


class CompareResponse(BaseModel):
    question: str
    results: dict[str, StrategyAnswer]


class EvalRunRequest(BaseModel):
    strategies: list[str] = Field(default=["v0", "v1", "v2"])
    limit: int | None = None
    question_ids: list[str] | None = None
    concurrency: int = 3


class EvalRunResponse(BaseModel):
    job_id: str


class JobStatus(BaseModel):
    job_id: str
    state: str  # pending | running | done | error
    progress: dict
    result_paths: list[str] | None = None
    report_url: str | None = None
    error: str | None = None
