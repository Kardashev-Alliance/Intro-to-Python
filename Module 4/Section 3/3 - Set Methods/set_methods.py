# ================================
# Module 4, Section 3.3: Set Methods
# ================================

# ------------------
# add() Method
# ------------------
# The add() method allows adding a single element to the set.
sample_set = {1, 2, 3}
sample_set.add(4)  # adds the integer 4 to the set
print(sample_set)  # Expected output: {1, 2, 3, 4}
sample_set.add(3)  # trying to add an existing item will not change the set
print(sample_set)  # Expected output: {1, 2, 3, 4}

# ------------------------------
# remove() and discard() Methods
# ------------------------------
# These methods are used to remove items from a set, but they behave differently when an item doesn't exist in the set.

sample_set.remove(4)  # removes the integer 4 from the set
print(sample_set)  # Expected output: {1, 2, 3}
# If you uncomment the next line, it will raise an error since 5 is not in the set.
# sample_set.remove(5)  

sample_set.discard(5)  # No error will be raised even though 5 doesn't exist in the set
print(sample_set)  # Expected output: {1, 2, 3}

# ----------------
# pop() Method
# ----------------
# The pop() method removes and returns an arbitrary element from the set.

popped_element = sample_set.pop()  # Removes an arbitrary element
print(popped_element)  # The popped element
print(sample_set)  # The set after popping

# ----------------
# clear() Method
# ----------------
# The clear() method empties the set.

sample_set.clear()
print(sample_set)  # Expected output: set()

# ----------------------------------------------------
# issubset(), issuperset(), and isdisjoint() Methods
# ----------------------------------------------------

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}

# issubset() checks if all elements of A are in B.
print(A.issubset(B))     # Expected output: True
# Explanation: A is considered a subset of B since every element of A is also an element of B.

# issuperset() checks if all elements of A are contained in B.
print(B.issuperset(A))   # Expected output: True
# Explanation: B is considered a superset of A since it contains every element from A and possibly more.

# isdisjoint() checks if A has no elements in common with C.
print(A.isdisjoint(C))   # Expected output: True
# Explanation: A and C are disjoint sets since they don't share any common elements.

# End of Module 4, Section 3.3: Set Methods
