# ==================================
# Module 3, Section 4.4
# Best Practices and Pitfalls
# ==================================

# 1. Infinite Loops
# ==================================
# A simple representation of an unintended infinite loop.
# Uncomment the below code to see it in action. Remember to stop the script manually!
"""
while True:
    print("This will run forever!")
"""

# 2. Over-nesting
# ==================================
# Excessive nesting can make the code harder to read.
for i in range(5):
    for j in range(5):
        for k in range(5):
            # ... and so on.
            print(f"i: {i}, j: {j}, k: {k}")

# 3. Not Using Else with For
# ==================================
# The 'else' can be paired with 'for' to run a block of code when the loop is done.
for num in range(5):
    print(num)
else:
    print("Loop is finished!")

# 4. Ignoring Break and Continue
# ==================================
# Demonstration of 'break' and 'continue'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 4:
        break
    print(num)

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# 5. Not Commenting Complex Conditions
# ==================================
# Always comment on complex conditions for clarity.

# The below condition checks if the number is odd and divisible by 3
num = 9
if num % 2 != 0 and num % 3 == 0:
    print(f"{num} is odd and divisible by 3")

