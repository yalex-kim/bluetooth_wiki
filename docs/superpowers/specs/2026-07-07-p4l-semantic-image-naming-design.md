# Semantic image naming for the PyMuPDF4LLM converter

**Date**: 2026-07-07
**Status**: Approved

## Problem

`scripts/convert_pymupdf4llm.py` (the 2-pass hybrid engine) writes figure
images with PyMuPDF4LLM's default names, `Core_v<version>.pdf-<page>-<idx>.png`
(e.g. `Core_v6.3.pdf-230-0.png`). The primary Core-spec converter,
`scripts/convert_to_md.py`, instead uses **semantic** names:
`Vol{N}_Part{P}_Figure{X_Y}.png` (e.g. `Vol1_PartA_Figure1_1.png`), falling
back to `Figure{X_Y}.png` when the Volume/Part is unknown.

Because the two engines can produce output for the same document (the p4l
engine is used with `--suffix` for side-by-side comparison, and as a fallback
for documents the primary engine mishandles), their image names must follow
the same convention. Today they don't, which breaks cross-engine comparison
and any tooling (e.g. the chunker's `Vol{N}_Part{P}_Figure` figure-reference
signal) that relies on semantic names.

## Goal

Make `convert_pymupdf4llm.py` emit figure images under the same
`Vol{N}_Part{P}_Figure{X_Y}.png` convention as `convert_to_md.py`, while
preserving images that have no figure caption (PyMuPDF4LLM extracts every
image on a page; the primary engine renders only captioned figures).

## Naming rules

For each image the converter emits:

| Case | Vol/Part known | Vol/Part unknown |
|------|----------------|------------------|
| Has a `Figure X.Y` caption | `Vol{N}_Part{P}_Figure{X_Y}.png` | `Figure{X_Y}.png` |
| No figure caption | `Vol{N}_Part{P}_Image_p{page}_{idx}.png` | `Image_p{page}_{idx}.png` |

- `X_Y` is the figure number with dots replaced by underscores (matches
  `convert_to_md.py`).
- `page` is the 0-based absolute PDF page index; `idx` is PyMuPDF4LLM's
  per-page image index. Both are parsed from the original filename
  (`...-<page>-<idx>.png`), which guarantees uniqueness for un-captioned
  images.
- Captioned images keep the primary engine's exact convention so the two
  engines' figure names match.

## Approach

**Post-pass rename after conversion** (chosen). PyMuPDF4LLM writes images and
the markdown links during `convert_page`; after the whole document is
converted and `postprocess` has run, a single pass over the final markdown
renames each image file on disk and rewrites its link. This keeps the
delicate pass-1 / pass-2 / caption-merge logic untouched and isolates the new
behavior in one testable function.

Rejected alternatives:
- **Assign names during `merge_page`.** Would entangle naming with the
  caption-merge logic, and images not routed through `merge_page` (already
  present in pass-1 output) would still need a separate pass. More invasive,
  no benefit.
- **Intercept PyMuPDF4LLM's image writing.** The public `to_markdown` API
  offers no filename hook; not feasible without forking the library.

## Components

1. **Reuse `build_vol_part_map(doc)` from `convert_to_md.py`** — maps 0-based
   page index → `(vol:int|None, part:str|None)` by walking the PDF's TOC
   bookmarks. It is import-safe (`convert_to_md.py` has only imports,
   constants, and regex at module scope; `check_fitz()` runs inside a
   function; a `__main__` guard wraps its CLI). `convert_pymupdf4llm.py` will
   `from convert_to_md import build_vol_part_map` (both live in `scripts/`,
   which is on `sys.path[0]` when either is run as a script).

2. **New function** `rename_images_semantically(md_text, img_dir, vol_part_map)
   -> str`:
   - Find every image link via the module's existing `IMG_RE`
     (`!\[[^\]]*\]\(([^)]+)\)`).
   - Parse `page` and `idx` from the on-disk filename tail
     (`-(\d+)-(\d+)\.png$`); if it doesn't match, leave the link unchanged.
   - Resolve the figure number: first from the link's alt text
     (`![Figure X.Y](...)`, set by `merge_page`), else by scanning the next
     few non-blank lines after the image for a `Figure X.Y` caption using the
     module's existing `FIG_CAP_RE`.
   - Compute the target name per the rules table; look up Vol/Part from
     `vol_part_map[page]`.
   - Rename the file on disk (on name collision, append `_2`, `_3`, …) and
     rewrite the markdown link to the new `img_dir.name/<newname>` path.
   - Guard: if the source file is missing, leave the link as-is.

3. **Call site**: in `convert_one`, after `body = postprocess(...)` and before
   `md_path.write_text(...)`, compute `vol_part_map = build_vol_part_map(doc)`
   (while `doc` is still open — move the `doc.close()` accordingly) and run
   the rename pass on `body`.

## Edge cases

- Filename not matching `-<page>-<idx>.png` → link left unchanged (defensive;
  covers any future PyMuPDF4LLM naming change).
- Missing source file on disk → link left unchanged.
- Table-of-Figures pages (3+ captions) already have their images suppressed
  by the existing merge logic, so no special handling is needed here.
- Name collisions (two images resolving to the same target) → numeric
  disambiguation suffix, so no file is silently overwritten.

## Testing

No PDF is required — the rename function is pure over (markdown, image
directory, vol/part map). A focused unit test creates a temp `img_dir` with
a few dummy PNG files and a synthetic markdown body, then asserts:
- a captioned image with a known Vol/Part → `Vol{N}_Part{P}_Figure{X_Y}.png`,
  link updated;
- a captioned image with unknown Vol/Part → `Figure{X_Y}.png`;
- an un-captioned image → `Vol{N}_Part{P}_Image_p{page}_{idx}.png`;
- an image whose file is missing → link unchanged;
- the renamed files exist on disk and the old names do not.

## Non-goals

- No change to the primary `convert_to_md.py` engine.
- No change to the p4l engine's text extraction, caption merging, or
  quality-gate reporting — only image file naming.
- No re-run of any conversion as part of this change (the existing p4l test
  artifacts under `sources/specs/6.3/` are incidental).
