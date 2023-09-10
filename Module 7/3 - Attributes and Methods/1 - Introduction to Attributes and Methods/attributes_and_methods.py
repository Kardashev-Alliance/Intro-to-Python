# Required Libraries
from datetime import datetime

# --------------------------- Introduction ------------------------------

# Classes provide a blueprint for creating objects.
# They encapsulate data (attributes) and functions (methods) that operate on the data.

# ---------------------- Example 1: Basic Class ------------------------

# A simple class with instance attributes and methods

class Dog:
    def __init__(self, name, breed):
        self.name = name    # instance attribute
        self.breed = breed  # instance attribute
        
    def bark(self):        # instance method
        return f"{self.name} barks!"
    

# ------------------- Example 2: Class Variables/Methods ---------------

# A class with both instance and class-level attributes/methods

class Car:
    production_year = datetime.now().year  # class attribute

    def __init__(self, brand, model):
        self.brand = brand       # instance attribute
        self.model = model       # instance attribute

    @classmethod
    def production_info(cls):   # class method
        return f"Production Year: {cls.production_year}"


# ------------------- Example 3: State vs. Behavior --------------------

# Attributes (state) store information about the instance. 
# In our Dog class, 'name' and 'breed' store state information about the Dog.

# Methods (behavior) define actions or functionalities. 
# The 'bark' method in Dog class is a behavior that the Dog can perform.


# ------------------------- Practical Usage ---------------------------

# Creating a Dog object
puppy = Dog("Buddy", "Golden Retriever")
print(puppy.name)       # Outputs: Buddy
print(puppy.bark())     # Outputs: Buddy barks!

# Accessing class attribute and method
car1 = Car("Toyota", "Corolla")
print(Car.production_info())  # Outputs: Production Year: [Current Year]

# Notice how we used the class name 'Car' to access the class method.

# ----------------------------------------------------------------------

# In upcoming sections, we'll dive deep into understanding the difference 
# between instance and class-level attributes/methods, and much more about OOP.

