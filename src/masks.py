import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rlt_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rlt_file_path)

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: int | str) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info("Создаем маску банковской карты")
    mask_number = str(card_number)
    if mask_number.isdigit() and 17 > len(mask_number) > 15:
        result = f"{mask_number[:4]} {mask_number[4:6]}** **** {mask_number[12:]}"
        logger.info("Создание маски карты успешно")
        return result
    else:
        logger.error("Ошибка! Введен некорректный номер карты")
        raise ValueError("Ошибка ввода! Пожалуйста, введите 16-значный номер карты.")


def get_mask_account(account_number: int | str) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info("Создаем маску номера счета")
    mask_account = str(account_number)
    if mask_account.isdigit() and len(mask_account) >= 20:
        result = f"**{mask_account[-4:]}"
        logger.info("Создание маски карты успешно")
        return result
    else:
        logger.error("Ошибка! Введен некорректный номер счета")
        raise ValueError("Ошибка ввода! Пожалуйста, введите корректный номер счета (не менее 20 цифр)")
