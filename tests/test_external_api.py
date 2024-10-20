from unittest.mock import patch

from src.external_api import convert_amount, get_transaction_amount


def test_get_transaction_amount() -> None:
    """Тестирование функции на получение суммы операции в рублях"""
    data_rub = {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    }
    assert get_transaction_amount(data_rub) == 48223.05


def test_get_zero_transaction_amount() -> None:
    """Тестирование функции на получение суммы операции в рублях"""
    assert get_transaction_amount({}) == 0.0
    assert get_transaction_amount([0, 1000]) == 0.0
    assert get_transaction_amount("amount - 100") == 0.0


@patch("requests.get")
def test_convert_amount(mock_get):
    """Тестирование функции конвертации иностранных валют в рубли"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "date": "2024-10-20",
        "info": {"rate": 95.802878, "timestamp": 1729400884},
        "query": {"amount": 5, "from": "USD", "to": "RUB"},
        "result": 479.01439,
        "success": True,
    }
    assert convert_amount("USD", 5) == 479.01

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "date": "2024-10-20",
        "info": {"rate": 104.178393, "timestamp": 1729401543},
        "query": {"amount": 10, "from": "EUR", "to": "RUB"},
        "result": 1041.78393,
        "success": True,
    }
    assert convert_amount("EUR", 10) == 1041.78


@patch("requests.get")
def test_convert_amount_invalid(mock_get):
    """Тестирование функции конвертации иностранных валют в рубли"""
    mock_get.return_value.status_code = 404
    mock_get.return_value.reason = "The requested resource doesn't exist."
    assert convert_amount("USD", 5) == "Ошибка запроса. Возможная причина: The requested resource doesn't exist."
