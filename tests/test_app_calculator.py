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

# Test the calculator command with a valid addition operation
def test_app_calculator_valid_addition(run_app_with_input, monkeypatch, capfd):
    """Test the 'calculator' command with a valid addition operation."""
    inputs = iter(['calculator', 'add', '5', '10', 'exit'])
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert "The result of 5 add 10 is: 15\n" in captured.out


# Test the calculator command with a valid subtraction operation
def test_app_calculator_subtraction(run_app_with_input, monkeypatch, capfd):
    """Test the 'calculator' command with a valid subtraction operation."""
    inputs = iter(['calculator', 'subtract', '20', '5', 'exit'])
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert "The result of 20 subtract 5 is: 15\n" in captured.out


# Test the calculator command with a valid multiplication operation
def test_app_calculator_valid_multiplication(run_app_with_input, monkeypatch, capfd):
    """Test the 'calculator' command with a valid multiplication operation."""
    inputs = iter(['calculator', 'multiply', '3', '4', 'exit'])
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert "The result of 3 multiply 4 is: 12\n" in captured.out


# Test the calculator command with a valid division operation
def test_app_calculator_valid_division(run_app_with_input, monkeypatch, capfd):
    """Test the 'calculator' command with a valid division operation."""
    inputs = iter(['calculator', 'divide', '10', '2', 'exit'])
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert "The result of 10 divide 2 is: 5\n" in captured.out


# Test the calculator command with division by zero
def test_app_calculator_division_by_zero(run_app_with_input, monkeypatch, capfd):
    """Test the 'calculator' command with division by zero."""
    inputs = iter(['calculator', 'divide', '10', '0', 'exit'])
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert "Error: Division by zero is not allowed.\n" in captured.out


# Test the calculator command with an invalid operation
def test_app_calculator_invalid_operation(run_app_with_input, monkeypatch, capfd):
    """Test the 'calculator' command with an invalid operation."""
    inputs = iter(['calculator', 'modulo', 'exit'])
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert "Error: 'modulo' is not a valid operation. Exiting to main menu.\n" in captured.out
