from unittest.mock import patch

from src.external_api import convert_amount


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
