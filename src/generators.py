from typing import Any, Iterator


def filter_by_currency(transactions_list: list[dict[str, Any]], currency: str) -> Iterator:
    """Функция фильтрует и возвращает список операций по заданной валюте по одной за раз"""
    if len(transactions_list) > 0:
        for transaction in transactions_list:
            if transaction.get("operationAmount").get("currency").get("code") == currency:
                yield transaction
            elif currency not in transaction:
                raise ValueError("Ошибка! Данной валюты нет в списке")
    else:
        raise ValueError("Ошибка ввода! Список пустой!")


def transaction_descriptions(transactions_list: list[dict[str, Any]]) -> Iterator | str:
    """Функция, возвращающая описание операции из заданного списка по одной за раз"""
    if len(transactions_list) > 0:
        for desc_srt in transactions_list:
            if len(desc_srt["description"]) > 0:
                yield desc_srt.get("description")
            else:
                yield "У данной операции нет описания"
    else:
        raise ValueError("Ошибка ввода! Список пустой!")


def card_number_generator(start: int, end: int) -> Iterator:
    """Функция для генерации номеров банковских карт"""
    if type(start) == int and type(end) == int:
        for numb_card in range(start, end):
            card_number = str(numb_card)
            while len(card_number) < 16:
                card_number = '0' + card_number
            formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
            yield formatted_card_number
    else:
        raise TypeError("Ошибка ввода! Диапазон для генерации номеров карт должен быть в виде чисел.")
