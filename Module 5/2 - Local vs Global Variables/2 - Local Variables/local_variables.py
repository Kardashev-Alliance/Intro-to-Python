# Module 5, Section 2.2: Local Variables

# Example 1: Creating and using a local variable within a function
def display_message():
    # This is a local variable
    message = "Hello from inside the function!"
    print(message)

display_message()

# Uncommenting the line below will raise an error because 'message' is a local variable
# print(message)


# Example 2: Demonstrating the life cycle of a local variable
def increment_counter():
    # Each time this function is called, counter is created and set to 1
    counter = 1
    print(f"Counter inside the function: {counter}")

increment_counter()
increment_counter()  # Note: The counter does not retain its value between calls


# Example 3: Enhancing code readability with local variables
def calculate_area(radius):
    # Using local variable 'pi' to make the code clearer
    pi = 3.14159
    area = pi * radius * radius
    return area

circle_area = calculate_area(5)
print(f"Area of the circle with radius 5: {circle_area}")


# Example 4: Limitations of local variables
def assign_value():
    local_variable = 10
    print(f"Inside the function, local_variable = {local_variable}")

assign_value()

# Uncommenting the line below will raise an error because 'local_variable' is not accessible outside the function
# print(local_variable)
