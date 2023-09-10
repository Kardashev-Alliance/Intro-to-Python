# Module 7 - Section 4.2: Creating and Using the __init__ Method

# Example 1: Using `__init__` for Data Validation
class Age:
    def __init__(self, years):
        if years < 0:
            raise ValueError("Age cannot be negative.")
        self.years = years

try:
    negative_age = Age(-5)
except ValueError as e:
    print(f"Error: {e}")

valid_age = Age(25)
print(f"Valid age: {valid_age.years} years.")


# Example 2: Using `__init__` to Initialize Mutable Default Arguments
class ToDoList:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

my_list = ToDoList()
my_list.items.append("Read a book")
print(f"My to-do list: {my_list.items}")


# Example 3: `__init__` Initialization with Dependency Injection
class Engine:
    def start(self):
        return "Engine starting..."

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

car_engine = Engine()
my_car = Car(car_engine)
print(my_car.start())


# Example 4: Flexible Initialization using `*args` and `**kwargs`
class Student:
    def __init__(self, name, *subjects, **details):
        self.name = name
        self.subjects = subjects
        self.details = details

student = Student("John", "Math", "History", age=20, grade="Sophomore")
print(f"{student.name} studies {student.subjects} and is a {student.details['grade']} aged {student.details['age']}.")


# Conclusion:
# The `__init__` method is about more than just assigning values. It's a powerful tool that, when used effectively,
# can ensure data integrity, allow for flexible object creation, and set the foundational behaviors of an object.
