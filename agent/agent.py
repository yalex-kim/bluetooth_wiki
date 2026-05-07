"""BluetoothWikiAgent — the embedded agentic loop.

External clients call a single entry point ``ask(question)`` and receive a
structured ``{answer, citations, reasoning}`` payload. The system prompt,
model, tool surface, and citation-URL resolution are all locked in here so
every client (HTTP, MCP, web sidebar) gets the same answer quality.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
    create_sdk_mcp_server,
)

from .citations import hydrate_citations
from .config import MAX_TURNS, MODEL, SYSTEM_PROMPT_PATH
from .tools import ALL_TOOLS


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


_FENCED_JSON_RE = re.compile(r"```json\s*\n(?P<body>.*?)\n```", re.DOTALL)


def _extract_json_payload(text: str) -> dict | None:
    """Extract the agent's structured answer.

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
    # Brace-balanced fallback: find the first '{' and walk until matched.
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


def _parse_final_text(text: str) -> AgentResponse:
    """Extract the JSON-formatted answer block the agent is instructed to emit."""
    data = _extract_json_payload(text)
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
    def __init__(self, model: str = MODEL):
        self._system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
        self._mcp_server = create_sdk_mcp_server(
            name="bluetooth-wiki",
            version="0.1.0",
            tools=ALL_TOOLS,
        )
        tool_names = [
            "mcp__bluetooth-wiki__list_index",
            "mcp__bluetooth-wiki__search_wiki",
            "mcp__bluetooth-wiki__read_page",
            "mcp__bluetooth-wiki__read_source",
        ]
        self._options = ClaudeAgentOptions(
            model=model,
            system_prompt=self._system_prompt,
            mcp_servers={"bluetooth-wiki": self._mcp_server},
            allowed_tools=tool_names,
            # Block all of Claude Code's built-in tools so the agent only sees
            # our four wiki tools. ToolSearch in particular kept showing up in
            # the loop trace; explicit denials + setting_sources=[] kill it.
            disallowed_tools=[
                "ToolSearch",
                "Bash",
                "Read",
                "Write",
                "Edit",
                "Glob",
                "Grep",
                "WebFetch",
                "WebSearch",
                "Task",
                "TodoWrite",
                "NotebookEdit",
            ],
            setting_sources=[],
            max_turns=MAX_TURNS,
            permission_mode="bypassPermissions",
        )

    async def ask(self, question: str) -> AgentResponse:
        text_blocks: list[str] = []  # every TextBlock seen, in order
        tool_calls = 0
        tools_used: dict[str, int] = {}
        result_msg: ResultMessage | None = None
        async with ClaudeSDKClient(options=self._options) as client:
            await client.query(question)
            async for msg in client.receive_response():
                if isinstance(msg, AssistantMessage):
                    for block in msg.content:
                        if isinstance(block, TextBlock):
                            if block.text:
                                text_blocks.append(block.text)
                        elif isinstance(block, ToolUseBlock):
                            tool_calls += 1
                            name = block.name
                            tools_used[name] = tools_used.get(name, 0) + 1
                elif isinstance(msg, ResultMessage):
                    result_msg = msg

        # Resolution order:
        # 1) ResultMessage.result (the SDK's authoritative final string)
        # 2) the last text block that contains a fenced ```json ... ``` payload
        # 3) the last non-empty text block
        # 4) all text concatenated (so the parser still has something to work with)
        final_text = ""
        if result_msg and getattr(result_msg, "result", None):
            final_text = result_msg.result
        if not final_text:
            for blk in reversed(text_blocks):
                if "```json" in blk:
                    final_text = blk
                    break
        if not final_text and text_blocks:
            final_text = text_blocks[-1]
        if not final_text and text_blocks:
            final_text = "\n\n".join(text_blocks)

        response = _parse_final_text(final_text)
        response.tool_calls = tool_calls
        response.tools_used = tools_used or None
        if result_msg is not None:
            response.num_turns = result_msg.num_turns
            response.duration_ms = result_msg.duration_ms
            response.duration_api_ms = result_msg.duration_api_ms
            response.total_cost_usd = result_msg.total_cost_usd
            response.usage = result_msg.usage
            response.stop_reason = result_msg.stop_reason
        return response
