from typing import Callable

from src.masks import get_mask_account, get_mask_card_number # type: ignore


def mask_account_card(user_card: str) -> str:
    """Функция маскировки карты или счета"""
    if len(user_card) <= 0:
        raise ValueError("Ошибка ввода! Пожалуйста, введите корректный номер карты или счета.")
    elif "Счет" in user_card:
        mask_acc_numb = f"{user_card[:4]} {get_mask_account(user_card[5:])}"
        return mask_acc_numb
    else:
        mask_cart_numb = f"{user_card[:-16]}{get_mask_card_number(user_card[-16:])}"
        return mask_cart_numb


def get_date(user_date: str) -> str:
    """Функция корректировки даты и возвращения оной в формате ДД.ММ.ГГГГ"""
    return f"{user_date[8:10]}.{user_date[5:7]}.{user_date[:4]}"
