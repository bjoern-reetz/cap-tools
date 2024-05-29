from hypothesis import strategies as st

group_listing_item = st.text(
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
