# ===============================================
# Module 3, Section 4.2 - Combining `for` and `while` loops
# ===============================================

# Intro: Demonstrating the combination of 'for' and 'while' loops
print("\nDemonstrating combining 'for' and 'while' loops:\n")

# ----- Example 1: Basic combination -----
print("Example 1: Basic combination\n")

tasks = ["task1", "task2", "task3", "task4"]
confirmation = "yes"

for task in tasks:
    print(f"Starting {task}...")
    
    user_response = ""
    while user_response != confirmation:
        user_response = input(f"Confirm to proceed with {task} (type 'yes' to continue): ")
    
    print(f"{task} completed!\n")
# ----- End of Example 1 -----

print("-" * 50)  # Divider

# ----- Example 2: Benefits of Combination -----
print("\nExample 2: Benefits of combining loops\n")

# Demonstrating a repeated request for a number until a valid one is given.
numbers = [5, 15, 30, 45]
for num in numbers:
    user_num = -1
    while user_num < num:
        user_num = int(input(f"Enter a number greater than {num}: "))
    
    print(f"You entered {user_num}, which is greater than {num}.\n")
# ----- End of Example 2 -----

print("-" * 50)  # Divider

# ----- Example 3: Caution when combining -----
print("\nExample 3: Caution when combining\n")

print("Always ensure the inner loop (in this case, the 'while' loop) has a condition that can be met. Otherwise, you risk creating an infinite loop!")

# A potentially risky combination: Uncomment the next lines to test, but be prepared to interrupt execution.
# for _ in range(5):
#     print("This will print indefinitely unless you break the loop!")
#     while True:
#         pass
# ----- End of Example 3 -----

print("\nConclusion: Combining 'for' and 'while' loops allows for more complex control flows but requires careful management to prevent infinite loops.")
