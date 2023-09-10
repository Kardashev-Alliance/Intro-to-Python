# ==========================
# Module 4, Section 1.2 & 1.3: Common List Operations & List Methods
# ==========================

# Declaring a sample list for demonstration
sample_list = [1, 2, 3, 4, 5]

# ------
# List Addition
# ------
print("Original List:", sample_list)

# Appending an element to the list
sample_list.append(6)
print("List after appending 6:", sample_list)

# ------
# Insertion
# ------
# Inserting an element at the second position (index 1)
sample_list.insert(1, 1.5)
print("List after inserting 1.5 at index 1:", sample_list)

# ------
# List Extension
# ------
# Extending the list with another list
sample_list.extend([7, 8, 9])
print("List after extending with [7, 8, 9]:", sample_list)

# Alternative way of extending a list using '+'
sample_list = sample_list + [10, 11]
print("List after extending with [10, 11] using '+':", sample_list)

# ------
# Removal
# ------
# Removing an element by value
sample_list.remove(1.5)
print("List after removing 1.5:", sample_list)

# Removing an element by index using pop
removed_element = sample_list.pop(2)  # Removing the third element
print(f"Removed the element {removed_element} from the list:", sample_list)

# ------
# Finding Elements
# ------
# Checking if an element exists in the list
is_five_in_list = 5 in sample_list
print("Is 5 in the list?", is_five_in_list)

# Finding the index of an element
index_of_five = sample_list.index(5)
print("Index of 5 in the list:", index_of_five)

# ------
# List Length
# ------
length_of_list = len(sample_list)
print("Length of the list:", length_of_list)

# ------
# Sorting and Reversing
# ------
# Sorting the list
sample_list.sort()
print("Sorted list:", sample_list)

# Sorting in reverse
sample_list.sort(reverse=True)
print("List sorted in reverse:", sample_list)

# Reversing the list
sample_list.reverse()
print("Reversed list:", sample_list)

# Using sorted() to sort a list without modifying the original
new_sorted_list = sorted(sample_list)
print("New sorted list:", new_sorted_list)
print("Original list after sorted():", sample_list)

# ------
# Counting Occurrences
# ------
sample_list.append(5)
count_of_fives = sample_list.count(5)
print("Count of 5s in the list:", count_of_fives)

# ------
# List Copy
# ------
# Using copy method
copied_list = sample_list.copy()
print("Copied list using copy method:", copied_list)
