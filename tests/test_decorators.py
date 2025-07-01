import pytest

from src.decorators import log


def test_my_function(capsys):
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert "my_function ok Result: 3\n" == captured.out