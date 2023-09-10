# Module 7: Object-Oriented Programming (OOP)
# Section 2.1: Defining Classes and Objects
# ------------------------------------------

# This script will illustrate the definition of classes, the creation of their objects,
# and the significance of the 'self' keyword in Python's OOP.

# Start by defining a class named Car.
class Car:
    # The __init__ method initializes the attributes of the class.
    # It acts as a constructor in other languages.
    def __init__(self, color, make, model):
        self.color = color  # 'self' refers to the instance of the object itself
        self.make = make    # it's used to access the object's attributes 
        self.model = model

    # A method to describe the car
    def describe(self):
        return f"A {self.color} {self.make} {self.model}"

    # A method for the car to honk
    def honk(self):
        return "Honk! Honk!"

# 'self' EXPLAINED:
# In Python, 'self' refers to the instance of the object itself. Most object-oriented
# languages pass this as a hidden parameter that is defined by the system, but in
# Python, it must be explicitly defined as the first parameter. It allows us to 
# differentiate between methods and attributes of the class and local variables.

# Create an instance of the Car class.
my_car = Car("red", "Toyota", "Corolla")

# Access the object's attributes using the dot notation.
print(my_car.color)   # Outputs: red
print(my_car.make)    # Outputs: Toyota
print(my_car.model)   # Outputs: Corolla

# Call the methods of the object.
print(my_car.describe())  # Outputs: A red Toyota Corolla
print(my_car.honk())      # Outputs: Honk! Honk!

# This example underscores the foundational OOP concepts in Python including classes, 
# objects, attributes, methods, and the role of 'self'.
