from typing import Iterable, Callable

from black import Union
from mypy.types import AnyType


def filter_by_state(my_list: Iterable[list[dict]], user_state: str) -> Iterable[list]:
    """Функция, которая фильтрует список словарей по указанному ключу и возвращает новый список словарей, у которых ключ совпадает с указанным"""
    sorted_list = []
    for i in my_list:
        if i["state"] == user_state:
            sorted_list.append(i)
    return sorted_list


def sort_by_date(my_list: Iterable[list[dict]], sorting_method=False) -> Iterable[list]:
    """Функция сортировки списка словарей по дате (по умолчанию - убывание)"""
    sorted_list = sorted(my_list, key=lambda x: x["date"], reverse=not sorting_method)
    return sorted_list


new_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(new_list, "EXECUTED"))
print(sort_by_date(new_list, sorting_method=True))
