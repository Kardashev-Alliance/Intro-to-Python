# ==============================================
# Module 3 - Section 1.4: The `else` Statement
# ==============================================

# -------------------------------
# Introduction to the else statement
# -------------------------------
print("Introduction to the 'else' statement")
print("=====================================")

# Demonstrating the basic usage of the else statement.
number = 5
if number > 10:
    print("Number is greater than 10.")
else:
    print("Number is 10 or less.")  # Expected Output: Number is 10 or less.
print("\n")

# -------------------------------
# Using else with if and elif statements
# -------------------------------
print("Using 'else' with 'if' and 'elif' statements")
print("============================================")

grade = 70
if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
else:
    print("Unfortunately, you did not pass.")  # Won't be printed in this case
print("\n")

# -------------------------------
# Validating user input with else
# -------------------------------
print("Validating user input using 'else'")
print("==================================")

user_input = input("Enter a positive number: ")
if user_input.isdigit():
    print(f"You entered {user_input}.")
else:
    print("That's not a positive number!")  # Will be printed if input isn't a positive number.
print("\n")

# -------------------------------
# Common pitfalls with else
# -------------------------------
print("Understanding common pitfalls using 'else'")
print("==========================================")

day = "Sunday"
if day == "Saturday":
    print("It's the weekend!")
elif day == "Sunday":
    print("Still the weekend!")
else:
    print("It's a weekday.")  # This won't be printed because Sunday is caught by the elif
print("\n")

# ==========================================
# End of Module 3 - Section 1.4 Examples
# ==========================================
