import logging
import os
from typing import Any, Hashable

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
rlt_file_path = os.path.join(current_dir, "../logs/read_files.log")
abs_file_path = os.path.abspath(rlt_file_path)

logger = logging.getLogger("read_files")
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_csv_file(file_path: str) -> list[dict[Hashable, Any]]:
    """Чтение CSV-файла и получение списка транзакций"""
    logger.info(f"Запрос на чтение CSV-файла {file_path}")
    try:
        transactions_df = pd.read_csv(file_path, delimiter=";", encoding="utf-8")
        result = transactions_df.to_dict(orient="records")
        logger.info("Список транзакций успешно создан.")
        return result

    except FileNotFoundError:
        logger.error("Ошибка! Файл не найден")
        return []
    except Exception as e:
        logger.error(f"Произошла ошибка {e}")
        return []


def read_excel_file(file_path: str) -> list[dict[Hashable, Any]]:
    """Чтение Excel-файла и получение списка транзакций"""
    logger.info(f"Запрос на чтение Excel-файла {file_path}")
    try:
        transactions_df = pd.read_excel(file_path)
        result = transactions_df.to_dict(orient="records")
        return result
    except FileNotFoundError:
        logger.error("Ошибка! Файл не найден")
        return []
    except Exception as e:
        logger.error(f"Произошла ошибка {e}")
        return []
