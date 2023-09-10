# cli_calculator.py

# Module 8: Section 1.3 - Building and Testing the CLI Calculator

# --------- Introduction to Testing with Assertions ---------

# In Python, 'assert' is a debugging aid that tests a condition as an internal self-check in your program.
# The 'assert' statement is used during debugging to check that an internal state is as expected.
# If the assert condition is true, the program continues to run as if nothing happened.
# However, if the condition is false, an exception AssertionError is raised.

# Let's see this in action with our calculator program.

# --------- Importing required libraries and modules ---------
import operator

# --------- Arithmetic Module: Calculation Logic ---------
def arithmetic_operation(operation, num1, num2):
    """
    Performs the arithmetic operation based on the provided operation type.
    Supports addition, subtraction, multiplication, and division.
    """
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    # Ensure the operation is valid
    if operation not in operations:
        return "Invalid Operation"
    
    return operations[operation](num1, num2)

# --------- History Module: Storage and Retrieval ---------
class History:
    def __init__(self):
        self._history = []

    def add(self, entry):
        self._history.append(entry)

    def retrieve(self):
        return self._history

    def clear(self):
        self._history = []

# --------- Testing for Arithmetic Module ---------
def test_arithmetic_operation():
    assert arithmetic_operation('+', 5, 3) == 8, "Addition operation failed!"
    assert arithmetic_operation('-', 5, 3) == 2, "Subtraction operation failed!"
    assert arithmetic_operation('*', 5, 3) == 15, "Multiplication operation failed!"
    assert arithmetic_operation('/', 6, 3) == 2, "Division operation failed!"
    print("All arithmetic tests passed!")

# --------- Testing for History Module ---------
def test_history():
    history = History()
    history.add("5 + 3 = 8")
    assert history.retrieve() == ["5 + 3 = 8"], "History retrieval failed after adding entry!"
    history.clear()
    assert history.retrieve() == [], "History retrieval failed after clearing entries!"
    print("All history tests passed!")

# --------- Main Driver: User Interaction and Management ---------
def main_driver():
    """
    The main driving function that captures user input and coordinates the calculator's functionalities.
    """
    # Instantiate the history object
    history = History()
    
    while True:
        # Displaying options to the user
        print("\nOptions:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'history' to view calculation history")
        print("Enter 'clear' to clear the history")
        print("Enter 'quit' to end the program")
        print("Enter 'test' to run tests")
        
        user_input = input(": ").lower()

        # End loop and exit calculator
        if user_input == 'quit':
            break

        # Run tests
        if user_input == 'test':
            test_arithmetic_operation()
            test_history()
            continue
        
        # Show calculation history
        if user_input == 'history':
            for item in history.retrieve():
                print(item)
            continue
        
        # Clear history
        if user_input == 'clear':
            history.clear()
            print("History cleared!")
            continue
        
        # Ensure user chooses a valid operation
        if user_input in ('add', 'subtract', 'multiply', 'divide'):
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                
                if user_input == 'divide' and y == 0:
                    print("Error: Division by zero!")
                    continue

                if user_input == 'add':
                    result = arithmetic_operation('+', x, y)
                    history.add(f"{x} + {y} = {result}")

                elif user_input == 'subtract':
                    result = arithmetic_operation('-', x, y)
                    history.add(f"{x} - {y} = {result}")

                elif user_input == 'multiply':
                    result = arithmetic_operation('*', x, y)
                    history.add(f"{x} * {y} = {result}")

                elif user_input == 'divide':
                    result = arithmetic_operation('/', x, y)
                    history.add(f"{x} / {y} = {result}")
                
                print(result)

            except ValueError:
                print("Error: Invalid number entered")

        else:
            print("Invalid Input")

if __name__ == "__main__":
    main_driver()
