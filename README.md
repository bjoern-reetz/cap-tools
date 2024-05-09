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
