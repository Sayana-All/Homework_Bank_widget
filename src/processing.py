from typing import Any


def filter_by_state(data: list[dict[str, Any]], user_state: str = "EXECUTED") -> list[dict[Any, Any]]:
    """Функция, которая фильтрует список словарей по указанному ключу"""
    sorted_list = []
    for i in data:
        if i["state"] == user_state:
            sorted_list.append(i)

    #if user_state not in data[1]["state"]:
    #    raise ValueError("Ключ не найден!")

    return sorted_list


def sort_by_date(data: list[dict[str, Any]], descending: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки списка банковских операций по дате (по умолчанию - убывание)"""
    sorted_list = sorted(data, key=lambda x: x["date"], reverse=descending)
    return sorted_list
