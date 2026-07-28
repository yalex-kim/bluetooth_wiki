"""§7.0 pre-filter — one cheap judgement before the loop is allowed to spend money.

Two jobs, per the design doc: reject clearly out-of-scope questions before any
retrieval happens (cost defence), and guess a document-family hint for the first
vector_search. The hint is explicitly *not* a hard constraint — §7.0 says the
loop may widen or change scope later.

Order of resolution, cheapest first:
  1. An explicit spec_scope from the Orchestrator wins outright — no LLM.
  2. Bluetooth vocabulary present -> in scope, with a doc-type hint.
  3. Off-domain marker and no Bluetooth vocabulary -> out of scope.
  4. Only the ambiguous middle costs an LLM call.
A failure in step 4 fails *open*: a broken gate must not swallow real questions.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from qa import config
from qa.llm import structured_call


@dataclass
class ScopeDecision:
    out_of_scope: bool
    scope_filter: dict | None
    reason: str
    used_llm: bool = False


# Vocabulary that is unambiguously Bluetooth in an engineering context.
_BT_TERMS = frozenset({
    "bluetooth", "ble", "bredr", "br/edr", "gatt", "gap", "att", "l2cap", "hci",
    "smp", "sdp", "rfcomm", "acl", "sco", "isoc", "iso", "cis", "big", "pdu",
    "advertising", "advertis", "scanning", "peripheral", "central", "broadcaster",
    "observer", "pairing", "bonding", "whitelist", "resolvable", "rpa", "irk",
    "ltk", "connsupervisiontimeout", "conninterval", "connevent", "supervision",
    "a2dp", "avrcp", "hfp", "hsp", "hid", "hogp", "pbap", "map", "opp", "spp",
    "mesh", "provisioning", "lc3", "auracast", "bap", "cap", "csip", "pbp",
    "tmap", "hap", "ascs", "pacs", "bass", "codec", "uuid", "characteristic",
    "assigned numbers", "errata", "channel sounding", "direction finding",
    "aoa", "aod", "pawr", "eatt", "subrating", "link layer", "controller",
    "host controller", "opcode", "att_mtu", "rssi", "atttribute",
})

# A doc-type hint per term group (§7.0 "관련 문서군 추정").
_DOC_TYPE_HINTS = (
    ({"mesh", "provisioning", "model", "element"}, "Mesh"),
    ({"lc3", "auracast", "bap", "cap", "csip", "pbp", "tmap", "hap", "ascs",
      "pacs", "bass", "le audio", "broadcast audio"}, "LEAudio"),
    ({"a2dp", "avrcp", "hfp", "hsp", "hid", "hogp", "pbap", "opp", "spp"}, "Profile"),
    ({"gatt", "characteristic", "uuid", "att", "descriptor"}, "GATT"),
    ({"assigned numbers"}, "Reference"),
    ({"errata"}, "Errata"),
)

# Markers of a question that is plainly about something else entirely.
_OFF_DOMAIN = (
    "capital of", "recipe", "weather", "stock price", "movie", "lyrics",
    "translate this poem", "who won", "population of", "president of",
    "birthday", "horoscope", "football", "restaurant",
)

_SCOPE_ALIASES = {
    "core": ["Core"], "core-le": ["Core"], "core-br": ["Core"], "core-bredr": ["Core"],
    "le": ["Core"], "bredr": ["Core"], "gatt": ["GATT"], "gss": ["GATT"],
    "mesh": ["Mesh"], "leaudio": ["LEAudio"], "le-audio": ["LEAudio"],
    "profile": ["Profile"], "profiles": ["Profile"],
    "reference": ["Reference"], "errata": ["Errata"],
}

_LLM_SCHEMA = {
    "type": "object",
    "required": ["out_of_scope"],
    "properties": {
        "out_of_scope": {"type": "boolean"},
        "doc_types": {"type": "array", "items": {"type": "string"}},
        "reason": {"type": "string"},
    },
}

_LLM_SYSTEM = (
    "You gate questions for a Bluetooth specification Q&A tool. "
    "Answer whether the question is about Bluetooth specifications (Core, GATT, "
    "profiles, Mesh, LE Audio, Assigned Numbers, errata). Be permissive: if it "
    "plausibly concerns Bluetooth or a wireless protocol detail, it is in scope. "
    "Return JSON only: {\"out_of_scope\": bool, \"doc_types\": [..], \"reason\": \"..\"}."
)


def _tokens(query: str) -> set[str]:
    return set(re.findall(r"[a-z0-9_/]+", (query or "").lower()))


def parse_scope(spec_scope, spec_version=None):
    """Map an Orchestrator-supplied scope hint onto a store filter, or None."""
    doc_types = None
    if spec_scope:
        key = str(spec_scope).strip().lower()
        doc_types = _SCOPE_ALIASES.get(key)
        if doc_types is None:
            doc_types = _SCOPE_ALIASES.get(key.split("-")[0])
    scope_filter = {}
    if doc_types:
        scope_filter["doc_type"] = list(doc_types)
    if spec_version:
        scope_filter["version"] = [str(spec_version)]
    return scope_filter or None


def _hint_from_text(query: str, spec_version=None):
    lowered = (query or "").lower()
    tokens = _tokens(query)
    doc_types = []
    for terms, doc_type in _DOC_TYPE_HINTS:
        if any((" " in t and t in lowered) or (" " not in t and t in tokens) for t in terms):
            if doc_type not in doc_types:
                doc_types.append(doc_type)
    scope_filter = {}
    if doc_types:
        scope_filter["doc_type"] = doc_types
    if spec_version:
        scope_filter["version"] = [str(spec_version)]
    return scope_filter or None


def _has_bt_vocabulary(query: str) -> bool:
    lowered = (query or "").lower()
    tokens = _tokens(query)
    for term in _BT_TERMS:
        if " " in term or "/" in term:
            if term in lowered:
                return True
        elif term in tokens:
            return True
        elif len(term) > 6 and term in lowered:
            return True  # catches inflections like "advertising"/"advertiser"
    return False


async def _llm_gate(query):
    payload = await structured_call(
        [{"role": "system", "content": _LLM_SYSTEM},
         {"role": "user", "content": query}],
        _LLM_SCHEMA, model=config.ACTION_MODEL,
    )
    return payload


async def classify(query, *, spec_scope=None, spec_version=None, llm_fn=None):
    explicit = parse_scope(spec_scope, spec_version)
    if explicit:
        return ScopeDecision(out_of_scope=False, scope_filter=explicit,
                             reason="explicit scope from orchestrator", used_llm=False)

    if _has_bt_vocabulary(query):
        return ScopeDecision(out_of_scope=False,
                             scope_filter=_hint_from_text(query, spec_version),
                             reason="bluetooth vocabulary present", used_llm=False)

    lowered = (query or "").lower()
    if any(marker in lowered for marker in _OFF_DOMAIN):
        return ScopeDecision(out_of_scope=True, scope_filter=None,
                             reason="off-domain question with no Bluetooth vocabulary",
                             used_llm=False)

    gate = llm_fn or _llm_gate
    try:
        payload = await gate(query)
    except Exception as exc:
        # Fail open (§7.0 is a cost defence, not a correctness gate).
        return ScopeDecision(out_of_scope=False, scope_filter=None,
                             reason=f"scope gate unavailable ({exc}); proceeding",
                             used_llm=True)

    doc_types = [d for d in (payload.get("doc_types") or []) if d]
    scope_filter = {}
    if doc_types:
        scope_filter["doc_type"] = doc_types
    if spec_version:
        scope_filter["version"] = [str(spec_version)]
    return ScopeDecision(
        out_of_scope=bool(payload.get("out_of_scope")),
        scope_filter=scope_filter or None,
        reason=payload.get("reason", "classified by scope gate"),
        used_llm=True,
    )
