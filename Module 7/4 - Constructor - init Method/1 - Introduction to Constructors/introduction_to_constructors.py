# Module 7: Object-Oriented Programming in Python
# Section 4.1: Introduction to Constructors

# Example 1: Basic Constructor
class Dog:
    def __init__(self):
        self.breed = "Unknown"
        self.name = "No Name"
    
    def bark(self):
        return f"{self.name} barks!"

basic_dog = Dog()
print(basic_dog.bark())  # Output: No Name barks!


# Example 2: Constructor with Parameters
class Cat:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def meow(self):
        return f"{self.name} says meow!"

whiskers = Cat("Siamese", "Whiskers")
print(whiskers.meow())  # Output: Whiskers says meow!


# Example 3: Constructor with Default Values
class Bird:
    def __init__(self, species="Sparrow"):
        self.species = species

    def chirp(self):
        return f"A {self.species} chirps!"

bird1 = Bird()
bird2 = Bird("Parrot")
print(bird1.chirp())  # Output: A Sparrow chirps!
print(bird2.chirp())  # Output: A Parrot chirps!


# Example 4: Constructor with Object Parameter
class Author:
    def __init__(self, name):
        self.name = name

class Book:
    # Here, 'author: Author' is a type hint. It suggests that the 'author' parameter 
    # should ideally be an instance of the Author class. It does NOT enforce the type but 
    # helps developers understand the intended type of the parameter.
    def __init__(self, title, author: Author):
        self.title = title
        self.author = author

    def info(self):
        return f"'{self.title}' written by {self.author.name}"

george = Author("George Orwell")
book = Book("1984", george)
print(book.info())  # Output: '1984' written by George Orwell

# Summary:
# Constructors allow us to initialize object attributes at the time of object creation.
# They can be flexible with parameters, default values, or even other object instances.
# Type hints in constructors (like 'author: Author') are used to suggest the intended 
# data type for a parameter, aiding in code readability and documentation.
