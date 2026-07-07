"""BluetoothWikiAgent — the embedded agentic loop (OpenAI-compatible backend).

External clients call ``ask(question)`` and receive a structured
``{answer, citations, reasoning}`` payload. Model, tool surface, system prompt,
and citation resolution are locked in here so every client (HTTP, MCP, web
sidebar) gets the same answer quality. The LLM is a company-hosted gpt-oss-120B
behind an OpenAI-compatible endpoint (see agent/llm.py).
"""
from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass

from .citations import hydrate_citations
from .config import MAX_TURNS, MODEL, SEARCH_STRATEGY, SYSTEM_PROMPT_PATH
from .json_extract import extract_json_payload
from .llm import get_client
from .tools import build_tools


@dataclass
class AgentResponse:
    answer: str
    citations: list[dict]
    reasoning: str
    raw: str
    num_turns: int = 0
    tool_calls: int = 0
    tools_used: dict[str, int] | None = None
    duration_ms: int = 0
    duration_api_ms: int = 0
    total_cost_usd: float | None = None
    usage: dict | None = None
    stop_reason: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def _parse_final_text(text: str) -> AgentResponse:
    """Extract the JSON-formatted answer block the agent is instructed to emit."""
    data = extract_json_payload(text)
    if data is not None:
        citations = data.get("citations") or []
        hydrated = [asdict(c) for c in hydrate_citations(citations)]
        return AgentResponse(
            answer=str(data.get("answer", "")).strip(),
            citations=hydrated,
            reasoning=str(data.get("reasoning", "")).strip(),
            raw=text,
        )
    return AgentResponse(answer=text.strip(), citations=[], reasoning="", raw=text)


class BluetoothWikiAgent:
    def __init__(self, model: str = MODEL, search_strategy: str = SEARCH_STRATEGY):
        self._model = model
        self._system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
        self.search_strategy = search_strategy
        self._schemas, self._handlers = build_tools(search_strategy)

    async def ask(self, question: str) -> AgentResponse:
        client = get_client()
        messages: list[dict] = [
            {"role": "system", "content": self._system_prompt},
            {"role": "user", "content": question},
        ]
        tool_calls = 0
        tools_used: dict[str, int] = {}
        prompt_tokens = completion_tokens = 0
        finish_reason: str | None = None
        final_text = ""
        num_turns = 0
        t0 = time.time()

        for _ in range(MAX_TURNS):
            num_turns += 1
            resp = await client.chat.completions.create(
                model=self._model, messages=messages, tools=self._schemas, tool_choice="auto",
            )
            usage = getattr(resp, "usage", None)
            if usage:
                prompt_tokens += getattr(usage, "prompt_tokens", 0) or 0
                completion_tokens += getattr(usage, "completion_tokens", 0) or 0
            choice = resp.choices[0]
            msg = choice.message
            finish_reason = choice.finish_reason
            calls = getattr(msg, "tool_calls", None)

            assistant_msg: dict = {"role": "assistant", "content": msg.content or ""}
            if calls:
                assistant_msg["tool_calls"] = [
                    {"id": c.id, "type": "function",
                     "function": {"name": c.function.name, "arguments": c.function.arguments}}
                    for c in calls
                ]
            messages.append(assistant_msg)

            if not calls:
                final_text = msg.content or ""
                break

            for c in calls:
                tool_calls += 1
                name = c.function.name
                tools_used[name] = tools_used.get(name, 0) + 1
                try:
                    args = json.loads(c.function.arguments or "{}")
                    if not isinstance(args, dict):
                        args = {}
                except json.JSONDecodeError:
                    args = {}
                handler = self._handlers.get(name)
                if handler is None:
                    result = f"Error: unknown tool {name!r}. Available: {list(self._handlers)}."
                else:
                    try:
                        result = await handler(args)
                    except Exception as exc:
                        result = f"Error running {name}: {exc}"
                messages.append({"role": "tool", "tool_call_id": c.id, "content": result})

        response = _parse_final_text(final_text or "")
        response.tool_calls = tool_calls
        response.tools_used = tools_used or None
        response.num_turns = num_turns
        response.duration_ms = int((time.time() - t0) * 1000)
        response.usage = {"prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens}
        response.total_cost_usd = None
        response.stop_reason = finish_reason
        return response
