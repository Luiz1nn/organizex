import os
import json


def load_normalizations(file_path: str = "../normalizations.json"):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, file_path)

    with open(full_path, 'r', encoding='utf-8') as f:
        normalizations = json.load(f)
    return normalizations
