from typing import Any, Iterator, Sized, SupportsIndex


def filter_by_currency(transactions_list: list[dict[str, int | str | dict[str, str | dict [str, str]]]], currency: str) -> Iterator[Any] | str:
    """Функция фильтрует и возвращает список операций по заданной валюте по одной за раз"""
    if len(transactions_list) <= 0:
        return str("Ошибка ввода! Список пустой!")
    else:
        for transaction in transactions_list:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions_list: list[dict[str, int | str | dict[str, str | dict [str, str]]]]) -> Iterator[Any] | str:
    """Функция, возвращающая описание операции из заданного списка по одной за раз"""
    if len(transactions_list) > 0:
        for desc_srt in transactions_list:
            if len(desc_srt["description"]) > 0:
                yield desc_srt.get("description")
            elif len(desc_srt["description"]) <= 0:
                return str("У данной операции нет описания")
    else:
        raise ValueError("Ошибка ввода! Список пустой!")


def card_number_generator(start: int, end: int) -> Iterator[Any]:
    """Функция для генерации номеров банковских карт"""
    for numb_card in range(start, end):
        card_number = str(numb_card)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number
