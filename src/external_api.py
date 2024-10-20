import os
from typing import Any

import requests
from dotenv import load_dotenv


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


def convert_amount(currency_code: str, amount: str) -> Any:
    """Конвертирует транзакции и возвращает сумму в рублях"""

    try:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        load_dotenv()
        api_key = os.getenv("API_KEY")
        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return f"Ошибка запроса. Возможная причина: {response.reason}"
        else:
            result = round(response.json()["result"], 2)
            return result

    except requests.exceptions.RequestException:
        print("Произошла ошибка. Пожалуйста, повторите попытку позже.")
