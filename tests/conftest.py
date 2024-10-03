import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

# Initialize Faker for generating test data
fake = Faker()

# Function to generate a set of random test data
def generate_random_test_cases(num_cases):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    # Generating random test cases with two numbers and an operation
    for _ in range(num_cases):
        number1 = Decimal(fake.random_number(digits=2))
        number2 = Decimal(fake.random_number(digits=2))
        operation_func = fake.random_element(elements=list(operations.values()))

        # Handle division cases where number2 is zero
        if operation_func == divide:
            number2 = Decimal('1') if number2 == Decimal('0') else number2
        
        # Perform the calculation and store expected result
        try:
            expected = operation_func(number1, number2)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield number1, number2, operation_func, expected

# Add pytest command-line option for specifying number of test cases
def pytest_addoption(parser):
    parser.addoption(
        "--test_cases", action="store", default=1000, type=int, help="Number of random test cases to generate"
    )

# Injecting the generated test data into test functions
def pytest_generate_tests(metafunc):
    # Only inject data into tests expecting 'a', 'b', 'operation', and 'expected' arguments
    if {"a", "b", "operation", "expected"}.issubset(metafunc.fixturenames):
        num_cases = metafunc.config.getoption("test_cases")
        random_test_data = list(generate_random_test_cases(num_cases))
        metafunc.parametrize("a,b,operation,expected", random_test_data)
