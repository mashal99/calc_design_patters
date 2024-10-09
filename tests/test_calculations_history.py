"""
Unit tests for the alculationsHistory class using pytest.
"""

import pytest
from app.calculator.calculation_history import CalculationsHistory
from app.calculator.calculations import Calculation
from app.calculator.operations import add, subtract, multiply, divide


@pytest.fixture(autouse=True)
def clear_history():
    """
    Fixture to clear the history before each test.
    """
    CalculationsHistory.clear_history()


def test_add_calculation_to_history():
    """
    Test that adding a calculation to history works correctly.
    """
    calculation = Calculation(1, 2, add)
    CalculationsHistory.add_calculation(calculation)
    assert len(CalculationsHistory.history) == 1
    assert CalculationsHistory.get_last_calculation().get_result() == 3


def test_get_last_calculation():
    """
    Test retrieving the last calculation from the history.
    """
    calculation1 = Calculation(3, 4, multiply)
    calculation2 = Calculation(6, 2, divide)
    CalculationsHistory.add_calculation(calculation1)
    CalculationsHistory.add_calculation(calculation2)

    last_calculation = CalculationsHistory.get_last_calculation()
    assert last_calculation.get_result() == 3  # 6 / 2


def test_clear_history():
    """
    Test clearing the history.
    """
    calculation = Calculation(5, 5, add)
    CalculationsHistory.add_calculation(calculation)
    assert len(CalculationsHistory.history) == 1
    CalculationsHistory.clear_history()
    assert len(CalculationsHistory.history) == 0


def test_get_history():
    """
    Test retrieving the full history.
    """
    calculation1 = Calculation(10, 2, subtract)
    calculation2 = Calculation(3, 5, add)
    CalculationsHistory.add_calculation(calculation1)
    CalculationsHistory.add_calculation(calculation2)
    history = CalculationsHistory.get_history()
    assert len(history) == 2
    assert history[0].get_result() == 8  # 10 - 2
    assert history[1].get_result() == 8  # 3 + 5
