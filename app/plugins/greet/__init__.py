"""
Module: greet_command

This module defines the `GreetCommand` class, which is used to print a greeting message
when executed. It inherits from the `Command` abstract base class.
"""
from app.commands import Command

class GreetCommand(Command):
    """
    GreetCommand class for printing a greeting message.

    This command prints a simple greeting message ('Hello, World!') when executed.
    """

    def execute(self, *args):
        """
        Execute the greet command, printing a greeting message.

        Args:
            *args: Optional positional arguments.

        Returns:
            None
        """
        print("Hello, World!")
