import sys
from pathlib import Path

import pytest

# scripts/ is not a package; put it on sys.path so we can import the module.
SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))

# pymupdf4llm is an import-time dependency of the module under test.
pytest.importorskip("pymupdf4llm")

import convert_pymupdf4llm as p4l  # noqa: E402


def _touch(path):
    path.write_bytes(b"\x89PNG\r\n\x1a\n")  # minimal PNG signature; content irrelevant


def test_rename_covers_all_cases(tmp_path):
    img_dir = tmp_path / "Core_v9.9.p4l_images"
    img_dir.mkdir()
    # Four extracted images (names as PyMuPDF4LLM writes them):
    _touch(img_dir / "Core_v9.9.pdf-230-0.png")   # captioned, vol/part known
    _touch(img_dir / "Core_v9.9.pdf-238-0.png")   # un-captioned, vol/part known
    _touch(img_dir / "Core_v9.9.pdf-500-1.png")   # captioned, vol/part UNKNOWN
    # note: page 999 file intentionally absent -> link must stay unchanged

    md = "\n".join([
        "![Figure 1.1](Core_v9.9.p4l_images/Core_v9.9.pdf-230-0.png)",
        "",
        "_Figure 1.1: Host and Controller_",
        "",
        "![](Core_v9.9.p4l_images/Core_v9.9.pdf-238-0.png)",
        "",
        "Some body text with no figure caption here.",
        "",
        "![](Core_v9.9.p4l_images/Core_v9.9.pdf-500-1.png)",
        "",
        "_Figure 9.9: Orphaned volume figure_",
        "",
        "![](Core_v9.9.p4l_images/Core_v9.9.pdf-999-0.png)",
        "",
    ])
    vol_part_map = {230: (1, "A"), 238: (1, "A"), 500: (None, None), 999: (None, None)}

    out = p4l.rename_images_semantically(md, img_dir, vol_part_map)

    # Captioned + known vol/part.
    assert "Core_v9.9.p4l_images/Vol1_PartA_Figure1_1.png" in out
    assert (img_dir / "Vol1_PartA_Figure1_1.png").is_file()
    # Un-captioned + known vol/part.
    assert "Core_v9.9.p4l_images/Vol1_PartA_Image_p238_0.png" in out
    assert (img_dir / "Vol1_PartA_Image_p238_0.png").is_file()
    # Captioned + unknown vol/part -> figure-only fallback.
    assert "Core_v9.9.p4l_images/Figure9_9.png" in out
    assert (img_dir / "Figure9_9.png").is_file()
    # Missing source file -> link left untouched, no new file invented.
    assert "Core_v9.9.p4l_images/Core_v9.9.pdf-999-0.png" in out
    # Old names for the renamed files are gone.
    assert not (img_dir / "Core_v9.9.pdf-230-0.png").exists()
    assert not (img_dir / "Core_v9.9.pdf-238-0.png").exists()
    assert not (img_dir / "Core_v9.9.pdf-500-1.png").exists()


def test_collision_gets_disambiguated(tmp_path):
    img_dir = tmp_path / "imgs"
    img_dir.mkdir()
    _touch(img_dir / "Core_v9.9.pdf-10-0.png")
    _touch(img_dir / "Core_v9.9.pdf-11-0.png")
    md = "\n".join([
        "![Figure 2.1](imgs/Core_v9.9.pdf-10-0.png)",
        "![Figure 2.1](imgs/Core_v9.9.pdf-11-0.png)",
        "",
    ])
    vol_part_map = {10: (2, "B"), 11: (2, "B")}

    out = p4l.rename_images_semantically(md, img_dir, vol_part_map)

    assert (img_dir / "Vol2_PartB_Figure2_1.png").is_file()
    assert (img_dir / "Vol2_PartB_Figure2_1_2.png").is_file()
    assert "imgs/Vol2_PartB_Figure2_1.png" in out
    assert "imgs/Vol2_PartB_Figure2_1_2.png" in out
