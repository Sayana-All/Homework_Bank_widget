

@log(filename="mylog.txt")
def my_function(x, y):
    """Функция суммирует два числа и возвращает результат"""
    return x + y


if __name__ == "__main__":
    my_function(1, 2) # my_function ok
    my_function(1, "_") # my_function error: тип ошибки. Inputs: (1, "_"), {}