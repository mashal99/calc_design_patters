import sys
from decimal import Decimal, InvalidOperation
from calculator.operations import add, subtract, multiply, divide  # Assuming operations are defined here

class CalculatorCommand:
    def __init__(self, operation_func, a, b):
        self.operation_func = operation_func
        self.a = a
        self.b = b

    def execute(self):
        """Execute the stored operation."""
        return self.operation_func(self.a, self.b)

def get_operation_function(operation_name):
    """Return the corresponding operation function based on the operation name."""
    operations_map = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    return operations_map.get(operation_name)

def calculate_and_print(a, b, operation_name):
    try:
        a_decimal, b_decimal = Decimal(a), Decimal(b)
        operation_func = get_operation_function(operation_name)

        if not operation_func:
            raise ValueError(f"Unknown operation: {operation_name}")

        command = CalculatorCommand(operation_func, a_decimal, b_decimal)
        result = command.execute()
        print(f"The result of {a} {operation_name} {b} is: {result}")

    except InvalidOperation:
        print(f"Invalid number input: '{a}' or '{b}' is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation_name = sys.argv
    calculate_and_print(a, b, operation_name)

if __name__ == '__main__':
    main()
