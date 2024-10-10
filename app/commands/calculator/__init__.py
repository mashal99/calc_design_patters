import sys
from decimal import Decimal, InvalidOperation
from app.calculator.operations import add, subtract, multiply, divide
from app.calculator.calculation_history import CalculationsHistory
from app.calculator.calculations import Calculation

class CalculatorCommand:
    def __init__(self, operation_func=None, a=0, b=0):
        self.operation_func = operation_func
        self.a = a
        self.b = b

    def execute(self):
        """Dynamically ask for input when executing the command."""
        try:
            # Prompt for the operation and validate it
            operation_name = input("Enter operation (add, subtract, multiply, divide, 'history', 'clear_history' or 'exit'): ").strip().lower()

            if operation_name == "exit":
                print("Returning to main menu...")
                return  # Exit the calculator and return to the main menu

            elif operation_name == "history":
                # Show calculation history
                self.display_history()

            elif operation_name == "clear_history":
                # Clear the calculation history
                self.clear_history()

            else:
                # Handle arithmetic operations
                self.handle_arithmetic_operations(operation_name)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_arithmetic_operations(self, operation_name):
        """Handles the arithmetic operations like add, subtract, etc."""
        self.operation_func = self.get_operation_function(operation_name)
        if not self.operation_func:
            print(f"Error: '{operation_name}' is not a valid operation. Exiting to main menu.")
            return  # Exit on invalid operation

        a = input("Enter first number: ").strip()
        b = input("Enter second number: ").strip()

        try:
            a_decimal, b_decimal = Decimal(a), Decimal(b)

            self.a = a_decimal
            self.b = b_decimal

            # Create a Calculation instance with the operation function
            calculation = Calculation(a_decimal, b_decimal, self.operation_func)

            # Get the result using the Calculation instance
            result = calculation.get_result()
            print(f"The result of {a} {operation_name} {b} is: {result}")

            # Add to history
            CalculationsHistory.add_calculation(calculation)

        except InvalidOperation:
            print(f"Invalid number input: '{a}' or '{b}' is not a valid number.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

    def display_history(self):
        """Displays the history of calculations."""
        history = CalculationsHistory.get_history()
        if history:
            print("\nCalculation History:")
            for calc in history:
                print(f"{calc.number_one} {calc.operation_func.__name__} {calc.number_two} = {calc.get_result()}")
        else:
            print("No calculations in history.")

    def clear_history(self):
        """Clears the history of calculations."""
        CalculationsHistory.clear_history()
        print("Calculation history cleared.")

    def get_operation_function(self, operation_name):
        """Return the corresponding operation function based on the operation name."""
        operations_map = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }
        return operations_map.get(operation_name)
