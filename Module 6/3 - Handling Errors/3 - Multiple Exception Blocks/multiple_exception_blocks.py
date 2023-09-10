# Module 6: File Handling and Exceptions in Python
# Section 3.3: Multiple Exception Blocks

# --------------------------------------------------------------------------------
# 1. Basic Usage of Multiple Exception Blocks
# --------------------------------------------------------------------------------

# Demonstrating the use of multiple exception blocks

try:
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
except Exception as e:
    print(f"An error occurred: {e}")

# --------------------------------------------------------------------------------
# 2. Handling Multiple Exceptions in a Single Block
# --------------------------------------------------------------------------------

# Handling multiple exceptions with a single except block

try:
    number = int(input("Enter another number: "))
    result = 10 / number
    print(f"Result: {result}")
    
except (ZeroDivisionError, ValueError):
    print("Either you tried to divide by zero or didn't input a valid number!")

# --------------------------------------------------------------------------------
# 3. Using the `else` and `finally` Clauses
# --------------------------------------------------------------------------------

# Demonstrating the use of else and finally

try:
    value = int(input("Enter a number for division: "))
    division_result = 100 / value
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Enter a valid number!")
else:
    print(f"100 divided by {value} is {division_result}")
finally:
    print("This 'finally' block will execute no matter what!")

# --------------------------------------------------------------------------------
# 4. Order of Exception Blocks
# --------------------------------------------------------------------------------

# Illustrating the importance of exception block order

try:
    some_input = int(input("Enter yet another number: "))
    output = 10 / some_input
    print(f"Output: {output}")
    
except Exception as e:
    print(f"An error occurred: {e}")
except ZeroDivisionError:
    print("This 'ZeroDivisionError' block will never be executed because the generic 'Exception' block is placed before it!")

# It's essential to place specific exception blocks before the generic ones!

