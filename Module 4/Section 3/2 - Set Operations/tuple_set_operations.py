# ==========================
# Module 4 - Section 3.2: Set Operations
# ==========================

# ==========================
# Basic Set Operations
# ==========================

# Example 1: Union Operation
# -------------------------
# The union() method or | operator returns a set that contains all items from both sets, duplicates are excluded.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union of A and B:", A.union(B))  # or A | B

# Example 2: Intersection Operation
# -------------------------
# The intersection() method or & operator returns a set that contains only items that exist in both sets.
print("Intersection of A and B:", A.intersection(B))  # or A & B

# Example 3: Difference Operation
# -------------------------
# The difference() method or - operator returns a set that contains only items that exist in the first set, and not in the second set.
print("Difference of A and B (A - B):", A.difference(B))  # or A - B

# Example 4: Symmetric Difference Operation
# -------------------------
# The symmetric_difference() method or ^ operator returns a set containing items from both sets, but not the common items.
print("Symmetric difference of A and B:", A.symmetric_difference(B))  # or A ^ B

# ==========================
# Set Methods
# ==========================

# Example 5: add() Method
# -------------------------
# The add() method adds a given element to the set. If the element is already present, it doesn't add any element.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print("Set after adding an element:", fruits)

# Example 6: remove() Method
# -------------------------
# The remove() method removes the specified element from the set. If the element is not found, it raises an error.
fruits.remove("banana")
print("Set after removing an element:", fruits)

# Example 7: pop() Method
# -------------------------
# The pop() method removes and returns an arbitrary set element. As sets are unordered, we cannot determine which item will be popped.
popped_item = fruits.pop()
print("Popped item from the set:", popped_item)
print("Set after popping an element:", fruits)

