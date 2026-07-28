from qa import ontology
from qa.llm import validate


def test_core_entity_types_cover_section_5_2():
    for t in ["Procedure", "State", "Event", "PDU", "Parameter", "Timer",
              "ErrorCode", "Role", "Layer", "Profile", "Characteristic"]:
        assert t in ontology.CORE_ENTITY_TYPES


def test_relation_types_include_amends_for_errata():
    for r in ["triggers", "requires", "definedIn", "partOf", "mandatoryFor",
              "optionalFor", "supersedes", "references", "amends"]:
        assert ontology.is_valid_relation(r)
    assert not ontology.is_valid_relation("causes")


def test_mesh_extension_types_only_valid_for_mesh():
    assert ontology.is_valid_node_type("Model", doc_type="Mesh")
    assert not ontology.is_valid_node_type("Model", doc_type="Core")
    assert ontology.is_valid_node_type("Codec", doc_type="LEAudio")


def test_extraction_schema_constrains_types_to_the_doc_type():
    schema = ontology.extraction_schema("Mesh")
    node_enum = schema["properties"]["entities"]["items"]["properties"]["type"]["enum"]
    assert "Model" in node_enum and "Codec" not in node_enum
    # a payload using a valid Mesh type validates; an invalid one does not
    ok = {"entities": [{"name": "Config Server", "type": "Model"}],
          "relations": [{"source": "Config Server", "target": "Element",
                         "type": "partOf"}]}
    assert validate(ok, schema) == []
    bad = {"entities": [{"name": "x", "type": "Codec"}], "relations": []}
    assert validate(bad, schema) != []
