import json
import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rlt_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rlt_file_path)

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_operations_data(file_path: str) -> list:
    """Обрабатывает JSON-файл и преобразует в список транзакций"""
    logger.info(f"Запрос на преобразование файла {file_path}")
    empty_data = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                operations = json.load(file)
                if len(operations) == 0:
                    logger.error("Файл пустой. Невозможно преобразовать.")
                    return empty_data
                elif len(operations) > 0:
                    logger.info("Список транзакций успешно создан.")
                    return operations
            except json.JSONDecodeError:
                logger.error("Ошибка декодирования JSON-файла")
                return empty_data
    except FileNotFoundError:
        logger.error("Ошибка! Файл не найден")
        return empty_data
