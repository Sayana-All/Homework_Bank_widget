import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_num, expected", [(1596837868705199, "1596 83** **** 5199"),
                                                (7000792289606361, "7000 79** **** 6361"),
                                                (5999414228426353, "5999 41** **** 6353"),])
def test_get_mask_card_number(card_num, expected):
    assert get_mask_card_number(card_num) == expected


def test_get_mask_invalid_card_number():
    with pytest.raises(ValueError):
        assert get_mask_card_number(427650005779000000)
        assert get_mask_card_number(0)
        assert get_mask_card_number("aaa")


@pytest.mark.parametrize("acc_num, expected", [(73654108430135874305, "**4305"),
                                               (35383033474447895560, "**5560"),
                                               (64686473678894779589, "**9589"),
                                               (8595745896200145620579, "**0579")])
def test_get_mask_account(acc_num, expected):
    assert get_mask_account(acc_num) == expected


def test_get_mask_invalid_account():
    with pytest.raises(ValueError):
        assert get_mask_account(6699857625)
        assert get_mask_account("abc")
