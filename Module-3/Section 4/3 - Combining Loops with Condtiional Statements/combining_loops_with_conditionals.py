# ========================================
# Module 3, Section 4.3: Combining Loops with Conditional Statements
# ========================================

# ---- Basic Combination ----
print("Example 1: For loop with a simple condition")

for i in range(5):
    if i % 2 == 0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")

# ---- Using `continue` in a loop with conditions ----
print("\nExample 2: Using `continue` to skip odd numbers")

for i in range(5):
    if i % 2 != 0:
        continue
    print(f"{i} is even and processed.")

# ---- Nested `if` within a `while` loop ----
print("\nExample 3: `while` loop with nested `if` conditions")

count = 0
while count < 5:
    if count % 2 == 0:
        print(f"{count} is even.")
    else:
        print(f"{count} is odd.")
    count += 1

# ---- Using `break` within a loop with conditions ----
print("\nExample 4: Breaking out of a loop based on a condition")

for i in range(10):
    if i == 5:
        print(f"Reached the stop value at {i}.")
        break
    print(i)

# ---- Combining `for` and `while` with conditions ----
print("\nExample 5: Combining `for` and `while` with conditions")

for i in range(5):
    j = 0
    while j < 3:
        if j == i:
            print(f"Match found for {i} and {j}.")
        j += 1
