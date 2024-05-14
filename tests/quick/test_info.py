from cap_tools.models import (
    Certainty,
    EventCode,
    Info,
    Parameter,
    Severity,
    Urgency,
    Value,
    ValueName,
)


def test_set_language():
    language = "foo"

    info = Info(
        event="my event",
        urgency=Urgency.IMMEDIATE,
        severity=Severity.SEVERE,
        certainty=Certainty.UNLIKELY,
        language=language,
    )

    assert info.language == language
    assert info.get_language() == language

    new_language = "bar"
    info.set_language(new_language)
    assert info.language == new_language
    assert info.get_language() == new_language

    default_language = "en-US"
    info.set_language(default_language)
    assert info.language is None
    assert info.get_language() == default_language


def test_event_codes_to_from_dict():
    event_codes_dict = {"foo": "bar", "lorem": "ipsum"}
    event_codes = [
        EventCode(ValueName(name), Value(value))
        for name, value in event_codes_dict.items()
    ]
    info = Info(
        event="my event",
        urgency=Urgency.IMMEDIATE,
        severity=Severity.SEVERE,
        certainty=Certainty.UNLIKELY,
        event_codes=event_codes,
    )
    assert info.event_codes_to_dict() == event_codes_dict

    new_event_codes_dict = {"foo": "baz", "dolor": "sit"}
    info.event_codes_from_dict(new_event_codes_dict)
    assert info.event_codes_to_dict() == new_event_codes_dict

    new_event_codes = [
        EventCode(ValueName(name), Value(value))
        for name, value in new_event_codes_dict.items()
    ]
    assert info.event_codes == new_event_codes


def test_parameters_to_from_dict():
    parameters_dict = {"foo": "bar", "lorem": "ipsum"}
    parameters = [
        Parameter(ValueName(name), Value(value))
        for name, value in parameters_dict.items()
    ]
    info = Info(
        event="my event",
        urgency=Urgency.IMMEDIATE,
        severity=Severity.SEVERE,
        certainty=Certainty.UNLIKELY,
        parameters=parameters,
    )
    assert info.parameters_to_dict() == parameters_dict

    new_parameters_dict = {"foo": "baz", "dolor": "sit"}
    info.parameters_from_dict(new_parameters_dict)
    assert info.parameters_to_dict() == new_parameters_dict

    new_parameters = [
        Parameter(ValueName(name), Value(value))
        for name, value in new_parameters_dict.items()
    ]
    assert info.parameters == new_parameters
