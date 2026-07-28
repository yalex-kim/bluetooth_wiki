import pytest

from qa import embeddings_local


class FakeEncoder:
    """Stands in for a SentenceTransformer: records what it was asked to encode."""

    def __init__(self, dim=4):
        self.dim = dim
        self.seen = []

    def encode(self, texts, **kw):
        self.seen.extend(texts)
        self.kwargs = kw
        return [[float(len(t) % 5)] + [0.0] * (self.dim - 1) for t in texts]


def test_bge_m3_gets_no_query_prefix():
    # BGE-M3 is trained without an instruction prefix; adding the bge-small
    # prefix silently degrades retrieval, so the distinction has to hold.
    enc = FakeEncoder()
    embeddings_local.encode(["what is connInterval"], model_name="BAAI/bge-m3",
                            is_query=True, encoder=enc)
    assert enc.seen == ["what is connInterval"]


def test_english_bge_small_does_get_the_query_prefix():
    enc = FakeEncoder()
    embeddings_local.encode(["what is connInterval"], model_name="BAAI/bge-small-en-v1.5",
                            is_query=True, encoder=enc)
    assert enc.seen[0].startswith("Represent this sentence")
    assert enc.seen[0].endswith("what is connInterval")


def test_passages_never_get_a_prefix():
    for model in ("BAAI/bge-m3", "BAAI/bge-small-en-v1.5"):
        enc = FakeEncoder()
        embeddings_local.encode(["passage text"], model_name=model, is_query=False, encoder=enc)
        assert enc.seen == ["passage text"]


def test_encode_returns_plain_lists_of_floats():
    enc = FakeEncoder(dim=3)
    out = embeddings_local.encode(["a", "bb"], model_name="BAAI/bge-m3", encoder=enc)
    assert isinstance(out, list) and len(out) == 2
    assert all(isinstance(v, list) and len(v) == 3 for v in out)
    assert all(isinstance(x, float) for x in out[0])


def test_encode_requests_normalised_embeddings():
    enc = FakeEncoder()
    embeddings_local.encode(["a"], model_name="BAAI/bge-m3", encoder=enc)
    assert enc.kwargs["normalize_embeddings"] is True


@pytest.mark.asyncio
async def test_embed_fn_is_an_async_callable_matching_the_pipeline_contract():
    enc = FakeEncoder()
    fn = embeddings_local.make_embed_fn(model_name="BAAI/bge-m3", encoder=enc)
    out = await fn(["a", "b"])
    assert len(out) == 2 and len(out[0]) == enc.dim


def test_availability_probe_does_not_raise():
    assert embeddings_local.available() in (True, False)
