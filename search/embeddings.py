"""Local embedding model wrapper + brute-force cosine top-k.

Uses a sentence-transformers model (default BAAI/bge-small-en-v1.5, 384-dim)
loaded lazily on first use. No vector DB: at this corpus's scale (a few
thousand chunks per spec version) a dense [N,384] @ [384] matmul is
single-digit milliseconds on CPU.

sentence-transformers (and its torch dependency) is intentionally imported
inside functions so that v0/v1 — and v2's ripgrep arm — work without it.
"""

from __future__ import annotations

import numpy as np

from agent.config import EMBED_MODEL

# bge models are asymmetric: queries get this prefix, passages do not.
_BGE_QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

_model_cache: dict[str, object] = {}


def embedding_available() -> bool:
    try:
        import sentence_transformers  # noqa: F401

        return True
    except ImportError:
        return False


def _load_model(model_name: str):
    if model_name not in _model_cache:
        from sentence_transformers import SentenceTransformer

        _model_cache[model_name] = SentenceTransformer(model_name)
    return _model_cache[model_name]


def encode(texts: list[str], *, is_query: bool = False, model_name: str = EMBED_MODEL, batch_size: int = 32) -> np.ndarray:
    """Encode texts to L2-normalized float32 vectors (n, dim)."""
    model = _load_model(model_name)
    if is_query and "bge" in model_name.lower():
        texts = [_BGE_QUERY_PREFIX + t for t in texts]
    vecs = model.encode(texts, batch_size=batch_size, normalize_embeddings=True, show_progress_bar=False)
    return np.asarray(vecs, dtype=np.float32)


def cosine_topk(query_vec: np.ndarray, matrix: np.ndarray, k: int) -> list[tuple[int, float]]:
    """Top-k (index, cosine) — rows of ``matrix`` must be L2-normalized."""
    if matrix.shape[0] == 0:
        return []
    scores = matrix @ query_vec
    k = min(k, scores.shape[0])
    idx = np.argpartition(-scores, k - 1)[:k]
    return sorted(((int(i), float(scores[i])) for i in idx), key=lambda t: -t[1])
