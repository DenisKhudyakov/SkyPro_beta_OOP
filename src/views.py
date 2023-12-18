import json
def read_json(path: str) -> dict:
    """Функция чтения json файла"""
    with open(path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data
