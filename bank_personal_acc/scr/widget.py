from mypy.types_utils import AnyType

import masks


def mask_account_card(user_card: str) -> AnyType:
    """Функция маскировки карты и счета"""
    if "Счет" in user_card:
        return print(get_mask_account(user_card[5:]))

    else:
        return print(get_mask_card_number(user_card[-16:]))


mask_account_card("Visa Platinum 7000792289606361")
mask_account_card("Счет 73654108430135874305")
