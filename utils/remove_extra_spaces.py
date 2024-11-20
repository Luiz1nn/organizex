import re


def remove_extra_spaces(text: str) -> str:
    text = re.sub(r'\s{2,}', ' ', text).strip()
    return text
