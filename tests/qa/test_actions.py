import pytest

from qa.retrieval.actions import RetrievalActions
from qa.store.base import GraphEdge, GraphNode, VectorRecord
from qa.store.graph_sqlite import SqliteGraphStore
from qa.store.vector_local import LocalVectorStore

SECTION_TEXT = """# Core

## 4 LINK LAYER

Chapter body.

### 4.5 CONNECTION STATE

The peripheral shall use connSupervisionTimeout.
"""


@pytest.fixture
def actions(tmp_path):
    src = tmp_path / "Core_v6.0.md"
    src.write_text(SECTION_TEXT, encoding="utf-8")

    vec = LocalVectorStore(tmp_path / "vec")
    vec.upsert([
        VectorRecord("core-6.0#4.5::s0", "connection state and supervision timeout",
                     [1.0, 0.0], {"doc_id": "core-6.0", "doc_type": "Core", "version": "6.0",
                                  "section": "4.5", "section_id": "core-6.0#4.5",
                                  "title": "CONNECTION STATE", "kind": "section",
                                  "page": 512, "doc_title": "Core Spec v6.0"}),
        VectorRecord("mesh#2::s0", "provisioning bearer",
                     [0.0, 1.0], {"doc_id": "mesh-1.1", "doc_type": "Mesh", "version": "1.1",
                                  "section": "2", "section_id": "mesh-1.1#2",
                                  "title": "PROVISIONING", "kind": "section",
                                  "page": 20, "doc_title": "Mesh 1.1"}),
    ])

    graph = SqliteGraphStore(":memory:")
    graph.add_nodes([
        GraphNode("core-6.0", "Document", "Core 6.0", {"doc_id": "core-6.0"}),
        GraphNode("core-6.0#4.5", "Section", "CONNECTION STATE",
                  {"doc_id": "core-6.0", "number": "4.5", "line_start": 7, "line_end": 10,
                   "page": 512, "version": "6.0"}),
        GraphNode("core-6.0:entity:connsupervisiontimeout", "Timer", "connSupervisionTimeout",
                  {"doc_id": "core-6.0", "aliases": ["supervision timeout"],
                   "section_id": "core-6.0#4.5"}),
        GraphNode("core-6.0:table:1", "Table", "Table 4.1: Connection parameters",
                  {"doc_id": "core-6.0", "section_id": "core-6.0#4.5",
                   "markdown": "| Parameter | Min |\n|---|---|\n| connInterval | 7.5 ms |"}),
        GraphNode("core-6.0:figure:1", "Figure", "Figure 4.3: Connection event timing",
                  {"doc_id": "core-6.0", "section_id": "core-6.0#4.5",
                   "image_path": "img/f43.png", "description": "Timing diagram."}),
    ])
    graph.add_edges([
        GraphEdge("core-6.0:entity:connsupervisiontimeout", "core-6.0#4.5", "definedIn"),
        GraphEdge("core-6.0#4.5", "core-6.0:table:1", "hasTable"),
        GraphEdge("core-6.0#4.5", "core-6.0:figure:1", "hasFigure"),
    ])

    async def fake_embed(texts):
        return [[1.0, 0.0] for _ in texts]

    yield RetrievalActions(
        vec, graph, embed_fn=fake_embed,
        doc_registry={"core-6.0": {"title": "Core Spec v6.0", "path": str(src),
                                   "doc_type": "Core", "version": "6.0"}},
    )
    graph.close()


@pytest.mark.asyncio
async def test_vector_search_returns_text_and_evidence(actions):
    result = await actions.vector_search("supervision timeout")
    assert "CONNECTION STATE" in result.text
    assert result.evidence and result.evidence[0].section == "4.5"
    assert result.evidence[0].page == 512


@pytest.mark.asyncio
async def test_vector_search_scope_filter_restricts_doc_type(actions):
    result = await actions.vector_search("provisioning", scope_filter={"doc_type": "Mesh"})
    assert len(result.evidence) == 1
    assert "Mesh" in result.evidence[0].doc


def test_graph_lookup_finds_by_alias_and_reports_node_ids(actions):
    result = actions.graph_lookup("supervision timeout")
    assert "connSupervisionTimeout" in result.text
    assert "core-6.0:entity:connsupervisiontimeout" in result.text


def test_graph_traverse_lists_typed_neighbours(actions):
    result = actions.graph_traverse("core-6.0#4.5", hops=1)
    assert "hasTable" in result.text and "definedIn" in result.text


def test_get_section_text_slices_the_source_file(actions):
    result = actions.get_section_text("core-6.0", "core-6.0#4.5")
    assert "connSupervisionTimeout" in result.text
    assert result.evidence[0].kind == "section"


def test_get_table_returns_markdown_preserved(actions):
    result = actions.get_table(table_id="core-6.0:table:1")
    assert "| connInterval | 7.5 ms |" in result.text


def test_get_table_by_section_finds_the_sections_tables(actions):
    result = actions.get_table(section_id="core-6.0#4.5")
    assert "Table 4.1" in result.text


def test_get_figure_returns_description_and_path(actions):
    result = actions.get_figure("core-6.0:figure:1")
    assert "Timing diagram." in result.text and "img/f43.png" in result.text


@pytest.mark.asyncio
async def test_run_dispatches_by_name_and_reports_unknown_actions(actions):
    ok = await actions.run("get_table", {"table_id": "core-6.0:table:1"})
    assert "connInterval" in ok.text
    bad = await actions.run("teleport", {})
    assert "unknown action" in bad.text.lower() and bad.evidence == []


@pytest.mark.asyncio
async def test_missing_ids_return_a_message_not_an_exception(actions):
    result = await actions.run("get_figure", {"figure_id": "nope"})
    assert "not found" in result.text.lower() and result.evidence == []


@pytest.mark.asyncio
async def test_erratum_is_appended_and_marked_as_taking_precedence(actions):
    actions.graph.add_nodes([GraphNode(
        "errata-1#3", "Section", "ERRATUM 1234",
        {"doc_id": "errata-1", "number": "3", "text": "connInterval minimum is 7.5 ms, not 6 ms.",
         "version": "6.0"})])
    actions.graph.add_edges([GraphEdge("errata-1#3", "core-6.0#4.5", "amends")])
    result = actions.get_section_text("core-6.0", "core-6.0#4.5")
    assert "ERRATUM" in result.text
    assert "precedence" in result.text.lower()


def test_tool_schemas_cover_all_six_actions():
    names = {s["function"]["name"] for s in RetrievalActions.TOOL_SCHEMAS}
    assert names == {"vector_search", "graph_lookup", "graph_traverse",
                     "get_section_text", "get_figure", "get_table"}
