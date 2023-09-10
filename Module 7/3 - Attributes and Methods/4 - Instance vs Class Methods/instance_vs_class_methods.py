# MODULE 7: Object-Oriented Programming in Python
# Section 3.4: Instance Methods vs. Class Methods

# Class definition
class MyClass:
    class_attribute = "This is a class attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    # Instance Method
    def instance_method(self):
        """This is an instance method. It takes 'self' as the first parameter.
        'self' refers to the specific instance of the class.
        It can interact with both instance and class attributes."""
        return f"Instance Method: {self.instance_attribute}, {MyClass.class_attribute}"

    # Class Method
    @classmethod
    def class_method(cls, additional_info):
        """This is a class method. It's prefixed with the @classmethod decorator.
        Instead of 'self', it takes 'cls' as the first parameter.
        'cls' refers to the class itself, not an instance of it.
        It primarily interacts with class attributes."""
        return f"Class Method: {cls.class_attribute}, Additional Info: {additional_info}"

# ----- Usage of the Methods -----

# Creating an instance of MyClass
obj = MyClass("This is an instance attribute")

# Calling the instance method
print(obj.instance_method()) 
# Output: Instance Method: This is an instance attribute, This is a class attribute

# Calling the class method directly from the class (not from an instance)
print(MyClass.class_method("Some additional information"))
# Output: Class Method: This is a class attribute, Additional Info: Some additional information

# Note:
# - "self" in instance methods allows them to access and modify attributes unique to each instance.
# - "cls" in class methods lets them deal with class-level attributes, 
#   which are shared among all instances of the class.
# - The @classmethod decorator indicates that the following method should be called on the class,
#   not on an instance of the class. 

# In the context of our course, the @classmethod decorator is a way to define methods 
# that belong to a class, rather than an instance of the class. This can be useful 
# for creating factory methods or methods that affect the overall state of the class.
