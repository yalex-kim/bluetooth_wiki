import asyncio
from types import SimpleNamespace


def _fake_client_returning(content: str):
    async def _create(*, model, messages, max_tokens):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=content))])
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=_create)))


def test_sufficiency_parses_openai_json(monkeypatch):
    import search.sufficiency as suf
    from search.base import SearchHit
    monkeypatch.setattr(
        suf, "get_client",
        lambda: _fake_client_returning('{"sufficient": false, "reason": "thin", "reformulated_query": "CS step mode"}'),
    )
    hits = [SearchHit(file_path="wiki/x.md", snippet="...")]
    v = asyncio.run(suf.check_sufficiency("q", "query", hits))
    assert v.sufficient is False
    assert v.reformulated_query == "CS step mode"
    assert v.llm_called is True


def test_judge_parses_openai_json(monkeypatch):
    import eval.judge as jm
    monkeypatch.setattr(
        jm, "get_client",
        lambda: _fake_client_returning('{"accuracy": 5, "completeness": 5, "citation": 5, "hallucination_penalty": 0, "usability": 5}'),
    )
    q = {"question": "q", "reference_answer": "r", "key_facts": ["a"], "expected_citations": ["[Core 6.0]"]}
    verdict = asyncio.run(jm.judge(q, "some answer"))
    assert verdict["scores"]["accuracy"] == 5 and verdict["scores"]["usability"] == 5
