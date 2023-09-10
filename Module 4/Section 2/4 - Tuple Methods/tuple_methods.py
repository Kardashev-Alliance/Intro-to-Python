# ========================
# Module 4, Section 2.4: Tuple Methods
# ========================

# Tuple for demonstration
sample_tuple = (1, 2, 3, 4, 2, 5, 2, 6, 7, 8, 9, 10)

# ------------------------
# Demonstrating the `count()` method
# ------------------------
# The count() method returns the number of times a specified value appears in the tuple.
count_of_2 = sample_tuple.count(2)
print(f"Number of times 2 appears in the tuple: {count_of_2}")  # Expected Output: 3

# ------------------------
# Demonstrating the `index()` method
# ------------------------
# The index() method returns the index of the first occurrence of the specified value.
index_of_5 = sample_tuple.index(5)
print(f"Index of first occurrence of 5 in the tuple: {index_of_5}")  # Expected Output: 5

# ------------------------
# Remember: 
# While tuples offer fewer methods compared to lists, their strength lies in immutability.
# The `count()` and `index()` methods, though limited in number, are powerful in their utility.
# ------------------------

# Note: When using these methods, ensure the element exists in the tuple to avoid errors.
