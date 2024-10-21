from src.utils import get_operations_data


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
