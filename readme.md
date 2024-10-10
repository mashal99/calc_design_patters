# Calculator Application

This project is a command-line application that follows the command pattern and supports dynamic plugin loading. The app allows users to interact with various commands via a REPL (Read, Evaluate, Print, Loop) interface. Commands are dynamically loaded from the plugins directory, which means new functionality can be added to the app without modifying the core codebase.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
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

