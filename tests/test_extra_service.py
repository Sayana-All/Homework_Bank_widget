from src.extra_service import search_by_string, count_operations_by_categories
from src.read_files import read_csv_file


def test_search_by_string(transactions: list[dict]) -> None:
    """Тестирование функции поиска операций по заданному описанию"""
    result_1 = search_by_string(transactions, "Перевод организации")
    assert result_1 == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    result_2 = search_by_string(transactions, "Перевод со счета")
    assert result_2 == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


def test_failed_search_by_string(transactions: list[dict]) -> None:
    """Проверка некорректного описания для поиска или не найденного в списке операций"""
    zero_result = search_by_string(transactions, "Открытие вклада")
    assert zero_result == []

    fail_result = search_by_string(transactions, "2020")
    assert fail_result == []


def test_count_operations_by_categories() -> None:
    """Тестирование функции подсчета количества операций по заданным категориям"""
    operations = read_csv_file(r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\transactions.csv")
    count_result1 = count_operations_by_categories(
        operations, ["Перевод с карты на карту", "Перевод со счета на счет", "Перевод организации"]
    )
    assert count_result1 == {
        "Перевод организации": 117,
        "Перевод с карты на карту": 587,
        "Перевод со счета на счет": 110,
    }

    count_result2 = count_operations_by_categories(operations, ["Перевод с карты на карту", "Открытие вклада"])
    assert count_result2 == {"Перевод с карты на карту": 587, "Открытие вклада": 185}


def test_zero_count_operations_by_categories(transactions) -> None:
    """Проверка случаев, когда заданная категория пустая или не в списке операций"""
    zero_count1 = count_operations_by_categories(transactions, [""])
    assert zero_count1 == {}

    zero_count2 = count_operations_by_categories(transactions, ["Открытие вклада"])
    assert zero_count2 == {}
