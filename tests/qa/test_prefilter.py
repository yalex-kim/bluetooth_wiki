import pytest

from qa import prefilter


@pytest.mark.asyncio
async def test_explicit_scope_from_orchestrator_skips_the_llm():
    d = await prefilter.classify("무슨 뜻인가요?", spec_scope="Core-LE", spec_version="5.4")
    assert d.out_of_scope is False and d.used_llm is False
    assert d.scope_filter["doc_type"] == ["Core"]
    assert d.scope_filter["version"] == ["5.4"]


@pytest.mark.asyncio
async def test_obvious_bluetooth_query_is_in_scope_without_the_llm():
    d = await prefilter.classify("What is connSupervisionTimeout in the LE Link Layer?")
    assert d.out_of_scope is False and d.used_llm is False


@pytest.mark.asyncio
async def test_mesh_vocabulary_produces_a_mesh_hint():
    d = await prefilter.classify("Mesh provisioning bearer 절차 알려줘")
    assert "Mesh" in d.scope_filter["doc_type"]


@pytest.mark.asyncio
async def test_obviously_unrelated_query_is_rejected_without_the_llm():
    d = await prefilter.classify("What is the capital of France?")
    assert d.out_of_scope is True and d.used_llm is False


@pytest.mark.asyncio
async def test_ambiguous_query_falls_back_to_the_llm():
    calls = []

    async def fake_llm(query):
        calls.append(query)
        return {"out_of_scope": False, "doc_types": ["Core"], "reason": "protocol question"}

    # No Bluetooth vocabulary and no off-domain marker: the ambiguous middle,
    # which is the only band that is allowed to cost an LLM call.
    d = await prefilter.classify("How does the handshake work here?", llm_fn=fake_llm)
    assert d.used_llm is True and calls
    assert d.out_of_scope is False


@pytest.mark.asyncio
async def test_pairing_vocabulary_is_caught_lexically_without_the_llm():
    async def unreachable(query):
        raise AssertionError("the lexical gate should have answered this")

    d = await prefilter.classify("How does the pairing handshake work?", llm_fn=unreachable)
    assert d.out_of_scope is False and d.used_llm is False


@pytest.mark.asyncio
async def test_llm_failure_fails_open_into_the_loop():
    async def boom(query):
        raise RuntimeError("endpoint down")

    d = await prefilter.classify("Something entirely ambiguous here", llm_fn=boom)
    assert d.out_of_scope is False  # never reject a question because the gate broke
