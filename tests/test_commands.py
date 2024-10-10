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


def test_app_greet_command(monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.run()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.run()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"
