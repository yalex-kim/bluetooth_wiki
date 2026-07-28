"""Local sentence-transformers embedding backend.

An alternative to the company endpoint's embedding API for building an index
offline. Same contract as ``qa.llm.embed`` — ``async (texts) -> list[list[float]]``
— so ``ingest_document(embed_fn=…)`` takes either without knowing the difference.

Model note: BGE-M3 is multilingual and 1024-dim, which is what makes §14.10
(Korean questions against English specification text) testable at all. It is also
trained *without* an instruction prefix, unlike the English-only
bge-small/base/large-en models — applying their prefix to M3 quietly degrades
retrieval rather than failing loudly, so the distinction is enforced here.

sentence-transformers and torch are imported lazily: the rest of qa/ works
without them.
"""
from __future__ import annotations

from qa import config

# bge English models are asymmetric and expect this on the query side only.
# BGE-M3 does not — see the module docstring.
_BGE_QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

_model_cache: dict[str, object] = {}


def available() -> bool:
    try:
        import sentence_transformers  # noqa: F401

        return True
    except ImportError:
        return False


def uses_query_prefix(model_name: str) -> bool:
    """True only for the English-only bge family, not for multilingual M3."""
    name = (model_name or "").lower()
    return "bge" in name and "m3" not in name


def load_model(model_name: str | None = None):
    model_name = model_name or config.LOCAL_EMBED_MODEL
    if model_name not in _model_cache:
        from sentence_transformers import SentenceTransformer

        _model_cache[model_name] = SentenceTransformer(model_name)
    return _model_cache[model_name]


def encode(texts, *, model_name=None, is_query=False, batch_size=None,
           encoder=None, show_progress_bar=False):
    """Encode to L2-normalised vectors as plain lists (JSON/np friendly)."""
    model_name = model_name or config.LOCAL_EMBED_MODEL
    batch_size = batch_size or config.LOCAL_EMBED_BATCH
    texts = list(texts)
    if is_query and uses_query_prefix(model_name):
        texts = [_BGE_QUERY_PREFIX + t for t in texts]
    model = encoder if encoder is not None else load_model(model_name)
    vectors = model.encode(texts, batch_size=batch_size, normalize_embeddings=True,
                           show_progress_bar=show_progress_bar)
    return [[float(x) for x in row] for row in vectors]


def make_embed_fn(*, model_name=None, is_query=False, encoder=None,
                  show_progress_bar=False):
    """Build the async ``embed_fn`` that the ingest pipeline and actions expect."""

    async def embed_fn(texts):
        return encode(texts, model_name=model_name, is_query=is_query,
                      encoder=encoder, show_progress_bar=show_progress_bar)

    return embed_fn
