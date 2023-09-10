# ========================================
# Module 4, Section 2.1: Introduction to Tuples
# ========================================

# -----------------------------
# Definition and Creation
# -----------------------------

# Creating an empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Creating a tuple containing mixed data types
mixed_tuple = (1, "Hello", 3.4, True)
print("Mixed Data Tuple:", mixed_tuple)

# Creating a nested tuple
nested_tuple = ("apple", [3, 4, 5], (1, 2, 3))
print("Nested Tuple:", nested_tuple)

# -----------------------------
# Accessing Elements
# -----------------------------

# Accessing tuple elements using positive indexing
print("Second Element:", mixed_tuple[1])

# Accessing tuple elements using negative indexing
print("Last Element:", mixed_tuple[-1])

# -----------------------------
# Immutability
# -----------------------------

# Tuples are immutable. Uncommenting the line below will raise a TypeError.
# mixed_tuple[1] = "World"

# -----------------------------
# Tuple Operations
# -----------------------------

# Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Tuple Repetition
repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)

