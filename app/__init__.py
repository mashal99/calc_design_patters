from app.commands import CommandHandler

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
    
    def run(self):


        while True:
            #Using REPL
            self.command_handler.execute_command(input(">>> "))