from qa.store.base import VectorRecord
from qa.store.vector_local import LocalVectorStore


def _store(tmp_path):
    s = LocalVectorStore(tmp_path / "vec")
    s.upsert([
        VectorRecord("a", "connection interval", [1.0, 0.0], {"doc_type": "Core", "version": "6.0"}),
        VectorRecord("b", "mesh provisioning", [0.0, 1.0], {"doc_type": "Mesh", "version": "1.1"}),
        VectorRecord("c", "connection timing", [0.9, 0.1], {"doc_type": "Core", "version": "5.4"}),
    ])
    return s


def test_search_ranks_by_cosine_similarity(tmp_path):
    hits = _store(tmp_path).search([1.0, 0.0], top_k=3)
    assert [h.id for h in hits] == ["a", "c", "b"]
    assert hits[0].score > hits[1].score > hits[2].score


def test_filters_restrict_by_metadata_equality_and_membership(tmp_path):
    s = _store(tmp_path)
    assert [h.id for h in s.search([1.0, 0.0], top_k=5, filters={"doc_type": "Mesh"})] == ["b"]
    ids = {h.id for h in s.search([1.0, 0.0], top_k=5, filters={"version": ["6.0", "5.4"]})}
    assert ids == {"a", "c"}


def test_upsert_replaces_an_existing_id(tmp_path):
    s = _store(tmp_path)
    s.upsert([VectorRecord("a", "replaced", [0.0, 1.0], {"doc_type": "Core"})])
    assert s.count() == 3
    assert s.get("a").text == "replaced"


def test_delete_removes_records(tmp_path):
    s = _store(tmp_path)
    s.delete(["a", "missing"])
    assert s.count() == 2 and s.get("a") is None


def test_persist_then_load_round_trips(tmp_path):
    _store(tmp_path).persist()
    reloaded = LocalVectorStore.load(tmp_path / "vec")
    assert reloaded.count() == 3
    assert [h.id for h in reloaded.search([1.0, 0.0], top_k=1)] == ["a"]


def test_search_on_empty_store_returns_empty(tmp_path):
    assert LocalVectorStore(tmp_path / "empty").search([1.0, 0.0]) == []
