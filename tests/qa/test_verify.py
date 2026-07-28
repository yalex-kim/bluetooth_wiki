from qa.retrieval.actions import Evidence
from qa.verify import verify_citations

OBSERVED = [
    Evidence(ref_id="core-6.0#4.5::s0", doc="Core Spec v6.0", section="4.5", page=512,
             path="sources/specs/6.0/Core_v6.0.md", kind="chunk", text="..."),
    Evidence(ref_id="core-6.0:table:1", doc="Core Spec v6.0", section="4.5", page=512,
             path="sources/specs/6.0/Core_v6.0.md", kind="table", text="..."),
]


def test_citation_matching_observed_evidence_is_kept_and_enriched():
    out = verify_citations([{"doc": "Core Spec v6.0", "section": "4.5"}], OBSERVED)
    assert out.dropped == []
    assert out.citations[0]["page"] == 512
    assert out.citations[0]["path"].endswith("Core_v6.0.md")


def test_citation_with_no_observed_evidence_is_dropped():
    out = verify_citations([{"doc": "Core Spec v6.0", "section": "9.9"}], OBSERVED)
    assert out.citations == [] and len(out.dropped) == 1


def test_section_matching_is_tolerant_of_formatting():
    out = verify_citations([{"doc": "core spec v6.0", "section": "§4.5"}], OBSERVED)
    assert len(out.citations) == 1


def test_duplicate_citations_collapse():
    claimed = [{"doc": "Core Spec v6.0", "section": "4.5"}] * 3
    assert len(verify_citations(claimed, OBSERVED).citations) == 1


def test_no_observed_evidence_drops_everything():
    out = verify_citations([{"doc": "Core Spec v6.0", "section": "4.5"}], [])
    assert out.citations == [] and len(out.dropped) == 1


def test_a_bare_ref_id_also_resolves():
    out = verify_citations([{"ref_id": "core-6.0:table:1"}], OBSERVED)
    assert len(out.citations) == 1 and out.citations[0]["section"] == "4.5"
