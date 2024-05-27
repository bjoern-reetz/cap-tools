import cap_tools.utils
from hypothesis import given
from hypothesis import strategies as st


@given(items=st.lists(st.text()))
def test_fuzz_join_and_maybe_add_quotes(items: list) -> None:
    cap_tools.utils.join_and_maybe_add_quotes(items=items)


@given(items=st.one_of(st.none(), st.text()))
def test_fuzz_split_and_remove_quotes(items: str | None) -> None:
    cap_tools.utils.split_and_remove_quotes(items=items)
