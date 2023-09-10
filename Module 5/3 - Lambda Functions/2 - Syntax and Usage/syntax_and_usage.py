# Module 5, Section 3.2: Syntax and Usage of Lambda Functions

# Example 1: Basic Syntax of Lambda Functions
# Here we define a lambda function to square a given number.
square = lambda x: x ** 2
print(f"Square of 5 is: {square(5)}")  # Expected Output: 25

# --------------------------------------------------

# Example 2: Lambda with Multiple Arguments
# This lambda function adds three numbers.
add = lambda x, y, z: x + y + z
print(f"Sum of 2, 3, and 4 is: {add(2, 3, 4)}")  # Expected Output: 9

# --------------------------------------------------

# Example 3: Use with Built-in Functions
# We'll use lambda with the filter() function to filter even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers in the list are: {even_numbers}")  # Expected Output: [2, 4, 6, 8]

# --------------------------------------------------

# Example 4: Limitations of Lambda Functions
# Lambda functions are limited in complexity. For more complex operations, traditional functions are preferred.
# Here's a demonstration:

# Using a lambda function
power = lambda x, y: x ** y
print(f"3 raised to the power 2 using lambda is: {power(3, 2)}")  # Expected Output: 9

# Using a traditional function
def traditional_power(x, y):
    return x ** y

print(f"3 raised to the power 2 using a traditional function is: {traditional_power(3, 2)}")  # Expected Output: 9

# The outputs are the same, but depending on the context, one might be more suitable than the other.
