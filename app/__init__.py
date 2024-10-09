from app.commands import CommandHandler
from app.commands.calculator import CalculatorCommand
from app.commands.exit import ExitCommand
from app.commands.greet import GreetCommand


class App:
    def __init__(self):
        self.command_handler = CommandHandler()
    
    def run(self):
        # Register commands
        self.command_handler.register_command("calculator", CalculatorCommand())
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("exit", ExitCommand())

        while True:
            # Using REPL
            self.command_handler.execute_command(input(">>> "))