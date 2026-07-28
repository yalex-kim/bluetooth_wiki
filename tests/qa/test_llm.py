import pytest

from qa import llm


class _FakeMsg:
    def __init__(self, content):
        self.content = content
        self.tool_calls = None


class _FakeChoice:
    def __init__(self, content):
        self.message = _FakeMsg(content)
        self.finish_reason = "stop"


class _FakeResp:
    def __init__(self, content):
        self.choices = [_FakeChoice(content)]
        self.usage = None


class _FakeCompletions:
    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = []

    async def create(self, **kw):
        self.calls.append(kw)
        return _FakeResp(self.replies.pop(0))


class _FakeClient:
    def __init__(self, replies):
        completions = _FakeCompletions(replies)
        self.chat = type("C", (), {"completions": completions})()


SCHEMA = {
    "type": "object",
    "required": ["entities"],
    "properties": {
        "entities": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["name", "type"],
                "properties": {
                    "name": {"type": "string"},
                    "type": {"type": "string", "enum": ["Procedure", "State"]},
                },
            },
        }
    },
}


@pytest.mark.asyncio
async def test_structured_call_accepts_valid_payload(monkeypatch):
    fake = _FakeClient(['{"entities": [{"name": "Connection", "type": "Procedure"}]}'])
    monkeypatch.setattr(llm, "get_client", lambda: fake)
    out = await llm.structured_call([{"role": "user", "content": "x"}], SCHEMA)
    assert out == {"entities": [{"name": "Connection", "type": "Procedure"}]}


@pytest.mark.asyncio
async def test_structured_call_retries_on_schema_violation(monkeypatch):
    fake = _FakeClient([
        '{"entities": [{"name": "Connection", "type": "Banana"}]}',  # enum violation
        '{"entities": [{"name": "Connection", "type": "State"}]}',  # repaired
    ])
    monkeypatch.setattr(llm, "get_client", lambda: fake)
    out = await llm.structured_call([{"role": "user", "content": "x"}], SCHEMA)
    assert out["entities"][0]["type"] == "State"
    # the repair turn must tell the model what was wrong
    assert "Banana" in str(fake.chat.completions.calls[1]["messages"])


@pytest.mark.asyncio
async def test_structured_call_raises_after_retries(monkeypatch):
    fake = _FakeClient(["not json", "still not json", "nope"])
    monkeypatch.setattr(llm, "get_client", lambda: fake)
    with pytest.raises(llm.StructuredOutputError):
        await llm.structured_call([{"role": "user", "content": "x"}], SCHEMA, retries=2)


@pytest.mark.asyncio
async def test_structured_call_strips_code_fence(monkeypatch):
    fake = _FakeClient(['```json\n{"entities": []}\n```'])
    monkeypatch.setattr(llm, "get_client", lambda: fake)
    assert await llm.structured_call([{"role": "user", "content": "x"}], SCHEMA) == {"entities": []}
