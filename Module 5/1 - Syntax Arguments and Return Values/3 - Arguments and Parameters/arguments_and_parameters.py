# Module 5, Section 1.3: Arguments and Parameters

# Example 1: Positional Arguments
def greet(name, age):
    """
    This function greets a person with their name and age.
    """
    print(f"Hello, {name}. You are {age} years old!")
    
# Calling the function with positional arguments
greet("Alice", 30)


# ----------------------------------------------------------

# Example 2: Default Arguments
def greet_again(name, age=25):
    """
    This function greets a person with their name and an optional age. 
    If age is not provided, a default age of 25 is used.
    """
    print(f"Hello again, {name}. You are {age} years old!")
    
# Calling the function without the age argument
greet_again("Bob")
# Calling the function with both arguments
greet_again("Charlie", 40)


# ----------------------------------------------------------

# Example 3: Keyword Arguments
def describe_pet(animal, pet_name):
    """
    This function provides a description of a pet.
    """
    print(f"I have a {animal} named {pet_name}.")
    
# Calling the function using keyword arguments out of order
describe_pet(pet_name="Whiskers", animal="cat")


# ----------------------------------------------------------

# Example 4: Arbitrary Arguments
# Using *args allows you to pass a variable number of positional arguments.
# The arguments are received in the form of a tuple.
def print_names(*names):
    """
    This function prints all the names provided. The *names parameter
    collects all the additional arguments into a tuple.
    """
    for name in names:
        print(name)

# Using **kwargs allows you to pass a variable number of keyword arguments.
# The arguments are received in the form of a dictionary.
def print_key_value_pairs(**key_value_pairs):
    """
    This function prints key-value pairs. The **key_value_pairs parameter 
    collects additional keyword arguments into a dictionary.
    """
    for key, value in key_value_pairs.items():
        print(f"{key}: {value}")
        
# Calling the function with multiple positional arguments
print_names("David", "Ella", "Frank", "Grace")
# Calling the function with multiple keyword arguments
print_key_value_pairs(first_name="Henry", last_name="Johnson", age=50)


# ----------------------------------------------------------

# Example 5: Combining Argument Types
def complex_function(a, b=10, *args, **kwargs):
    """
    This function demonstrates the combination of different types of arguments.
    It starts with regular positional arguments, followed by default ones,
    then collects extra positional ones in args and keyword ones in kwargs.
    """
    print(a)
    print(b)
    print(args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
# Calling the function
complex_function(1, 2, 3, 4, 5, name="Ian", job="Engineer")

