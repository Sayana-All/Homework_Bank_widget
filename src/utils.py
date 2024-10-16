from typing import Any
import json


def get_operations_data(file_path: str) -> list[dict[str, Any]]:
    """Обрабатывает JSON-файл и преобразует в словарь с транзакциями"""
    empty_data = []
    try:
        with open(file_path) as file:
            if len(file) == 0:
                return empty_data
            else:
                operations = json.load(file)
                return operations
    except json.JSONDecodeError:
        print("Ошибка выгрузки JSON-файла")


if __name__ == '__main__':
    data = get_operations_data('\data\operations.json')
