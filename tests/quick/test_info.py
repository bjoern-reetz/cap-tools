from cap_tools.models import Certainty, Info, Severity, Urgency


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
