# Module 5, Section 1.4: Return Values

# ------------------------------
# Returning a Single Value
# ------------------------------

def square(num):
    """
    Returns the square of the given number.

    Parameters:
    - num: A numeric value

    Returns:
    - The square of num
    """
    return num * num

# Testing the function
result = square(5)
print(f"The square of 5 is {result}")  # Expected output: 25

# ------------------------------
# Returning Multiple Values
# ------------------------------

def rectangle_info(length, width):
    """
    Calculates and returns the area and perimeter of a rectangle.

    Parameters:
    - length: The length of the rectangle
    - width: The width of the rectangle

    Returns:
    - A tuple containing the area and perimeter of the rectangle
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # This implicitly returns a tuple

# Testing the function
area, perimeter = rectangle_info(10, 5)
print(f"Area: {area}, Perimeter: {perimeter}")  # Expected output: Area: 50, Perimeter: 30

# ------------------------------
# The Implicit None
# ------------------------------

def greet(name):
    """
    Prints a greeting message.

    Parameters:
    - name: The name to greet

    Returns:
    - None (implicitly)
    """
    print(f"Hello, {name}!")

# Testing the function
result = greet("Alice")
print(result)  # Expected output: Hello, Alice! followed by None

# ------------------------------
# Returning from Nested Functions
# ------------------------------

def outer_function(num):
    """
    Defines a nested function and calls it.

    Parameters:
    - num: A numeric value

    Returns:
    - The result of the nested function
    """
    def nested_function(x):
        return x + 2

    return nested_function(num * 2)  # Call the nested function

# Testing the function
result = outer_function(3)
print(f"Result from nested function: {result}")  # Expected output: 8
