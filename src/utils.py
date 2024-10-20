import json

from src.external_api import convert_amount


def get_operations_data(file_path: str) -> list:
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


def get_transaction_amount(transaction: dict) -> float:
    """Получает данные о транзакции и возвращает сумму в рублях"""
    if len(transaction) == 0 or type(transaction) is not dict:
        print("Ошибка ввода данных!")
        return 0.0
    elif len(transaction) > 0:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return float(transaction["operationAmount"]["amount"])
        else:
            currency_code = transaction["operationAmount"]["currency"]["code"]
            amount_transaction = transaction["operationAmount"]["amount"]
            amount_convert = convert_amount(currency_code, amount_transaction)
            return amount_convert
