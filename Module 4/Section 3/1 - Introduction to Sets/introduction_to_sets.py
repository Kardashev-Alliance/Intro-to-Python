# ===========================================
# Module 4, Section 3.1: Introduction to Sets
# ===========================================

# --------------
# Definition and Creation
# --------------
# Sets are created using curly braces or the set() function. Sets do not allow duplicates.

# Example 1: Creating a set and demonstrating the unique property
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Trying to add duplicates to the set
my_set.add(3)  # No error, but element won't be added since it's a duplicate
print(my_set)  # Output: {1, 2, 3, 4, 5}

# --------------
# Unordered Nature of Sets
# --------------
# Sets are unordered. This means we can't rely on an element to be in a specific position.

# Example 2: Demonstrating the unordered property of sets
# Note: Attempting to index or slice a set will result in an error, hence commented out.
# print(my_set[1])  # TypeError: 'set' object is not subscriptable

# --------------
# Mutable but Elements are Immutable
# --------------
# Sets are mutable, but the elements within them should be of an immutable type.

# Example 3: Adding immutable types to a set
# We can add a tuple to a set since tuples are immutable
my_set.add((6, 7))
print(my_set)  # Output: {1, 2, 3, 4, 5, (6, 7)}

# Trying to add a mutable type like a list will result in an error
# my_set.add([8, 9])  # TypeError: unhashable type: 'list'

# --------------
# Basic Set Operations
# --------------
# Sets support operations like union, intersection, and difference

# Example 4: Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set1.intersection(set2))  # Output: {3, 4}
