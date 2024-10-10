"""
Module: exit_command

This module defines the `ExitCommand` class, which is used to gracefully exit the application
by invoking the system's exit method. It inherits from the `Command` abstract base class.
"""
import sys
from app.commands import Command

class ExitCommand(Command):
    """
    ExitCommand class for exiting the application.

    This command executes a system exit, terminating the program with an exit message.
    """

    def execute(self, *args):
        """
        Execute the exit command, terminating the program.

        Args:
            *args: Optional positional arguments.

        Returns:
            None
        """
        sys.exit("Exiting...")
