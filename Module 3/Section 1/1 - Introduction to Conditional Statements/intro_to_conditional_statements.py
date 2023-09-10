# ========================================
# Module 3: Conditional Statements in Python
# Section 1.1: Introduction to Conditional Statements
# ========================================

# -------------------------------------------------
# The Essence of Conditional Statements
# -------------------------------------------------
# An example to decide which road to take based on a sign.

sign = "Left"
if sign == "Left":
    direction = "Turn left at the crossroad."
else:
    direction = "Continue straight."

print(direction)  # Outputs: "Turn left at the crossroad."

# -------------------------------------------------
# The Power of 'if'
# -------------------------------------------------
# Using the if statement to determine if a number is even.

number = 8
if number % 2 == 0:
    print(f"{number} is even.")  # Outputs: "8 is even."

# -------------------------------------------------
# The Balance of 'else'
# -------------------------------------------------
# Using else to handle when a condition isn't met.

value = -5
if value > 0:
    print(f"{value} is positive.")  # This won't be printed.
else:
    print(f"{value} is negative.")  # Outputs: "-5 is negative."

# -------------------------------------------------
# The Flexibility of 'elif'
# -------------------------------------------------
# Using elif to categorize an age.

age = 15
if age < 13:
    category = "Child"
elif 13 <= age < 18:
    category = "Teenager"
else:
    category = "Adult"

print(f"An individual of {age} years is a {category}.")  # Outputs: "An individual of 15 years is a Teenager."

# ========================================
# End of Section 1.1
# ========================================
