import json
from typing import Any


def get_operations_data(file_path):
    """Обрабатывает JSON-файл и преобразует в словарь с транзакциями"""

    empty_data = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                operations = json.load(file)
                if len(operations) == 0:
                    return empty_data
                return operations
            except json.JSONDecodeError:
                print("Ошибка декодирования JSON-файла")
                return empty_data
    except FileNotFoundError:
        print("Ошибка! Файл не найден")
        return empty_data


if __name__ == "__main__":
    data = get_operations_data(r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\operations.json")
    print(data)
