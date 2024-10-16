from decimal import Decimal, InvalidOperation
import logging
from app.commands import Command
from app.calculator.operations import add, subtract, multiply, divide
from app.calculator.calculation_history import CalculationsHistory
from app.calculator.calculations import Calculation

# Configure logging
logger = logging.getLogger(__name__)

class CalculatorCommand(Command):
    """
    CalculatorCommand class handles arithmetic operations and calculation history.
    
    The CalculatorCommand class allows the user to dynamically input arithmetic operations, such as
    addition, subtraction, multiplication, and division, through the command-line interface. It also 
    supports retrieving and clearing the history of previous calculations.
    """
    def __init__(self, operation_func=None, num_one=0, num_two=0):
        self.operation_func = operation_func
        self.num_one = num_one
        self.num_two = num_two

    def execute(self, *args):
        """
        Dynamically ask for input when executing the command.
        
        Args:
            *args: Optional positional arguments.
        """
        try:
            operation_name = input(
                "Enter operation (add, subtract, multiply, divide"
                ", 'history', 'clear_history' or 'exit'): ").strip().lower()

            if operation_name == "exit":
                logger.info("User chose to exit the calculator.")
                print("Returning to main menu...")
                return  # Exit the calculator and return to the main menu

            if operation_name == "history":
                logger.info("User requested to view calculation history.")
                self.display_history()

            elif operation_name == "clear_history":
                logger.info("User requested to clear calculation history.")
                self.clear_history()

            else:
                logger.info(f"User selected '{operation_name}' operation.")
                self.handle_arithmetic_operations(operation_name)

        except InvalidOperation:
            logger.error("Invalid operation or input was encountered.")
            print("Invalid operation or input was encountered.")
        except ZeroDivisionError:
            logger.error("Division by zero is not allowed.")
            print("Error: Division by zero is not allowed.")
        except ValueError:
            logger.error("Invalid numeric value provided.")
            print("Error: Invalid numeric value provided.")
        except Exception as e:
            logger.critical(f"Critical error in execute method: {e}")
            print("Critical error occurred. Exiting...")

    def handle_arithmetic_operations(self, operation_name):
        """Handles the arithmetic operations like add, subtract, etc."""
        self.operation_func = self.get_operation_function(operation_name)
        if not self.operation_func:
            logger.warning(f"'{operation_name}' is not a valid operation.")
            print(f"Error: '{operation_name}' is not a valid operation. Exiting to main menu.")
            return  # Exit on invalid operation

        num_one = input("Enter first number: ").strip()
        num_two = input("Enter second number: ").strip()

        try:
            num_one_decimal, num_two_decimal = Decimal(num_one), Decimal(num_two)

            self.num_one = num_one_decimal
            self.num_two = num_two_decimal

            # Create a Calculation instance with the operation function
            calculation = Calculation(num_one_decimal, num_two_decimal, self.operation_func)

            # Get the result using the Calculation instance
            result = calculation.get_result()
            logger.info(f"Calculated result for {num_one} {operation_name} {num_two}: {result}")
            print(f"The result of {num_one} {operation_name} {num_two} is: {result}")

            # Add to history
            CalculationsHistory.add_calculation(calculation)
            logger.debug(f"Added calculation to history: {num_one} {operation_name} {num_two}")

        except InvalidOperation:
            logger.error(f"Invalid number input: '{num_one}' or '{num_two}' is not a valid number.")
            print(f"Invalid number input: '{num_one}' or '{num_two}' is not a valid number.")
        except ZeroDivisionError:
            logger.error("Division by zero is not allowed.")
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            logger.critical(f"Critical error in handle_arithmetic_operations: {e}")
            print("Critical error occurred. Exiting...")

    def display_history(self):
        """Displays the history of calculations."""
        history = CalculationsHistory.get_history()
        if history:
            logger.info("Displaying calculation history.")
            print("\nCalculation History:")
            for calc in history:
                result = calc.get_result()
                logger.debug(f"History: {calc.number_one} {calc.operation_func.__name__} {calc.number_two} = {result}")
                print(f"{calc.number_one} {calc.operation_func.__name__} {calc.number_two} = {result}")
        else:
            logger.info("No calculations in history.")
            print("No calculations in history.")

    def clear_history(self):
        """Clears the history of calculations."""
        CalculationsHistory.clear_history()
        logger.info("Calculation history cleared.")
        print("Calculation history cleared.")

    def get_operation_function(self, operation_name):
        """Return the corresponding operation function based on the operation name."""
        operations_map = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }
        operation_func = operations_map.get(operation_name)
        if operation_func:
            logger.debug(f"Mapped '{operation_name}' to function '{operation_func.__name__}'.")
        else:
            logger.warning(f"Invalid operation name: '{operation_name}'.")
        return operation_func
