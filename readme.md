# Calculator Application

This project is a Python-based calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division). The application is designed to be tested using Pytest and is capable of dynamically generating test cases based on user-defined parameters.

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
   git clone https://github.com/yourusername/calc-app.git
   cd calc-app
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
python main.py <number1> <number2> <operation>
```
### Example:
```bash
python main.py 10 5 add
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

## Project
Structure
- `main.py`: The main script that runs the calculator application.
- `tests/`: Directory containing unit tests.
- `requirements.txt`: List of required Python packages.
- `README.md`: This documentation file.

## Features
- Dynamic test case generation.
- Exception handling for invalid inputs.
- Support for basic arithmetic operations.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
## Acknowledgments
- This project was created as a learning exercise for Python and testing.
- Special thanks to the Python community for their contributions and resources.
Feel free to customize this README to match your project's specific details and requirements.

