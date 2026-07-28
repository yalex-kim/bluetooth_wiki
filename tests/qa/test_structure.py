from qa.ingest import structure

SAMPLE = """# Core Specification

## 4 LINK LAYER SPECIFICATION

Intro paragraph for chapter 4.

### 4.5 CONNECTION STATE

The Link Layer enters the Connection State. See Section 4.5.2 for timing.

| Parameter | Min | Max |
|---|---|---|
| connInterval | 7.5 ms | 4 s |

Table 4.1: Connection parameters

### 4.5.2 CONNECTION TIMING

![Figure 4.3](Core_v6.0_images/Vol6_PartB_Figure4_3.png)

Figure 4.3: Connection event timing

Timing is derived from connInterval as shown in Figure 4.3.
"""


def _parse():
    return structure.parse_markdown(SAMPLE, doc_id="core-6.0", title="Core 6.0",
                                    doc_type="Core", version="6.0")


def test_headings_become_a_parent_linked_section_tree():
    doc = _parse()
    by_number = {s.number: s for s in doc.sections}
    assert set(by_number) >= {"4", "4.5", "4.5.2"}
    assert by_number["4.5"].parent_id == by_number["4"].id
    assert by_number["4.5.2"].parent_id == by_number["4.5"].id
    assert by_number["4.5"].title == "CONNECTION STATE"


def test_section_text_excludes_nested_subsection_bodies():
    doc = _parse()
    ch4 = next(s for s in doc.sections if s.number == "4")
    assert "Intro paragraph" in ch4.text
    assert "CONNECTION TIMING" not in ch4.text


def test_tables_are_captured_as_their_own_nodes_with_markdown_preserved():
    doc = _parse()
    assert len(doc.tables) == 1
    tbl = doc.tables[0]
    assert tbl.caption.startswith("Table 4.1")
    assert "connInterval" in tbl.markdown and "| Parameter |" in tbl.markdown
    assert tbl.section_id == next(s for s in doc.sections if s.number == "4.5").id


def test_figures_capture_image_path_and_caption():
    doc = _parse()
    assert len(doc.figures) == 1
    fig = doc.figures[0]
    assert fig.image_path.endswith("Vol6_PartB_Figure4_3.png")
    assert fig.caption.startswith("Figure 4.3")
    assert fig.section_id == next(s for s in doc.sections if s.number == "4.5.2").id


def test_crossrefs_extracted_for_sections_and_figures():
    doc = _parse()
    targets = {(c.target_kind, c.target_ref) for c in doc.crossrefs}
    assert ("section", "4.5.2") in targets
    assert ("figure", "4.3") in targets


def test_section_hash_is_stable_and_text_sensitive():
    doc = _parse()
    s = doc.sections[0]
    assert structure.section_hash(s) == structure.section_hash(s)
    other = structure.SectionNode(**{**s.__dict__, "text": s.text + " changed"})
    assert structure.section_hash(other) != structure.section_hash(s)
