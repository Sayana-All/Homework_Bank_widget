from typing import Any


def filter_by_state(data: list[dict[str, Any]], user_state: str = "EXECUTED") -> list[dict[Any, Any]]:
    """Функция, которая фильтрует список словарей по указанному ключу"""
    sorted_list = []
    for i in data:
        if i["state"] == user_state:
            sorted_list.append(i)
    return sorted_list


def sort_by_date(data: list[dict[str, Any]], descending: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки списка словарей по дате (по умолчанию - убывание)"""
    sorted_list = sorted(data, key=lambda x: x["date"], reverse=descending)
    return sorted_list


new_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == '__main__':
    print(filter_by_state(new_data))
    print(filter_by_state(new_data, "CANCELED"))
    print(sort_by_date(new_data, descending=False))
    print(sort_by_date(new_data))
