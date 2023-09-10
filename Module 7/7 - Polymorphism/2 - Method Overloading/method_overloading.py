# Module 7: Section 7.2 - Method Overloading

# Introduction:
# In most programming languages, method overloading refers to the ability
# of a class to have multiple methods with the same name but different parameters.
# Python handles method overloading differently due to its dynamic nature.
# Let's explore this with examples.

class MathOperations:
    
    # Example 1: Using Default Arguments for Method Overloading
    # Here, we're defining a method `product` which can calculate the product of two or three numbers.
    # If three numbers aren't provided, the default value for z becomes 1.
    def product(self, x, y, z=1):
        return x * y * z

    # Example 2: Using Variable-length Arguments (*args) for Method Overloading
    # The method `sum_values` can accept any number of arguments and will return their sum.
    def sum_values(self, *args):
        return sum(args)
    
# Let's create an instance of our class and try out the methods
math_ops = MathOperations()

# Using product method with 2 arguments
print(math_ops.product(3, 4))  # This will output: 12

# Using product method with 3 arguments
print(math_ops.product(3, 4, 2))  # This will output: 24

# Using sum_values method with 2 arguments
print(math_ops.sum_values(3, 4))  # This will output: 7

# Using sum_values method with 4 arguments
print(math_ops.sum_values(3, 4, 5, 6))  # This will output: 18

# Conclusion:
# Python's approach to method overloading is versatile and dynamic, making it possible
# to achieve the benefits of traditional method overloading in statically typed languages,
# but with added flexibility. Understanding this concept is key to designing robust and
# intuitive classes in Python.
