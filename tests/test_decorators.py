from typing import re

import pytest

from src.decorators import log


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция суммирует два числа и возвращает результат"""
    return x + y

def test_log_save_file():
    positive_result = my_function(2, 2)
    assert positive_result == 4


def test_crash_log():
    with pytest.raises(AssertionError, match="unsupported operand type(s) for +: 'int' and 'str'"):
        my_function(1, "a")



def test_log_captured(capsys):
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
