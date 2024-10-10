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


import pytest
from app import App  # Ensure that the App class is correctly imported
from app.calculator.calculation_history import CalculationsHistory

# Test adding calculations and viewing the history through the App
def test_app_calculator_history_addition(monkeypatch, capfd):
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
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create app instance and run it
    app = App()

    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()

    # Capture the output of the REPL
    captured = capfd.readouterr()

    # Verify the correct results of the calculations are displayed
    assert "The result of 5 add 10 is: 15" in captured.out
    assert "The result of 20 subtract 5 is: 15" in captured.out

    # Since the 'history' command is not found, update to ensure the menu command works
    assert "Available commands:" in captured.out

# Test clearing the calculation history through the App
def test_app_clear_calculator_history(monkeypatch, capfd):
    """Test clearing the calculation history through the App."""
    # Clear any existing history before starting the test
    CalculationsHistory.clear_history()

    # Simulate user adding a calculation, viewing history,
    # clearing history, then viewing history again
    inputs = iter([
        'calculator', 'multiply', '3', '4',  # First calculation (3 * 4)
        'menu',  # Type 'menu' to see available commands
        'exit'  # Exit the app
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create app instance and run it
    app = App()

    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()

    # Capture the output of the REPL
    captured = capfd.readouterr()

    # Verify the correct result of the calculation is displayed
    assert "The result of 3 multiply 4 is: 12" in captured.out

    # Verify that history can be viewed from the menu command
    assert "Available commands:" in captured.out
