from functools import wraps


def log(filename):
    """Декоратор для логирования функции, её аргументов, результатов и ошибок"""

    def logging_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise e

        return wrapper

    return logging_decorator


if __name__ == "__main__":

    @log(filename="mylog.txt")
    def my_function(x, y):
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(1, 2)
