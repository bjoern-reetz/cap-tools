import itertools

import pytest

from cap_tools.utils import join_and_maybe_add_quotes, split_and_remove_quotes

test_suite_symmetric = {
    None: [],
    "foo bar baz": ["foo", "bar", "baz"],
    'foo "bar baz" bam': ["foo", "bar baz", "bam"],
    '"foo bar baz"': ["foo bar baz"],
}

test_suite_asymmetric = {"": [], '"foobar" baz': ["foobar", "baz"]}


@pytest.mark.parametrize(
    ("test_input", "expected"),
    itertools.chain(test_suite_symmetric.items(), test_suite_asymmetric.items()),
)
def test_split_and_remove_quotes(test_input: str, expected: list[str]) -> None:
    assert split_and_remove_quotes(test_input) == expected


@pytest.mark.parametrize(("expected", "test_input"), test_suite_symmetric.items())
def test_join_and_maybe_add_quotes(test_input: list[str], expected: str) -> None:
    assert join_and_maybe_add_quotes(test_input) == expected
