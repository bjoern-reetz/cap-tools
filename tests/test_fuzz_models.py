import decimal

import xsdata.models.datatype
from hypothesis import given
from hypothesis import strategies as st
from xsdata.models.datatype import XmlDateTime

import cap_tools
import cap_tools.models
from cap_tools.models import EventCode, Geocode, Parameter, Resource, Value, ValueName


@given(
    identifier=st.text(),
    sender=st.text(),
    sent=st.builds(
        XmlDateTime,
        day=st.integers(),
        fractional_second=st.integers(),
        hour=st.integers(),
        minute=st.integers(),
        month=st.integers(),
        offset=st.one_of(st.none(), st.integers()),
        second=st.integers(),
        year=st.integers(),
    ),
    status=st.sampled_from(cap_tools.models.Status),
    msg_type=st.sampled_from(cap_tools.models.MsgType),
    source=st.one_of(st.none(), st.text()),
    scope=st.sampled_from(cap_tools.models.Scope),
    restriction=st.one_of(st.none(), st.text()),
    addresses=st.one_of(st.none(), st.text()),
    codes=st.lists(st.text()),
    note=st.one_of(st.none(), st.text()),
    references=st.one_of(st.none(), st.text()),
    incidents=st.one_of(st.none(), st.text()),
    infos=st.from_type(list[cap_tools.models.Info]),
)
def test_fuzz_alert(  # noqa: PLR0913
    identifier: str,
    sender: str,
    sent: xsdata.models.datatype.XmlDateTime,
    status: cap_tools.Status,
    msg_type: cap_tools.MsgType,
    source: str | None,
    scope: cap_tools.Scope,
    restriction: str | None,
    addresses: str | None,
    codes: list[str],
    note: str | None,
    references: str | None,
    incidents: str | None,
    infos: list[cap_tools.models.Info],
) -> None:
    _ = cap_tools.models.Alert(
        identifier=identifier,
        sender=sender,
        sent=sent,
        status=status,
        msg_type=msg_type,
        source=source,
        scope=scope,
        restriction=restriction,
        addresses=addresses,
        codes=codes,
        note=note,
        references=references,
        incidents=incidents,
        infos=infos,
    )


@given(
    area_desc=st.text(),
    polygons=st.lists(st.text()),
    circles=st.lists(st.text()),
    geocodes=st.lists(
        st.builds(
            Geocode,
            value=st.builds(Value, value=st.text()),
            value_name=st.builds(ValueName, value=st.text()),
        )
    ),
    altitude=st.one_of(st.none(), st.decimals()),
    ceiling=st.one_of(st.none(), st.decimals()),
)
def test_fuzz_area(  # noqa: PLR0913
    area_desc: str,
    polygons: list[str],
    circles: list[str],
    geocodes: list[cap_tools.models.Geocode],
    altitude: decimal.Decimal | None,
    ceiling: decimal.Decimal | None,
) -> None:
    _ = cap_tools.models.Area(
        area_desc=area_desc,
        polygons=polygons,
        circles=circles,
        geocodes=geocodes,
        altitude=altitude,
        ceiling=ceiling,
    )


@given(
    value_name=st.builds(ValueName, value=st.text()),
    value=st.builds(Value, value=st.text()),
)
def test_fuzz_event_code(
    value_name: cap_tools.models.ValueName, value: cap_tools.models.Value
) -> None:
    _ = cap_tools.models.EventCode(value_name=value_name, value=value)


@given(
    value_name=st.builds(ValueName, value=st.text()),
    value=st.builds(Value, value=st.text()),
)
def test_fuzz_geocode(
    value_name: cap_tools.models.ValueName, value: cap_tools.models.Value
) -> None:
    _ = cap_tools.models.Geocode(value_name=value_name, value=value)


@given(
    language=st.one_of(st.none(), st.text()),
    categories=st.lists(st.sampled_from(cap_tools.models.Category)),
    event=st.text(),
    response_types=st.lists(st.sampled_from(cap_tools.models.ResponseType)),
    urgency=st.sampled_from(cap_tools.models.Urgency),
    severity=st.sampled_from(cap_tools.models.Severity),
    certainty=st.sampled_from(cap_tools.models.Certainty),
    audience=st.one_of(st.none(), st.text()),
    event_codes=st.lists(
        st.builds(
            EventCode,
            value=st.builds(Value, value=st.text()),
            value_name=st.builds(ValueName, value=st.text()),
        )
    ),
    effective=st.one_of(
        st.none(),
        st.builds(
            XmlDateTime,
            day=st.integers(),
            fractional_second=st.integers(),
            hour=st.integers(),
            minute=st.integers(),
            month=st.integers(),
            offset=st.one_of(st.none(), st.integers()),
            second=st.integers(),
            year=st.integers(),
        ),
    ),
    onset=st.one_of(
        st.none(),
        st.builds(
            XmlDateTime,
            day=st.integers(),
            fractional_second=st.integers(),
            hour=st.integers(),
            minute=st.integers(),
            month=st.integers(),
            offset=st.one_of(st.none(), st.integers()),
            second=st.integers(),
            year=st.integers(),
        ),
    ),
    expires=st.one_of(
        st.none(),
        st.builds(
            XmlDateTime,
            day=st.integers(),
            fractional_second=st.integers(),
            hour=st.integers(),
            minute=st.integers(),
            month=st.integers(),
            offset=st.one_of(st.none(), st.integers()),
            second=st.integers(),
            year=st.integers(),
        ),
    ),
    sender_name=st.one_of(st.none(), st.text()),
    headline=st.one_of(st.none(), st.text()),
    description=st.one_of(st.none(), st.text()),
    instruction=st.one_of(st.none(), st.text()),
    web=st.one_of(st.none(), st.text()),
    contact=st.one_of(st.none(), st.text()),
    parameters=st.lists(
        st.builds(
            Parameter,
            value=st.builds(Value, value=st.text()),
            value_name=st.builds(ValueName, value=st.text()),
        )
    ),
    resources=st.lists(
        st.builds(
            Resource,
            deref_uri=st.one_of(st.none(), st.text()),
            digest=st.one_of(st.none(), st.text()),
            mime_type=st.text(),
            resource_desc=st.text(),
            size=st.one_of(st.none(), st.integers()),
            uri=st.one_of(st.none(), st.text()),
        )
    ),
    areas=st.from_type(list[cap_tools.models.Area]),
)
def test_fuzz_info(  # noqa: PLR0913
    language: str | None,
    categories: list[cap_tools.Category],
    event: str,
    response_types: list[cap_tools.ResponseType],
    urgency: cap_tools.Urgency,
    severity: cap_tools.Severity,
    certainty: cap_tools.Certainty,
    audience: str | None,
    event_codes: list[cap_tools.models.EventCode],
    effective: xsdata.models.datatype.XmlDateTime | None,
    onset: xsdata.models.datatype.XmlDateTime | None,
    expires: xsdata.models.datatype.XmlDateTime | None,
    sender_name: str | None,
    headline: str | None,
    description: str | None,
    instruction: str | None,
    web: str | None,
    contact: str | None,
    parameters: list[cap_tools.models.Parameter],
    resources: list[cap_tools.models.Resource],
    areas: list[cap_tools.models.Area],
) -> None:
    info = cap_tools.models.Info(
        language=language,
        categories=categories,
        event=event,
        response_types=response_types,
        urgency=urgency,
        severity=severity,
        certainty=certainty,
        audience=audience,
        event_codes=event_codes,
        effective=effective,
        onset=onset,
        expires=expires,
        sender_name=sender_name,
        headline=headline,
        description=description,
        instruction=instruction,
        web=web,
        contact=contact,
        parameters=parameters,
        resources=resources,
        areas=areas,
    )

    assert info.get_language() == ("en-US" if language is None else language)


@given(
    value_name=st.builds(ValueName, value=st.text()),
    value=st.builds(Value, value=st.text()),
)
def test_fuzz_parameter(
    value_name: cap_tools.models.ValueName, value: cap_tools.models.Value
) -> None:
    _ = cap_tools.models.Parameter(value_name=value_name, value=value)


@given(
    resource_desc=st.text(),
    mime_type=st.text(),
    size=st.one_of(st.none(), st.integers()),
    uri=st.one_of(st.none(), st.text()),
    deref_uri=st.one_of(st.none(), st.text()),
    digest=st.one_of(st.none(), st.text()),
)
def test_fuzz_resource(  # noqa: PLR0913
    resource_desc: str,
    mime_type: str,
    size: int | None,
    uri: str | None,
    deref_uri: str | None,
    digest: str | None,
) -> None:
    _ = cap_tools.models.Resource(
        resource_desc=resource_desc,
        mime_type=mime_type,
        size=size,
        uri=uri,
        deref_uri=deref_uri,
        digest=digest,
    )


@given(value=st.text())
def test_fuzz_value(value: str) -> None:
    _ = cap_tools.models.Value(value=value)


@given(value=st.text())
def test_fuzz_value_name(value: str) -> None:
    _ = cap_tools.models.ValueName(value=value)
