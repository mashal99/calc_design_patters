import pytest
import random

# Add a pytest command-line option for generating records
def pytest_addoption(parser):
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )

# Generate the test data based on the --num_records argument
def pytest_generate_tests(metafunc):
    num_records = metafunc.config.getoption("num_records")
    if "a" in metafunc.fixturenames and "b" in metafunc.fixturenames and "operation" in metafunc.fixturenames and "expected_result" in metafunc.fixturenames:
        operations = ['add', 'subtract', 'multiply', 'divide']
        test_data = []

        for _ in range(num_records):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            operation = random.choice(operations)

            if operation == 'add':
                expected_result = a + b
            elif operation == 'subtract':
                expected_result = a - b
            elif operation == 'multiply':
                expected_result = a * b
            elif operation == 'divide':
                b = b if b != 0 else 1  # avoid division by zero
                expected_result = a / b

            test_data.append((a, b, operation, expected_result))

        metafunc.parametrize("a, b, operation, expected_result", test_data)
