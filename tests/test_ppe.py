import pytest
from ppe import ppe_debug


def test_custom_message():
    @ppe_debug
    def test_func():
        x = 5  ## Test message
        return x

    result = test_func()
    assert result == 5


def test_statement_echo():
    @ppe_debug
    def test_func():
        x = 10  ## -
        return x

    result = test_func()
    assert result == 10


def test_return_statement():
    @ppe_debug
    def test_func():
        return 42  ## Return test value

    result = test_func()
    assert result == 42