"""
This module defines the `App` class, which serves as the main interface for running the command-line
application. The app dynamically loads command modules (plugins) from the `plugins` directory, 
registers commands, and manages the REPL (Read, Evaluate, Print, Loop) that allows users to 
interact with various commands.

The `App` class supports:
- Dynamic loading of commands from the `plugins` directory.
- Manually registering the `MenuCommand`.
- Handling user input in a continuous loop, where users can execute commands or exit the app.

Modules used:
- `pkgutil`: For walking through packages and finding modules in the plugins directory.
- `importlib`: For dynamically importing plugin modules.
- `os`: For file path operations.
- `dotenv`: For loading environment variables from a `.env` file.
- `logging`: For logging application behavior and errors.
"""

import pkgutil
import importlib
import os
import logging
from dotenv import load_dotenv
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand
from app.commands import Command

# Load environment variables from the .env file
load_dotenv()

# Create 'log' folder if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging to write to a file in the 'log' folder
log_file = os.path.join('logs', 'app.log')
logging.basicConfig(
    level=logging.DEBUG if os.getenv("DEBUG") == "true" else logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),  # Log to file
        logging.StreamHandler()         # Log to console
    ]
)

class App:
    """
    The `App` class is responsible for loading and 
    registering commands, running the REPL (Read, Evaluate, 
    Print, Loop), and handling dynamic plugin loading.

    Attributes:
        command_handler (CommandHandler): 
        An instance of `CommandHandler` used to register and execute commands.
    """
    def __init__(self):
        self.command_handler = CommandHandler()
        self.environment = os.getenv("ENVIRONMENT", "production")
        self.debug = os.getenv("DEBUG", "false").lower() == 'true'
        
        # Log the startup message
        logging.info(f"App started in {self.environment} environment.")
        
        if self.debug:
            logging.debug("Debugging is enabled.")

    def load_plugins(self):
        """Dynamically load all command modules in the plugins directory, 
           including subdirectories."""
        plugins_package = 'app.plugins'
        package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins')

        # Walk through all modules and submodules in the plugins directory
        for module_finder, module_name, is_pkg in pkgutil.walk_packages([package_dir]):
            if not is_pkg and not module_name.startswith(plugins_package):
                continue

            full_module_name = f'{plugins_package}.{module_name.split(".")[-1]}'

            # Skip MenuCommand since it's manually registered
            if 'menu' in module_name:
                continue

            try:
                # Import the module dynamically
                module = importlib.import_module(full_module_name)
                # Iterate over the attributes in the module and look for Command subclasses
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    # Check if the attribute is a Command subclass
                    # (excluding the base Command class)
                    if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                        # Register the command using the module name (or directory name) as the command name
                        command_name = module_name.split('.')[-1].lower()
                        self.command_handler.register_command(command_name, attribute())
                logging.info(f"Loaded module: {full_module_name}")
            except ModuleNotFoundError as e:
                logging.error(f"Error loading module {full_module_name}: {e}")

    def run(self):
        """
        Starts the app's main loop, allowing users to 
        input commands. The REPL will continue to run until 
        the user enters the 'exit' command.

        - Registers the `MenuCommand` manually.
        - Loads dynamic plugins using the `load_plugins` method.
        - Continuously accepts and executes user input as commands.
        """
        # Manually register the MenuCommand with command_handler
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        # Load dynamic plugins (excluding MenuCommand)
        self.load_plugins()

        logging.info("Type 'exit' to exit.")
        while True:
            try:
                user_input = input(">>> ").strip()
                logging.debug(f"User input: {user_input}")
                self.command_handler.execute_command(user_input)
            except Exception as e:
                logging.error(f"Error executing command: {e}")
