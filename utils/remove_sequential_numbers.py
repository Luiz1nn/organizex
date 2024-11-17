import re


def remove_sequential_numbers(text: str) -> str:
    return re.sub(r'(?<!/)\b\d{3,}\b', '', text)
