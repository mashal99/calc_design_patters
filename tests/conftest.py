"""
This module provides additional configuration for pytest to dynamically generate 
test cases based on command-line arguments, such as the number of records to generate.
"""

import random

# Add a pytest command-line option for generating records
def pytest_addoption(parser):
    """
    Adds a command-line option to pytest for specifying the number of records.
    """
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )


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
