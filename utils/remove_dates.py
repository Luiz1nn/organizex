import re


def remove_dates(text: str) -> str:
    return re.sub(r'\b\d{2}/\d{2}\b(?!/\d{4})', '', text)
