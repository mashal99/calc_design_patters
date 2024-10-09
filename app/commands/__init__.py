from abc import ABC, classmethod

class Command(ABC):
    @classmethod
    def execute(SELF):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"Command '{command_name}' not found.")
