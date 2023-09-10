# ================================================
# Module 3, Section 1.3: The 'elif' Statement
# ================================================

# The 'elif' statement allows for multiple conditions to be checked in sequence.
# It's an abbreviation for "else if".

# -----------------------------
# Example: Grading System
# -----------------------------

# Given student marks, we'll assign a grade using 'elif' for clarity and simplicity.

marks = 85  # Example student's score

if marks > 90:
    print("Grade: A")
elif marks > 80:
    print("Grade: B")
elif marks > 70:
    print("Grade: C")
elif marks > 60:
    print("Grade: D")
else:
    print("Grade: F")

# Here, each 'elif' checks a new condition if the previous ones were false.
# The 'else' at the end covers all other cases (when marks are 60 or below).

# -----------------------------
# Multiple Conditions
# -----------------------------

# 'elif' is perfect for situations with many possible conditions.
# Let's use it to identify the day of the week based on a given number.

day_number = 3  # Example: Representing Wednesday

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid number for a day!")

# With 'elif', the flow is clear, and the program will exit the structure once a true condition is met.

# -----------------------------
# Everyday Analogy: Doors
# -----------------------------

# Let's simulate a scenario where a character tries multiple doors until finding an open one.

doors = ["locked", "locked", "open", "locked"]

for door in doors:
    if door == "open":
        print("Found an open door!")
        break  # Exit the loop when an open door is found
    elif door == "locked":
        print("This door is locked.")
    else:
        print("This is not a door!")

# Here, our character checks each door and reacts based on its status.
# The 'elif' helps to add clarity to our conditions.
