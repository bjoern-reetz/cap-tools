# CAP-Tools

Python data bindings for the [Common Alerting Protocol Version 1.2](https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.html).

## Getting started

This package contains a Python model for CAP XML documents that was generated using using [xsData](https://xsdata.readthedocs.io/).

To parse a CAP XML from a file into an instance of `cappy.models.Alert`, do as follows:

```python
from cappy.models import Alert
from xsdata.formats.dataclass.parsers import XmlParser

parser = XmlParser()
alert = parser.parse("path/to/my/cap.xml", Alert)
```

For advanced usage, just take a look at the [xsData](https://xsdata.readthedocs.io/en/latest/data_binding/basics/) docs.

## Limitations

While this library is fully typed to enable Python type safety, it currently does neither implement the pattern restrictions from the [CAP v1.2 XSD specification](./CAP-v1.2.xsd) (i.e. the pattern restriction for the XmlDateTime fields) nor the additional restrictions imposed by the [normative alert message structure](https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.html#_Toc454352650) (e.g. Alert.identifier must not include spaces, commas or the characters "<" and "&").

This does not matter much when using this library for reading CAP messages - but when you are using this library to create CAP messages, **you are responsible** for respecting those additional restrictions yourself!
