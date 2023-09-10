# Module 5, Section 3.1: Introduction to Lambda Functions

# ----------------------------------------------
# Example 1: Creating a lambda function to add two numbers
# ----------------------------------------------
# Regular function
def add_numbers(x, y):
    return x + y

# Equivalent lambda function
lambda_add = lambda x, y: x + y

print(f"Regular Function Result: {add_numbers(5, 3)}")
print(f"Lambda Function Result: {lambda_add(5, 3)}")

# ----------------------------------------------
# Example 2: Using a lambda function within the filter() function
# ----------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original List: {numbers}")
print(f"Even Numbers Filtered using Lambda: {even_numbers}")

# ----------------------------------------------
# Example 3: Sorting a list of strings based on their length using lambda
# ----------------------------------------------
names = ["Alice", "Bob", "Charlie", "Dave"]
sorted_names = sorted(names, key=lambda x: len(x))

print(f"Original Names List: {names}")
print(f"Names Sorted by Length using Lambda: {sorted_names}")

# ----------------------------------------------
# Example 4: A scenario where regular function might be more appropriate
# ----------------------------------------------
# The below logic is hard to express as a single expression in lambda
def complex_logic(x):
    if x % 2 == 0 and x % 5 == 0:
        return True
    elif x % 3 == 0:
        return "Multiple of 3"
    else:
        return False

result = complex_logic(15)
print(f"Result of the complex logic for 15: {result}")

# Note: Lambda functions shine in simplicity. For more complex logic like the one above, regular functions are usually preferred.
