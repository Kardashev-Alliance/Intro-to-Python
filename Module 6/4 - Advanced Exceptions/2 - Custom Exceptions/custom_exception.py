# -----------------------------------------------------------------------
# MODULE 6 - SECTION 4.2: CUSTOM EXCEPTIONS WITH BASIC INHERITANCE
# -----------------------------------------------------------------------

# Custom exceptions provide a way to define user-specific error messages, 
# which can be helpful for debugging. Inheritance in exceptions showcases 
# the power of Python's OOP features. This file demonstrates the creation and 
# usage of custom exceptions derived from the base Python Exception class.

# -----------------------------------------------------------------------
# 1. BASIC INHERITANCE DEMONSTRATION
# -----------------------------------------------------------------------

class Animal:
    """A basic class representing an animal."""
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes some sound."

class Dog(Animal):
    """Derived class from Animal representing a dog."""
    def fetch_stick(self):
        return f"{self.name} fetched the stick!"

# Let's use the basic inheritance
rex = Dog("Rex")
print(rex.speak())  # Output: Rex makes some sound.
print(rex.fetch_stick())  # Output: Rex fetched the stick!

# -----------------------------------------------------------------------
# 2. DEFINING CUSTOM EXCEPTIONS USING INHERITANCE
# -----------------------------------------------------------------------

class Error(Exception):
    """Base class for our custom exceptions."""
    pass

class ValueTooSmallError(Error):
    """Exception raised for values too small."""
    pass

class ValueTooLargeError(Error):
    """Exception raised for values too large."""
    pass

# -----------------------------------------------------------------------
# 3. USING CUSTOM EXCEPTIONS
# -----------------------------------------------------------------------

number = 10

try:
    value = int(input("Enter a number: "))

    if value < number:
        raise ValueTooSmallError
    elif value > number:
        raise ValueTooLargeError
    else:
        print("Congratulations! You guessed it correctly.")

except ValueTooSmallError:
    print("The value is too small!")

except ValueTooLargeError:
    print("The value is too large!")

# This script showcases the power of inheritance in Python, focusing on 
# attributes inherited by derived classes and using custom exceptions.
