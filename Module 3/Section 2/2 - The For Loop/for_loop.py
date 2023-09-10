# MODULE 3: Loops
# Section 2.2: The For Loop

# -----------------------------------
# Basics of the For Loop
# -----------------------------------
# A simple for loop iterating over a list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n")  # Adding a newline for clarity in output

# -----------------------------------
# Looping Through Strings
# -----------------------------------
# Using for loop to iterate through each character of a string

word = "Python"
for char in word:
    print(char)

print("\n")  # Adding a newline for clarity in output

# -----------------------------------
# Using the range() Function
# -----------------------------------
# Using range() to iterate a specific number of times

for i in range(5):  # Will loop from 0 to 4
    print(i)

print("\n")  # Adding a newline for clarity in output

# -----------------------------------
# Nesting For Loops
# -----------------------------------
# Nested for loop to iterate over a 2D list (matrix)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=' ')  # Using end to print in the same line
    print()  # Newline for each row

print("\n")  # Adding a newline for clarity in output

# -----------------------------------
# Loop Control with break and continue
# -----------------------------------
# Using break to exit the loop prematurely

for num in range(10):
    if num == 5:
        break
    print(num, end=' ')

print("\n")  # Adding a newline for clarity in output

# Using continue to skip an iteration

for num in range(10):
    if num % 2 == 0:  # Checking if the number is even
        continue  # If even, skip the print statement and move to the next iteration
    print(num, end=' ')

print("\n")  # Adding a newline for clarity in output

