#!/usr/bin/env python3
"""
Convert Bluetooth Core Spec PDFs to Markdown.

Extracts:
  - Text with correct heading depths (## for Vol sections → ###### for 4-dot levels)
  - Tables as inline Markdown tables (positioned where they appear in the page)
  - Figures as PNG images named Vol{N}_Part{P}_Figure{X_Y}.png, inserted inline

Usage:
    python scripts/convert_to_md.py              # Convert all unconverted PDFs
    python scripts/convert_to_md.py 6.0          # Single version
    python scripts/convert_to_md.py 5.2 6.0      # Multiple versions

Requirements:
    pip install PyMuPDF

Output per version:
    sources/specs/{ver}/Core_v{ver}.md
    sources/specs/{ver}/Core_v{ver}_images/Vol{N}_Part{P}_Figure{X_Y}.png  (one per figure)
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SPECS_DIR = REPO_ROOT / "sources" / "specs"

# Matches blocks that open with a section number followed by a title.
# Limit to 150 chars total so body sentences starting with numerals don't match.
_SEC_RE = re.compile(r"^(\d+(?:\.\d+)*)\s+(.{1,140})$")

# Figure caption: block must start with "Figure N.M:" or "Figure N.M –".
# Colon/dash is REQUIRED to distinguish captions from in-text references
# like "see Figure 3.2 for details".
_FIG_RE = re.compile(r"^Figure\s+(\d+\.\d+)\s*[:\-–]", re.IGNORECASE)

# TOC leader pattern: 4+ consecutive dots (e.g. "Introduction ......... 78").
# These are Table-of-Contents entries and should be skipped entirely.
_TOC_RE = re.compile(r"\.{4,}")

# Running headers / footers to discard
_SKIP_RE = re.compile(
    r"^(BLUETOOTH\s+(CORE\s+)?SPEC(IFICATION)?|"
    r"Host Controller Interface|HCI Commands|Bluetooth SIG Proprietary|"
    r"\d{1,2}\s+\w{3,9}\s+\d{4}$|page\s+\d+$)",
    re.IGNORECASE,
)


# ─── Dependency check ────────────────────────────────────────────────────────

def check_fitz():
    try:
        import fitz
        return fitz
    except ImportError:
        print("ERROR: PyMuPDF is not installed.\n  pip install PyMuPDF")
        sys.exit(1)


# ─── Heading depth ───────────────────────────────────────────────────────────

def heading_prefix(num_str: str) -> str:
    """
    Map section-number depth to a markdown heading level.
      "4"       → ##      (h2)
      "4.1"     → ###     (h3)
      "4.1.1"   → ####    (h4)
      "4.1.1.1" → #####   (h5)
      deeper    → ######  (h6)
    """
    return "#" * min(num_str.count(".") + 2, 6)


# ─── Volume / Part map from PDF bookmarks ────────────────────────────────────

def build_vol_part_map(doc) -> dict:
    """
    Return {page_idx (0-based): (vol_num: int|None, part_str: str|None)}
    by walking the PDF table of contents (bookmarks).
    """
    toc = doc.get_toc()          # [(level, title, 1-based page), ...]
    raw: dict = {}
    cv, cp = None, None

    for _lvl, title, page in toc:
        vm = re.search(r"\bVol(?:ume)?\s*(\d+)\b", title, re.I)
        pm = re.search(r"\bPart\s+([A-Z])\b", title, re.I)
        if vm:
            cv = int(vm.group(1))
            cp = None            # reset Part when Volume changes
        if pm:
            cp = pm.group(1).upper()
        raw[page - 1] = (cv, cp)

    # Fill forward so every page inherits the last known Vol/Part
    filled: dict = {}
    cv2, cp2 = None, None
    for i in range(len(doc)):
        if i in raw:
            cv2, cp2 = raw[i]
        filled[i] = (cv2, cp2)
    return filled


# ─── Figure region detection & rendering ─────────────────────────────────────

def _r(v, attr, idx):
    """Extract a float coord from a fitz.Rect or sequence."""
    try:
        return float(getattr(v, attr))
    except AttributeError:
        return float(v[idx])


def find_figure_bounds(page, caption_y0: float, min_y: float, fitz,
                       drawings=None):
    """
    Return (x0, y0, x1, y1) of the tightest bounding box around the figure
    (vector-drawing cluster) that sits above *caption_y0*.

    Strategy:
    - Collect all drawings above the caption within [min_y, caption_y0].
      *min_y* is normally HEADER_Y for the first figure on a page, or the
      bottom of the previous figure's caption for subsequent figures — this
      prevents the cluster from reaching into the area of the figure above.
    - Walk downward from the drawing with the highest bottom (closest to caption),
      accumulating a cluster until a vertical gap > 50 pt is seen.
    - Use the cluster's union bbox for both x and y bounds (tight crop).
    - Falls back to full content width if no drawings are found.

    The x bounds eliminate the wide blank margins that surround the figure
    on a standard letter/A4 page.

    Pass *drawings* (from page.get_drawings()) to reuse a cached result
    when this function is called multiple times on the same page.
    """
    pw = page.rect.width

    if drawings is None:
        try:
            drawings = page.get_drawings()
        except Exception:
            return (0.0, header_y, pw, caption_y0 - 2)

    above = []
    for d in drawings:
        r = d.get("rect")
        if r is None:
            continue
        try:
            rx0 = _r(r, "x0", 0)
            ry0 = _r(r, "y0", 1)
            rx1 = _r(r, "x1", 2)
            ry1 = _r(r, "y1", 3)
        except (IndexError, TypeError, ValueError):
            continue
        # Only drawings strictly above the caption and within the content zone.
        # Do NOT filter by prev_text_y — figure labels (text blocks) inside
        # the diagram would otherwise push prev_text_y into the figure area.
        if ry1 <= caption_y0 and ry0 >= min_y:
            above.append((rx0, ry0, rx1, ry1))

    if not above:
        return (0.0, min_y, pw, caption_y0 - 2)

    # Sort by y1 descending: drawing closest to caption comes first.
    above.sort(key=lambda r: r[3], reverse=True)

    GAP = 50  # pt — gap larger than this means a separate figure above
    cluster = [above[0]]
    walk_top = above[0][1]   # y0 of the topmost rect in the cluster so far

    for i in range(1, len(above)):
        cx0, cy0, cx1, cy1 = above[i]
        if walk_top - cy1 > GAP:
            break
        cluster.append(above[i])
        walk_top = min(walk_top, cy0)

    MARGIN = 8   # pt padding around the tight bbox (sides + bottom only)
    bx0 = max(min(r[0] for r in cluster) - MARGIN, 0.0)
    by0 = max(min(r[1] for r in cluster), min_y)   # clamp to min_y to avoid overlap with previous figure
    bx1 = min(max(r[2] for r in cluster) + MARGIN, pw)
    by1 = caption_y0 - 2

    return (bx0, by0, bx1, by1)


def render_region(page, x0: float, y0: float, x1: float, y1: float,
                  img_path: Path, fitz) -> bool:
    """
    Render the clipped rectangle (x0,y0)–(x1,y1) of *page* as a 2× PNG.
    Returns False and saves nothing if the region is trivially small or
    entirely white (no actual figure content).
    """
    if (y1 - y0) < 20 or (x1 - x0) < 20:
        return False

    clip = fitz.Rect(x0, y0, x1, y1)
    mat = fitz.Matrix(2.0, 2.0)
    pix = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csRGB)

    # Skip if >97 % of pixels are white (blank / empty region)
    samp = pix.samples
    n = pix.width * pix.height
    if n > 0:
        white = sum(
            1 for i in range(0, len(samp), 3)
            if samp[i] > 245 and samp[i + 1] > 245 and samp[i + 2] > 245
        )
        if white / n > 0.97:
            return False

    img_path.parent.mkdir(parents=True, exist_ok=True)
    pix.save(str(img_path))
    return True


# ─── Per-page conversion ─────────────────────────────────────────────────────

def _bbox_overlaps(a, b) -> bool:
    return a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]


def _block_text(b) -> str:
    """Join all span texts within a block into a single stripped string."""
    return " ".join(
        "".join(s["text"] for s in ln["spans"]).strip()
        for ln in b["lines"]
        if "".join(s["text"] for s in ln["spans"]).strip()
    ).strip()


def _fmt_row(row, ncols: int) -> str:
    cells = [
        ("" if c is None else str(c).replace("|", "\\|").replace("\n", " ").strip())
        for c in row
    ]
    while len(cells) < ncols:
        cells.append("")
    return "| " + " | ".join(cells) + " |"


def process_page(page, p_idx: int, vol_part_map: dict,
                 img_dir: Path, fitz) -> list:
    """Return a list of markdown strings for one PDF page."""
    ph = page.rect.height
    HEADER_Y = ph * 0.09   # 9%: safely below the running header (title + logo band)
    FOOTER_Y = ph * 0.91
    vol_num, part_str = vol_part_map.get(p_idx, (None, None))

    # ── Pass 1: scan ALL text blocks to find figure captions ─────────────
    # Must happen before table extraction so that grid lines drawn inside
    # architecture/timing diagrams are not mistaken for real data tables.
    _all_text = [
        b for b in page.get_text("dict")["blocks"]
        if b["type"] == 0
        and b["bbox"][1] < FOOTER_Y
        and b["bbox"][3] > HEADER_Y
    ]
    _all_text.sort(key=lambda b: (b["bbox"][1], b["bbox"][0]))

    # Collect figure captions sorted top-to-bottom.  For each caption the
    # upper drawing-search limit is the bottom of the previous caption
    # (HEADER_Y for the first one).  This prevents Figure N+1's cluster
    # from reaching into Figure N's drawing area when both appear on the
    # same page and their drawings are less than GAP=50 pt apart.
    _cap_blocks = []
    for b in _all_text:
        bt = _block_text(b)
        if not _TOC_RE.search(bt) and _FIG_RE.match(bt):
            _cap_blocks.append(b)
    _cap_blocks.sort(key=lambda b: b["bbox"][1])

    # (caption_y0, min_y) — min_y is the lower bound for drawing search
    _cap_info = [
        (b["bbox"][1], (_cap_blocks[i - 1]["bbox"][3] if i > 0 else HEADER_Y))
        for i, b in enumerate(_cap_blocks)
    ]

    _page_drawings = None
    _fig_zones = []   # list of (y0, y1) bands to suppress content inside
    for cap_y0, min_y in _cap_info:
        if _page_drawings is None:
            try:
                _page_drawings = page.get_drawings()
            except Exception:
                _page_drawings = []
            _, fy0, _, fy1 = find_figure_bounds(
                page, cap_y0, min_y, fitz, _page_drawings)
            _fig_zones.append((fy0, fy1))

    def _in_figure(by0, by1):
        """True if the block [by0, by1] sits entirely inside a figure zone."""
        return any(fz0 <= by0 and by1 <= fz1 for fz0, fz1 in _fig_zones)

    # ── Tables (skip those whose top falls inside a figure zone) ─────────
    table_bboxes = []
    table_items = []        # (y_top, md_rows, y_bot)

    try:
        tf = page.find_tables()
        for tab in (tf.tables if hasattr(tf, "tables") else list(tf)):
            if _in_figure(tab.bbox[1], tab.bbox[3]):
                continue   # grid lines inside a diagram — not a real table
            grid = tab.extract()
            if not grid or len(grid) < 2:
                continue
            ncols = max(len(r) for r in grid)
            rows = [
                "",
                _fmt_row(grid[0], ncols),
                "| " + " | ".join("---" for _ in range(ncols)) + " |",
            ]
            rows += [_fmt_row(r, ncols) for r in grid[1:]]
            rows.append("")
            table_bboxes.append(tab.bbox)
            table_items.append((tab.bbox[1], rows, tab.bbox[3]))
    except Exception:
        pass

    # ── Text blocks (skip those inside real table bounding boxes) ─────────
    text_blocks = [
        b for b in _all_text
        if not any(_bbox_overlaps(b["bbox"], tb) for tb in table_bboxes)
    ]

    # ── Unified reading-order stream ─────────────────────────────────────
    stream = [(b["bbox"][1], "text", b) for b in text_blocks]
    stream += [(y, "table", (rows, yb)) for y, rows, yb in table_items]
    stream.sort(key=lambda x: x[0])

    md = []
    prev_text_y = HEADER_Y  # bottom of the last non-figure text / table block

    for _y, kind, data in stream:

        # ── Table element ────────────────────────────────────────────────
        if kind == "table":
            rows, yb = data
            md.extend(rows)
            prev_text_y = yb
            continue

        # ── Text block ───────────────────────────────────────────────────
        b = data
        by0 = b["bbox"][1]
        by1 = b["bbox"][3]
        all_spans = [s for ln in b["lines"] for s in ln["spans"]]

        block_text = _block_text(b)
        if not block_text or _SKIP_RE.match(block_text):
            continue

        # ── Skip TOC entries (leader dots like "Section .......... 42") ──
        if _TOC_RE.search(block_text):
            continue

        # ── Skip diagram labels (text inside a figure region) ────────────
        if _in_figure(by0, by1):
            continue

        # ── Figure caption? ───────────────────────────────────────────────
        fig_m = _FIG_RE.match(block_text)
        if fig_m:
            fig_num = fig_m.group(1)
            safe_num = fig_num.replace(".", "_")
            if vol_num is not None and part_str is not None:
                fname = f"Vol{vol_num}_Part{part_str}_Figure{safe_num}.png"
            else:
                fname = f"Figure{safe_num}.png"
            img_path = img_dir / fname
            if not img_path.exists():
                # Use the per-caption min_y so we don't overlap the figure above
                min_y = next(
                    (my for cy, my in _cap_info if abs(cy - by0) < 2),
                    HEADER_Y,
                )
                bx0, fy0, bx1, fy1 = find_figure_bounds(
                    page, by0, min_y, fitz, _page_drawings)
                if render_region(page, bx0, fy0, bx1, fy1, img_path, fitz):
                    rel = f"{img_dir.name}/{fname}"
                    md.append(f"\n![Figure {fig_num}]({rel})\n")
            md.append(f"\n**{block_text}**\n")
            prev_text_y = by1   # advance past caption; next figure search starts here
            continue

        # ── Section heading? ──────────────────────────────────────────────
        sec_m = _SEC_RE.match(block_text)
        if sec_m:
            num_str = sec_m.group(1)
            depth = num_str.count(".")
            is_bold = any(s.get("flags", 0) & 16 for s in all_spans)
            max_font = max((s.get("size", 0) for s in all_spans), default=0)
            # Accept as heading when: shallow depth, or bold, or large font
            if depth <= 1 or is_bold or max_font >= 11:
                md.append(f"\n{heading_prefix(num_str)} {block_text}\n")
                prev_text_y = by1
                continue

        # ── Body text ─────────────────────────────────────────────────────
        md.append(block_text)
        prev_text_y = by1

    return md


# ─── Top-level converter ─────────────────────────────────────────────────────

def convert_spec(version: str, fitz) -> bool:
    pdf_path = SPECS_DIR / version / f"Core_v{version}.pdf"
    md_path = SPECS_DIR / version / f"Core_v{version}.md"
    img_dir = SPECS_DIR / version / f"Core_v{version}_images"

    if not pdf_path.exists():
        print(f"  [SKIP] {pdf_path} — PDF not found.")
        return False
    if md_path.exists():
        print(f"  [SKIP] {md_path.name} already exists. Delete to reconvert.")
        return True

    size_mb = pdf_path.stat().st_size // (1024 * 1024)
    print(f"  Opening {pdf_path.name} ({size_mb} MB) ...")
    doc = fitz.open(str(pdf_path))
    img_dir.mkdir(exist_ok=True)

    vol_part_map = build_vol_part_map(doc)

    all_lines = [
        f"# Bluetooth Core Specification {version} — Full Text",
        "",
        f"> Source: PDF converted via PyMuPDF.",
        f"> Wiki summary: [core-spec-{version}](../../wiki/versions/core-spec-{version}.md)",
        "",
        "---",
        "",
    ]

    total = len(doc)
    for p in range(total):
        if p % 200 == 0 and p > 0:
            print(f"    {p:,}/{total:,} pages ...")
        all_lines.extend(
            process_page(doc[p], p, vol_part_map, img_dir, fitz)
        )

    doc.close()

    content = "\n".join(all_lines)
    md_path.write_text(content, encoding="utf-8")
    n_imgs = len(list(img_dir.glob("*.png")))
    print(f"  [OK] {md_path.name}: {len(all_lines):,} lines | {n_imgs} figures extracted")
    return True


def convert_pdf_file(pdf_path: Path, fitz) -> bool:
    """Convert any single Bluetooth spec PDF (Errata, ICS, redlines, etc.)."""
    stem = pdf_path.stem
    md_path = pdf_path.parent / f"{stem}.md"
    img_dir = pdf_path.parent / f"{stem}_images"

    if md_path.exists():
        print(f"  [SKIP] {md_path.name} already exists. Delete to reconvert.")
        return True

    size_mb = pdf_path.stat().st_size // (1024 * 1024)
    size_str = f"{size_mb} MB" if size_mb >= 1 else f"{pdf_path.stat().st_size // 1024} KB"
    print(f"  Opening {pdf_path.name} ({size_str}) ...")
    doc = fitz.open(str(pdf_path))
    img_dir.mkdir(exist_ok=True)

    vol_part_map = build_vol_part_map(doc)

    all_lines = [
        f"# {stem.replace('_', ' ')}",
        "",
        "> Source: PDF converted via PyMuPDF.",
        "",
        "---",
        "",
    ]

    total = len(doc)
    for p in range(total):
        if p % 200 == 0 and p > 0:
            print(f"    {p:,}/{total:,} pages ...")
        all_lines.extend(
            process_page(doc[p], p, vol_part_map, img_dir, fitz)
        )

    doc.close()

    content = "\n".join(all_lines)
    md_path.write_text(content, encoding="utf-8")
    n_imgs = len(list(img_dir.glob("*.png")))
    print(f"  [OK] {md_path.name}: {len(all_lines):,} lines | {n_imgs} figures extracted")
    return True


# ─── Entry point ─────────────────────────────────────────────────────────────

def main():
    fitz = check_fitz()

    all_pdfs_mode = "--all-pdfs" in sys.argv
    given = [v for v in sys.argv[1:] if not v.startswith("--")]

    if all_pdfs_mode:
        # Convert all non-Core-Spec PDFs in every version subdirectory.
        # Skip: Core_v*.pdf (handled by convert_spec)
        # Skip: *showing_changes* / CS_*.pdf (redline diffs — visual markup lost in text extraction)
        def _is_showing_changes(p: Path) -> bool:
            s = p.stem.lower()
            return "showing_changes" in s or s.startswith("cs_")

        pdfs = sorted(
            p for p in SPECS_DIR.glob("*/*.pdf")
            if not p.stem.startswith("Core_v") and not _is_showing_changes(p)
        )
        print("=== Bluetooth Spec PDF → Markdown (supplemental PDFs) ===")
        print(f"Found {len(pdfs)} PDFs\n")
        ok, failed = [], []
        for pdf in pdfs:
            print(f"--- {pdf.parent.name}/{pdf.name} ---")
            if convert_pdf_file(pdf, fitz):
                ok.append(pdf.name)
            else:
                failed.append(pdf.name)
            print()
        print("=== Done ===")
        if ok:
            print(f"  Converted : {len(ok)} files")
        if failed:
            print(f"  Failed    : {', '.join(failed)}")
        return

    # Default mode: convert Core_v*.pdf by version number
    if given:
        versions = given
    else:
        versions = [
            pdf.parent.name
            for pdf in sorted(SPECS_DIR.glob("*/Core_v*.pdf"))
            if not (pdf.parent / f"Core_v{pdf.parent.name}.md").exists()
        ]

    if not versions:
        print("Nothing to convert — all PDFs already have .md counterparts.")
        sys.exit(0)

    print("=== Bluetooth Spec PDF → Markdown ===")
    print(f"Versions : {', '.join(versions)}\n")

    ok, failed = [], []
    for v in versions:
        print(f"--- {v} ---")
        if convert_spec(v, fitz):
            ok.append(v)
        else:
            failed.append(v)
        print()

    print("=== Done ===")
    if ok:
        print(f"  Converted : {', '.join(ok)}")
    if failed:
        print(f"  Skipped   : {', '.join(failed)}")
    print()
    print("Next: run `python scripts/ingest.py --status` to check wiki coverage.")


if __name__ == "__main__":
    main()
