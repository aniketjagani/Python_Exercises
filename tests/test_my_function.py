import pytest
import source.my_function as my_function


def test_add():
    result = my_function.add(1, 4)
    assert result == 5


def test_divide():
    result = my_function.divide(4, 2)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = my_function.divide(4, 0)
