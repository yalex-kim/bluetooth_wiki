"""Build the Q&A index from converted spec markdown.

    python scripts/qa_ingest.py --version 6.0             # skeleton + embeddings
    python scripts/qa_ingest.py --version 6.0 --extract   # + §5.3 entity extraction
    python scripts/qa_ingest.py --version 6.0 --figures   # + §5.4 figure descriptions
    python scripts/qa_ingest.py --all
    python scripts/qa_ingest.py --version 6.0 --dry-run   # parse only, no endpoint calls

--extract and --figures are off by default: §14.7 flags LLM extraction as the
quota-dominant stage, and the deterministic skeleton alone already supports the
graph actions. Re-running is cheap — §5.5 hashing means unchanged sections are
not re-embedded.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from qa import config  # noqa: E402
from qa.ingest.pipeline import Manifest, build_chunks, build_skeleton, ingest_document  # noqa: E402
from qa.ingest.structure import parse_markdown  # noqa: E402
from qa.store.graph_sqlite import SqliteGraphStore  # noqa: E402
from qa.store.vector_local import LocalVectorStore  # noqa: E402


def discover(version=None):
    """Find sources/specs/X.Y/Core_vX.Y.md, newest-numbered last."""
    specs_dir = config.SOURCES_DIR / "specs"
    found = []
    for path in sorted(specs_dir.glob("*/Core_v*.md")):
        ver = path.parent.name
        if version and ver != version:
            continue
        found.append({
            "doc_id": f"core-{ver}",
            "title": f"Core Spec v{ver}",
            "doc_type": "Core",
            "version": ver,
            "path": path,
        })
    return found


def _dry_run(doc):
    text = doc["path"].read_text(encoding="utf-8", errors="ignore")
    parsed = parse_markdown(text, doc_id=doc["doc_id"], title=doc["title"],
                            doc_type=doc["doc_type"], version=doc["version"],
                            path=str(doc["path"]))
    nodes, edges = build_skeleton(parsed)
    chunks = build_chunks(parsed)
    tables = sum(1 for c in chunks if c["metadata"]["kind"] == "table")
    print(f"  {doc['title']}: {len(parsed.sections)} sections | {len(parsed.tables)} tables "
          f"| {len(parsed.figures)} figures | {len(parsed.crossrefs)} xrefs")
    print(f"  -> graph {len(nodes)} nodes / {len(edges)} edges | "
          f"chunks {len(chunks)} ({tables} table chunks)")
    print(f"  -> would embed {len(chunks)} chunks (no endpoint call made)")


async def run(args):
    docs = discover(args.version)
    if not docs:
        target = args.version or "any version"
        print(f"No Core spec markdown found for {target} under {config.SOURCES_DIR / 'specs'}.")
        return 1
    if not args.all and not args.version:
        docs = docs[-1:]  # default to the newest version rather than the whole corpus

    if args.dry_run:
        print(f"Dry run over {len(docs)} document(s):")
        for doc in docs:
            _dry_run(doc)
        return 0

    index_dir = Path(args.index_dir) if args.index_dir else config.QA_INDEX_DIR
    index_dir.mkdir(parents=True, exist_ok=True)
    vector = LocalVectorStore.load(index_dir / "vectors")
    graph = SqliteGraphStore(index_dir / "graph.db")
    manifest = Manifest.load(index_dir / "manifest.json")

    registry_path = index_dir / "registry.json"
    registry = (json.loads(registry_path.read_text(encoding="utf-8"))
                if registry_path.is_file() else {})

    try:
        for doc in docs:
            print(f"Ingesting {doc['title']} …")
            stats = await ingest_document(
                doc["path"], doc_id=doc["doc_id"], title=doc["title"],
                doc_type=doc["doc_type"], version=doc["version"],
                vector_store=vector, graph_store=graph, manifest=manifest,
                extract=args.extract, figures=args.figures,
            )
            print(f"  sections {stats.sections} "
                  f"(changed {stats.sections_changed}, skipped {stats.sections_skipped}) "
                  f"| chunks {stats.chunks} | edges {stats.edges} "
                  f"| entities {stats.entities} | {stats.elapsed_ms} ms")
            registry[doc["doc_id"]] = {"title": doc["title"], "path": str(doc["path"]),
                                       "doc_type": doc["doc_type"], "version": doc["version"]}
        registry_path.write_text(json.dumps(registry, indent=2), encoding="utf-8")
    finally:
        graph.close()

    print(f"\nIndex at {index_dir}: {vector.count()} vectors, {len(registry)} document(s).")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Build the Bluetooth Spec Q&A index.")
    parser.add_argument("--version", help="Spec version to ingest, e.g. 6.0.")
    parser.add_argument("--all", action="store_true", help="Ingest every discovered version.")
    parser.add_argument("--extract", action="store_true",
                        help="Run §5.3 LLM entity/relation extraction (costs quota).")
    parser.add_argument("--figures", action="store_true",
                        help="Run §5.4 figure description generation (costs quota).")
    parser.add_argument("--index-dir", help="Override the index directory.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Parse and report counts without embedding or writing.")
    args = parser.parse_args()
    raise SystemExit(asyncio.run(run(args)))


if __name__ == "__main__":
    main()
