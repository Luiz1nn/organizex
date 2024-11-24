import os
import json


def ensure_categories() -> None:
    file_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'categories.json'
    )
    file_path = os.path.abspath(file_path)

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({}, f, indent=4)
