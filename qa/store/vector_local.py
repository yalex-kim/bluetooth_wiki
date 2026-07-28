"""Dependency-free vector store: a numpy matrix plus a JSON sidecar on disk.

Adequate for the Phase 1 corpus (Core + GATT): a brute-force cosine scan over a
float32 matrix is milliseconds at that size, and it keeps the §12 vector-DB
decision off the critical path. Swapping in Qdrant later means writing another
class against qa.store.base.VectorStore.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from qa.store.base import VectorHit, VectorRecord, matches


class LocalVectorStore:
    def __init__(self, path):
        self.path = Path(path)
        self._ids: list[str] = []
        self._pos: dict[str, int] = {}
        self._texts: list[str] = []
        self._meta: list[dict] = []
        self._vectors: list = []

    # ── writes ──────────────────────────────────────────────────────────
    def upsert(self, records) -> None:
        for rec in records:
            vec = np.asarray(rec.embedding, dtype=np.float32)
            if rec.id in self._pos:
                i = self._pos[rec.id]
                self._texts[i] = rec.text
                self._meta[i] = dict(rec.metadata)
                self._vectors[i] = vec
                continue
            self._pos[rec.id] = len(self._ids)
            self._ids.append(rec.id)
            self._texts.append(rec.text)
            self._meta.append(dict(rec.metadata))
            self._vectors.append(vec)

    def delete(self, ids) -> None:
        drop = {i for i in ids if i in self._pos}
        if not drop:
            return
        keep = [i for i, rid in enumerate(self._ids) if rid not in drop]
        self._ids = [self._ids[i] for i in keep]
        self._texts = [self._texts[i] for i in keep]
        self._meta = [self._meta[i] for i in keep]
        self._vectors = [self._vectors[i] for i in keep]
        self._pos = {rid: i for i, rid in enumerate(self._ids)}

    # ── reads ───────────────────────────────────────────────────────────
    def search(self, embedding, *, top_k=8, filters=None):
        if not self._ids:
            return []
        candidates = [i for i in range(len(self._ids)) if matches(self._meta[i], filters)]
        if not candidates:
            return []
        matrix = np.stack([self._vectors[i] for i in candidates])
        query = np.asarray(embedding, dtype=np.float32)
        denom = (np.linalg.norm(matrix, axis=1) * np.linalg.norm(query)) + 1e-12
        scores = (matrix @ query) / denom
        order = np.argsort(-scores)[:top_k]
        return [
            VectorHit(id=self._ids[candidates[j]], text=self._texts[candidates[j]],
                      score=float(scores[j]), metadata=self._meta[candidates[j]])
            for j in order
        ]

    def get(self, id):
        i = self._pos.get(id)
        if i is None:
            return None
        return VectorRecord(id=id, text=self._texts[i],
                            embedding=self._vectors[i].tolist(), metadata=self._meta[i])

    def count(self) -> int:
        return len(self._ids)

    # ── persistence ─────────────────────────────────────────────────────
    def persist(self) -> None:
        self.path.mkdir(parents=True, exist_ok=True)
        matrix = np.stack(self._vectors) if self._vectors else np.zeros((0, 0), dtype=np.float32)
        np.save(self.path / "vectors.npy", matrix)
        (self.path / "records.json").write_text(
            json.dumps({"ids": self._ids, "texts": self._texts, "metadata": self._meta}),
            encoding="utf-8",
        )

    @classmethod
    def load(cls, path):
        store = cls(path)
        records_file = Path(path) / "records.json"
        vectors_file = Path(path) / "vectors.npy"
        if not records_file.is_file() or not vectors_file.is_file():
            return store  # a not-yet-built index reads as empty, not as an error
        payload = json.loads(records_file.read_text(encoding="utf-8"))
        matrix = np.load(vectors_file)
        store._ids = payload["ids"]
        store._texts = payload["texts"]
        store._meta = payload["metadata"]
        store._vectors = [matrix[i] for i in range(len(store._ids))]
        store._pos = {rid: i for i, rid in enumerate(store._ids)}
        return store
