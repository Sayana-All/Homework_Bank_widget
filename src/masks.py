def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    mask_number = str(card_number)
    if mask_number.isdigit() and 17 > len(mask_number) > 15:
        return f"{mask_number[:4]} {mask_number[4:6]}** **** {mask_number[12:]}"
    else:
        warning_message: str = "Ошибка ввода! Пожалуйста, введите 16-значный номер карты."
        return warning_message


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    mask_account = str(account_number)
    return f"**{mask_account[-4:]}"

