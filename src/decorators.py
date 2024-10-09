from functools import wraps
from typing import Callable, Optional, Any


def log(filename: Optional[str]) -> Any:
    """Декоратор для логирования функции, её аргументов, результатов и ошибок"""

    def logging_decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"\n{func.__name__} ok")
                else:
                    print(f"\n{func.__name__} ok")
                return result
            except Exception as err:
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"\n{func.__name__} error: {err}. Inputs: {args}, {kwargs}")
                else:
                    print(f"\n{func.__name__} error: {err}. Inputs: {args}, {kwargs}")
                raise err

        return wrapper

    return logging_decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Функция суммирует два числа и возвращает результат"""
    return x + y


if __name__ == "__main__":
    my_function(2, 2)  # my_function ok
    my_function(2, "2")  # my_function error: тип ошибки. Inputs: (1, "_"), {}
