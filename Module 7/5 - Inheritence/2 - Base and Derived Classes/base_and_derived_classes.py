# MODULE 7 SECTION 5.2 - Base and Derived Classes

# ---- Dynamics of Inheritance ----

# Base Class: Bird
class Bird:
    def __init__(self):
        # This attribute is common for all birds
        self.wings = 2
    
    def fly(self):
        return "I can fly!"

# Derived Class: Penguin
# The Penguin class is a derived class of the Bird class. It inherits all its attributes and methods.
class Penguin(Bird):
    def __init__(self):
        # Call the constructor of the base class Bird using the super() function.
        super().__init__()
        # Additional attribute specific to penguins.
        self.cannot_fly = True
    
    # Overriding the fly method to provide specific behavior for penguins.
    def fly(self):
        if self.cannot_fly:
            return "Penguins can't fly."
        else:
            return super().fly()  # Call the fly method from the base class.

# ---- Methods and Behavior ----

# Using the Bird and Penguin classes defined above, we have showcased how a derived class (Penguin) can 
# override a method (fly) from its base class (Bird) while still having the capability to access the 
# base class method using the super() function.

# Instantiate objects and showcase behavior
bird_instance = Bird()
print(bird_instance.fly())  # Expected: I can fly!

penguin_instance = Penguin()
print(penguin_instance.fly())  # Expected: Penguins can't fly.

# ---- Complexities and Edge Cases ----

# 1. Attribute Shadowing:
# The derived class can shadow attributes of the base class by defining an attribute with the same name.

class Sparrow(Bird):
    def __init__(self):
        self.wings = "I have beautiful wings!"  # This shadows the wings attribute of the base class.

sparrow_instance = Sparrow()
print(sparrow_instance.wings)  # Expected: I have beautiful wings!

# 2. Multiple Inheritance:
# Python supports multiple inheritance, where a derived class can inherit from more than one base class.

class FlyingFish(Bird):
    def swim(self):
        return "I can swim!"

class SuperFish(Penguin, FlyingFish):
    pass

# Note: Multiple inheritance can lead to complexities, such as the Diamond Problem, and requires a careful design approach.
# Python resolves this using a mechanism called the Method Resolution Order (MRO). While we have defined a structure 
# that supports multiple inheritance, for simplicity, we have not dived deep into MRO in this example.

superfish_instance = SuperFish()
print(superfish_instance.fly())   # Expected: Penguins can't fly.
print(superfish_instance.swim())  # Expected: I can swim!

# Conclusion:
# Inheritance allows for a powerful way to create a hierarchy of classes, enabling code reusability and 
# a structured way to design complex software systems.
