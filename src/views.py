import json
import os

PATH_FILE = os.path.abspath('products.json')
def read_json(path: str) -> dict:
    """Функция чтения json файла"""
    with open(path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data


if __name__ == '__main__':
    print(read_json(PATH_FILE))