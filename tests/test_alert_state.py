import hypothesis.strategies as st
from hypothesis import given

from cap_tools import AlertState
from cap_tools.models import Alert, MsgType, Reference

from . import strategies as custom_st


@given(alerts=st.lists(custom_st.alerts()))
def test_alert_collection_holds_unrelated_alerts(alerts: list[Alert]) -> None:
    alert_collection = AlertState()
    for alert in alerts:
        alert_collection.ingest(alert)
    assert alerts == list(alert_collection)


@given(
    alerts=custom_st.alerts().flatmap(
        lambda alert: st.tuples(
            st.just(alert),
            custom_st.alerts(
                msg_type=st.just(MsgType.UPDATE),
                references=st.just(str(Reference.from_alert(alert))),
            ),
        )
    )
)
def test_alert_collection_replaces_updated_alerts(alerts: tuple[Alert, Alert]) -> None:
    alert, update = alerts

    alert_collection = AlertState()
    alert_collection.ingest(alert)
    assert alert in alert_collection

    alert_collection.ingest(update)

    assert alert not in alert_collection
    assert update in alert_collection
