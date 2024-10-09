"""
The CalculationsHistory class manages the history of arithmetic calculations.
"""

from typing import List
from .calculations import Calculation


class CalculationsHistory:
    """
    This class manages a history of Calculation instances.
    """

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """
        Add a new calculation to the history.

        :param calculation: A Calculation instance.
        """
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """
        Retrieve the most recent calculation from the history.

        :return: The last Calculation instance.
        """
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        """
        Clear all calculations from the history.
        """
        cls.history.clear()

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """
        Retrieve the full history of calculations.

        :return: List of Calculation instances.
        """
        return cls.history
