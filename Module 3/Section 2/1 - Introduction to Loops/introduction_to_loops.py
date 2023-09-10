# ---------------------------------------
# Module 3 Section 2.1: Introduction to Loops
# ---------------------------------------

# Basics of Looping
# ---------------------------------------
# A simple loop that prints numbers from 1 to 5
for i in range(1, 6):
    print(f"Number: {i}")

# ---------------------------------------
print("\n")  # A separator for the output
# ---------------------------------------

# Types of Loops: For Loop
# ---------------------------------------
# Using a for loop to iterate over a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# ---------------------------------------
print("\n")  # A separator for the output
# ---------------------------------------

# Types of Loops: While Loop
# ---------------------------------------
# Using a while loop to print numbers till a condition is met
number = 1
while number <= 3:
    print(f"While Loop Number: {number}")
    number += 1

# ---------------------------------------
print("\n")  # A separator for the output
# ---------------------------------------

# Why Loop? Demonstrating the power of loops
# ---------------------------------------
# Printing a message multiple times using a for loop
for _ in range(3):
    print("This message is printed using a loop!")

# ---------------------------------------
print("\n")  # A separator for the output
# ---------------------------------------

# Loop Components
# Initialization, Condition, Increment/Decrement demonstrated using a while loop
count = 0  # Initialization
while count < 3:  # Condition
    print(f"Count: {count}")
    count += 1  # Increment

# End of Introduction to Loops
# ---------------------------------------
