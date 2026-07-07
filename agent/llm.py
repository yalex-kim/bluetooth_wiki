"""Shared OpenAI-compatible async client.

The agent loop, the eval judge, and the v2 sufficiency judge all talk to the
same endpoint (a company-hosted gpt-oss-120B behind an OpenAI-compatible
/v1/chat/completions API), configured via OPENAI_BASE_URL / OPENAI_API_KEY.
"""
from __future__ import annotations

from agent.config import OPENAI_API_KEY, OPENAI_BASE_URL

_client = None


def get_client():
    """Return a process-cached AsyncOpenAI client for the configured endpoint."""
    global _client
    if _client is None:
        from openai import AsyncOpenAI

        _client = AsyncOpenAI(
            base_url=OPENAI_BASE_URL or None,
            api_key=OPENAI_API_KEY or "not-needed",
        )
    return _client
