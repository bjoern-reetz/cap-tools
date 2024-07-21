from pathlib import Path

from hypothesis import settings
from xsdata.formats.dataclass.parsers import XmlParser

from cap_tools.models import Alert

settings.register_profile("fast", max_examples=10)
settings.register_profile("pre-bump")


def parser() -> XmlParser:
    return XmlParser()


def oasis_xml_paths() -> list[Path]:
    return [
        Path("data/oasis/example1.xml"),
        Path("data/oasis/example2.xml"),
        Path("data/oasis/example3.xml"),
        Path("data/oasis/example4.xml"),
    ]


def oasis_alerts(parser: XmlParser, oasis_xml_paths: list[Path]) -> list[Alert]:
    return [parser.parse(path, Alert) for path in oasis_xml_paths]
