# --------------------------------------------------------------------------------
# Module 6: File Handling and Exceptions in Python
# Section 3.2: Basic Exception Handling
# --------------------------------------------------------------------------------

# Introduction:
# Exception handling is crucial for creating robust and error-free programs. In this section,
# we will explore basic exception handling mechanisms in Python.

# --------------------------------------------------------------------------------
# 1. The try-except Block
# --------------------------------------------------------------------------------

# The try block contains code that may raise an exception. If an exception occurs, the try block
# is skipped, and the corresponding except block is executed.

# Example: Handling division by zero error
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# --------------------------------------------------------------------------------
# 2. Handling Specific Exceptions
# --------------------------------------------------------------------------------

# Python provides numerous built-in exceptions, allowing for specific error handling.

# Example: ValueError
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid integer value!")

# Example: FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist!")

# --------------------------------------------------------------------------------
# 3. Generic Exception Handling
# --------------------------------------------------------------------------------

# While it's better to handle specific exceptions, you can use a generic except clause 
# to catch any exception.

try:
    # This will raise a TypeError
    result = "5" + 5
except:
    print("An error occurred!")

# Note: It's recommended to handle specific exceptions to provide more meaningful feedback to users.

# --------------------------------------------------------------------------------
# Conclusion:
# By understanding and implementing basic exception handling, you can create resilient and 
# user-friendly programs that gracefully handle unforeseen errors.
# --------------------------------------------------------------------------------
