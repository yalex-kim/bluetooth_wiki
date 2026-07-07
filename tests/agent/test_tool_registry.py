import asyncio


def test_build_tools_schemas_and_handlers():
    from agent.tools import build_tools
    schemas, handlers = build_tools("v1")

    names = [s["function"]["name"] for s in schemas]
    assert set(names) == {"list_index", "search_wiki", "read_page", "read_source"}
    assert set(handlers) == set(names)

    for s in schemas:
        assert s["type"] == "function"
        assert "parameters" in s["function"]
        assert s["function"]["parameters"]["type"] == "object"

    reqs = {s["function"]["name"]: s["function"]["parameters"].get("required", []) for s in schemas}
    assert reqs["search_wiki"] == ["query"]
    assert reqs["read_page"] == ["path"]
    assert reqs["read_source"] == ["version"]
    assert reqs["list_index"] == []


def test_list_index_handler_runs_real_logic():
    from agent.tools import build_tools
    _, handlers = build_tools("v1")
    out = asyncio.run(handlers["list_index"]({}))
    assert isinstance(out, str) and out.strip()
