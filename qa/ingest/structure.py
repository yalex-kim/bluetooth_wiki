"""§5.1 deterministic structure parsing.

The converted markdown already carries the spec's explicit structure, so the
graph skeleton is transcription, not inference: heading tree -> Section nodes,
pipe tables -> Table nodes, image links -> Figure nodes, "see Section 4.5.2" /
"Figure 3.2" -> REFERENCES edges. No LLM is involved, so this layer is accurate
and effectively free; the §5.3 extraction pass only decorates what is built here.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

_HEADING_RE = re.compile(r"^(#{1,6})\s+(?P<rest>\S.*)$")
_NUMBER_RE = re.compile(r"^(?P<num>\d+(?:\.\d+)*)\s+(?P<title>\S.*)$")
_TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
_TABLE_CAPTION_RE = re.compile(r"^\**\s*(Table\s+[\w.\-]+)\s*[:.\-]\s*(.*)$", re.I)
_FIGURE_CAPTION_RE = re.compile(r"^\**\s*(Figure\s+[\w.\-]+)\s*[:.\-]\s*(.*)$", re.I)
_IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<path>[^)]+)\)")
_PAGE_RE = re.compile(r"^\s*\[?page\s+(?P<n>\d+)\]?\s*$", re.I)
_XREF_SECTION_RE = re.compile(r"\b(?:see\s+)?Section\s+(\d+(?:\.\d+)+)", re.I)
_XREF_FIGURE_RE = re.compile(r"\bFigure\s+(\d+(?:\.\d+)*)", re.I)
_XREF_TABLE_RE = re.compile(r"\bTable\s+(\d+(?:\.\d+)*)", re.I)


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "section"


@dataclass
class SectionNode:
    id: str
    doc_id: str
    number: str
    title: str
    level: int
    parent_id: str | None
    line_start: int  # 1-based, inclusive
    line_end: int  # 1-based, inclusive
    text: str
    page: int | None = None


@dataclass
class TableNode:
    id: str
    doc_id: str
    section_id: str
    caption: str
    markdown: str
    line_start: int
    line_end: int


@dataclass
class FigureNode:
    id: str
    doc_id: str
    section_id: str
    caption: str
    image_path: str
    line_start: int


@dataclass
class CrossRef:
    source_section_id: str
    target_kind: str  # "section" | "figure" | "table"
    target_ref: str
    raw: str


@dataclass
class ParsedDocument:
    doc_id: str
    title: str
    doc_type: str
    version: str
    path: str
    sections: list = field(default_factory=list)
    tables: list = field(default_factory=list)
    figures: list = field(default_factory=list)
    crossrefs: list = field(default_factory=list)


def section_hash(section) -> str:
    """§5.5 change detection: content identity, insensitive to whitespace churn."""
    normalised = re.sub(r"\s+", " ", f"{section.number}|{section.title}|{section.text}").strip()
    return hashlib.sha1(normalised.encode("utf-8")).hexdigest()


def parse_markdown(text, *, doc_id, title, doc_type="Core", version="", path=""):
    lines = text.split("\n")
    doc = ParsedDocument(doc_id=doc_id, title=title, doc_type=doc_type,
                         version=version, path=path)

    # 1. Heading boundaries -> section spans; parents come off the level stack.
    heads = []  # (line_idx, level, number, title)
    for i, line in enumerate(lines):
        m = _HEADING_RE.match(line)
        if not m:
            continue
        level, rest = len(m.group(1)), m.group("rest").strip()
        nm = _NUMBER_RE.match(rest)
        number, heading_title = (nm.group("num"), nm.group("title").strip()) if nm else ("", rest)
        heads.append((i, level, number, heading_title))
    if not heads:
        return doc

    stack: list[tuple[int, str]] = []  # [(level, section_id)]
    id_by_number: dict[str, str] = {}
    page = None
    for idx, (line_idx, level, number, heading_title) in enumerate(heads):
        end = heads[idx + 1][0] if idx + 1 < len(heads) else len(lines)
        while stack and stack[-1][0] >= level:
            stack.pop()
        # Heading depth is unreliable in converted specs — 4.5 and 4.5.2 are both
        # '###' in Core conversions. When a heading carries a dotted number, the
        # number is the authority on parentage; the level stack is the fallback
        # for unnumbered headings.
        parent_id = None
        if "." in number:
            parent_number = number.rsplit(".", 1)[0]
            parent_id = id_by_number.get(parent_number)
        if parent_id is None:
            parent_id = stack[-1][1] if stack else None
        sid = f"{doc_id}#{number or _slug(heading_title)}"
        if number:
            id_by_number[number] = sid
        body_lines = lines[line_idx + 1 : end]
        for bl in body_lines:
            pm = _PAGE_RE.match(bl)
            if pm:
                page = int(pm.group("n"))
        doc.sections.append(SectionNode(
            id=sid, doc_id=doc_id, number=number, title=heading_title, level=level,
            parent_id=parent_id, line_start=line_idx + 1, line_end=end,
            text="\n".join(body_lines).strip(), page=page,
        ))
        stack.append((level, sid))

    # 2. Tables, figures and cross-references, attributed to the owning section.
    spans = [(s.line_start, s.line_end, s.id) for s in doc.sections]

    def owner(line_no: int) -> str:
        for start, end, sid in spans:
            if start <= line_no <= end:
                return sid
        return doc.sections[0].id

    i = 0
    table_seq = fig_seq = 0
    while i < len(lines):
        if _TABLE_ROW_RE.match(lines[i]):
            start = i
            while i < len(lines) and _TABLE_ROW_RE.match(lines[i]):
                i += 1
            block = "\n".join(lines[start:i])
            caption = ""
            # Spec conversions put the caption just below the table, sometimes above.
            probes = list(range(i, min(i + 3, len(lines)))) + list(range(max(start - 3, 0), start))
            for probe in probes:
                cm = _TABLE_CAPTION_RE.match(lines[probe].strip())
                if cm:
                    caption = f"{cm.group(1)}: {cm.group(2)}".strip().rstrip(":")
                    break
            table_seq += 1
            doc.tables.append(TableNode(
                id=f"{doc_id}:table:{table_seq}", doc_id=doc_id,
                section_id=owner(start + 1), caption=caption or f"Table {table_seq}",
                markdown=block, line_start=start + 1, line_end=i,
            ))
            continue

        im = _IMAGE_RE.search(lines[i])
        if im:
            caption = ""
            for probe in range(i + 1, min(i + 4, len(lines))):
                fm = _FIGURE_CAPTION_RE.match(lines[probe].strip())
                if fm:
                    caption = f"{fm.group(1)}: {fm.group(2)}".strip().rstrip(":")
                    break
            fig_seq += 1
            doc.figures.append(FigureNode(
                id=f"{doc_id}:figure:{fig_seq}", doc_id=doc_id,
                section_id=owner(i + 1), caption=caption or im.group("alt"),
                image_path=im.group("path"), line_start=i + 1,
            ))
        i += 1

    for section in doc.sections:
        seen = set()
        for kind, regex in (("section", _XREF_SECTION_RE),
                            ("figure", _XREF_FIGURE_RE),
                            ("table", _XREF_TABLE_RE)):
            for m in regex.finditer(section.text):
                ref = m.group(1)
                if kind == "section" and ref == section.number:
                    continue  # a section citing itself is not a cross-reference
                key = (kind, ref)
                if key in seen:
                    continue
                seen.add(key)
                doc.crossrefs.append(CrossRef(
                    source_section_id=section.id, target_kind=kind,
                    target_ref=ref, raw=m.group(0),
                ))
    return doc
