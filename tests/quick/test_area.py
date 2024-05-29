from cap_tools.models import Area, Geocode, Value, ValueName


def test_geocode_to_from_dict() -> None:
    geocodes_dict = {"foo": "bar", "lorem": "ipsum"}
    geocodes = [
        Geocode(ValueName(name), Value(value)) for name, value in geocodes_dict.items()
    ]
    area = Area(area_desc="my area", geocodes=geocodes)
    assert area.geocodes_to_dict() == geocodes_dict

    new_geocodes_dict = {"foo": "baz", "dolor": "sit"}
    area.geocodes_from_dict(new_geocodes_dict)
    assert area.geocodes_to_dict() == new_geocodes_dict

    new_geocodes = [
        Geocode(ValueName(name), Value(value))
        for name, value in new_geocodes_dict.items()
    ]
    assert area.geocodes == new_geocodes
