import pytest

from qa.store.base import GraphEdge, GraphNode
from qa.store.graph_sqlite import SqliteGraphStore


@pytest.fixture
def store():
    s = SqliteGraphStore(":memory:")
    s.add_nodes([
        GraphNode("n1", "Procedure", "Connection Establishment",
                  {"doc_id": "core-6.0", "aliases": ["Connection Setup"]}),
        GraphNode("n2", "State", "Connection State", {"doc_id": "core-6.0"}),
        GraphNode("n3", "Timer", "connSupervisionTimeout", {"doc_id": "core-6.0"}),
        GraphNode("n4", "Event", "Disconnection Event", {"doc_id": "core-5.4"}),
    ])
    s.add_edges([
        GraphEdge("n1", "n2", "triggers"),
        GraphEdge("n2", "n3", "requires"),
        GraphEdge("n2", "n4", "triggers"),
    ])
    yield s
    s.close()


def test_lookup_is_case_insensitive_and_alias_aware(store):
    assert [n.id for n in store.lookup("connection establishment")] == ["n1"]
    assert [n.id for n in store.lookup("Connection Setup")] == ["n1"]


def test_lookup_can_filter_by_type(store):
    assert [n.id for n in store.lookup("Connection State", type="State")] == ["n2"]
    assert store.lookup("Connection State", type="Procedure") == []


def test_neighbors_one_hop_returns_both_directions(store):
    got = {(n.node.id, n.direction) for n in store.neighbors("n2", hops=1)}
    assert got == {("n1", "in"), ("n3", "out"), ("n4", "out")}


def test_neighbors_respects_relation_type_filter(store):
    got = [n.node.id for n in store.neighbors("n2", relation_types=["requires"], hops=1)]
    assert got == ["n3"]


def test_neighbors_two_hops_reaches_transitive_nodes_with_hop_recorded(store):
    by_id = {n.node.id: n for n in store.neighbors("n1", hops=2)}
    assert by_id["n2"].hop == 1
    assert by_id["n3"].hop == 2


def test_neighbors_limit_caps_the_result(store):
    assert len(store.neighbors("n2", hops=2, limit=2)) == 2


def test_add_nodes_is_idempotent_and_updates_properties(store):
    store.add_nodes([GraphNode("n1", "Procedure", "Connection Establishment",
                               {"doc_id": "core-6.0", "note": "updated"})])
    node = store.get_node("n1")
    assert node.properties["note"] == "updated"
    assert len(store.lookup("Connection Establishment")) == 1


def test_delete_document_removes_its_nodes_and_incident_edges(store):
    store.delete_document("core-5.4")
    assert store.get_node("n4") is None
    assert [n.node.id for n in store.neighbors("n2", relation_types=["triggers"], hops=1)] == ["n1"]


def test_persists_to_a_file(tmp_path):
    path = tmp_path / "graph.db"
    s = SqliteGraphStore(path)
    s.add_nodes([GraphNode("x", "Layer", "L2CAP", {"doc_id": "core-6.0"})])
    s.close()
    again = SqliteGraphStore(path)
    assert again.get_node("x").name == "L2CAP"
    again.close()
