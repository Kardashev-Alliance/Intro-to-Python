# Module 2: Variables in Python

# ========================================
# 2.3 Types of Variables
# ========================================

# Integers and Floating Points
# ----------------------------------------

# Integer: Whole numbers
integer_example = 10
print("Integer example:", integer_example)

# Floating Point: Decimal numbers
float_example = 10.5
print("Float example:", float_example)

# Basic arithmetic using both
result = integer_example + float_example
print("Result of addition:", result)


# Strings
# ----------------------------------------

# Using different types of quotes for strings
single_quote_string = 'Hello'
double_quote_string = "World"
triple_quote_string = '''Hello World!'''

print(single_quote_string, double_quote_string)
print("Triple quoted string:", triple_quote_string)

# Conversion from number to string and vice versa
num_as_str = "123"
converted_num = int(num_as_str)
print("Converted string to integer:", converted_num)


# Lists, Tuples, and Dictionaries
# ----------------------------------------

# List: Ordered collection of items
list_example = [1, 2, 3, "Python", [10.5, 20.5]]
print("List example:", list_example)

# Tuple: Immutable ordered collection
tuple_example = (1, 2, 3, "Python", (10.5, 20.5))
print("Tuple example:", tuple_example)

# Dictionary: Key-value pairs
dictionary_example = {
    "name": "John",
    "age": 30,
    "scores": [85, 90, 88]
}
print("Dictionary example:", dictionary_example)

# Combining data structures
complex_list = [
    (1, "apple", 0.5),  # Tuple inside list
    (2, "banana", 0.3),
    {"id": 3, "name": "cherry", "price": 0.2}  # Dictionary inside list
]
print("Complex list:", complex_list)


# Using type() to identify variable types
# ----------------------------------------

print("Type of integer_example:", type(integer_example))
print("Type of float_example:", type(float_example))
print("Type of single_quote_string:", type(single_quote_string))
print("Type of list_example:", type(list_example))
print("Type of tuple_example:", type(tuple_example))
print("Type of dictionary_example:", type(dictionary_example))
