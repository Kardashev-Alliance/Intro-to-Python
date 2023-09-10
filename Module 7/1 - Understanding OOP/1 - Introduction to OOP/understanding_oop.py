# --------------------------------------------------------------------------------
# Module 7: Object-Oriented Programming (OOP)
# Section 1.1: Understanding OOP
# --------------------------------------------------------------------------------

# This script will demonstrate the difference between procedural and OOP paradigms.

# ---- Procedural Approach ----
# Data and functions are kept separate.

# Defining data:
user_name_procedural = "Alice"
user_age_procedural = 30

# Defining procedures/functions:
def display_user_procedural(name, age):
    return f"User's name is {name} and age is {age}."

# Calling the function:
print(display_user_procedural(user_name_procedural, user_age_procedural))
# Output: User's name is Alice and age is 30.


# ---- Object-Oriented Approach ----
# Data (attributes) and methods (behaviors) are encapsulated into objects.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_user(self):
        return f"User's name is {self.name} and age is {self.age}."

# Creating an object instance:
user_oop = User("Bob", 25)

# Calling the method:
print(user_oop.display_user())
# Output: User's name is Bob and age is 25.

# Note: In the OOP example, we encapsulated the user data and behavior within a single class.
# This makes it easier to manage and extend as we can easily add more attributes and methods to the User class.

# --------------------------------------------------------------------------------
# Explore further: Experiment by adding more attributes and methods to the User class.
# Notice how OOP allows for easy expansion and management of the object's attributes and behaviors.
# --------------------------------------------------------------------------------
