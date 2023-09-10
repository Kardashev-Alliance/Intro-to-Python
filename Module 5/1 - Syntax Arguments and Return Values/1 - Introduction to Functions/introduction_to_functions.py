# Module 5, Section 1.1: Introduction to Functions

# ----------------------------------
# Defining a Simple Function
# ----------------------------------
# A function encapsulates a task or operation for reusability.

def greet():
    """This function simply greets the user"""
    print("Hello!")

print("Example 1: Using the greet function")
greet()  # This will print "Hello!"
print("\n")


# ----------------------------------
# Reusing a Function with Different Inputs
# ----------------------------------
# Functions can be reused with different inputs for flexibility and reduced redundancy.

def calculate_area(length, width):
    """This function returns the area of a rectangle"""
    return length * width

print("Example 2: Reusing the calculate_area function")
area1 = calculate_area(5, 10)
print(f"Area of a rectangle with length 5 and width 10 is: {area1}")

area2 = calculate_area(8, 12)
print(f"Area of a rectangle with length 8 and width 12 is: {area2}")
print("\n")


# ----------------------------------
# Function Reusability in Operations
# ----------------------------------
# Functions can be reused in various operations without rewriting the code.

def multiply_by_two(num):
    """This function multiplies the given number by 2"""
    return num * 2

print("Example 3: Reusing the multiply_by_two function in different operations")
double_of_five = multiply_by_two(5)
print(f"Double of 5 is: {double_of_five}")

sum_of_doubles = multiply_by_two(3) + multiply_by_two(4)
print(f"Sum of double of 3 and double of 4 is: {sum_of_doubles}")
print("\n")

