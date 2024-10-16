# Calculator Application

This project is a command-line application that follows the command pattern and supports dynamic plugin loading. The app allows users to interact with various commands via a REPL (Read, Evaluate, Print, Loop) interface. Commands are dynamically loaded from the plugins directory, which means new functionality can be added to the app without modifying the core codebase.

Additionally, the project now includes GitHub Actions for automated testing, environment variables for secure input handling, and logging for tracking application behavior and performance.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Environment Variables](#environment-variables)
- [GitHub Actions (CI)](#github-actions)
- [Logging](#logging)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

### Prerequisites
- Python 3.11 or higher
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository**:
   ```bash
   git clone hhttps://github.com/mashal99/calc_design_patters.git
   cd calc_design_patters
2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install the required dependencies**:
   Install the necessary dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt

## Usage

To use the calculator application, you can run the `main.py` script. The script accepts three command-line arguments: two numbers and the operation to perform.

### Example Usage
```bash
python main.py
>>> menu
Available commands:
 - greet
 - goodbye
 - calculator
 - exit
>>> greet
Hello, World!
>>> exit
Exiting...
```
# Output: The result of 10 add 5 is: 15
Supported operations:
- `add`
- `subtract`
- `multiply`
- `divide`

## Exception Handling

The application is designed to handle common exceptions:
- **InvalidOperation**: Raised if non-numeric inputs are provided.
- **ZeroDivisionError**: Raised if a division by zero is attempted.
- **ValueError**: Raised if an invalid operation is provided.

## Testing

This project uses Pytest to handle unit testing. The tests are dynamically generated based on a specified number of test cases. You can run the tests with the following command:

### Running Tests:
```bash
pytest --num_records=<number_of_tests>
```

### Example:
```bash
pytest --num_records=100
```

## Environment Variables
Environment variables are essential for securely managing sensitive data like API keys, passwords, and other inputs that shouldn't be hardcoded into the project or pushed to version control.

### Setting up Environment Variables
Create a .env file in the root directory of the project.
```bash
ENVIRONMENT=development
DEBUG=true
```

## Logging
Logging is a crucial aspect of any application, especially in a dynamic environment like this one. It helps in tracking the application's behavior, performance, and debugging issues.

### Logging Levels
- **DEBUG**: Detailed information, typically of interest only when diagnosing problems.
- **INFO**: Confirmation that things are working as expected.
- **WARNING**: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., 'disk space low'). The software is still working as expected.
- **ERROR**: Due to a more serious problem, the software has not been able to perform some function.
- **CRITICAL**: A serious

### How to use logging
```python
import logging

logging.basicConfig(filename='app/logs/app.log', level=logging.INFO)

logging.info("Application has started")
logging.error("An error occurred")
```
Logs are stored in the app/logs/app.log file. You can view this file to track what’s happening in the application, including user inputs, command executions, and errors.

## GitHub Actions (CI)
GitHub Actions is a powerful tool for automating workflows and tasks in your project. In this project, GitHub Actions are used for Continuous Integration (CI).

### How to Use GitHub Actions:
- **Push Changes to GitHub:** After pushing changes to your repository, GitHub Actions will automatically run the tests defined in your test suite.
- **View Results:** Go to the "Actions" tab on the GitHub repository to view the results of the automated tests. You'll be able to see which tests passed or failed and view logs for further investigation.



## Project Structure
├── app/
│   ├── __init__.py            # Main app entry point
│   ├── calculator/            # Calculator-specific logic
│   ├── commands/              # Command handler and command-related logic
│   ├── plugins/               # Plugin directory for dynamic commands
├── tests/                     # Unit tests for the app and its components
│   ├── test_app.py            # Test for the main App class
│   ├── test_commands.py       # Test for individual commands
│   ├── test_calculator.py     # Test for the calculator functionality
│   └── ...
├── requirements.txt           # Project dependencies
└── README.md                  # This file


## Features
- REPL Interface: A user-friendly command-line interface that supports multiple commands.
- Dynamic Plugin Loading: Commands (or plugins) are loaded dynamically from the plugins directory.
- Command Pattern: Follows the command pattern design for organizing commands and their execution.
- Commands Included:
    - GreetCommand: Prints "Hello, World!".
    - GoodbyeCommand: Prints "Goodbye".
    - MenuCommand: Lists all available commands.
    - CalculatorCommand: Handles basic arithmetic operations (addition, subtraction, multiplication, division).
    - History: Keeps track of previous calculations and can clear history.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
## Acknowledgments
- This project was created as a learning exercise for Python and testing.
- Special thanks to the Python community for their contributions and resources.
Feel free to customize this README to match your project's specific details and requirements.

