"""§7.1 loop actions over the vector + graph indexes.

Every action returns two things: text for the model, and structured Evidence for
the verifier. That split is what makes §7.4 possible — the model never gets to
assert a citation the retrieval layer did not actually produce.

§14.11 is enforced here rather than in the prompt: when a section carries an
inbound ``amends`` edge, its text is returned with the erratum appended and
marked as taking precedence, so the model cannot see the stale clause alone.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from qa import config


@dataclass
class Evidence:
    """One observed piece of evidence — the unit §7.4 verifies citations against."""

    ref_id: str
    doc: str
    section: str
    page: int | None
    path: str
    kind: str  # "chunk" | "section" | "table" | "figure" | "node"
    text: str


@dataclass
class ActionResult:
    text: str
    evidence: list = field(default_factory=list)


_ERRATUM_BANNER = "[ERRATUM — takes precedence over the text above]"


def _truncate(text: str, limit: int) -> str:
    text = text or ""
    return text if len(text) <= limit else text[:limit].rstrip() + " …[truncated]"


class RetrievalActions:
    TOOL_SCHEMAS = [
        {
            "type": "function",
            "function": {
                "name": "vector_search",
                "description": (
                    "Semantic search over the indexed specification text. Start here. "
                    "Use scope_filter to restrict document family or version."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search text."},
                        "scope_filter": {
                            "type": "object",
                            "description": (
                                "Metadata filter, e.g. {\"doc_type\": [\"Core\"], "
                                "\"version\": [\"6.0\"]}. Omit to search everything."
                            ),
                        },
                        "top_k": {"type": "integer", "description": "Number of hits."},
                    },
                    "required": ["query"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "graph_lookup",
                "description": (
                    "Find a specification entity node (Procedure, State, Timer, PDU, …) "
                    "by name or alias. Returns node ids usable with graph_traverse."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"entity_name": {"type": "string"}},
                    "required": ["entity_name"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "graph_traverse",
                "description": (
                    "Walk relations out of a node. Use for multi-hop questions: which "
                    "procedure triggers which state, what a section references."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "node_id": {"type": "string"},
                        "relation_types": {"type": "array", "items": {"type": "string"}},
                        "hops": {"type": "integer", "description": "Default 1."},
                    },
                    "required": ["node_id"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_section_text",
                "description": "Read a section's full specification text verbatim.",
                "parameters": {
                    "type": "object",
                    "properties": {"doc": {"type": "string"}, "section_id": {"type": "string"}},
                    "required": ["doc", "section_id"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_figure",
                "description": "Read a figure's description, states and events.",
                "parameters": {
                    "type": "object",
                    "properties": {"figure_id": {"type": "string"}},
                    "required": ["figure_id"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_table",
                "description": (
                    "Read a parameter / Assigned Numbers table with its structure intact. "
                    "Prefer this for value, range and default questions."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"table_id": {"type": "string"},
                                   "section_id": {"type": "string"}},
                },
            },
        },
    ]

    def __init__(self, vector_store, graph_store, *, embed_fn=None, doc_registry=None):
        self.vector = vector_store
        self.graph = graph_store
        self.doc_registry = doc_registry or {}
        self._embed_fn = embed_fn

    # ── dispatch ────────────────────────────────────────────────────────
    async def run(self, name, args):
        args = args or {}
        try:
            if name == "vector_search":
                return await self.vector_search(
                    args.get("query", ""), scope_filter=args.get("scope_filter"),
                    top_k=args.get("top_k"))
            if name == "graph_lookup":
                return self.graph_lookup(args.get("entity_name", ""))
            if name == "graph_traverse":
                return self.graph_traverse(
                    args.get("node_id", ""), relation_types=args.get("relation_types"),
                    hops=int(args.get("hops") or 1))
            if name == "get_section_text":
                return self.get_section_text(args.get("doc", ""), args.get("section_id", ""))
            if name == "get_figure":
                return self.get_figure(args.get("figure_id", ""))
            if name == "get_table":
                return self.get_table(table_id=args.get("table_id"),
                                      section_id=args.get("section_id"))
        except Exception as exc:  # a bad argument costs one loop step, not a 500
            return ActionResult(text=f"Error running {name}: {exc}", evidence=[])
        return ActionResult(
            text=f"Error: unknown action {name!r}. Available: "
                 f"{[s['function']['name'] for s in self.TOOL_SCHEMAS]}.",
            evidence=[],
        )

    # ── helpers ─────────────────────────────────────────────────────────
    async def _embed(self, text):
        if self._embed_fn is not None:
            return (await self._embed_fn([text]))[0]
        from qa import llm

        return (await llm.embed([text]))[0]

    def _doc_title(self, doc_id, fallback=""):
        entry = self.doc_registry.get(doc_id)
        if entry and entry.get("title"):
            return entry["title"]
        return fallback or doc_id

    def _doc_path(self, doc_id):
        entry = self.doc_registry.get(doc_id) or {}
        return entry.get("path", "")

    def _errata_for(self, section_id):
        """§14.11: inbound `amends` edges override the amended clause."""
        out = []
        for neighbor in self.graph.neighbors(section_id, relation_types=["amends"], hops=1):
            if neighbor.direction != "in":
                continue
            props = neighbor.node.properties or {}
            body = props.get("text") or props.get("description") or neighbor.node.name
            out.append((neighbor.node, body))
        return out

    # ── §7.1 actions ────────────────────────────────────────────────────
    async def vector_search(self, query, scope_filter=None, top_k=None):
        if not query:
            return ActionResult(text="Error: vector_search needs a query.", evidence=[])
        embedding = await self._embed(query)
        hits = self.vector.search(embedding, top_k=int(top_k or config.VECTOR_TOP_K),
                                  filters=scope_filter)
        if not hits:
            return ActionResult(
                text=f"No matches for {query!r}"
                     + (f" under scope_filter {scope_filter}. Try widening the scope."
                        if scope_filter else "."),
                evidence=[],
            )
        lines, evidence = [], []
        for hit in hits:
            md = hit.metadata or {}
            doc = self._doc_title(md.get("doc_id", ""), md.get("doc_title", ""))
            snippet = _truncate(hit.text, config.SNIPPET_CHARS)
            lines.append(
                f"- ref_id={hit.id} | {doc} §{md.get('section', '?')} "
                f"{md.get('title', '')} | kind={md.get('kind', 'section')} "
                f"| score={hit.score:.3f}\n  {snippet}"
            )
            evidence.append(Evidence(
                ref_id=hit.id, doc=doc, section=str(md.get("section", "")),
                page=md.get("page"), path=md.get("path", "") or self._doc_path(md.get("doc_id", "")),
                kind="chunk", text=snippet,
            ))
        return ActionResult(text=f"{len(hits)} hits for {query!r}:\n" + "\n".join(lines),
                            evidence=evidence)

    def graph_lookup(self, entity_name):
        nodes = self.graph.lookup(entity_name)
        if not nodes:
            return ActionResult(
                text=f"No entity node found for {entity_name!r}. "
                     f"Try vector_search to find the wording the spec uses.",
                evidence=[],
            )
        lines, evidence = [], []
        for node in nodes:
            props = node.properties or {}
            aliases = props.get("aliases") or []
            lines.append(
                f"- node_id={node.id} | type={node.type} | name={node.name}"
                + (f" | aliases={aliases}" if aliases else "")
                + (f" | defined in section {props['section_id']}" if props.get("section_id") else "")
            )
            evidence.append(Evidence(
                ref_id=node.id, doc=self._doc_title(props.get("doc_id", "")),
                section=str(props.get("number", "")), page=props.get("page"),
                path=self._doc_path(props.get("doc_id", "")), kind="node", text=node.name,
            ))
        return ActionResult(text=f"{len(nodes)} node(s) for {entity_name!r}:\n" + "\n".join(lines),
                            evidence=evidence)

    def graph_traverse(self, node_id, relation_types=None, hops=1):
        if self.graph.get_node(node_id) is None:
            return ActionResult(text=f"Node {node_id!r} not found.", evidence=[])
        cap = config.TRAVERSE_NODE_CAP
        neighbors = self.graph.neighbors(node_id, relation_types=relation_types,
                                         hops=int(hops or 1), limit=cap)
        if not neighbors:
            return ActionResult(text=f"Node {node_id} has no matching relations.", evidence=[])
        lines, evidence = [], []
        for n in neighbors:
            arrow = "->" if n.direction == "out" else "<-"
            props = n.node.properties or {}
            lines.append(f"- {arrow} [{n.edge.type}] node_id={n.node.id} "
                         f"| type={n.node.type} | {n.node.name} (hop {n.hop})")
            evidence.append(Evidence(
                ref_id=n.node.id, doc=self._doc_title(props.get("doc_id", "")),
                section=str(props.get("number", "")), page=props.get("page"),
                path=self._doc_path(props.get("doc_id", "")), kind="node", text=n.node.name,
            ))
        text = f"{len(neighbors)} relation(s) from {node_id}:\n" + "\n".join(lines)
        if len(neighbors) >= cap:
            text += (f"\n[capped at {cap} nodes — narrow with relation_types "
                     f"or traverse from a more specific node]")
        return ActionResult(text=text, evidence=evidence)

    def get_section_text(self, doc, section_id):
        node = self.graph.get_node(section_id)
        if node is None:
            return ActionResult(text=f"Section {section_id!r} not found.", evidence=[])
        props = node.properties or {}
        doc_id = props.get("doc_id") or doc
        path = self._doc_path(doc_id)
        body = ""
        if path and Path(path).is_file():
            lines = Path(path).read_text(encoding="utf-8", errors="ignore").split("\n")
            start = max(int(props.get("line_start", 1)) - 1, 0)
            end = int(props.get("line_end", start + 1))
            body = "\n".join(lines[start:end]).strip()
        if not body:
            body = props.get("text", "") or node.name

        title = self._doc_title(doc_id)
        section_no = str(props.get("number", ""))
        text = f"{title} §{section_no} {node.name}\n\n{body}"
        evidence = [Evidence(ref_id=section_id, doc=title, section=section_no,
                             page=props.get("page"), path=path, kind="section", text=body)]

        for errata_node, errata_body in self._errata_for(section_id):
            eprops = errata_node.properties or {}
            edoc = self._doc_title(eprops.get("doc_id", ""))
            text += f"\n\n{_ERRATUM_BANNER}\n{edoc} {errata_node.name}\n{errata_body}"
            evidence.append(Evidence(
                ref_id=errata_node.id, doc=edoc, section=str(eprops.get("number", "")),
                page=eprops.get("page"), path=self._doc_path(eprops.get("doc_id", "")),
                kind="section", text=errata_body,
            ))
        return ActionResult(text=text, evidence=evidence)

    def get_figure(self, figure_id):
        node = self.graph.get_node(figure_id)
        if node is None or node.type != "Figure":
            return ActionResult(text=f"Figure {figure_id!r} not found.", evidence=[])
        props = node.properties or {}
        doc_id = props.get("doc_id", "")
        parts = [f"{node.name}", f"image: {props.get('image_path', '(none)')}"]
        if props.get("description"):
            parts.append(props["description"])
        if props.get("states"):
            parts.append(f"states: {', '.join(props['states'])}")
        if props.get("events"):
            parts.append(f"events: {', '.join(props['events'])}")
        if props.get("low_confidence"):
            parts.append("[low-confidence figure description — do not rely on it alone]")
        else:
            if not props.get("description"):
                parts.append("[no generated description — run ingest with --figures]")
        text = "\n".join(parts)
        section_id = props.get("section_id", "")
        section_node = self.graph.get_node(section_id) if section_id else None
        section_no = str((section_node.properties or {}).get("number", "")) if section_node else ""
        return ActionResult(text=text, evidence=[Evidence(
            ref_id=figure_id, doc=self._doc_title(doc_id), section=section_no,
            page=props.get("page"), path=self._doc_path(doc_id), kind="figure", text=text,
        )])

    def get_table(self, table_id=None, section_id=None):
        """§14.12: tables are the shape chunk embeddings miss, so they get a direct action."""
        nodes = []
        if table_id:
            node = self.graph.get_node(table_id)
            if node is not None and node.type == "Table":
                nodes = [node]
        elif section_id:
            nodes = [n.node for n in self.graph.neighbors(
                section_id, relation_types=["hasTable"], hops=1) if n.node.type == "Table"]
        if not nodes:
            target = table_id or section_id or "(no id given)"
            return ActionResult(text=f"Table for {target!r} not found.", evidence=[])

        blocks, evidence = [], []
        for node in nodes:
            props = node.properties or {}
            doc_id = props.get("doc_id", "")
            owner = props.get("section_id", "")
            owner_node = self.graph.get_node(owner) if owner else None
            section_no = str((owner_node.properties or {}).get("number", "")) if owner_node else ""
            markdown = props.get("markdown", "")
            body = f"{node.name}\n\n{markdown}".strip()
            blocks.append(f"table_id={node.id}\n{body}")
            evidence.append(Evidence(
                ref_id=node.id, doc=self._doc_title(doc_id), section=section_no,
                page=props.get("page"), path=self._doc_path(doc_id), kind="table", text=body,
            ))
            for errata_node, errata_body in self._errata_for(owner) if owner else []:
                eprops = errata_node.properties or {}
                edoc = self._doc_title(eprops.get("doc_id", ""))
                blocks.append(f"{_ERRATUM_BANNER}\n{edoc} {errata_node.name}\n{errata_body}")
                evidence.append(Evidence(
                    ref_id=errata_node.id, doc=edoc, section=str(eprops.get("number", "")),
                    page=eprops.get("page"), path=self._doc_path(eprops.get("doc_id", "")),
                    kind="section", text=errata_body,
                ))
        return ActionResult(text="\n\n".join(blocks), evidence=evidence)
