# ------------------------------------------------------------
# Module 3 - Section 1.5: Combining Conditions
# ------------------------------------------------------------

# ------------------------------
# Basics of Multiple Conditions
# ------------------------------

# Using logical operators: and, or, not

# Example with and operator
age = 25
has_license = True

if age >= 18 and has_license:
    print("You're allowed to drive!")
else:
    print("Sorry, you cannot drive.")

# ------------------------------
# Embracing the or Operator
# ------------------------------

# Either condition can be true for the statement to execute

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("Enjoy your day off!")
else:
    print("It's a working day.")

# ------------------------------
# Inverting with the not Operator
# ------------------------------

# Negating a condition

is_raining = False

if not is_raining:
    print("It's a sunny day!")
else:
    print("Take an umbrella.")

# ------------------------------
# Logical Operators' Precedence
# ------------------------------

# not > and > or

value = True
value2 = False

# This checks not value2 (which becomes True) AND value
if not value2 and value:
    print("This condition is true!")

# This checks value OR not value2 (either of them is True)
if value or not value2:
    print("This condition is also true!")

# ------------------------------
# Practical Scenarios
# ------------------------------

# Combining multiple conditions can be useful in many scenarios

grade = 85
attendance = 90

if grade >= 80 and attendance >= 75:
    print("You passed the course!")
else:
    print("You need to meet both criteria to pass.")

# END
