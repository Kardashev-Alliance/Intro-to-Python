# ==========================
# Introduction to While Loop
# ==========================

# Basics of the While Loop
# ------------------------

# A simple counter demonstration using the while loop
counter = 0
while counter < 5:
    print(f"Counter value: {counter}")
    counter += 1
# Expected output:
# Counter value: 0
# Counter value: 1
# Counter value: 2
# Counter value: 3
# Counter value: 4


# Setting the Initial Condition
# ------------------------------

# Demonstrating the importance of setting an initial condition
# Resetting the counter value
counter = 0
while counter < 3:
    print(f"Initial condition demonstration: {counter}")
    counter += 1
# Expected output:
# Initial condition demonstration: 0
# Initial condition demonstration: 1
# Initial condition demonstration: 2


# Breaking Out of the Loop
# ------------------------

# Demonstrating the use of 'break' to exit a loop prematurely
counter = 0
while True:
    if counter == 3:
        break
    print(f"Break statement demonstration: {counter}")
    counter += 1
# Expected output:
# Break statement demonstration: 0
# Break statement demonstration: 1
# Break statement demonstration: 2


# Loop Control with continue
# --------------------------

# Demonstrating the 'continue' statement in a while loop
counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue
    print(f"Continue statement demonstration: {counter}")
# Expected output:
# Continue statement demonstration: 1
# Continue statement demonstration: 2
# Continue statement demonstration: 4
# Continue statement demonstration: 5


# Applications of While Loops
# ---------------------------

# Simple demonstration using while loop to read from a list until a certain value
data = ["apple", "banana", "cherry", "stop", "date", "fig"]
index = 0
while data[index] != "stop":
    print(f"Reading data: {data[index]}")
    index += 1
# Expected output:
# Reading data: apple
# Reading data: banana
# Reading data: cherry
