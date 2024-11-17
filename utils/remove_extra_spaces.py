import re


def remove_extra_spaces(text: str) -> str:
    return re.sub(r'\s{2,}', ' ', text)
