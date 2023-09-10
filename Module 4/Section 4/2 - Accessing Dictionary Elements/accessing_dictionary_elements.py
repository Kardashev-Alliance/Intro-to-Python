# ========================
# Module 4, Section 4.2: Accessing Dictionary Elements
# ========================

# -----------------
# Using Keys for Access
# -----------------
# Description: Demonstrating accessing a dictionary's value using its key.
sample_dict = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

print("Name:", sample_dict['name'])  # Output: John Doe

# -----------------
# Using the `get` Method
# -----------------
# Description: Showing how to use the `get` method to access values.
print("Age:", sample_dict.get('age'))  # Output: 30
print("Country:", sample_dict.get('country', 'USA'))  # Output: USA (default value provided)

# -----------------
# Checking for Key Existence
# -----------------
# Description: Demonstrating the use of the `in` keyword.
key_to_check = 'city'
if key_to_check in sample_dict:
    print(f"{key_to_check} found!")  # Output: city found!
else:
    print(f"{key_to_check} not found!")

# -----------------
# Accessing All Keys, Values, and Items
# -----------------
# Description: Exploring dictionary methods to retrieve content.

# Retrieving all keys
print("Keys:", sample_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# Retrieving all values
print("Values:", sample_dict.values())  # Output: dict_values(['John Doe', 30, 'New York'])

# Retrieving all key-value pairs
print("Items:", sample_dict.items())  # Output: dict_items([('name', 'John Doe'), ('age', 30), ('city', 'New York')])

# -----------------
# Nested Dictionaries
# -----------------
# Description: Accessing values inside a nested dictionary.
nested_dict = {
    'student': {
        'name': 'Jane Smith',
        'grade': 'A'
    },
    'course': 'Python for Beginners'
}

print("Student's name:", nested_dict['student']['name'])  # Output: Jane Smith
print("Student's grade:", nested_dict['student']['grade'])  # Output: A

