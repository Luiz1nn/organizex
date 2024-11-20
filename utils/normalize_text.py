from utils.load_normalizations import load_normalizations


def normalize_text(text: str) -> str:
    normalizations = load_normalizations()

    for key, value in normalizations.items():
        if text == key:
            text = value
            break

    return text
