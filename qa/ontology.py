"""§5.2 ontology — the fixed schema every extracted node and edge must fit.

Extraction is constrained to these types (not open extraction) so that the same
concept named differently across sections normalises to one node, traversal
queries stay writable, and adding a document family reuses the schema instead of
inventing one.
"""
from __future__ import annotations

# §5.1 deterministic skeleton — built from markdown structure, never from an LLM.
STRUCTURAL_TYPES = frozenset({
    "Document", "Chapter", "Section", "Subsection", "Table", "Figure",
})

# §5.2 common core entity types.
CORE_ENTITY_TYPES = frozenset({
    "Procedure", "State", "Event", "PDU", "Parameter", "Timer",
    "ErrorCode", "Role", "Layer", "Profile", "Characteristic",
})

# §5.2 "문서 유형별 확장 예".
EXTENSION_TYPES = {
    "Mesh": frozenset({"Model", "Element", "Message"}),
    "LEAudio": frozenset({"Codec", "ContextType"}),
}

RELATION_TYPES = frozenset({
    # §5.2 common relations
    "triggers", "requires", "definedIn", "partOf", "mandatoryFor",
    "optionalFor", "supersedes", "references",
    # §14.11 — errata overrides the clause it amends; the same shape covers a
    # Profile narrowing a Core parameter.
    "amends",
    # structural, emitted by the §5.1 skeleton
    "hasTable", "hasFigure",
})

DOC_TYPES = ("Core", "GATT", "Profile", "Mesh", "LEAudio", "Reference", "Errata")

# Relations an LLM may propose; the structural ones are ours to emit, not its.
EXTRACTABLE_RELATIONS = RELATION_TYPES - {"hasTable", "hasFigure"}


def entity_types(doc_type: str) -> frozenset:
    """Core types plus whatever this document family adds."""
    return CORE_ENTITY_TYPES | EXTENSION_TYPES.get(doc_type, frozenset())


def is_valid_node_type(t: str, doc_type: str = "Core") -> bool:
    return t in STRUCTURAL_TYPES or t in entity_types(doc_type)


def is_valid_relation(t: str) -> bool:
    return t in RELATION_TYPES


def extraction_schema(doc_type: str) -> dict:
    """JSON schema handed to qa.llm.structured_call for §5.3 extraction."""
    types = sorted(entity_types(doc_type))
    relations = sorted(EXTRACTABLE_RELATIONS)
    return {
        "type": "object",
        "required": ["entities", "relations"],
        "properties": {
            "entities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["name", "type"],
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": types},
                        "aliases": {"type": "array", "items": {"type": "string"}},
                    },
                },
            },
            "relations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["source", "target", "type"],
                    "properties": {
                        "source": {"type": "string"},
                        "target": {"type": "string"},
                        "type": {"type": "string", "enum": relations},
                    },
                },
            },
        },
    }
