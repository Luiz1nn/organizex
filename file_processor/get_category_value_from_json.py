import json
import os


def get_category_value_from_json(
    category_name: str,
    json_file: str = '../categories.json'
) -> str:
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_path, json_file)

        with open(full_path, 'r', encoding='utf-8') as file:
            categories = json.load(file)

        return categories.get(category_name, 'Categoria não encontrada')
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo JSON: {e}")
        return 'Erro ao ler o arquivo JSON'
