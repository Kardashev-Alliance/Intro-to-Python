# Module 4: Data Structures in Python
# Section 4.3: Dictionary Methods

# Initialization of a sample dictionary
sample_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 1. Adding Elements using the update() method
print("Original Dictionary:", sample_dict)
new_data = {"job": "Engineer", "hobby": "Reading"}
sample_dict.update(new_data)
print("Updated Dictionary:", sample_dict)

# ==================================================================================

# 2. Retrieving Elements using the get() method
# The get() method allows safe retrieval of values. If the key is not found, it will return a default value.
print("\nValue for 'name':", sample_dict.get("name", "Key not found"))
print("Value for 'gender':", sample_dict.get("gender", "Key not found"))

# 3. Using keys() method to retrieve all keys
print("\nKeys in the dictionary:", list(sample_dict.keys()))

# ==================================================================================

# 4. Removing Elements using pop()
# Removes a key-value pair based on the provided key and returns its value.
removed_value = sample_dict.pop("hobby")
print("\nRemoved 'hobby':", removed_value)
print("Dictionary after pop():", sample_dict)

# 5. Using popitem() to remove the last key-value pair
last_item = sample_dict.popitem()
print("\nRemoved last item:", last_item)
print("Dictionary after popitem():", sample_dict)

# 6. Clearing all elements using clear()
sample_dict.clear()
print("\nDictionary after clear():", sample_dict)

# ==================================================================================

# Miscellaneous Methods

# Resetting the dictionary for further examples
sample_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 7. Using items() method to retrieve key-value pairs
print("\nKey-Value pairs in the dictionary:", list(sample_dict.items()))

# 8. Using values() to get all the values in the dictionary
print("\nValues in the dictionary:", list(sample_dict.values()))

# 9. Creating a shallow copy of a dictionary using copy()
copied_dict = sample_dict.copy()
print("\nOriginal Dictionary:", sample_dict)
print("Copied Dictionary:", copied_dict)
