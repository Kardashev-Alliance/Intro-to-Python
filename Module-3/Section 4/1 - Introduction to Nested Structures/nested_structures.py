# Module 3, Section 4.1 - Introduction to Nested Structures

# -------------------------
# Nested If Statements
# -------------------------

age = 17
has_permission = False

# Outer condition
if age >= 18:
    # Inner condition
    if has_permission:
        print("You can enter the club!")
    else:
        print("You might be 18 or above, but you need permission.")
else:
    print("Sorry, you're too young.")

# -------------------------
# Nested Loops
# -------------------------

# Using nested loops to print a simple 2D matrix
for i in range(3):  # Outer loop
    for j in range(3):  # Inner loop
        print(f"({i}, {j})", end=" ")
    print()  # for new line after inner loop completes one cycle

# -------------------------
# Combining Nested Structures
# -------------------------

numbers = [1, 2, 3, 4, 5]

# Outer condition
if len(numbers) > 0:
    # Inner loop
    for num in numbers:
        if num % 2 == 0:  # Innermost condition
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
else:
    print("The list is empty.")

# -------------------------
# Limitations and Best Practices
# -------------------------

# While it's possible to nest structures deeply, it's good practice to avoid it 
# when possible to maintain readability and ease of debugging. 
# If you find your code getting too nested, consider breaking it into functions 
# or using other strategies to simplify.

