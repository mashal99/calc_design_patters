from calculator.operations import add, subtract, multiply, divide

def test_operation(a, b, operation, expected):
    '''Test different operations using dynamically generated test data'''
    result = operation(a, b)
    assert result == expected, f"Expected {expected} but got {result} for {operation.__name__} with {a}, {b}"


##Test