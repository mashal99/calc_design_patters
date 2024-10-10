"""
This test suite verifies the functionality of the calculator app by simulating user inputs
and capturing the resulting outputs. Each test is designed to check different operations 
(addition, subtraction, multiplication, division, and invalid operations) as well as edge 
cases such as division by zero. The tests use the pytest framework to ensure correct behavior 
and exception handling in the app.

Test cases include:
1. Valid addition operation: Verifies that the calculator performs correct addition.
2. Valid subtraction operation: Verifies that the calculator performs correct subtraction.
3. Valid multiplication operation: Verifies that the calculator performs correct multiplication.
4. Valid division operation: Verifies that the calculator performs correct division.
5. Division by zero: Ensures the app handles division by zero appropriately.
6. Invalid operation: Verifies that an error message is 
        displayed when an invalid operation is entered.

All tests utilize the 'capfd' fixture to capture console output and the 'monkeypatch' fixture 
to simulate user inputs during the REPL (Read, Evaluate, Print, Loop).
"""

import pytest
from app import App

# Test the calculator command with a valid addition operation
def test_app_calculator_valid_addition(capfd, monkeypatch):
    """Test the 'calculator' command with a valid addition operation."""
    # Simulate user entering 'calculator', then 'add', then two numbers, followed by 'exit'
    inputs = iter(['calculator', 'add', '5', '10', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()
    # Capture the output of the REPL
    captured = capfd.readouterr()
    # Verify that the calculator performed the addition correctly
    assert "The result of 5 add 10 is: 15\n" in captured.out


# Test the calculator command with a valid subtraction operation
def test_app_calculator_subtraction(capfd, monkeypatch):
    """Test the 'calculator' command with a valid subtraction operation."""
    # Simulate user entering 'calculator', then 'subtract', then two numbers, followed by 'exit'
    inputs = iter(['calculator', 'subtract', '20', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()
    # Capture the output of the REPL
    captured = capfd.readouterr()
    # Verify that the calculator performed the subtraction correctly
    assert "The result of 20 subtract 5 is: 15\n" in captured.out


# Test the calculator command with a valid multiplication operation
def test_app_calculator_valid_multiplication(capfd, monkeypatch):
    """Test the 'calculator' command with a valid multiplication operation."""
    # Simulate user entering 'calculator', then 'multiply', then two numbers, followed by 'exit'
    inputs = iter(['calculator', 'multiply', '3', '4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()
    # Capture the output of the REPL
    captured = capfd.readouterr()
    # Verify that the calculator performed the multiplication correctly
    assert "The result of 3 multiply 4 is: 12\n" in captured.out


# Test the calculator command with a valid division operation
def test_app_calculator_valid_division(capfd, monkeypatch):
    """Test the 'calculator' command with a valid division operation."""
    # Simulate user entering 'calculator', then 'divide', then two numbers, followed by 'exit'
    inputs = iter(['calculator', 'divide', '10', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()
    # Capture the output of the REPL
    captured = capfd.readouterr()
    # Verify that the calculator performed the division correctly
    assert "The result of 10 divide 2 is: 5\n" in captured.out


# Test the calculator command with division by zero
def test_app_calculator_division_by_zero(capfd, monkeypatch):
    """Test the 'calculator' command with division by zero."""
    # Simulate user entering 'calculator', then 'divide',
    # then two numbers (10 and 0), followed by 'exit'
    inputs = iter(['calculator', 'divide', '10', '0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()
    # Capture the output of the REPL
    captured = capfd.readouterr()
    # Verify that division by zero was handled correctly
    assert "Error: Division by zero is not allowed.\n" in captured.out


# Test the calculator command with an invalid operation
def test_app_calculator_invalid_operation(capfd, monkeypatch):
    """Test the 'calculator' command with an invalid operation."""
    # Simulate user entering 'calculator', then an invalid operation, followed by 'exit'
    inputs = iter(['calculator', 'modulo', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()
    # Capture the output of the REPL
    captured = capfd.readouterr()
    # Verify that an error message was shown for the invalid operation
    assert "Error: 'modulo' is not a valid operation. Exiting to main menu.\n" in captured.out
