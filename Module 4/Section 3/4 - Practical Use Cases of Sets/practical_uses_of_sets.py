# ================================
# Module 4, Section 3.4: Practical Use Cases of Sets
# ================================

# =====================================
# 1. De-duplication of Data
# =====================================

# Often, when working with data, you may end up with duplicate values. With sets, it becomes
# straightforward to keep only the unique entries.

# Creating a list with duplicate values
duplicate_list = [1, 2, 2, 3, 4, 4, 5]

# Converting the list to a set to de-duplicate
unique_set = set(duplicate_list)
print("Unique values using set:", unique_set)

# Optionally, converting back to a list
unique_list = list(unique_set)
print("Unique values as list:", unique_list)


# =====================================
# 2. Membership Testing
# =====================================

# When you need to check if a certain item exists in a collection, sets can perform this operation
# much faster than lists, especially when the collection is large.

# Demonstrating membership test speed for sets vs lists
sample_set = {i for i in range(100000)}
sample_list = [i for i in range(100000)]

# Check for membership in set (notice the speed difference when executing)
print(99999 in sample_set)

# Check for membership in list
print(99999 in sample_list)


# =====================================
# 3. Mathematical Set Operations
# =====================================

# Sets in Python can be used to perform various mathematical set operations like union, intersection,
# difference, and symmetric difference.

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# Union: Items that are present in either of the sets
print("Union of setA and setB:", setA.union(setB))

# Intersection: Items that are common to both sets
print("Intersection of setA and setB:", setA.intersection(setB))

# Difference: Items present in setA but not in setB
print("Difference between setA and setB:", setA.difference(setB))

# Symmetric Difference: Items that are unique to each set
print("Symmetric difference between setA and setB:", setA.symmetric_difference(setB))


# =====================================
# 4. Interacting with Unordered Data
# =====================================

# There are scenarios where the order of data doesn't influence the result, and in such cases,
# using sets can be more appropriate.

# Sample data of students who attended on different days
day1_students = {"John", "Jane", "Doe"}
day2_students = {"Doe", "John", "Smith"}

# To see if the same set of students attended on both days (irrespective of order)
are_same_students = day1_students == day2_students
print("Same students on both days?", are_same_students)

