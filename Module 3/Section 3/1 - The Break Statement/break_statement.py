# Module 3 - Section 3.1: The break Statement

# --------------------------------------------------
# Introduction to the break statement
# --------------------------------------------------
print("Introduction to the 'break' statement:")

for num in range(1, 11):
    if num == 5:
        print(f"Found the number {num}. Exiting the loop!")
        break
    print(num)

# --------------------------------------------------
# Using the break statement in a for loop
# --------------------------------------------------
print("\nUsing 'break' in 'for' loops:")

# Let's imagine a scenario where we're looking for a specific item in a list
items = ["apple", "banana", "cherry", "date", "fig"]
print(f"\nSearching for 'cherry' in the list: {items}")

for item in items:
    if item == "cherry":
        print(f"\nFound the item '{item}'!")
        break

# --------------------------------------------------
# Using the break statement in a while loop
# --------------------------------------------------
print("\nUsing 'break' with 'while' loops:")

# An example where we want to stop the loop once an external condition is met
count = 0
while count < 10:
    print(count)
    if count == 7:
        print(f"\nCount reached {count}. Exiting the loop!")
        break
    count += 1

# --------------------------------------------------
# Conclusion
# --------------------------------------------------
print("\nWith the power of the 'break' statement, you can have better control over your loops and can exit them whenever necessary!")

