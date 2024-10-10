import pkgutil
import importlib
import os
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand
from app.commands import Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """Dynamically load all command modules in the plugins directory, including subdirectories."""
        plugins_package = 'app.plugins'
        package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins')

        # Walk through all modules and submodules in the plugins directory
        for finder, module_name, is_pkg in pkgutil.walk_packages([package_dir], f'{plugins_package}.'):
            # Filter out non-module directories or unintended files
            if not is_pkg and not module_name.startswith(plugins_package):
                continue

            full_module_name = f'{plugins_package}.{module_name.split(".")[-1]}'
            # print(f"Loading module: {full_module_name}")  # Debugging line to see what's being loaded

            # Skip MenuCommand since it's manually registered
            if 'menu' in module_name:
                continue

            try:
                # Import the module dynamically
                module = importlib.import_module(full_module_name)
                
                # Iterate over the attributes in the module and look for Command subclasses
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    # Check if the attribute is a Command subclass (excluding the base Command class)
                    if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                        # Register the command using the module name (or directory name) as the command name
                        command_name = module_name.split('.')[-1].lower()
                        self.command_handler.register_command(command_name, attribute())
            except ModuleNotFoundError as e:
                print(f"Error loading module {full_module_name}: {e}")

    def run(self):
        # Manually register the MenuCommand with command_handler
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        
        # Load dynamic plugins (excluding MenuCommand)
        self.load_plugins()

        print("Type 'exit' to exit.")
        while True:  # REPL: Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())
