"""§5.3 ontology-constrained entity/relation extraction and §5.4 figure descriptions.

Both stages are opt-in per ingest run because they are the quota-hungry half
(§14.7). Extraction is constrained to qa.ontology types, so anything the model
invents outside the schema is rejected by structured_call before it can reach
the graph. Low-confidence figure output is flagged rather than silently trusted
(§13: "Figure 설명의 부정확성이 그래프에 잘못된 관계로 유입될 위험").
"""
from __future__ import annotations

import re

from qa import config, ontology
from qa.llm import StructuredOutputError, structured_call
from qa.store.base import GraphEdge, GraphNode

_EXTRACT_SYSTEM = (
    "You extract Bluetooth specification entities and relations. "
    "Use ONLY the entity types and relation types given in the schema. "
    "Do not invent types. Prefer the exact wording the specification uses for names. "
    "Return JSON only."
)

_FIGURE_SYSTEM = (
    "You describe a Bluetooth specification figure. Identify the states, events and "
    "transitions it shows. Be literal: describe only what the figure depicts. "
    "Return JSON only."
)

_FIGURE_SCHEMA = {
    "type": "object",
    "required": ["description", "confidence"],
    "properties": {
        "description": {"type": "string"},
        "states": {"type": "array", "items": {"type": "string"}},
        "events": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
    },
}

MIN_SECTION_CHARS = 200


def _entity_id(doc_id: str, name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return f"{doc_id}:entity:{slug}"


async def _extract_entities(doc, section, graph_store, schema):
    body = (section.text or "").strip()
    if len(body) < MIN_SECTION_CHARS:
        return 0
    try:
        payload = await structured_call(
            [
                {"role": "system", "content": _EXTRACT_SYSTEM},
                {"role": "user", "content":
                    f"Schema:\n{schema}\n\nSection {section.number} {section.title}:\n"
                    f"{body[:6000]}"},
            ],
            schema, model=config.EXTRACT_MODEL,
        )
    except StructuredOutputError:
        return 0  # §13: a section that will not extract is skipped, never guessed

    nodes, edges, by_name = [], [], {}
    for entity in payload.get("entities", []):
        nid = _entity_id(doc.doc_id, entity["name"])
        by_name[entity["name"]] = nid
        nodes.append(GraphNode(
            id=nid, type=entity["type"], name=entity["name"],
            properties={"doc_id": doc.doc_id, "doc_type": doc.doc_type,
                        "version": doc.version, "aliases": entity.get("aliases", []),
                        "section_id": section.id},
        ))
        edges.append(GraphEdge(nid, section.id, "definedIn"))

    for relation in payload.get("relations", []):
        src = by_name.get(relation["source"])
        dst = by_name.get(relation["target"])
        if src and dst and ontology.is_valid_relation(relation["type"]):
            edges.append(GraphEdge(src, dst, relation["type"]))

    if nodes:
        graph_store.add_nodes(nodes)
    if edges:
        graph_store.add_edges(edges)
    return len(nodes)


async def _describe_figure(doc, figure, graph_store):
    try:
        payload = await structured_call(
            [
                {"role": "system", "content": _FIGURE_SYSTEM},
                {"role": "user", "content":
                    f"Figure caption: {figure.caption}\nImage file: {figure.image_path}\n"
                    f"Describe it as JSON matching the schema."},
            ],
            _FIGURE_SCHEMA, model=config.VISION_MODEL,
        )
    except StructuredOutputError:
        return 0
    graph_store.add_nodes([GraphNode(
        id=figure.id, type="Figure", name=figure.caption,
        properties={"doc_id": doc.doc_id, "doc_type": doc.doc_type,
                    "version": doc.version, "section_id": figure.section_id,
                    "image_path": figure.image_path,
                    "description": payload["description"],
                    "states": payload.get("states", []),
                    "events": payload.get("events", []),
                    "confidence": payload["confidence"],
                    "low_confidence": payload["confidence"] == "low"},
    )])
    return 1


async def enrich(doc, *, graph_store, sections, do_entities=True, do_figures=False):
    """Decorate the deterministic skeleton with LLM-derived nodes. Returns node count."""
    added = 0
    if do_entities:
        schema = ontology.extraction_schema(doc.doc_type)
        for section in sections:
            added += await _extract_entities(doc, section, graph_store, schema)

    if do_figures:
        section_ids = {s.id for s in sections}
        for figure in doc.figures:
            if figure.section_id in section_ids:
                added += await _describe_figure(doc, figure, graph_store)
    return added
