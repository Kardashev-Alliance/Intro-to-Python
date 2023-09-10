# Module 5, Section 1.2: Basic Syntax of Functions

# ------------------------------
# Function Definition
# ------------------------------
# In Python, we start with the 'def' keyword to define a function.

def greet():
    print("Hello, world!")

# This function, when called, will simply print "Hello, world!" to the console.


# ------------------------------
# Function Call
# ------------------------------
# Functions don't execute on their own. We "call" or "invoke" them using their name followed by parentheses.

greet()  # This will print "Hello, world!"


# ------------------------------
# Parameters and Arguments
# ------------------------------
# Functions can take input values known as parameters. When calling the function, we provide these values - called arguments.

def custom_greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

custom_greet("Alice")  # "Alice" is an argument
custom_greet("Bob")    # "Bob" is another argument


# ------------------------------
# Return Values
# ------------------------------
# Functions can return values using the 'return' keyword. This allows outputting a result for further use in the code.

def add(a, b):  # Takes two parameters, 'a' and 'b'
    result = a + b
    return result

sum_result = add(5, 3)  # Calls the function with arguments 5 and 3 and stores the return value in 'sum_result'
print(sum_result)  # This will print 8


# ------------------------------
# Multiple Parameters
# ------------------------------
# Functions can have multiple parameters, allowing for more complex operations.

def introduce(first_name, last_name, age):
    print(f"My name is {first_name} {last_name} and I am {age} years old.")

introduce("John", "Doe", 30)  # Calls the function with appropriate arguments


# Remember, the key to functions is reusability. Once defined, they can be used multiple times with different arguments.

