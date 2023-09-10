# Module 5, Section 3.3: Common Scenarios for Lambda Functions

# Sorting Lists with Custom Key
# Lambda can be used to sort lists based on custom criteria.
list_of_strings = ["apple", "banana", "cherry", "date"]
sorted_list = sorted(list_of_strings, key=lambda x: len(x))
print(f"Original List: {list_of_strings}")
print(f"Sorted by Length: {sorted_list}")
# The sorted() function, along with lambda, sorts the strings based on their length.

# Filtering Elements from a List
# We can use lambda with the filter() function to filter out specific elements from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"All Numbers: {numbers}")
print(f"Even Numbers: {even_numbers}")
# The filter() function, combined with lambda, filters out only the even numbers.

# Using Lambda with map()
# The map() function can be combined with lambda to transform every element of a list.
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Numbers: {numbers}")
print(f"Squared Numbers: {squared_numbers}")
# The map() function, used with lambda, squares each number in the list.

# Event-driven Programming (Conceptual, not executable in this example)
# In GUI-based applications, lambda functions can serve as inline event handlers.
# For instance:
# button_clicked = lambda: print("Button was clicked!")
# When the button is clicked in the GUI, the lambda function prints a message. 

# Using Lambdas in Functional Programming Constructs
# The reduce() function from the functools module can be used to apply a binary function (a function that takes two 
# arguments) to the items of an iterable, from left to right, so as to reduce the iterable to a single value.
# For example, if used with a multiplication lambda function and a list [1, 2, 3, 4], it would compute: (((1*2)*3)*4)
from functools import reduce
factorial_of_five = reduce(lambda x, y: x*y, range(1, 6))
print(f"Factorial of 5: {factorial_of_five}")
# The reduce() function, combined with lambda, computes the factorial of 5 by multiplying the numbers in sequence.

# Note: To understand and execute some of these scenarios, additional knowledge or modules might be required.
