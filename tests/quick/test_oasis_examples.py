import pathlib

from cap_tools.models import Alert
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


def test_reproduce_oasis_examples():
    parser = XmlParser()
    serializer = XmlSerializer(config=SerializerConfig(indent="  "))

    for example_path in pathlib.Path("data/oasis").iterdir():
        example_xml = example_path.read_text()

        alert = parser.parse(example_path, Alert)
        serialized_alert = serializer.render(
            alert, ns_map={None: "urn:oasis:names:tc:emergency:cap:1.2"}
        )

        assert serialized_alert == example_xml
