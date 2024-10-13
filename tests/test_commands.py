"""
This test suite verifies the functionality of the `greet` 
and `goodbye` commands in the app, as well as
how the REPL (Read, Evaluate, Print, Loop) interface handles these commands. The tests simulate user 
input, capture output, and check that the correct responses are displayed for each command.

Test cases include:

1. **Testing the `GreetCommand`**:
    - Directly tests the `GreetCommand` to ensure it 
        prints the expected greeting message: "Hello, World!".

2. **Testing the `GoodbyeCommand`**:
    - Directly tests the `GoodbyeCommand` to ensure 
        it prints the expected farewell message: "Goodbye".

3. **Testing the 'greet' Command in the REPL**:
    - Simulates the user entering the 'greet' command within the REPL, followed by 'exit'.
    - Verifies that the REPL outputs the correct greeting message and exits gracefully.

4. **Testing the 'menu' Command in the REPL**:
    - Simulates the user entering the 'menu' command 
        within the REPL, followed by 'exit'.
    - Verifies that the REPL lists available commands and exits gracefully.

Each test uses the `capfd` fixture to capture console 
output and the `monkeypatch` fixture to simulate user input.
The tests expect a `SystemExit` exception to be raised 
when the 'exit' command is entered, ensuring the REPL
terminates correctly.
"""

import pytest
from app import App
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand


# Helper function to avoid code repetition
def run_app_with_input(monkeypatch, capfd, inputs):
    """Helper function to run the App with simulated inputs and capture the output."""
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.run()
    return capfd.readouterr()


def test_greet_command(capfd):
    """Test that the GreetCommand prints the expected greeting."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()  # Unpack the output
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"


def test_goodbye_command(capfd):
    """Test that the GoodbyeCommand prints the expected farewell message."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()  # Unpack the output
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"


def test_app_greet_command(monkeypatch, capfd):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])
    out, _ = run_app_with_input(monkeypatch, capfd, inputs)
    assert "Hello, World!" in out, "'greet' command did not print the expected message"


def test_app_menu_command(monkeypatch, capfd):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    out, _ = run_app_with_input(monkeypatch, capfd, inputs)
    assert "Available commands" in out, "'menu' command did not list available commands"
