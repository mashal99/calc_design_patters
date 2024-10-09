import sys
from decimal import Decimal, InvalidOperation
from app.calculator.operations import add, subtract, multiply, divide

class CalculatorCommand:
    def __init__(self, operation_func=None, a=0, b=0):
        self.operation_func = operation_func
        self.a = a
        self.b = b

    def execute(self):
        """Dynamically ask for input when executing the command."""
        try:
            # Prompt for the operation and numbers
            operation_name = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
            a = input("Enter first number: ").strip()
            b = input("Enter second number: ").strip()

            # Convert inputs to Decimal
            a_decimal, b_decimal = Decimal(a), Decimal(b)

            # Get the operation function
            self.operation_func = self.get_operation_function(operation_name)
            if not self.operation_func:
                raise ValueError(f"Unknown operation: {operation_name}")

            # Set the values for the operation
            self.a = a_decimal
            self.b = b_decimal

            # Perform the calculation and return the result
            result = self.operation_func(self.a, self.b)
            print(f"The result of {a} {operation_name} {b} is: {result}")
            return result

        except InvalidOperation:
            print(f"Invalid number input: '{a}' or '{b}' is not a valid number.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_operation_function(self, operation_name):
        """Return the corresponding operation function based on the operation name."""
        operations_map = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }
        return operations_map.get(operation_name)
