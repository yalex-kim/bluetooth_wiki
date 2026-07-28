"""Single entry point for every LLM call the Q&A agent makes.

The company endpoint is OpenAI-compatible (chat + embeddings). Structured
output goes through ``structured_call``, which validates against a JSON schema
and re-prompts on violation — the §5.3 fallback for a serving stack whose
grammar-constrained decoding support is still unconfirmed. If guided JSON turns
out to be available, it becomes one extra kwarg here and nothing else changes.
"""
from __future__ import annotations

import json
import re

from qa import config

_client = None


class StructuredOutputError(RuntimeError):
    """The model could not produce schema-valid JSON within the retry budget."""


def get_client():
    """Return a process-cached AsyncOpenAI client for the configured endpoint."""
    global _client
    if _client is None:
        from openai import AsyncOpenAI

        _client = AsyncOpenAI(
            base_url=config.OPENAI_BASE_URL or None,
            api_key=config.OPENAI_API_KEY or "not-needed",
        )
    return _client


async def chat(messages, *, model=None, tools=None, tool_choice="auto"):
    kwargs = {"model": model or config.MODEL, "messages": messages}
    if tools:
        kwargs["tools"] = tools
        kwargs["tool_choice"] = tool_choice
    return await get_client().chat.completions.create(**kwargs)


async def embed(texts, *, model=None):
    resp = await get_client().embeddings.create(
        model=model or config.EMBED_MODEL, input=list(texts)
    )
    return [d.embedding for d in resp.data]


_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)```", re.S)


def extract_json(text):
    """Best-effort JSON object out of a model reply (fenced, bare, or embedded)."""
    if not text:
        return None
    for candidate in [m.group(1) for m in _FENCE_RE.finditer(text)] + [text]:
        candidate = candidate.strip()
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            start, end = candidate.find("{"), candidate.rfind("}")
            if start != -1 and end > start:
                try:
                    return json.loads(candidate[start : end + 1])
                except json.JSONDecodeError:
                    continue
    return None


_TYPE_CHECKS = {
    "object": dict,
    "array": list,
    "string": str,
    "integer": int,
    "number": (int, float),
    "boolean": bool,
}


def validate(payload, schema, path="$"):
    """Validate against the JSON-Schema subset we actually emit.

    Returns a list of human-readable error strings (empty == valid). Kept
    deliberately small — type/required/properties/items/enum is everything the
    ontology and tool schemas use, and a real validator would be a new
    dependency (see the plan's no-new-deps constraint).
    """
    errors = []
    expected = schema.get("type")
    if expected in _TYPE_CHECKS:
        wrong_type = not isinstance(payload, _TYPE_CHECKS[expected])
        # bool is an int subclass — reject it where a number is expected
        if not wrong_type and expected in ("integer", "number") and isinstance(payload, bool):
            wrong_type = True
        if wrong_type:
            got = type(payload).__name__
            return [f"{path}: expected {expected}, got {got}"]

    if "enum" in schema and payload not in schema["enum"]:
        errors.append(f"{path}: {payload!r} is not one of {schema['enum']}")

    if expected == "object":
        for key in schema.get("required", []):
            if key not in payload:
                errors.append(f"{path}: missing required key {key!r}")
        for key, sub in schema.get("properties", {}).items():
            if key in payload:
                errors.extend(validate(payload[key], sub, f"{path}.{key}"))

    if expected == "array" and "items" in schema:
        for i, item in enumerate(payload):
            errors.extend(validate(item, schema["items"], f"{path}[{i}]"))

    return errors


async def structured_call(messages, schema, *, model=None, retries=None):
    """Ask for JSON, validate it, and re-prompt with the validator's complaint."""
    retries = config.STRUCTURED_RETRIES if retries is None else retries
    convo = list(messages)
    last_error = "no response"
    for attempt in range(retries + 1):
        resp = await chat(convo, model=model or config.EXTRACT_MODEL)
        text = resp.choices[0].message.content or ""
        payload = extract_json(text)
        if payload is None:
            last_error = "response was not valid JSON"
        else:
            errors = validate(payload, schema)
            if not errors:
                return payload
            last_error = "; ".join(errors)
        if attempt == retries:
            break
        convo = convo + [
            {"role": "assistant", "content": text},
            {
                "role": "user",
                "content": (
                    f"That reply was rejected: {last_error}. "
                    f"Reply again with JSON only, matching this schema exactly:\n"
                    f"{json.dumps(schema)}"
                ),
            },
        ]
    raise StructuredOutputError(last_error)
