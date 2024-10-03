"""
Test module for verifying the functionality of the arithmetic operations.

This module tests the core functions for basic arithmetic (add, subtract, multiply, divide)
using dynamically generated test data. The test data is provided via pytest fixtures and is 
used to assert the correct behavior of these functions.
"""

from calculator.operations import add, subtract, multiply, divide

def test_operations(first_num, second_num, operation, expected_result):
    """
    Test the arithmetic operations using dynamic test data.

    This function receives dynamically generated test data, which includes two numbers (`a`
    and `b`), the operation to perform (`operation`), and the expected result (`expected_result`).
    It then performs the corresponding arithmetic operation 
        and asserts that the result matches the expectation.

    Args:
        a (Decimal): The first number in the operation.
        b (Decimal): The second number in the operation.
        operation (str): The operation to be performed ('add', 'subtract', 'multiply', or 'divide').
        expected_result (Decimal): The expected result of the operation.
    
    Raises:
        AssertionError: If the result of the operation does not match the expected result.
    """
    if operation == 'add':
        assert add(first_num, second_num) == expected_result
    elif operation == 'subtract':
        assert subtract(first_num, second_num) == expected_result
    elif operation == 'multiply':
        assert multiply(first_num, second_num) == expected_result
    elif operation == 'divide':
        assert divide(first_num, second_num) == expected_result
