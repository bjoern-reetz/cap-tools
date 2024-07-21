import pathlib

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from cap_tools.models import Alert


def test_reproduce_oasis_examples() -> None:
    parser = XmlParser()
    serializer = XmlSerializer(config=SerializerConfig(indent="  "))

    for example_path in pathlib.Path("data/oasis").iterdir():
        example_xml = example_path.read_text()

        alert = parser.parse(example_path, Alert)
        serialized_alert = serializer.render(  # pyright: ignore[reportUnknownMemberType]
            alert, ns_map={None: "urn:oasis:names:tc:emergency:cap:1.2"}
        )

        assert serialized_alert == example_xml


def test_multidict_oasis() -> None:
    parser = XmlParser()

    example_path = pathlib.Path("data/oasis/example2.xml")

    alert = parser.parse(example_path, Alert)
    geocodes_multidict = alert.infos[0].areas[0].geocodes_to_dict()

    assert geocodes_multidict["SAME"] == "006109"
    assert geocodes_multidict.getall("SAME") == ["006109", "006009", "006003"]


def test_references_oasis() -> None:
    parser = XmlParser()

    example_path = pathlib.Path("data/oasis/example3.xml")

    reference_str = "trinet@caltech.edu,TRI13970876.1,2003-06-11T20:30:00-07:00"
    alert = parser.parse(example_path, Alert)
    assert alert.references == reference_str

    references = list(alert.references_to_list())
    assert len(references) == 1
    assert str(references[0]) == reference_str

    sender, identifier, sent_str = reference_str.split(",")
    assert references[0] == (sender, identifier, XmlDateTime.from_string(sent_str))
