class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation

    def get_result(self):
        # Call stored operation
        return self.operation(self.a, self.b)