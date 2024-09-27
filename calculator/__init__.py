from calculator.calculations import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a, b, add)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)  # Pass the subtract function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def multiply(a,b):
        calculation = Calculation(a, b, multiply)  # Pass the multiply function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)  # Pass the divide function from calculator.operations
        return calculation.get_result()