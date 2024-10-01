def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    mask_number = str(card_number)
    return f"{mask_number[:4]} {mask_number[4:6]}** **** {mask_number[12:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    mask_account = str(account_number)
    return f"**{mask_account[-4:]}"


