"""
The Operations module contains functions for performing basic arithmetic operations.
"""


def add(number_one: float, number_two: float) -> float:
    """
    Perform addition of two numbers.

    :param number_one: The first number.
    :param number_two: The second number.
    :return: The result of addition.
    """
    return number_one + number_two


def subtract(number_one: float, number_two: float) -> float:
    """
    Perform subtraction of two numbers.

    :param number_one: The first number.
    :param number_two: The second number.
    :return: The result of subtraction.
    """
    return number_one - number_two


def multiply(number_one: float, number_two: float) -> float:
    """
    Perform multiplication of two numbers.

    :param number_one: The first number.
    :param number_two: The second number.
    :return: The result of multiplication.
    """
    return number_one * number_two


def divide(number_one: float, number_two: float) -> float:
    """
    Perform division of two numbers.

    :param number_one: The first number.
    :param number_two: The second number.
    :return: The result of division.
    :raises ZeroDivisionError: If the second number is zero.
    """
    if number_two == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return number_one / number_two
