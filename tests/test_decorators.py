import pytest

from unittest.mock import mock_open, patch

from src.decorators import log, my_function


def test_my_function(capsys):
    """ Тест успешного выполнения функции. """
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert "my_function ok Result: 3\n" == captured.out


def test_error_function(capsys):
    """Тест обработки исключения."""
    @log()
    def error_function(x, y):
        raise ValueError("An error occurred")

    try:
        error_function(1, 2)
    except ValueError:
        pass
    captured = capsys.readouterr()
    assert "error_function error: ValueError. Inputs: (1, 2), kwargs: {}\n" in captured.out


def test_error_function_open_file(capsys):
    """Тест обработки исключения."""
    @log(filename=None)
    def error_function_open_file(x, y):
        raise ValueError("An error occurred")

    try:
        error_function_open_file(1, 2)
    except ValueError:
        pass
    captured = capsys.readouterr()
    assert "error_function_open_file error: ValueError. Inputs: (1, 2), kwargs: {}\n" in captured.out

def test_logging_error_to_file():
    m = mock_open()
    with patch('builtins.open', m):
        try:
            # вызови функцию с неправильными параметрами, чтобы вызвать ошибку
            my_function(1, 'a')
        except TypeError:
            pass

    m().write.assert_called_once_with("my_function error: TypeError. Inputs: (1, 'a'), kwargs: {}\n")


def test_file_logging():
    """Тестирование логирования в файл."""
    my_function(3, 4)
    with open('mylog.txt', 'r') as f:
        content = f.read().strip()
    assert "my_function ok Result: 7" in content


def test_no_filename_logging(capsys):
    """Тест отсутствия файла логирования и вывода в консоль."""
    @log()
    def simple_function(a, b):
        return a * b

    result = simple_function(2, 3)
    assert result == 6
    captured = capsys.readouterr()
    assert "simple_function ok Result: 6" in captured.out.strip()

