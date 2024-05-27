import cap_tools.utils
from hypothesis import given
from hypothesis import strategies as st


@given(
    items=st.lists(
        st.text(
            min_size=1,
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
    )
)
def test_roundtrip_join_and_maybe_add_quotes_split_and_remove_quotes(
    items: list[str],
) -> None:
    value0 = cap_tools.utils.join_and_maybe_add_quotes(items=items)
    value1 = cap_tools.utils.split_and_remove_quotes(items=value0)
    assert items == value1, (items, value1)
