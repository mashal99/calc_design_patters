"""
Module: goodbye_command

This module defines the `GoodbyeCommand` class, which is used to print a goodbye message
when executed. It inherits from the `Command` abstract base class.
"""
from app.commands import Command

class GoodbyeCommand(Command):
    """
    GoodbyeCommand class for printing a farewell message.

    This command prints a simple goodbye message when executed.
    """

    def execute(self, *args):
        """
        Execute the goodbye command, printing a farewell message.

        Args:
            *args: Optional positional arguments.

        Returns:
            None
        """
        print("Goodbye")
