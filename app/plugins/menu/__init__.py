"""
Module: menu_command

This module defines the `MenuCommand` class, which is used to display a list of available
commands to the user. It inherits from the `Command` abstract base class and relies on
the command handler to retrieve the list of registered commands.
"""
from app.commands import Command

class MenuCommand(Command):
    """
    MenuCommand class for displaying available commands.

    This command displays a list of all registered commands when executed, providing users
    with an overview of what commands they can use.
    
    Attributes:
        command_handler (CommandHandler): The command handler that manages registered commands.
    """

    def __init__(self, command_handler):
        """
        Initialize the MenuCommand with a command handler.

        Args:
            command_handler (CommandHandler): The handler responsible for managing the commands.
        """
        self.command_handler = command_handler

    def execute(self, *args):
        """
        Execute the menu command, displaying the available commands.

        Args:
            *args: Optional positional arguments.

        Returns:
            None
        """
        print("\nAvailable commands:")
        for command in self.command_handler.get_registered_commands():
            print(f" - {command}")
