"""
Module: main

This script initializes and runs the main application by creating an instance of the `App` class 
and invoking its `run` method. 
The `App` class is responsible for loading plugins, handling commands, 
and managing the application's core logic.
"""
from app import App

if __name__ == "__main__":
    App().run()  # Run the app without assigning the return since it's not needed.
