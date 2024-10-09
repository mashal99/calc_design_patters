"""
Unit tests for the Calculator class.
"""
import pytest
from app.calculator import Calculator

def test_add():
    """
    Test addition operation in Calculator.
    """
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(-1, -1) == -2
    assert Calculator.add(0, 0) == 0


def test_subtract():
    """
    Test subtraction operation in Calculator.
    """
    assert Calculator.subtract(3, 2) == 1
    assert Calculator.subtract(-1, -1) == 0
    assert Calculator.subtract(0, 5) == -5


def test_multiply():
    """
    Test multiplication operation in Calculator.
    """
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-1, -1) == 1
    assert Calculator.multiply(0, 5) == 0


def test_divide():
    """
    Test division operation in Calculator.
    """
    assert Calculator.divide(6, 3) == 2


def test_divide_by_zero():
    """
    Test that dividing by zero raises a ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(1, 0)
