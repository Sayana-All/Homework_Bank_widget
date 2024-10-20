from src.utils import get_operations_data, get_transaction_amount


def test_get_operations_data():
    """Тестирование функции получения данных операций из JSON-файла"""
    test_path = r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\test_file.json"
    assert get_operations_data(test_path) == [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"},
    ]


def test_empty_get_operations_data() -> None:
    """Тестирование на ошибки и получение пустого списка операций из JSON-файла"""
    data = get_operations_data(r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\operation.json")
    assert data == []


def test_get_transaction_amount() -> None:
    """Тестирование функции на получение суммы операции в рублях"""
    data_rub = {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    }
    assert get_transaction_amount(data_rub) == 48223.05


def test_get_zero_transaction_amount() -> None:
    """Тестирование функции на получение суммы операции в рублях"""
    assert get_transaction_amount({}) == 0.0
    assert get_transaction_amount([0, 1000]) == 0.0
    assert get_transaction_amount("amount - 100") == 0.0
