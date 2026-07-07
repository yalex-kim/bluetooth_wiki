#!/usr/bin/env python3
"""Build the chunk + embedding index for spec versions.

Usage:
    python scripts/build_search_index.py --version 6.0 6.2
    python scripts/build_search_index.py --all [--force]
    python scripts/build_search_index.py --version 6.0 --chunks-only

Idempotent: a version whose source sha256 + chunker version + model name all
match the existing meta.json is skipped unless --force is given.

--chunks-only writes chunks.jsonl without embeddings (no sentence-transformers
needed) — v2 then still gets chunk-accurate ripgrep-source hits, just no
vector arm, until a full build runs.

First full run downloads the embedding model (~130 MB for the default
BAAI/bge-small-en-v1.5) into the Hugging Face cache.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agent.config import EMBED_MODEL, SOURCES_DIR  # noqa: E402
from search import index_store  # noqa: E402
from search.chunker import chunk_core_spec  # noqa: E402


def detect_versions() -> list[str]:
    specs = SOURCES_DIR / "specs"
    return sorted(
        p.name for p in specs.iterdir() if p.is_dir() and (p / f"Core_v{p.name}.md").is_file()
    )


def build_chunks_only(version: str) -> dict:
    chunks = chunk_core_spec(version)
    out = index_store.index_dir(version)
    out.mkdir(parents=True, exist_ok=True)
    payload = "\n".join(json.dumps(asdict(c), ensure_ascii=False) for c in chunks)
    index_store._atomic_write_bytes(out / "chunks.jsonl", payload.encode("utf-8"))
    return {"version": version, "num_chunks": len(chunks), "skipped": False, "chunks_only": True}


def main() -> int:
    # Progress lines use an em dash; force UTF-8 so a cp949/Windows console
    # (which would otherwise raise UnicodeEncodeError) doesn't abort the build.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--version", nargs="+", default=None, help="spec versions, e.g. 6.0 6.2")
    ap.add_argument("--all", action="store_true", help="build every version under sources/specs/")
    ap.add_argument("--force", action="store_true", help="rebuild even if up to date")
    ap.add_argument("--model", default=EMBED_MODEL, help=f"embedding model (default {EMBED_MODEL})")
    ap.add_argument("--batch-size", type=int, default=32)
    ap.add_argument("--chunks-only", action="store_true", help="skip embeddings (no ML deps needed)")
    args = ap.parse_args()

    versions = detect_versions() if args.all else (args.version or [])
    if not versions:
        ap.error("specify --version X.Y ... or --all")

    ok = True
    for v in versions:
        t0 = time.time()
        try:
            if args.chunks_only:
                summary = build_chunks_only(v)
            else:
                summary = index_store.build_index(v, model_name=args.model, batch_size=args.batch_size, force=args.force)
        except FileNotFoundError as exc:
            print(f"[{v}] SKIP: {exc}")
            ok = False
            continue
        except ImportError as exc:
            print(f"[{v}] ERROR: {exc}\n      Install ML deps (`pip install sentence-transformers`) or use --chunks-only.")
            return 1
        state = "up to date" if summary.get("skipped") else f"built in {time.time() - t0:.1f}s"
        print(f"[{v}] {summary['num_chunks']} chunks — {state}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
