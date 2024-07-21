from datetime import datetime, timedelta, timezone

from hypothesis import strategies as st
from xsdata.models.datatype import XmlDateTime

from cap_tools.models import (
    Alert,
    Area,
    Category,
    Certainty,
    EventCode,
    Info,
    MsgType,
    Parameter,
    Resource,
    ResponseType,
    Scope,
    Severity,
    Status,
    Urgency,
)


def group_listing_items(
    *, min_size: int = 1, max_size: int | None = None
) -> st.SearchStrategy[str]:
    return st.text(
        min_size=min_size,
        max_size=max_size,
        alphabet=st.characters(
            codec="utf-8",
            categories=[
                "L",  #  Letter
                "M",  #  Mark
                "N",  #  Number
                "P",  #  Punctuation
                "S",  #  Symbol
                "Zs",  # Separator, space
            ],
            exclude_characters="<&'\"\\",
        ),
    )


@st.composite
def optional_xml_date_times(
    draw: st.DrawFn,
    datetimes: st.SearchStrategy[datetime | None] = st.one_of(
        st.none(), st.datetimes()
    ),
    /,
) -> XmlDateTime | None:
    drawn_obj = draw(datetimes)
    if drawn_obj is None:
        return None
    return XmlDateTime.from_datetime(drawn_obj)


@st.composite
def infos(
    draw: st.DrawFn,
    *,
    language: st.SearchStrategy[str | None] = st.none(),
    categories: st.SearchStrategy[list[Category]] = st.sets(
        st.sampled_from(Category)
    ).map(list),
    event: st.SearchStrategy[str] = st.text(min_size=8),
    response_types: st.SearchStrategy[list[ResponseType]] = st.sets(
        st.sampled_from(ResponseType)
    ).map(list),
    urgency: st.SearchStrategy[Urgency] = st.sampled_from(Urgency),
    severity: st.SearchStrategy[Severity] = st.sampled_from(Severity),
    certainty: st.SearchStrategy[Certainty] = st.sampled_from(Certainty),
    audience: st.SearchStrategy[str | None] = st.none(),
    event_codes: st.SearchStrategy[list[EventCode]] = st.lists(
        st.from_type(EventCode), max_size=0
    ),
    effective: st.SearchStrategy[datetime | None] = st.none(),
    onset: st.SearchStrategy[datetime | None] = st.none(),
    expires: st.SearchStrategy[datetime | None] = st.none(),
    sender_name: st.SearchStrategy[str | None] = st.none(),
    headline: st.SearchStrategy[str | None] = st.none(),
    description: st.SearchStrategy[str | None] = st.none(),
    instruction: st.SearchStrategy[str | None] = st.none(),
    web: st.SearchStrategy[str | None] = st.none(),
    contact: st.SearchStrategy[str | None] = st.none(),
    parameters: st.SearchStrategy[list[Parameter]] = st.lists(
        st.from_type(Parameter), max_size=0
    ),
    resources: st.SearchStrategy[list[Resource]] = st.lists(
        st.from_type(Resource), max_size=0
    ),
    areas: st.SearchStrategy[list[Area]] = st.lists(st.from_type(Area), max_size=0),
) -> Info:
    return Info(
        language=draw(language),
        categories=draw(categories),
        event=draw(event),
        response_types=draw(response_types),
        urgency=draw(urgency),
        severity=draw(severity),
        certainty=draw(certainty),
        audience=draw(audience),
        event_codes=draw(event_codes),
        effective=draw(optional_xml_date_times(effective)),
        onset=draw(optional_xml_date_times(onset)),
        expires=draw(optional_xml_date_times(expires)),
        sender_name=draw(sender_name),
        headline=draw(headline),
        description=draw(description),
        instruction=draw(instruction),
        web=draw(web),
        contact=draw(contact),
        parameters=draw(parameters),
        resources=draw(resources),
        areas=draw(areas),
    )


@st.composite
def alerts(
    draw: st.DrawFn,
    *,
    identifier: st.SearchStrategy[str] = st.uuids().map(str),
    sender: st.SearchStrategy[str] = st.uuids().map(str),
    sent: st.SearchStrategy[datetime] = st.datetimes(
        timezones=st.just(timezone(timedelta(hours=1)))
    ),
    status: st.SearchStrategy[Status] = st.just(Status.ACTUAL),
    msg_type: st.SearchStrategy[MsgType] = st.just(MsgType.ALERT),
    source: st.SearchStrategy[str | None] = st.none(),
    scope: st.SearchStrategy[Scope] = st.just(Scope.PUBLIC),
    restriction: st.SearchStrategy[str | None] = st.none(),
    addresses: st.SearchStrategy[str | None] = st.none(),
    codes: st.SearchStrategy[list[str]] = st.lists(st.from_type(str), max_size=0),
    note: st.SearchStrategy[str | None] = st.none(),
    references: st.SearchStrategy[str | None] = st.none(),
    incidents: st.SearchStrategy[str | None] = st.none(),
    infos: st.SearchStrategy[list[Info]] = st.lists(infos(), max_size=0),
    _signatures: st.SearchStrategy[list[object]] = st.lists(
        st.from_type(object), max_size=0
    ),
) -> Alert:
    return Alert(
        identifier=draw(identifier),
        sender=draw(sender),
        sent=XmlDateTime.from_datetime(draw(sent)),
        status=draw(status),
        msg_type=draw(msg_type),
        source=draw(source),
        scope=draw(scope),
        restriction=draw(restriction),
        addresses=draw(addresses),
        codes=draw(codes),
        note=draw(note),
        references=draw(references),
        incidents=draw(incidents),
        infos=draw(infos),
        _signatures=draw(_signatures),
    )
