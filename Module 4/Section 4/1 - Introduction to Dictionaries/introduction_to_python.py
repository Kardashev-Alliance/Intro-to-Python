# ===============================
# Module 4, Section 4.1: Introduction to Dictionaries
# ===============================

# -------------------------------
# Definition and Creation
# -------------------------------

# Dictionaries are collections of key-value pairs, enclosed within curly braces {}.
# Here, we are defining a dictionary with student details.

student = {
    "name": "John Doe",
    "age": 22,
    "marks": [85, 90, 78, 92]
}
print("Student Dictionary:", student)

# A dictionary can also be created using the dict() constructor.

student_2 = dict(name="Jane Smith", age=21, marks=[88, 76, 90, 85])
print("Student 2 Dictionary:", student_2)

# -------------------------------
# Accessing Dictionary Values
# -------------------------------

# Retrieve the name of the student.
student_name = student["name"]
print("Student Name:", student_name)

# Using the `get` method to fetch the age. If the key doesn't exist, it will return None.
student_age = student.get("age")
print("Student Age:", student_age)

# -------------------------------
# Modifying a Dictionary
# -------------------------------

# Add a new key-value pair for address.
student["address"] = "123 Main St"
print("Updated Student Dictionary with Address:", student)

# Update the age of the student.
student["age"] = 23
print("Updated Student Age:", student["age"])

# Delete the marks key-value pair from the dictionary.
del student["marks"]
print("Student Dictionary after removing marks:", student)

# -------------------------------
# Dictionary Methods
# -------------------------------

# Retrieve all the keys from the dictionary.
all_keys = student.keys()
print("All Keys in Student Dictionary:", all_keys)

# Retrieve all the values from the dictionary.
all_values = student.values()
print("All Values in Student Dictionary:", all_values)

# Retrieve all the key-value pairs as tuples from the dictionary.
all_items = student.items()
print("All Key-Value Pairs in Student Dictionary:", all_items)

# -------------------------------
# Utility of Dictionaries
# -------------------------------

# Storing configuration settings using dictionaries.
config = {
    "theme": "dark",
    "font": "Arial",
    "fontsize": 14
}
print("Configuration Settings Dictionary:", config)

# Managing user profiles using dictionaries.
user_profile = {
    "username": "jdoe",
    "email": "jdoe@example.com",
    "date_joined": "2022-08-01"
}
print("User Profile Dictionary:", user_profile)

# -------------------------------
# End of Module 4, Section 4.1: Introduction to Dictionaries
# -------------------------------
