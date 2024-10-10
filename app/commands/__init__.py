"""
This module defines a command pattern framework for registering and executing commands.

The framework includes an abstract `Command` class that defines a common interface for all commands 
and a `CommandHandler` class to manage the registration and execution of these commands. 

### Classes:
- `Command`:
  An abstract base class that requires concrete implementations to define an `execute` method. 
  It serves as a template for creating various commands in the application.

- `CommandHandler`:
  A manager class that allows registering commands with a 
  name and an associated callable. It provides methods 
  to execute these commands by name, handling errors 
  appropriately when a command cannot be executed. This 
  class also allows querying the available commands.

### Usage Example:
```python
# Define a custom command by subclassing Command
class PrintCommand(Command):
    def execute(self, message):
        print(f"Executing PrintCommand: {message}")

# Create a CommandHandler instance
handler = CommandHandler()

# Register the command
handler.register_command('print', PrintCommand())

# Execute the command by name
handler.execute_command('print', 'Hello, World!')
"""

from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for commands in the application.
    
    The Command class defines a common interface for all commands, enforcing the implementation
    of the 'execute' method in subclasses. This ensures that any concrete command class will
    have an 'execute' method that can be called with the appropriate arguments.
    """
    @abstractmethod
    def execute(self, *args):
        """
        Execute the command.

        This method should be overridden by any class inheriting from Command. It defines
        the behavior that occurs when the command is executed.

        Args:
            cls (type): Class of the command being executed.
            self (instance): The instance on which the command is being executed.

        Returns:
            None
        """
        #pass


class CommandHandler:
    """
    CommandHandler class manages the registration and execution of commands.
    
    The CommandHandler class allows registering commands with a name and callable,
    executing those commands by name, and handling any errors that may occur during
    the execution process. It also provides a method to list all registered commands.
    """
    def __init__(self):
        """
        Initialize a new CommandHandler instance.

        This method initializes the 'commands' dictionary, which maps command names to
        their associated callable functions.

        Attributes:
            commands (dict): A dictionary mapping command names (str) to command callables.
        """
        self.commands = {}

    def register_command(self, name, command_callable):
        """
        Register a new command with the CommandHandler.

        This method associates a command name with a callable that implements the command.
        The callable is expected to implement an 'execute' method.

        Args:
            name (str): The name of the command to register.
            command_callable (Command): A callable that implements the 'execute' method.
        
        Returns:
            None
        """
        self.commands[name] = command_callable

    def execute_command(self, name, *args):
        """
        Execute a registered command by name, passing any additional arguments.

        This method attempts to execute the command associated with the given name. If the 
        command is not found or does not have an 'execute' method, appropriate error messages 
        will be printed.

        Args:
            name (str): The name of the command to execute.
            *args: Additional arguments to pass to the command's 'execute' method.

        Returns:
            None
        """
        try:
            command_callable = self.commands[name]
            # Try to call the 'execute' method of the command
            command_callable.execute(*args)
        except KeyError:
            # Handle the case where the command is not found
            print(f"Command '{name}' not found. Type 'menu' to see available commands.")
        except AttributeError:
            # Handle the case where the 'execute' method is missing or not callable
            print(f"The command '{name}' cannot be executed.")
        except TypeError as e:
            # Handle incorrect number or type of arguments passed
            print(f"Command '{name}' failed due to a type error: {e}")



    def get_registered_commands(self):
        """
        Get the names of all registered commands.

        This method returns the list of all command names that have been registered
        with the CommandHandler.

        Returns:
            dict_keys: A view of the command names in the 'commands' dictionary.
        """
        return self.commands.keys()
