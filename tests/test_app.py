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

# Test that the REPL exits correctly on the 'exit' command
def test_app_start_exit_command(monkeypatch, capfd, run_app_with_input):
    """Test that the REPL exits correctly on 'exit' command."""
    inputs = iter(['exit'])  # Simulate user entering 'exit'
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert captured is not None  # SystemExit is expected

# Test how the REPL handles an unknown command before exiting
def test_app_start_unknown_command(capfd, monkeypatch, run_app_with_input):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])  # Simulate unknown command and 'exit'
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert ("Command 'unknown_command' not found. Type 'menu' to see available commands.\n"
            in captured.out)

# Test that the 'menu' command displays the available commands
def test_app_menu_command(capfd, monkeypatch, run_app_with_input):
    """Test the 'menu' command to verify it displays the available commands."""
    inputs = iter(['menu', 'exit'])  # Simulate user entering 'menu', followed by 'exit'
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert ("Available commands:\n - menu\n - calculator\n"
            " - exit\n - goodbye\n - greet\n" in captured.out)

# Test the 'greet' command
def test_app_greet_command(capfd, monkeypatch, run_app_with_input):
    """Test the 'greet' command to ensure it outputs the greeting message."""
    inputs = iter(['greet', 'exit'])  # Simulate user entering 'greet', followed by 'exit'
    captured = run_app_with_input(monkeypatch, capfd, inputs)
    assert "Hello, World!\n" in captured.out
