# Module 7: Section 7.1 - Introduction to Polymorphism

# Introduction:
# In Python, polymorphism allows different classes to be treated as instances of the same class 
# through inheritance, with a focus on behavior.

# Let's demonstrate this.

# --- The Essence of Polymorphism ---

# Defining a base class called 'Shape' with a method 'calculate_area'
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses should implement this method!")

# 'Circle' class inherits from 'Shape'
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding the calculate_area method for Circle
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# 'Square' class inherits from 'Shape'
class Square(Shape):
    def __init__(self, side):
        self.side = side

    # Overriding the calculate_area method for Square
    def calculate_area(self):
        return self.side * self.side

# Polymorphism in action:
# Creating objects for both Circle and Square
shape1 = Circle(5)
shape2 = Square(4)

# We can use the same method name to get area, irrespective of the shape type
print(shape1.calculate_area())
print(shape2.calculate_area())

# --- The Power of Polymorphism ---

# Flexibility: Using a list of shapes and demonstrating polymorphism
shapes = [Circle(3), Square(5), Circle(7)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.calculate_area()}")

# This shows how polymorphism brings flexibility. The same method can be called on different 
# objects, and the right version of the method gets executed.

# --- Distinguishing from Inheritance ---

# 'Rectangle' class inherits from 'Shape' and has its own calculate_area method
class Rectangle(Shape):
    def __init__(self, length, width):  # Changed 'breadth' to 'width'
        self.length = length
        self.width = width

    # Overriding the calculate_area method for Rectangle
    def calculate_area(self):
        return self.length * self.width  # Updated 'breadth' to 'width'

# Creating a Rectangle object
rectangle = Rectangle(5, 3)

# Polymorphism allows us to use the same method name, even though the underlying logic differs
print(rectangle.calculate_area())

# While inheritance (Rectangle IS a Shape) lets us reuse code, polymorphism allows us to 
# use the inherited methods in child classes in ways that suit their needs.
