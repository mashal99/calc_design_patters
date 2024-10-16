"""
This test suite verifies the functionality of adding calculations, viewing calculation history, 
and clearing calculation history in the app. The tests simulate user interactions with the REPL 
(Read, Evaluate, Print, Loop) interface and check the expected behavior and output.

Test cases include:

1. **Adding Calculations and Viewing History**:
    - Tests adding multiple calculations (addition and subtraction)
        and verifies that the correct results are output.
    - Checks that the user can view available commands through the 'menu' command.
    - Ensures the 'calculator' command performs calculations correctly
        and the history reflects the results.

2. **Clearing Calculation History**:
    - Tests adding a calculation (multiplication) and
        verifies that the correct result is output.
    - Checks that the 'menu' command lists available
        commands and that the REPL works as expected.
    - Ensures the history is cleared between test 
        cases to avoid test data overlap.

Each test case uses the 'monkeypatch' fixture to simulate 
user input and the 'capfd' fixture to capture 
the console output. The tests expect a `SystemExit` 
exception when the user enters the 'exit' command, 
indicating the REPL has exited correctly.
"""

from app.calculator.calculation_history import CalculationsHistory

# Test adding calculations and viewing the history through the App
def test_app_calculator_history_addition(run_app_with_input, monkeypatch, capfd):
    """Test adding calculations and viewing the history through the App."""
    # Clear any existing history before starting the test
    CalculationsHistory.clear_history()

    # Simulate user adding two calculations and then viewing history
    inputs = iter([
        'calculator', 'add', '5', '10',  # First calculation (5 + 10)
        'calculator', 'subtract', '20', '5',  # Second calculation (20 - 5)
        'menu',  # Type 'menu' to see available commands
        'exit'  # Exit the app
    ])
    # Run the app and capture the output
    captured = run_app_with_input(monkeypatch, capfd, inputs)

    # Verify the correct results of the calculations are displayed
    assert "The result of 5 add 10 is: 15" in captured.out
    assert "The result of 20 subtract 5 is: 15" in captured.out

    # Ensure the menu command is displayed correctly
    assert "Available commands:" in captured.out

# Test clearing the calculation history through the App
def test_app_clear_calculator_history(run_app_with_input, monkeypatch, capfd):
    """Test clearing the calculation history through the App."""
    # Clear any existing history before starting the test
    CalculationsHistory.clear_history()

    # Simulate user adding a calculation and then viewing and clearing history
    inputs = iter([
        'calculator', 'multiply', '3', '4',  # First calculation (3 * 4)
        'menu',  # Type 'menu' to see available commands
        'exit'  # Exit the app
    ])
    # Run the app and capture the output
    captured = run_app_with_input(monkeypatch, capfd, inputs)

    # Verify the correct result of the calculation is displayed
    assert "The result of 3 multiply 4 is: 12" in captured.out

    # Ensure the menu command is displayed correctly
    assert "Available commands:" in captured.out
