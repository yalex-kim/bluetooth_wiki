"""HTTP exposure of the Spec Q&A Tool (§1.2).

One endpoint, one contract. The Orchestrator posts §8.1's input and gets §8.1's
output; the vector and graph stores stay behind this process and are never
reachable directly.
"""
from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from qa import config
from qa.service import SpecQAService

app = FastAPI(title="Bluetooth Spec Q&A Agent", version="0.1.0")

_service: SpecQAService | None = None


def get_service() -> SpecQAService:
    """Built on first request so importing this module stays cheap."""
    global _service
    if _service is None:
        _service = SpecQAService.from_index()
    return _service


class AskRequest(BaseModel):
    query: str
    spec_scope: str | None = None
    spec_version: str | None = None
    conversation_context: list[dict] = Field(default_factory=list)
    include_trace: bool = False


class Citation(BaseModel):
    doc: str
    section: str
    page: int | None = None
    path: str = ""


class AskResponse(BaseModel):
    answer: str
    citations: list[Citation]
    related_entities: list[str]
    confidence: str
    out_of_scope: bool
    retrieval_trace: dict | None = None


@app.post("/qa/ask", response_model=AskResponse)
async def ask(req: AskRequest):
    return await get_service().ask(
        req.query,
        spec_scope=req.spec_scope,
        spec_version=req.spec_version,
        conversation_context=req.conversation_context or None,
        include_trace=req.include_trace,
    )


@app.get("/qa/health")
async def health():
    return get_service().health()


def main():
    import uvicorn

    uvicorn.run(app, host=config.HTTP_HOST, port=config.HTTP_PORT)


if __name__ == "__main__":
    main()
