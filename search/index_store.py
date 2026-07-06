"""On-disk chunk/embedding index: build, load, and query.

Layout per spec version (gitignored — fully reproducible from sources/):

    search/index/<version>/
        chunks.jsonl    one JSON object per chunk
        embeddings.npy  float32 [num_chunks, dim], L2-normalized rows
        meta.json       build fingerprint (model, chunker version, source sha)
"""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np

from agent.config import EMBED_MODEL, SEARCH_INDEX_DIR

from .chunker import CHUNKER_VERSION, Chunk, chunk_core_spec, spec_path


def index_dir(version: str) -> Path:
    return SEARCH_INDEX_DIR / version


def _source_sha256(version: str) -> str:
    h = hashlib.sha256()
    with open(spec_path(version), "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _fingerprint(version: str, model_name: str) -> dict:
    return {
        "model_name": model_name,
        "chunker_version": CHUNKER_VERSION,
        "source_sha256": _source_sha256(version),
    }


def is_up_to_date(version: str, model_name: str = EMBED_MODEL) -> bool:
    meta_path = index_dir(version) / "meta.json"
    if not meta_path.is_file():
        return False
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    fp = _fingerprint(version, model_name)
    return all(meta.get(k) == v for k, v in fp.items())


def _atomic_write_bytes(path: Path, data: bytes) -> None:
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def build_index(version: str, *, model_name: str = EMBED_MODEL, batch_size: int = 32, force: bool = False) -> dict:
    """Chunk + embed one spec version. Idempotent unless ``force``.

    Returns a summary dict {version, num_chunks, skipped}.
    """
    from .embeddings import encode  # deferred: requires sentence-transformers

    if not force and is_up_to_date(version, model_name):
        chunks_file = index_dir(version) / "chunks.jsonl"
        n = sum(1 for _ in chunks_file.open(encoding="utf-8")) if chunks_file.is_file() else 0
        return {"version": version, "num_chunks": n, "skipped": True}

    chunks = chunk_core_spec(version)
    matrix = encode([c.text for c in chunks], model_name=model_name, batch_size=batch_size)

    out = index_dir(version)
    out.mkdir(parents=True, exist_ok=True)
    _atomic_write_bytes(out / "chunks.jsonl", "\n".join(json.dumps(asdict(c), ensure_ascii=False) for c in chunks).encode("utf-8"))

    import io

    import numpy as np

    buf = io.BytesIO()
    np.save(buf, matrix)
    _atomic_write_bytes(out / "embeddings.npy", buf.getvalue())

    meta = _fingerprint(version, model_name) | {
        "built_at": datetime.now(timezone.utc).isoformat(),
        "num_chunks": len(chunks),
        "dim": int(matrix.shape[1]),
    }
    _atomic_write_bytes(out / "meta.json", json.dumps(meta, indent=2).encode("utf-8"))
    return {"version": version, "num_chunks": len(chunks), "skipped": False}


class VersionIndex:
    """Loaded chunk index for one spec version (embeddings optional)."""

    def __init__(self, version: str, chunks: list[Chunk], matrix: np.ndarray | None):
        self.version = version
        self.chunks = chunks
        self.matrix = matrix  # None when only chunks.jsonl exists

    def find_chunk_for_line(self, line: int) -> Chunk | None:
        """Map a 1-based source line number to its containing chunk."""
        lo, hi = 0, len(self.chunks) - 1
        best: Chunk | None = None
        while lo <= hi:
            mid = (lo + hi) // 2
            c = self.chunks[mid]
            if c.line_start <= line:
                if line <= c.line_end:
                    return c
                best = best if best and best.line_start > c.line_start else c
                lo = mid + 1
            else:
                hi = mid - 1
        return best


_index_cache: dict[str, VersionIndex] = {}


def available_versions() -> list[str]:
    if not SEARCH_INDEX_DIR.is_dir():
        return []
    return sorted(p.name for p in SEARCH_INDEX_DIR.iterdir() if (p / "chunks.jsonl").is_file())


def load_index(version: str) -> VersionIndex | None:
    if version in _index_cache:
        return _index_cache[version]
    d = index_dir(version)
    chunks_file = d / "chunks.jsonl"
    if not chunks_file.is_file():
        return None
    chunks = [Chunk(**json.loads(line)) for line in chunks_file.open(encoding="utf-8") if line.strip()]
    chunks.sort(key=lambda c: c.line_start)
    emb_file = d / "embeddings.npy"
    matrix = None
    if emb_file.is_file():
        import numpy as np

        matrix = np.load(emb_file)
    idx = VersionIndex(version, chunks, matrix)
    _index_cache[version] = idx
    return idx
