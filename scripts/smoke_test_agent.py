"""Phase 1 smoke test — run a single question through BluetoothWikiAgent.

Usage:
    pip install -e .
    export ANTHROPIC_API_KEY=...
    python scripts/smoke_test_agent.py "What is Channel Sounding introduced in?"
"""

from __future__ import annotations

import asyncio
import json
import sys

from agent import BluetoothWikiAgent


DEFAULT_QUESTION = "Which Bluetooth version introduced Channel Sounding, and what does it do?"


async def main() -> int:
    question = " ".join(sys.argv[1:]).strip() or DEFAULT_QUESTION
    print(f"Q: {question}\n")
    agent = BluetoothWikiAgent()
    response = await agent.ask(question)
    print("=" * 60)
    print("ANSWER")
    print("=" * 60)
    print(response.answer)
    print()
    print("=" * 60)
    print("CITATIONS")
    print("=" * 60)
    print(json.dumps(response.citations, indent=2))
    print()
    print("=" * 60)
    print("REASONING")
    print("=" * 60)
    print(response.reasoning)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
