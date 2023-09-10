# --------------------------------------------------------------------------------
# Module 6, Section 4.3: Exception as Objects
# --------------------------------------------------------------------------------

# ----------------------
# 1. Basic Inheritance
# ----------------------
# Before we dive deep into exceptions as objects, let's introduce a very basic concept:
# inheritance in object-oriented programming.
# For a comprehensive understanding, consider checking the official Python documentation:
# https://docs.python.org/3/tutorial/classes.html#inheritance

class Animal:
    def __init__(self, species_name):
        self.species_name = species_name

    def describe(self):
        return f"This is a {self.species_name}"

class Bird(Animal):
    def __init__(self, species_name, can_fly=True):
        super().__init__(species_name)
        self.can_fly = can_fly

    def fly_status(self):
        return "can fly" if self.can_fly else "cannot fly"

penguin = Bird("Penguin", can_fly=False)
print(penguin.describe())
print(f"Penguin {penguin.fly_status()}")


# ------------------------------
# 2. Custom Exception as Objects
# ------------------------------
# Now, onto the main topic. When creating custom exceptions, we're essentially creating new classes.
# These classes inherit from a base class, typically 'Exception'. 
# But how does this work?

# The 'Exception' class is a built-in Python class specifically designed to handle errors.
# Its documentation provides insight into its attributes and methods:
# https://docs.python.org/3/library/exceptions.html#Exception

class CustomError(Exception):
    """Custom error class inheriting from the base Exception class."""
    def __init__(self, message, code):
        # Passing message to the parent Exception class
        # The super() function here calls the constructor (__init__ method) of the parent (Exception) class.
        # The Exception class expects a message as its argument, which describes the error.
        super().__init__(message)
        
        # Add any custom attributes you want
        self.code = code

# Example of raising the custom error
try:
    raise CustomError("Something went wrong!", 404)
except CustomError as ce:
    print(f"Caught an error: {ce.message} with code: {ce.code}")


# ------------------------------
# 3. Delving Deeper
# ------------------------------
# To fully understand how custom exceptions and inheritance work, consider delving deeper into:
# - Python's official documentation on classes: https://docs.python.org/3/tutorial/classes.html
# - External resources and tutorials on Object-Oriented Programming in Python.
# - Courses on platforms like Coursera, Udemy, or Khan Academy related to Python OOP concepts.
