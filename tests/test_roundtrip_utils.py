from hypothesis import given
from hypothesis import strategies as st

import cap_tools.utils

from . import strategies as custom_st


@given(items=st.lists(custom_st.group_listing_item))
def test_roundtrip_join_and_maybe_add_quotes_split_and_remove_quotes(
    items: list[str],
) -> None:
    value0 = cap_tools.utils.join_and_maybe_add_quotes(items)
    value1 = cap_tools.utils.split_and_remove_quotes(value0)
    assert items == value1, (items, value1)
