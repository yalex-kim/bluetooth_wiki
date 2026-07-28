"""MCP exposure of the Spec Q&A Tool (§1.2).

The design doc's "팀 공용" is one shared *tool interface*, not a shared database:
every orchestrator and teammate calls this single tool, and the vector/graph
stores stay hidden behind it. The tool's input and output are §8.1 verbatim, so
an MCP caller and an HTTP caller see the identical contract.

MCP imports are deferred into the functions that need them, so this module
imports cleanly (and tests can reason about it) even where the optional `mcp`
package is not installed.
"""
from __future__ import annotations

import json

from qa.service import SpecQAService

TOOL_NAME = "bluetooth_spec_qa"

TOOL_DESCRIPTION = (
    "Answer a question about the Bluetooth specifications (Core, GATT, profiles, "
    "Mesh, LE Audio, Assigned Numbers, errata) with verified citations to the "
    "specification text. Returns {answer, citations, related_entities, confidence, "
    "out_of_scope, retrieval_trace}. If out_of_scope is true, the question was not "
    "about Bluetooth and should be routed elsewhere."
)

TOOL_INPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "query": {"type": "string", "description": "The question, in any language."},
        "spec_scope": {
            "type": "string",
            "description": "Optional document-family hint, e.g. 'Core-LE', 'GATT', 'Mesh', 'LEAudio'.",
        },
        "spec_version": {
            "type": "string",
            "description": "Optional specification version, e.g. '5.4' or '6.0'.",
        },
        "conversation_context": {
            "type": "array",
            "description": (
                "Optional prior turns, used only to re-interpret the question. "
                "This tool is stateless and stores nothing between calls."
            ),
            "items": {"type": "object"},
        },
        "include_trace": {
            "type": "boolean",
            "description": "Populate retrieval_trace for debugging and evaluation.",
        },
    },
    "required": ["query"],
}

_service: SpecQAService | None = None


def get_service() -> SpecQAService:
    global _service
    if _service is None:
        _service = SpecQAService.from_index()
    return _service


async def call_tool(arguments: dict) -> dict:
    """Run one §8.1 request. Separated from the MCP plumbing so it stays testable."""
    arguments = arguments or {}
    return await get_service().ask(
        arguments.get("query", ""),
        spec_scope=arguments.get("spec_scope"),
        spec_version=arguments.get("spec_version"),
        conversation_context=arguments.get("conversation_context") or None,
        include_trace=bool(arguments.get("include_trace")),
    )


def build_server():
    from mcp.server import Server
    from mcp.types import TextContent, Tool

    server = Server("bluetooth-spec-qa")

    @server.list_tools()
    async def list_tools() -> list:
        return [Tool(name=TOOL_NAME, description=TOOL_DESCRIPTION,
                     inputSchema=TOOL_INPUT_SCHEMA)]

    @server.call_tool()
    async def handle_call(name: str, arguments: dict) -> list:
        if name != TOOL_NAME:
            raise ValueError(f"Unknown tool: {name}")
        payload = await call_tool(arguments)
        return [TextContent(type="text", text=json.dumps(payload, ensure_ascii=False))]

    return server


async def serve():
    from mcp.server.stdio import stdio_server

    server = build_server()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main():
    import asyncio

    asyncio.run(serve())


if __name__ == "__main__":
    main()
