from functools import wraps


def log(filename=None):
    """ Декоратор, который автоматически логирует начало и конец выполнения функции, а также ее результаты
    или возникшие ошибки. """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # print(f"Запуск функции {func.__name__}")
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok Result: {result}"
                if filename:
                    with open(filename, 'a') as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as err:
                error_message = f"{func.__name__} error: {type(err).__name__}, args: {args}, kwargs: {kwargs}"
                if filename:
                    with open(filename, 'a') as file:
                        file.write(error_message + "\n")
                else:
                    print(error_message)
                raise

        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении:
# my_function ok
# Ожидаемый вывод при ошибке: my_function error: тип ошибки. Inputs: (1, 2), {}
# Где тип ошибки заменяется на текст ошибки.


# @log()
# def another_function(a, b):
#     if a > b:
#         raise ValueError("A больше B")
#     return a * b


# Тестовые вызовы функций
# my_function(1, 2)
# another_function(3, 4)
# another_function(5, 1)  # Это вызовет ошибку