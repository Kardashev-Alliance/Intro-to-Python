# ========================================
# Module 4, Section 2.2: Tuple Operations
# ========================================

# --------------
# Concatenation:
# --------------
# Combining two tuples into a single tuple using the + operator.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(f"Combined Tuple: {combined_tuple}")

# -----------
# Repetition:
# -----------
# Repeating a tuple multiple times to form a larger tuple.

repeated_tuple = tuple1 * 3
print(f"Repeated Tuple: {repeated_tuple}")

# ----------------------
# Indexing and Slicing:
# ----------------------
# Accessing specific elements and slices from a tuple using positive and negative indexing.

# Indexing
print(f"Element at index 2: {tuple1[2]}")
print(f"Element at index -1: {tuple2[-1]}")

# Slicing
print(f"Elements from index 1 to 3: {combined_tuple[1:4]}")
print(f"Every other element: {combined_tuple[::2]}")

# ------------------
# Tuple Membership:
# ------------------
# Demonstrating the use of 'in' and 'not in' to check for element presence in a tuple.

if 3 in tuple1:
    print("3 is present in tuple1")
else:
    print("3 is not present in tuple1")

if 7 not in tuple2:
    print("7 is not present in tuple2")
else:
    print("7 is present in tuple2")

# -----------------------------
# Tuple Length, Min, Max:
# -----------------------------
# Using built-in functions to retrieve various properties of a tuple.

print(f"Length of tuple1: {len(tuple1)}")
print(f"Minimum value in tuple2: {min(tuple2)}")
print(f"Maximum value in combined_tuple: {max(combined_tuple)}")
