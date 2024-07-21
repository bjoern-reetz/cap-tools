from collections.abc import Iterator
from dataclasses import dataclass, field

from cap_tools.models import Alert, MsgType, Reference
from cap_tools.models import Area as Area
from cap_tools.models import Category as Category
from cap_tools.models import Certainty as Certainty
from cap_tools.models import EventCode as EventCode
from cap_tools.models import Geocode as Geocode
from cap_tools.models import Info as Info
from cap_tools.models import Parameter as Parameter
from cap_tools.models import Resource as Resource
from cap_tools.models import ResponseType as ResponseType
from cap_tools.models import Scope as Scope
from cap_tools.models import Severity as Severity
from cap_tools.models import Status as Status
from cap_tools.models import Urgency as Urgency
from cap_tools.models import Value as Value
from cap_tools.models import ValueName as ValueName


@dataclass(slots=True)
class AlertState:
    _alerts: dict[Reference, Alert] = field(
        init=False, repr=False, default_factory=dict
    )

    @property
    def alerts(self) -> list[Alert]:
        return list(self._alerts.values())

    def ingest(self, alert: Alert, /) -> None:
        self._alerts[Reference.from_alert(alert)] = alert
        match alert.msg_type:
            case MsgType.UPDATE | MsgType.CANCEL:
                for reference in alert.references_to_list():
                    del self._alerts[reference]
            case _:
                pass

    def __iter__(self) -> Iterator[Alert]:
        return iter(self._alerts.values())
