from collections.abc import Mapping
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from multidict import MultiDict
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:oasis:names:tc:emergency:cap:1.2"
DEFAULT_LANGUAGE = "en-US"


class Category(Enum):
    GEO = "Geo"
    MET = "Met"
    SAFETY = "Safety"
    SECURITY = "Security"
    RESCUE = "Rescue"
    FIRE = "Fire"
    HEALTH = "Health"
    ENV = "Env"
    TRANSPORT = "Transport"
    INFRA = "Infra"
    CBRNE = "CBRNE"
    OTHER = "Other"


class Certainty(Enum):
    OBSERVED = "Observed"
    LIKELY = "Likely"
    POSSIBLE = "Possible"
    UNLIKELY = "Unlikely"
    UNKNOWN = "Unknown"


@dataclass(slots=True, kw_only=True)
class Resource:
    class Meta:
        global_type = False

    resource_desc: str = field(
        metadata={
            "name": "resourceDesc",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    mime_type: str = field(
        metadata={
            "name": "mimeType",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    size: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    uri: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    deref_uri: str | None = field(
        default=None,
        metadata={
            "name": "derefUri",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    digest: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )


class ResponseType(Enum):
    SHELTER = "Shelter"
    EVACUATE = "Evacuate"
    PREPARE = "Prepare"
    EXECUTE = "Execute"
    AVOID = "Avoid"
    MONITOR = "Monitor"
    ASSESS = "Assess"
    ALL_CLEAR = "AllClear"
    NONE = "None"


class Severity(Enum):
    EXTREME = "Extreme"
    SEVERE = "Severe"
    MODERATE = "Moderate"
    MINOR = "Minor"
    UNKNOWN = "Unknown"


class Urgency(Enum):
    IMMEDIATE = "Immediate"
    EXPECTED = "Expected"
    FUTURE = "Future"
    PAST = "Past"
    UNKNOWN = "Unknown"


class MsgType(Enum):
    ALERT = "Alert"
    UPDATE = "Update"
    CANCEL = "Cancel"
    ACK = "Ack"
    ERROR = "Error"


class Scope(Enum):
    PUBLIC = "Public"
    RESTRICTED = "Restricted"
    PRIVATE = "Private"


class Status(Enum):
    ACTUAL = "Actual"
    EXERCISE = "Exercise"
    SYSTEM = "System"
    TEST = "Test"
    DRAFT = "Draft"


@dataclass(slots=True)
class Value:
    class Meta:
        name = "value"
        namespace = "urn:oasis:names:tc:emergency:cap:1.2"

    value: str = field(
        metadata={
            "required": True,
        },
    )


@dataclass(slots=True)
class ValueName:
    class Meta:
        name = "valueName"
        namespace = "urn:oasis:names:tc:emergency:cap:1.2"

    value: str = field(
        metadata={
            "required": True,
        },
    )


@dataclass(slots=True)
class Geocode:
    class Meta:
        global_type = False

    value_name: ValueName = field(
        metadata={
            "name": "valueName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    value: Value = field(
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )


@dataclass(slots=True)
class EventCode:
    class Meta:
        global_type = False

    value_name: ValueName = field(
        metadata={
            "name": "valueName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    value: Value = field(
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )


@dataclass(slots=True)
class Parameter:
    class Meta:
        global_type = False

    value_name: ValueName = field(
        metadata={
            "name": "valueName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    value: Value = field(
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )


@dataclass(slots=True, kw_only=True)
class Area:
    class Meta:
        global_type = False

    area_desc: str = field(
        metadata={
            "name": "areaDesc",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    polygons: list[str] = field(
        default_factory=list,
        metadata={
            "name": "polygon",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    circles: list[str] = field(
        default_factory=list,
        metadata={
            "name": "circle",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    geocodes: list[Geocode] = field(
        default_factory=list,
        metadata={
            "name": "geocode",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    altitude: Decimal | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    ceiling: Decimal | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )

    def geocodes_to_dict(self) -> MultiDict[str, str]:
        """Return the Area.geocodes as a MultiDict."""
        return MultiDict(
            (geocode.value_name.value, geocode.value.value) for geocode in self.geocodes
        )

    def geocodes_from_dict(self, geocodes: Mapping[str, str]) -> None:
        """Overwrite Area.geocodes with values derived from the given mapping (e.g. dict or MultiDict)."""
        self.geocodes = [
            Geocode(ValueName(name), Value(value)) for name, value in geocodes.items()
        ]


@dataclass(slots=True, kw_only=True)
class Info:
    class Meta:
        global_type = False

    language: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    categories: list[Category] = field(
        default_factory=list,
        metadata={
            "name": "category",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "min_occurs": 1,
        },
    )
    event: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    response_types: list[ResponseType] = field(
        default_factory=list,
        metadata={
            "name": "responseType",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    urgency: Urgency = field(
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    severity: Severity = field(
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    certainty: Certainty = field(
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
            "required": True,
        }
    )
    audience: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    event_codes: list[EventCode] = field(
        default_factory=list,
        metadata={
            "name": "eventCode",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    effective: XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    onset: XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    expires: XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    sender_name: str | None = field(
        default=None,
        metadata={
            "name": "senderName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    headline: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    instruction: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    web: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    contact: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    parameters: list[Parameter] = field(
        default_factory=list,
        metadata={
            "name": "parameter",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    resources: list[Resource] = field(
        default_factory=list,
        metadata={
            "name": "resource",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )
    areas: list[Area] = field(
        default_factory=list,
        metadata={
            "name": "area",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:emergency:cap:1.2",
        },
    )

    def get_language(self) -> str:
        """Get the language of this Info.

        If the language is not explicitly set,
        "en-US" is returned as per CAP spec v1.2.
        """
        return DEFAULT_LANGUAGE if self.language is None else self.language

    def set_language(self, language: str | None) -> None:
        """Set the language of this Info.

        Using this method to set the language to the default language (i.e. passing "en-US" as argument)
        will set `Info.language` to `None`. Retrieving the language then via `Info.get_language`
        will correctly return "en-US".

        If you want to set the language to 'en-US' explicitly, use `Info.language = "en-US"` instead.
        """
        self.language = None if language == DEFAULT_LANGUAGE else language

    def event_codes_to_dict(self) -> MultiDict[str, str]:
        return MultiDict(
            (event_code.value_name.value, event_code.value.value)
            for event_code in self.event_codes
        )

    def event_codes_from_dict(self, event_codes: Mapping[str, str]) -> None:
        self.event_codes = [
            EventCode(ValueName(name), Value(value))
            for name, value in event_codes.items()
        ]

    def parameters_to_dict(self) -> MultiDict[str, str]:
        return MultiDict(
            (parameter.value_name.value, parameter.value.value)
            for parameter in self.parameters
        )

    def parameters_from_dict(self, parameters: Mapping[str, str]) -> None:
        self.parameters = [
            Parameter(ValueName(name), Value(value))
            for name, value in parameters.items()
        ]


@dataclass(slots=True, kw_only=True)
class Alert:
    """
    CAP Alert Message (version 1.2)
    """

    class Meta:
        name = "alert"
        namespace = "urn:oasis:names:tc:emergency:cap:1.2"

    identifier: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    sender: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    sent: XmlDateTime = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: Status = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    msg_type: MsgType = field(
        metadata={
            "name": "msgType",
            "type": "Element",
            "required": True,
        }
    )
    source: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scope: Scope = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    restriction: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    addresses: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    codes: list[str] = field(
        default_factory=list,
        metadata={
            "name": "code",
            "type": "Element",
        },
    )
    note: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    references: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    incidents: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    infos: list[Info] = field(
        default_factory=list,
        metadata={
            "name": "info",
            "type": "Element",
        },
    )
    _signatures: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
