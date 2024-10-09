from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        """Display the available commands to the user."""
        print("\nAvailable commands:")
        for command in self.command_handler.get_registered_commands():
            print(f" - {command}")
