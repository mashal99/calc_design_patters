"""
This module provides additional configuration for pytest to dynamically generate 
test cases based on command-line arguments, such as the number of records to generate.
"""

import random
import pytest
from app import App

# Add a pytest command-line option for generating records
def pytest_addoption(parser):
    """
    Adds a command-line option to pytest for specifying the number of records.
    """
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )


@pytest.fixture
def run_app_with_input():
    """
    Provides a helper function for running the App with mocked user inputs 
    and capturing REPL output during tests.

    This function is designed to be used in test cases where the App's REPL 
    (Read-Eval-Print Loop) is tested. It accepts a sequence of user inputs, 
    runs the App, and captures the output to verify the behavior of the commands.

        The helper function makes use of pytest fixtures for mocking input (`monkeypatch`)
        and capturing output (`capfd`).

        Returns:
            _run_app_with_input (function): 
                A nested function that accepts the `monkeypatch`, `capfd`, and `inputs` 
                as arguments, runs the App, and captures REPL output for further 
                assertions in test cases.
    """
    def _run_app_with_input(monkeypatch, capfd, inputs):
        """
        Helper function to run the App with mocked user inputs and capture REPL output.

        Args:
            monkeypatch: Fixture to mock built-in input.
            capfd: Fixture to capture output from the REPL.
            inputs: Iterable containing user inputs to be fed into the REPL.

        Returns:
            The captured output of the REPL.
        """
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        app = App()
        with pytest.raises(SystemExit):
            app.run()
        captured = capfd.readouterr()
        return captured
    return _run_app_with_input



def pytest_generate_tests(metafunc):
    """
    Dynamically generates test cases based on the --num_records argument.

    This function intercepts pytest's test generation process and uses the specified number
    of records to create test cases dynamically. It generates random numbers and operations,
    which are used to test different arithmetic functions.

    Args:
        metafunc (Metafunc): Pytest's metafunc object, 
                            which provides information about the test function
                             being executed, including its parameters and options.
    """
    num_records = metafunc.config.getoption("num_records")
    # Only parametrize if all required parameters are in the test function
    if "first_num" in metafunc.fixturenames and "second_num" in metafunc.fixturenames and \
       "operation" in metafunc.fixturenames and "expected_result" in metafunc.fixturenames:
        operations = ['add', 'subtract', 'multiply', 'divide']
        test_data = []

        for _ in range(num_records):
            first_num = random.randint(1, 100)
            second_num = random.randint(1, 100)
            operation = random.choice(operations)

            expected_result = None

            if operation == 'add':
                expected_result = first_num + second_num
            elif operation == 'subtract':
                expected_result = first_num - second_num
            elif operation == 'multiply':
                expected_result = first_num * second_num
            elif operation == 'divide':
                second_num = second_num if second_num != 0 else 1  # Avoid division by zero
                expected_result = first_num / second_num

            # Add the generated data to the test cases
            test_data.append((first_num, second_num, operation, expected_result))

        # Parametrize the test function with the generated test data
        metafunc.parametrize("first_num, second_num, operation, expected_result", test_data)
