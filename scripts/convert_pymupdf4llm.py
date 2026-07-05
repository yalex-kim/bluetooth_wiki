#!/usr/bin/env python3
"""
Alternative PDF → Markdown engine using PyMuPDF4LLM (2-pass hybrid).

Complements (does not replace) scripts/convert_to_md.py:

  convert_to_md.py       — custom caption-driven engine. Best for Core Specs:
                           semantic figure names (Vol{N}_Part{P}_Figure{X_Y}.png),
                           Vol/Part-aware headings, TOC skipping.
  convert_pymupdf4llm.py — generic layout-engine conversion for supplemental
                           PDFs (errata, profiles, test suites) and documents
                           whose formatting breaks the caption heuristics.

Design notes (validated on Core Spec v5.4, Vol 6 Part B, Figures 2.1–2.9):

  * The PUBLIC wrapper `pymupdf4llm.to_markdown` has a bug: it does not
    forward some keyword args (e.g. table_strategy=None) and mangles vector
    diagrams into fake markdown tables with mojibake. We therefore call the
    INTERNAL `pymupdf4llm.helpers.pymupdf_rag.to_markdown` per page.
  * Pass 1 (tables ON) runs per page with a crash-fallback strategy chain
    lines_strict → lines → None (works around an upstream find_tables
    ValueError on some pages).
  * Caption safety net: if a "Figure X.Y:" caption has a markdown table (a
    misdetected diagram) or nothing image-like directly above it, Pass 2
    (tables OFF) is run for that page and its figure image is merged in.
  * A quality-gate report (mojibake count, captions without images, strategy
    fallbacks) is printed per document — use it to decide when to escalate a
    document to a model-based converter (e.g. Marker) instead.

Output convention (identical to convert_to_md.py):
    {pdf_dir}/{stem}.md
    {pdf_dir}/{stem}_images/*.png

Usage:
    pip install pymupdf4llm

    python scripts/convert_pymupdf4llm.py path/to/file.pdf          # single PDF
    python scripts/convert_pymupdf4llm.py 6.0                        # Core spec version
    python scripts/convert_pymupdf4llm.py --all-pdfs                 # supplemental PDFs
    python scripts/convert_pymupdf4llm.py 6.0 --suffix .p4l          # keep both engines'
                                                                     # output side by side
    python scripts/convert_pymupdf4llm.py file.pdf --pages 2682-2695 # page range (0-based)
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SPECS_DIR = REPO_ROOT / "sources" / "specs"

FIG_CAP_RE = re.compile(r"^[_*]{0,2}\s*Figure\s+(\S+?)\s*[:：\-–]", re.IGNORECASE)
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
TBL_ROW_RE = re.compile(r"^\|.*\|\s*$")
_PICTURE_TEXT_RE = re.compile(
    r"<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->",
    re.DOTALL,
)
_BLANKS_RE = re.compile(r"\n{3,}")

STRATEGY_CHAIN = ("lines_strict", "lines", None)


def check_deps():
    try:
        import pymupdf
        from pymupdf4llm.helpers.pymupdf_rag import to_markdown
        return pymupdf, to_markdown
    except ImportError:
        print("ERROR: pymupdf4llm is not installed.\n  pip install pymupdf4llm")
        sys.exit(1)


# ─── Per-page conversion (internal API — see design notes) ───────────────────

def convert_page(core_md, doc, page_no: int, img_dir: Path, table_strategy):
    return core_md(
        doc, pages=[page_no], write_images=True, image_path=str(img_dir),
        image_format="png", dpi=150, table_strategy=table_strategy,
    )


def pass1_page(core_md, doc, page_no: int, img_dir: Path):
    """Tables-ON pass with crash-fallback chain. Returns (md, strategy_used)."""
    for strat in STRATEGY_CHAIN:
        try:
            return convert_page(core_md, doc, page_no, img_dir, strat), strat
        except Exception:
            continue
    return "", "failed"


# ─── Caption-aware merge helpers ─────────────────────────────────────────────

def find_caption_blocks(lines):
    for i, ln in enumerate(lines):
        m = FIG_CAP_RE.match(ln.strip())
        if m:
            yield i, m.group(1)


def preceding_block(lines, cap_idx):
    """Span + kind ('table'|'image'|'text'|None) of nearest block above caption."""
    j = cap_idx - 1
    while j >= 0 and not lines[j].strip():
        j -= 1
    if j < 0:
        return None, None
    if TBL_ROW_RE.match(lines[j]):
        end = j
        start = j
        while j >= 0 and (TBL_ROW_RE.match(lines[j]) or not lines[j].strip()):
            if TBL_ROW_RE.match(lines[j]):
                start = j
            j -= 1
        return (start, end), "table"
    if IMG_RE.search(lines[j]):
        return (j, j), "image"
    return (j, j), "text"


def image_for_caption(p2_lines, fig_id):
    """In pass-2 output, image link nearest above the matching caption."""
    for i, ln in enumerate(p2_lines):
        m = FIG_CAP_RE.match(ln.strip())
        if m and m.group(1) == fig_id:
            for j in range(i - 1, max(i - 15, -1), -1):
                im = IMG_RE.search(p2_lines[j])
                if im:
                    return im.group(1)
    return None


def merge_page(core_md, doc, page_no, l1, img_dir, stats):
    """Apply caption safety net; runs Pass 2 lazily only when needed."""
    caps = list(find_caption_blocks(l1))
    stats["captions_total"] += len(caps)
    if not caps:
        return l1

    l2 = None  # lazy pass-2

    def get_pass2():
        nonlocal l2
        if l2 is None:
            l2 = convert_page(core_md, doc, page_no, img_dir, None).splitlines()
        return l2

    # 1. Replace fake diagram-tables (bottom-up keeps indices valid)
    for cap_idx, fig_id in reversed(caps):
        span, kind = preceding_block(l1, cap_idx)
        if kind == "table":
            img = image_for_caption(get_pass2(), fig_id)
            if img:
                l1[span[0]:span[1] + 1] = [f"![Figure {fig_id}]({img})"]
                stats["fake_tables_replaced"] += 1

    # 2. Borrow an image for captions that still lack one
    for cap_idx, fig_id in reversed(list(find_caption_blocks(l1))):
        _, kind = preceding_block(l1, cap_idx)
        if kind != "image":
            img = image_for_caption(get_pass2(), fig_id)
            if img:
                l1.insert(cap_idx, f"![Figure {fig_id}]({img})")
                stats["images_borrowed"] += 1
            else:
                stats["captions_no_image"].append(fig_id)
    return l1


# ─── Post-processing ─────────────────────────────────────────────────────────

def postprocess(md: str, img_dir_name: str) -> str:
    """Strip picture-text noise, relativize image links, collapse blanks."""
    md = _PICTURE_TEXT_RE.sub("", md)
    md = re.sub(
        r"!\[([^\]]*)\]\([^)]*[/\\]([^/\\)]+\.(?:png|jpg|jpeg))\)",
        rf"![\1]({img_dir_name}/\2)",
        md,
    )
    md = _BLANKS_RE.sub("\n\n", md)
    return md.strip() + "\n"


# ─── Document conversion ─────────────────────────────────────────────────────

def convert_one(pdf_path: Path, pymupdf, core_md,
                suffix: str = "", pages=None) -> bool:
    stem = pdf_path.stem + suffix
    md_path = pdf_path.parent / f"{stem}.md"
    img_dir = pdf_path.parent / f"{stem}_images"

    if md_path.exists():
        print(f"  [SKIP] {md_path.name} already exists. Delete to reconvert.")
        return True

    size_kb = pdf_path.stat().st_size // 1024
    size_str = f"{size_kb // 1024} MB" if size_kb >= 1024 else f"{size_kb} KB"
    print(f"  Converting {pdf_path.name} ({size_str}) via PyMuPDF4LLM hybrid ...")

    try:
        doc = pymupdf.open(str(pdf_path))
    except Exception as e:
        print(f"  [FAIL] cannot open {pdf_path.name}: {e}")
        return False

    img_dir.mkdir(exist_ok=True)
    page_list = pages if pages is not None else range(len(doc))

    stats = {
        "captions_total": 0, "fake_tables_replaced": 0, "images_borrowed": 0,
        "captions_no_image": [], "fallbacks": [], "failed_pages": [],
    }
    out_pages = []
    total = len(page_list) if hasattr(page_list, "__len__") else len(doc)

    for n, p in enumerate(page_list):
        if n % 200 == 0 and n > 0:
            print(f"    {n:,}/{total:,} pages ...")
        md1, strat = pass1_page(core_md, doc, p, img_dir)
        if strat == "failed":
            stats["failed_pages"].append(p + 1)
            continue
        if strat != "lines_strict":
            stats["fallbacks"].append((p + 1, str(strat)))
        lines = merge_page(core_md, doc, p, md1.splitlines(), img_dir, stats)
        out_pages.append("\n".join(lines))

    doc.close()

    merged = "\n\n".join(out_pages)
    header = (
        f"# {pdf_path.stem.replace('_', ' ')}\n\n"
        "> Source: PDF converted via PyMuPDF4LLM (2-pass hybrid engine).\n\n"
        "---\n\n"
    )
    body = postprocess(merged, img_dir.name)
    md_path.write_text(header + body, encoding="utf-8")

    # ── Quality-gate report ──────────────────────────────────────────────
    mojibake = body.count("\ufffd")
    n_imgs = len(list(img_dir.glob("*")))
    print(f"  [OK] {md_path.name}: {len(body.splitlines()):,} lines | {n_imgs} images")
    print(f"       figures: {stats['captions_total']} captions | "
          f"{stats['fake_tables_replaced']} fake tables replaced | "
          f"{stats['images_borrowed']} images borrowed")
    gate_fail = []
    if mojibake:
        gate_fail.append(f"mojibake chars: {mojibake}")
    if stats["captions_no_image"]:
        gate_fail.append(f"captions w/o image: {stats['captions_no_image'][:10]}")
    if stats["failed_pages"]:
        gate_fail.append(f"failed pages: {stats['failed_pages'][:10]}")
    if stats["fallbacks"]:
        print(f"       strategy fallbacks: {stats['fallbacks'][:5]}")
    if gate_fail:
        print("  [QUALITY GATE] " + " | ".join(gate_fail))
        print("       → consider escalating this document to a model-based "
              "converter (e.g. Marker).")
    return True


# ─── Entry point ─────────────────────────────────────────────────────────────

def parse_pages(spec: str):
    """'2682-2695' or '5,7,9' → list of 0-based page numbers."""
    if "-" in spec:
        a, b = spec.split("-", 1)
        return list(range(int(a), int(b) + 1))
    return [int(x) for x in spec.split(",")]


def main():
    pymupdf, core_md = check_deps()

    args = sys.argv[1:]
    all_pdfs_mode = "--all-pdfs" in args
    suffix, pages = "", None
    if "--suffix" in args:
        i = args.index("--suffix")
        suffix = args[i + 1]
        del args[i:i + 2]
    if "--pages" in args:
        i = args.index("--pages")
        pages = parse_pages(args[i + 1])
        del args[i:i + 2]
    positional = [a for a in args if not a.startswith("--")]

    targets: list[Path] = []
    if all_pdfs_mode:
        # Same skip rules as convert_to_md.py --all-pdfs
        def _is_showing_changes(p: Path) -> bool:
            s = p.stem.lower()
            return "showing_changes" in s or s.startswith("cs_")

        targets = sorted(
            p for p in SPECS_DIR.glob("*/*.pdf")
            if not p.stem.startswith("Core_v") and not _is_showing_changes(p)
        )
    else:
        for a in positional:
            p = Path(a)
            if p.suffix.lower() == ".pdf" and p.exists():
                targets.append(p)
            elif (SPECS_DIR / a / f"Core_v{a}.pdf").exists():
                targets.append(SPECS_DIR / a / f"Core_v{a}.pdf")
            else:
                print(f"  [WARN] not found: {a}")

    if not targets:
        print("Nothing to convert. Pass a PDF path, a version number, or --all-pdfs.")
        sys.exit(0)

    print("=== PDF → Markdown (PyMuPDF4LLM 2-pass hybrid engine) ===")
    print(f"Targets : {len(targets)} file(s)\n")

    ok, failed = [], []
    for pdf in targets:
        print(f"--- {pdf.parent.name}/{pdf.name} ---")
        (ok if convert_one(pdf, pymupdf, core_md, suffix, pages)
         else failed).append(pdf.name)
        print()

    print("=== Done ===")
    if ok:
        print(f"  Converted : {len(ok)} files")
    if failed:
        print(f"  Failed    : {', '.join(failed)}")


if __name__ == "__main__":
    main()
