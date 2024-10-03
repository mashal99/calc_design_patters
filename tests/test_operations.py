import pytest
from calculator.operations import add, subtract, multiply, divide

def test_operations(a, b, operation, expected_result):
    """Test multiple operations using the dynamically generated test data."""
    if operation == 'add':
        assert add(a, b) == expected_result
    elif operation == 'subtract':
        assert subtract(a, b) == expected_result
    elif operation == 'multiply':
        assert multiply(a, b) == expected_result
    elif operation == 'divide':
        assert divide(a, b) == expected_result
