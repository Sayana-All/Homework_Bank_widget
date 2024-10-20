import os
from typing import Any

import requests
from dotenv import load_dotenv


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
