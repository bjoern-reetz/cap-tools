import shlex


def split_and_remove_quotes(items: str | None) -> list[str]:
    if not items:
        return []
    return shlex.split(items)


def join_and_maybe_add_quotes(items: list[str]) -> str | None:
    if not items:
        return None
    return " ".join(f'"{item}"' if " " in item else item for item in items)
