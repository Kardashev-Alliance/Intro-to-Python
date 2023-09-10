# Module 7: Object-Oriented Programming (OOP)
# Section 2.2: Creating Classes

# Example 1: Car class
class Car:
    def __init__(self, color, make):
        self.color = color
        self.make = make
    
    def describe(self):
        return f"A {self.color} {self.make} car."

    def drive(self):
        return f"The {self.color} {self.make} car is now driving!"

# Instance creation
my_car = Car("red", "Toyota")
print(my_car.describe())

# Example 2: A simple Dog class without parameterized initialization but with a method to set breed
class Dog:
    breed = "Unknown"  # Default attribute
    
    def setBreed(self, breed_name):
        self.breed = breed_name
    
    def bark(self):
        return f"The {self.breed} dog barks!"

# Instance creation
dog1 = Dog()
dog1.setBreed("Golden Retriever")
print(dog1.bark())

# Example 3: A Rectangle class with parameterized initialization
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Instance creation
rect1 = Rectangle(5, 10)
print(f"Area of the rectangle: {rect1.area()} square units")

# This file demonstrates the versatility in class definition and object instantiation,
# including how to modify attributes post-instantiation using methods.
