"""
This test suite verifies the functionality of the REPL (Read, Evaluate, Print, Loop) in the app.
Each test simulates user input, captures the output, and checks whether the correct behavior occurs.
The suite uses the pytest framework with the 'monkeypatch' 
fixture to simulate user input and the 'capfd' fixture to capture console output.

Test cases include:

1. **REPL Exit on 'exit' Command**:
    - Verifies that the REPL exits gracefully when the 'exit' command is entered.
    
2. **Handling Unknown Commands**:
    - Tests how the REPL handles unknown or invalid commands and 
      verifies that an appropriate error message is displayed before exiting.

3. **'Menu' Command Functionality**:
    - Checks that the 'menu' command correctly lists
        all available commands, including dynamically loaded commands.
    
4. **'Greet' Command Functionality**:
    - Ensures that the 'greet' command outputs the expected greeting message.

Each test creates an instance of the app and 
uses 'monkeypatch' to simulate a sequence of user inputs 
(e.g., entering commands like 'exit', 'menu', or 'greet'). 
The tests also expect a `SystemExit` to be raised when the REPL encounters the 'exit' command, 
and the 'capfd' fixture captures the output to verify that the commands behave as expected.
"""

import pytest
from app import App

# Test that the REPL exits correctly on the 'exit' command
def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit) as e:
        app.run()
    # Check that the exit command triggered a SystemExit
    assert e.type == SystemExit


# Test how the REPL handles an unknown command before exiting
def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()
    # Capture the output of the REPL
    captured = capfd.readouterr()
    # Verify that the unknown command was handled properly
    assert ("Command 'unknown_command' not found. Type 'menu' to see available commands.\n"
        in captured.out)



# Test that the 'menu' command displays the available commands
def test_app_menu_command(capfd, monkeypatch):
    """Test the 'menu' command to verify it displays the available commands."""
    # Simulate user entering 'menu', followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()
    # Capture the output of the REPL
    captured = capfd.readouterr()
    # Verify that the 'menu' command listed all available commands, including 'goodbye'
    assert ("Type 'exit' to exit.\n\nAvailable commands:\n - menu\n - calculator\n"
        " - exit\n - goodbye\n - greet\n" in captured.out)



# Test the 'greet' command
def test_app_greet_command(capfd, monkeypatch):
    """Test the 'greet' command to ensure it outputs the greeting message."""
    # Simulate user entering 'greet', followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Create app instance
    app = App()
    # Expect the REPL to raise SystemExit when 'exit' is entered
    with pytest.raises(SystemExit):
        app.run()
    # Capture the output of the REPL
    captured = capfd.readouterr()
    # Verify that the 'greet' command output the greeting message
    assert "Hello, World!\n" in captured.out
    