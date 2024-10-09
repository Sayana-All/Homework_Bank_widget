from functools import wraps
from typing import Optional, Callable


def log(filename: Optional[str]):
    """Декоратор для логирования функции, её аргументов, результатов и ошибок"""
    def logging_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename != None:
                    with open(filename, "a") as file:
                        file.write(f"\n{func.__name__} ok")
                else:
                    print(f"\n{func.__name__} ok")
                return result
            except Exception as err:
                if filename != None:
                    with open(filename, "a") as file:
                        file.write(f"\n{func.__name__} error: {err}. Inputs: {args}, {kwargs}")
                else:
                    print(f"\n{func.__name__} error: {err}. Inputs: {args}, {kwargs}")
                raise err

        return wrapper

    return logging_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция суммирует два числа и возвращает результат"""
    return x + y


if __name__ == "__main__":
    my_function(2, 2) # my_function ok
    my_function(2, "2") # my_function error: тип ошибки. Inputs: (1, "_"), {}
