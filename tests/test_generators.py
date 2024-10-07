from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list[dict[str, int | str | dict[str, str | dict [str, str]]]]) -> None:
    usd_generator = filter_by_currency(transactions, "USD")
    assert next(usd_generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(usd_generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }

    rub_generator = filter_by_currency(transactions, "RUB")
    assert next(rub_generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(rub_generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_invalid_filter_by_currency() -> None:
    with pytest.raises(StopIteration):
        assert next(filter_by_currency([], "RUB"))


def test_transaction_descriptions(transactions: list[dict[str, int | str | dict[str, str | dict [str, str]]]]) -> None:
    """Функция тестирует генератор транзакций"""
    expected_descriptions = transaction_descriptions(transactions)
    assert next(expected_descriptions) == "Перевод организации"
    assert next(expected_descriptions) == "Перевод со счета на счет"
    assert next(expected_descriptions) == "Перевод со счета на счет"
    assert next(expected_descriptions) == "Перевод с карты на карту"


def test_transaction_with_zero_descriptions(zero_description: list[dict[str, int | str | dict[str, str | dict [str, str]]]]) -> None:
    with pytest.raises(StopIteration):
        assert next(transaction_descriptions(zero_description))


def test_invalid_transaction_descriptions() -> None:
    with pytest.raises(ValueError):
        assert next(transaction_descriptions([]))


def test_card_number_generator() -> None:
    """Функция тестирует генератор номеров карт"""
    card_number = card_number_generator(1000, 1004)
    assert next(card_number) == "0000 0000 0000 1000"
    assert next(card_number) == "0000 0000 0000 1001"
    assert next(card_number) == "0000 0000 0000 1002"
    assert next(card_number) == "0000 0000 0000 1003"
