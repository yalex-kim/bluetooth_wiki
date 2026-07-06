"""Structural chunker for the converted Core spec markdown files.

Fixes the Vol/Part addressing that the original ``read_source`` regex got
wrong: ``[Vol N]``/``Part X`` *tagged* headings only exist in the front-matter
(consolidated ToC / acknowledgments), while real Part boundaries in the body
appear as untagged plain-text marker lines. Verified against Core_v6.0.md:

* The consolidated ToC near the top lists, per volume, ``Part A CONSOLIDATED
  TABLE OF CONTENTS``-style lines plus ``{Volume Title} Specification Volume N``
  banners (the Vol 4 banner is missing in the conversion — handled below).
* Body Part boundaries are either ``{Volume Title} Part {L}`` standalone lines
  (Vols 0-3, 6, 7) or, for Vol 4, just the ALL-CAPS part title standalone
  (e.g. ``UART TRANSPORT LAYER``).
* ~1-2% of ``##`` headings are PyMuPDF equation noise (``## 1 when 0 ≤f …``,
  ``## 216 mod N``) that must not become chunk boundaries.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from agent.config import SOURCES_DIR

CHUNKER_VERSION = "1"

MAX_CHUNK_CHARS = 4000
MIN_CHUNK_CHARS = 50

_NO_LONGER_USED = "[THIS PART IS NO LONGER USED]"

_VOL_BANNER_RE = re.compile(r"^(?P<title>.+?)\s+Specification Volume\s+(?P<num>\d+)\s*$")
# 5.x conversions split the banner over two lines: '{Title}\nSpecification Volume N'.
_VOL_BANNER_BARE_RE = re.compile(r"^Specification Volume\s+(?P<num>\d+)\s*$")
_TOC_PART_RE = re.compile(r"^Part\s+(?P<letter>[A-Z])\s+(?P<title>\S.*)$")
_VOL_TAG_RE = re.compile(r"\[Vol\s+(?P<num>\d+)\]\s+(?P<title>[^|]+?)\s*$")

# Characters that only appear in equation fragments mis-parsed as headings.
_NOISE_CHAR_RE = re.compile(r"[∀-⋿Ͱ-Ͽ±×÷√-∞]")


def _norm(s: str) -> str:
    """Lowercase and strip everything but alphanumerics, for fuzzy line matching."""
    return re.sub(r"[^a-z0-9]+", "", s.lower())


@dataclass
class PartSpan:
    vol: str
    part: str
    part_title: str
    vol_title: str
    line_start: int  # 0-based, inclusive (the marker line)
    line_end: int  # 0-based, exclusive


@dataclass
class Chunk:
    id: str
    version: str
    vol: str
    part: str
    part_title: str
    section: str  # dotted heading number, e.g. "4.4.2" ("" for part preamble)
    heading_title: str
    line_start: int  # 1-based, inclusive
    line_end: int  # 1-based, inclusive
    text: str


def spec_path(version: str) -> Path:
    return SOURCES_DIR / "specs" / version / f"Core_v{version}.md"


# ─── Consolidated-ToC parsing ────────────────────────────────────────────


def _first_heading_idx(lines: list[str]) -> int:
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            return i
    return len(lines)


def _parse_toc(lines: list[str]) -> list[tuple[str, str, str]]:
    """Parse the consolidated ToC block → ordered [(vol, part_letter, part_title)].

    Handles the missing Vol 4 banner: a ``Part A …`` line whose letter restarts
    the sequence bumps the current volume number.
    """
    end = _first_heading_idx(lines)
    out: list[tuple[str, str, str]] = []
    cur_vol: int | None = None
    last_letter = ""
    for ln in lines[:end]:
        s = ln.strip()
        m = _VOL_BANNER_RE.match(s) or _VOL_BANNER_BARE_RE.match(s)
        if m:
            cur_vol = int(m.group("num"))
            last_letter = ""
            continue
        m = _TOC_PART_RE.match(s)
        if m and cur_vol is not None:
            letter, title = m.group("letter"), m.group("title").strip()
            if letter <= last_letter:  # e.g. 'A' after 'H' with no banner between
                cur_vol += 1
            # Skip duplicate (vol, letter) rows: 5.x files repeat the volume's
            # own ToC before each volume body.
            if not any(v == str(cur_vol) and pl == letter for v, pl, _ in out):
                out.append((str(cur_vol), letter, title))
            last_letter = letter
    return out


def _parse_vol_titles(lines: list[str]) -> dict[str, str]:
    """Map vol number → canonical title from '[Vol N] Title' tagged headings."""
    titles: dict[str, str] = {}
    for ln in lines:
        if not ln.startswith("#"):
            continue
        m = _VOL_TAG_RE.search(ln)
        if m and m.group("num") not in titles:
            titles[m.group("num")] = m.group("title").strip()
    return titles


# ─── Body Part-boundary detection ────────────────────────────────────────


def parse_part_spans(text: str) -> list[PartSpan]:
    """Locate every real Part's span in the body via sequential marker matching."""
    lines = text.split("\n")  # NOT splitlines(): \x0b/\x0c in PDF text would shift line numbers vs editors/grep
    toc = _parse_toc(lines)
    if not toc:
        return []
    vol_titles = _parse_vol_titles(lines)

    # Volume-title variants seen in ToC banners (for marker-style (a) lines).
    banner_titles: dict[str, str] = {}
    end = _first_heading_idx(lines)
    prev_nonempty = ""
    for ln in lines[:end]:
        s = ln.strip()
        m = _VOL_BANNER_RE.match(s)
        if m:
            banner_titles[m.group("num")] = m.group("title").strip()
        else:
            m = _VOL_BANNER_BARE_RE.match(s)
            if m and m.group("num") not in banner_titles and prev_nonempty:
                banner_titles[m.group("num")] = prev_nonempty
        if s:
            prev_nonempty = s

    # Pre-index normalized line → sorted positions, so per-part lookups are O(log n).
    positions: dict[str, list[int]] = {}
    # Figure refs like 'Vol4_PartE_Figure1_1.png' carry vol/part metadata and
    # survive conversion even when a Part's banner page was dropped entirely
    # (true for Vol 4 Part E in Core_v6.0.md) — index them as a fallback signal.
    fig_positions: dict[tuple[str, str], list[int]] = {}
    fig_re = re.compile(r"Vol(\d+)_Part([A-Z])_Figure")
    exact_positions: dict[str, list[int]] = {}  # case-sensitive, for 'PART X: TITLE' markers
    for i, ln in enumerate(lines):
        m = fig_re.search(ln)
        if m:
            fig_positions.setdefault((m.group(1), m.group(2)), []).append(i)
        s = ln.strip()
        if not s or len(s) > 120:
            continue
        positions.setdefault(_norm(s), []).append(i)
        exact_positions.setdefault(s, []).append(i)

    def _find_after(keys: list[tuple[dict, str]], after: int) -> int | None:
        best: int | None = None
        for table, k in keys:
            for pos in table.get(k, []):
                if pos > after and (best is None or pos < best):
                    best = pos
                    break
        return best

    spans: list[PartSpan] = []
    cursor = 0  # scan from the very top: Vol 0 Part A's marker sits above the ToC block
    for vol, letter, title in toc:
        # Primary markers are unambiguous: '{Volume Title} Part {L}' (6.x style)
        # and the case-sensitive 'PART {L}: {TITLE}' (5.x style). The bare
        # ALL-CAPS title is ambiguous (the ToC listing normalizes to similar
        # strings), so it is only consulted when the primary markers miss.
        primary: list[tuple[dict, str]] = []
        for vt in filter(None, {banner_titles.get(vol), vol_titles.get(vol)}):
            primary.append((positions, _norm(f"{vt} Part {letter}")))
        if title != _NO_LONGER_USED:
            primary.append((exact_positions, f"PART {letter}: {title}"))
        found = _find_after(primary, cursor)
        if found is None and title != _NO_LONGER_USED:
            found = _find_after([(positions, _norm(title))], cursor)
        if found is None:
            # Last resort: locate the part via its first figure reference, then
            # backtrack to the nearest preceding '## 1 …' heading (the part's
            # numbering restart). Rescues parts whose banner page was lost
            # entirely (true for Vol 4 Part E in Core_v6.0.md).
            fig = next((p for p in fig_positions.get((vol, letter), []) if p > cursor), None)
            if fig is not None:
                found = fig
                for j in range(fig, cursor, -1):
                    if lines[j].startswith("## 1 "):
                        found = j
                        break
        if found is None:
            continue  # part absent from body (e.g. "no longer used" with no stub)
        spans.append(
            PartSpan(vol=vol, part=letter, part_title=title, vol_title=vol_titles.get(vol, banner_titles.get(vol, "")), line_start=found, line_end=len(lines))
        )
        cursor = found
    for prev, nxt in zip(spans, spans[1:]):
        prev.line_end = nxt.line_start
    return spans


def get_part_span(text: str, vol: str, part: str) -> tuple[int, int] | None:
    """1-based (start, end_exclusive) line span for a Vol/Part, or None.

    This is the correctness fix consumed by agent/tools.py::_read_source.
    """
    for span in parse_part_spans(text):
        if span.vol == str(vol).strip() and span.part == str(part).strip().upper():
            return (span.line_start + 1, span.line_end + 1)
    return None


# ─── Heading acceptance (noise filtering) ────────────────────────────────

_H2_RE = re.compile(r"^##\s+(?P<num>\d{1,3})\s+(?P<title>\S.*)$")
_HD_RE = re.compile(r"^(?P<hashes>#{3,5})\s+(?P<num>\d{1,3}(?:\.\d{1,3})+)\s+(?P<title>\S.*)$")
_H2_APPENDIX_RE = re.compile(r"^##\s+(?P<title>APPENDIX\b.*)$")


def _is_noisy(title: str) -> bool:
    return bool(_NOISE_CHAR_RE.search(title))


def _accept_heading(line: str, open_nums: dict[int, tuple[int, ...]]) -> tuple[int, str, str] | None:
    """Return (level, dotted_number, title) if this line is a real heading.

    ``open_nums`` maps heading level → currently open number components; used
    to reject out-of-sequence equation fragments like ``## 216 mod N``.
    """
    m = _H2_APPENDIX_RE.match(line)
    if m and not _is_noisy(m.group("title")):
        return (2, "", m.group("title").strip())
    m = _H2_RE.match(line)
    if m:
        title = m.group("title").strip()
        # Real level-2 spec headings are ALL CAPS: reject any lowercase letter
        # (kills '## 1 when 0 ≤f …', '## 216 mod N', '## 31 octets of …') and
        # require at least two consecutive letters (kills digit-run fragments).
        if _is_noisy(title) or re.search(r"[a-z]", title) or not re.search(r"[A-Z]{2}", title):
            return None
        return (2, m.group("num"), title)
    m = _HD_RE.match(line)
    if m:
        level = len(m.group("hashes"))
        title = m.group("title").strip()
        comps = tuple(int(c) for c in m.group("num").split("."))
        if len(comps) != level - 1:
            return None  # wrong nesting depth for its number → conversion noise
        if _is_noisy(title) or not re.search(r"[A-Za-z]", title):
            return None
        parent = open_nums.get(level - 1)
        if parent is None or comps[: len(parent)] != parent:
            return None  # doesn't belong under the currently open section
        return (level, m.group("num"), title)
    return None


# ─── Chunk construction ──────────────────────────────────────────────────


def _split_oversized(text: str, max_chars: int) -> list[str]:
    """Split chunk text at paragraph breaks, keeping pieces under max_chars.

    Blocks with no blank lines at all (giant converted tables) are hard-split
    on line boundaries so no piece can dodge the size cap.
    """
    if len(text) <= max_chars:
        return [text]
    paras: list[str] = []
    for para in text.split("\n\n"):
        if len(para) <= max_chars * 1.5:
            paras.append(para)
            continue
        lines = para.split("\n")
        cur: list[str] = []
        size = 0
        for ln in lines:
            if size + len(ln) > max_chars and cur:
                paras.append("\n".join(cur))
                cur, size = [], 0
            cur.append(ln)
            size += len(ln) + 1
        if cur:
            paras.append("\n".join(cur))
    pieces: list[str] = []
    cur = []
    size = 0
    for para in paras:
        if size + len(para) > max_chars and cur:
            pieces.append("\n\n".join(cur))
            cur, size = [], 0
        cur.append(para)
        size += len(para) + 2
    if cur:
        pieces.append("\n\n".join(cur))
    return pieces


def chunk_core_spec(version: str, *, max_chars: int = MAX_CHUNK_CHARS, min_chars: int = MIN_CHUNK_CHARS) -> list[Chunk]:
    path = spec_path(version)
    if not path.is_file():
        raise FileNotFoundError(f"No spec markdown at {path}")
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.split("\n")  # NOT splitlines(): \x0b/\x0c in PDF text would shift line numbers vs editors/grep
    spans = parse_part_spans(text)

    raw: list[Chunk] = []
    for span in spans:
        if span.part_title == _NO_LONGER_USED:
            continue
        # Section boundaries within this part.
        open_nums: dict[int, tuple[int, ...]] = {}
        bounds: list[tuple[int, str, str]] = []  # (line_idx, section, title)
        for i in range(span.line_start, span.line_end):
            ln = lines[i]
            if not ln.startswith("#"):
                continue
            acc = _accept_heading(ln, open_nums)
            if acc is None:
                continue
            level, num, title = acc
            comps = tuple(int(c) for c in num.split(".")) if num else ()
            open_nums[level] = comps
            for deeper in list(open_nums):
                if deeper > level:
                    del open_nums[deeper]
            bounds.append((i, num, title))

        seg_edges = [span.line_start] + [b[0] for b in bounds] + [span.line_end]
        seg_meta = [("", span.part_title)] + [(b[1], b[2]) for b in bounds]
        for (start, end), (section, title) in zip(zip(seg_edges, seg_edges[1:]), seg_meta):
            body = "\n".join(lines[start:end]).strip()
            if not body:
                continue
            raw.append(
                Chunk(
                    id=f"{version}:{span.vol}:{span.part}:{section or 'preamble'}:{start + 1}",
                    version=version,
                    vol=span.vol,
                    part=span.part,
                    part_title=span.part_title,
                    section=section,
                    heading_title=title,
                    line_start=start + 1,
                    line_end=end,
                    text=body,
                )
            )

    # Size normalization: merge tiny chunks forward, split oversized ones.
    merged: list[Chunk] = []
    for c in raw:
        if merged and len(merged[-1].text) < min_chars and merged[-1].part == c.part and merged[-1].vol == c.vol:
            prev = merged[-1]
            prev.text = prev.text + "\n\n" + c.text
            prev.line_end = c.line_end
            if not prev.section:
                prev.section, prev.heading_title = c.section, c.heading_title
            continue
        merged.append(c)

    final: list[Chunk] = []
    for c in merged:
        pieces = _split_oversized(c.text, max_chars)
        if len(pieces) == 1:
            final.append(c)
            continue
        offset = 0
        for n, piece in enumerate(pieces):
            nlines = piece.count("\n") + 1
            final.append(
                Chunk(
                    id=f"{c.id}#{n}",
                    version=c.version,
                    vol=c.vol,
                    part=c.part,
                    part_title=c.part_title,
                    section=c.section,
                    heading_title=c.heading_title,
                    line_start=c.line_start + offset,
                    line_end=min(c.line_start + offset + nlines - 1, c.line_end),
                    text=piece,
                )
            )
            offset += nlines + 1
    return final
