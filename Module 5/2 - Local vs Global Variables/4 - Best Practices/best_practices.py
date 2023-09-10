# Module 5, Section 2.4: Best Practices with Variables and Scope

# Example 1: Using local variables in a function
def calculate_area(radius):
    """Calculate area of a circle using local variable 'radius'."""
    pi = 3.14159  # Local variable
    return pi * (radius**2)

# This local variable 'pi' is restricted to the calculate_area function.
print(calculate_area(5))

# Example 2: The potential pitfalls of global variables
global_counter = 0  # Global variable

def increment_counter():
    global global_counter
    global_counter += 1

def reset_counter():
    global global_counter
    global_counter = 0

# Using global variables across functions can lead to unintended side effects
increment_counter()
print(global_counter)  # Expected: 1

reset_counter()
print(global_counter)  # Expected: 0

# Example 3: Limited use of the 'global' keyword
counter = 0

def add_to_counter(value):
    """Add a value to counter without using global."""
    return counter + value

# Avoid modifying the global state within functions
print(add_to_counter(5))

# Example 4: Using function parameters over global variables
def greet(name, greeting="Hello"):
    """Function that greets a user with a message."""
    return f"{greeting}, {name}!"

# Using function parameters makes the function more predictable
print(greet("Alice"))
print(greet("Bob", "Hi"))

# Example 5: Encapsulation in class structures
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Encapsulated data

    def area(self):
        pi = 3.14159
        return pi * (self.radius**2)

# Using encapsulation to control access to data
circle_instance = Circle(5)
print(circle_instance.area())

# Note: While encapsulation is a broader topic, this is a basic example for demonstration purposes.
