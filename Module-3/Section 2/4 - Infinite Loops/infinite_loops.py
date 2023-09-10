# ================================================
# Module 3, Section 2.4: Infinite Loops
# ================================================

# ---------------------------
# What is an Infinite Loop?
# ---------------------------
print("Demonstrating an infinite loop (Press Ctrl+C to stop):")
# Uncomment the below lines to see an infinite loop in action.
# CAUTION: This will run indefinitely unless stopped.
# while True:
#     print("This will run forever!")

# A small pause before the next demonstration.
input("\nPress Enter to continue to the next section...\n")

# --------------------------------------
# The Good Side of Infinite Loops
# --------------------------------------
# Infinite loops can be useful in certain scenarios where a program 
# or service needs to run indefinitely until an external input stops it.
# Here's a simulated server checking for requests:
print("Simulated server checking for requests (Press Ctrl+C to stop):")
# Uncomment the lines below to see this in action.
# while True:
#     user_input = input("Send a request or type 'exit' to stop: ")
#     if user_input == 'exit':
#         break
#     print(f"Processing request: {user_input}")

input("\nPress Enter to continue to the next section...\n")

# --------------------------------
# The Accidental Infinite Loop
# --------------------------------
# It's common to unintentionally create infinite loops when 
# forgetting to update loop conditions. Here's an example:
counter = 0
print("Supposed to print numbers 1 to 5:")
# Uncomment the lines below to see the mistake in action. 
# CAUTION: This loop will not stop on its own.
# while counter <= 5:
#     print(counter)
#     # Mistakenly left out: counter += 1

input("\nPress Enter to continue to the next section...\n")

# ----------------
# Breaking Free
# ----------------
# Here's how you can use the 'break' statement to escape an infinite loop.
print("Demonstrating 'break' to escape an infinite loop:")
while True:
    user_decision = input("Type 'stop' to exit the loop: ")
    if user_decision == 'stop':
        break
    print("Still in the loop...")

print("\nThat's all for this section on Infinite Loops!")
