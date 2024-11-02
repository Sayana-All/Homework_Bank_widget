from typing import Any
from unittest.mock import patch

from src.read_files import read_csv_file, read_excel_file


@patch("pandas.read_csv")
def test_read_csv_file(mock_read_csv: Any) -> None:
    """Тестирование функции считывания CSV-файла"""
    mock_read_csv.return_value.to_dict.return_value = [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]
    result = read_csv_file("test_file_path.csv")
    assert result == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]


def test_read_not_csv_file() -> None:
    assert read_csv_file("test_file.json") == []
    assert read_csv_file(r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\transactions_excel.xlsx") == []


@patch("pandas.read_excel")
def test_read_excel_file(mock_read_excel: Any) -> None:
    mock_read_excel.return_value.to_dict.return_value = [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"},
    ]
    result = read_excel_file("test_file_path.xlsx")
    assert result == [{"test_dict": "01", "test_key": "test_value_1"}, {"test_dict": "02", "test_key": "test_value_2"}]


def test_read_not_excel_file() -> None:
    assert read_excel_file("test_file.json") == []
    assert read_excel_file(r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\operations.json") == []
    assert read_excel_file("test_file_path.csv") == []
