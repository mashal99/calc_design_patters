from abc import ABC, abstractclassmethod

class Command(ABC):
    @abstractclassmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command_callable):
        """Register a command with the given name and associated callable."""
        self.commands[name] = command_callable

    def execute_command(self, name, *args):
        """Execute the registered command if it exists."""
        if name in self.commands:
            command_callable = self.commands[name]
            if callable(command_callable.execute):
                return command_callable.execute(*args)
            else:
                print(f"{name} is not callable")
        else:
            print(f"Command '{name}' not found. Type 'menu' to see available commands.")

    def get_registered_commands(self):
        """Return the list of registered command names."""
        return self.commands.keys()

