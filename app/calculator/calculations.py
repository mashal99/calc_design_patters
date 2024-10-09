"""
The Calculations module provides the Calculation class that encapsulates
the logic for performing and storing arithmetic operations.
"""

from typing import Callable


class Calculation:
    """
    This class stores the details of a single calculation and allows for
    performing the operation.
    """

    def __init__(self, number_one: float, number_two: float,
                 operation_func: Callable[[float, float], float]):
        """
        Initialize the Calculation with two numbers and an operation function.

        :param number_one: The first number.
        :param number_two: The second number.
        :param operation_func: The function to perform the arithmetic operation.
        """
        self.number_one = number_one
        self.number_two = number_two
        self.operation_func = operation_func

    def get_result(self) -> float:
        """
        Execute the arithmetic operation and return the result.

        :return: The result of the operation.
        """
        return self.operation_func(self.number_one, self.number_two)

# The commented-out CalculationsHistory class below is ignored by pylint.
# Remove the pointless string statement and the unused List import to fix warnings.
