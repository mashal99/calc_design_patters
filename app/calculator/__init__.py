"""
The Calculator module provides static methods for performing arithmetic operations
by leveraging the Calculation and Operations classes.
"""

from calculator.calculations import Calculation
from calculator.operations import add, subtract, multiply, divide


class Calculator:
    """
    A simple calculator with static methods for basic arithmetic operations.
    """

    @staticmethod
    def add(number_one: float, number_two: float) -> float:
        """
        Perform addition of two numbers.

        :param number_one: The first number.
        :param number_two: The second number.
        :return: The result of the addition.
        """
        calculation = Calculation(number_one, number_two, add)
        return calculation.get_result()

    @staticmethod
    def subtract(number_one: float, number_two: float) -> float:
        """
        Perform subtraction of two numbers.

        :param number_one: The first number.
        :param number_two: The second number.
        :return: The result of the subtraction.
        """
        calculation = Calculation(number_one, number_two, subtract)
        return calculation.get_result()

    @staticmethod
    def multiply(number_one: float, number_two: float) -> float:
        """
        Perform multiplication of two numbers.

        :param number_one: The first number.
        :param number_two: The second number.
        :return: The result of the multiplication.
        """
        calculation = Calculation(number_one, number_two, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(number_one: float, number_two: float) -> float:
        """
        Perform division of two numbers.

        :param number_one: The first number.
        :param number_two: The second number.
        :return: The result of the division.
        :raises ZeroDivisionError: If the second number is zero.
        """
        calculation = Calculation(number_one, number_two, divide)
        return calculation.get_result()
