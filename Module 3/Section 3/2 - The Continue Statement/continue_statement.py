# Module 3, Section 3.2: The continue Statement
# ---------------------------------------------

# Introduction and Basics
print("Introduction to the continue statement:\n")
print("The continue statement allows you to skip the rest of the loop's current iteration and move on to the next one.")
input("Press Enter to continue...")

# Using `continue` in a for loop
print("\nUsing `continue` within a for loop:\n")
for num in range(10):
    if num % 2 == 0:  # If the number is even
        continue  # Skip the rest of the loop's body
    print(num, "is an odd number.")
input("Press Enter to continue...")

# The difference between `break` and `continue`
print("\nDifference between `break` and `continue`:\n")
print("In a loop, `break` will exit the loop entirely, while `continue` will just skip the current iteration.")
input("Press Enter to continue...")

# Using `continue` in a while loop
print("\nUsing `continue` within a while loop:\n")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print("Count is:", count)
input("Press Enter to continue...")

# Practical Applications
print("\nPractical applications of the continue statement:\n")
data = [1, 2, 'corrupted', 3, 4, 'corrupted', 5]
print("Given a list with some corrupted data entries:", data)
print("\nUsing continue to process only valid data entries:\n")
for item in data:
    if item == 'corrupted':
        continue
    print("Processed item:", item)
input("Press Enter to finish...")
