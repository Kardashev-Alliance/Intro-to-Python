# cli_calculator.py

# Module 8: Section 1.3 - Building the CLI Calculator

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
        
        user_input = input(": ").lower()

        # End loop and exit calculator
        if user_input == 'quit':
            break
        
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
