from masks import get_mask_account, get_mask_card_number  # type: ignore


def mask_account_card(user_card: str) -> None:
    """Функция маскировки карты или счета"""
    if "Счет" in user_card:
        mask_acc_numb = f"{user_card[:4]} {get_mask_account(user_card[5:])}"
        return print(mask_acc_numb)
    else:
        mask_cart_numb = f"{user_card[:-16]}{get_mask_card_number(user_card[-16:])}"
        return print(mask_cart_numb)


def get_date(user_date: str) -> None:
    """Функция корректировки даты и возвращения оной в формате ДД.ММ.ГГГГ"""
    return print(f"{user_date[8:10]}.{user_date[5:7]}.{user_date[:4]}")


if __name__ == '__main__':
    mask_account_card("Visa Classic 6831982476737658")
    mask_account_card("Счет 73654108430135874305")
    get_date("2024-03-22T02:26:18.671407")
