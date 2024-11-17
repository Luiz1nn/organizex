import re


def remove_times(text: str) -> str:
    return re.sub(r'\b\d{2}:\d{2}\b', '', text)
