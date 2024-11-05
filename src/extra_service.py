import re
from collections import Counter


def search_by_string(operations_list: list[dict], search_string: str) -> list[dict]:
    """Поиск в списке операций по заданной строке. Возвращает список операций с подходящим описанием"""
    operations_found = []
    pattern = rf"{search_string}"

    for operation in operations_list:
        descr = str(operation["description"])
        match = re.search(pattern, descr, flags=re.IGNORECASE)
        if match:
            operations_found.append(operation)

    return operations_found


def count_operations_by_categories(operations_list: list[dict], user_categories: list) -> dict:
    """Функция подсчета операций по заданным пользователем категориям. Возвращает словарь с названиями категорий и их количеством"""
    counted = Counter()

    for operation in operations_list:
        descr = str(operation["description"]).lower()
        if len(descr) > 0:
            for category in user_categories:
                if len(category) > 0:
                    if category.lower() in descr:
                        counted[category] += 1
                else:
                    print("Ошибка запроса!")
                    return {}
        else:
            print("Ошибка запроса!")
            return {}

    return dict(counted)
