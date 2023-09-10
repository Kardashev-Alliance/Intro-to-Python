# --------------------------------------------------------------------------------
# 1. Basic Usage of `finally`
# --------------------------------------------------------------------------------

# Let's see how `finally` always executes irrespective of the occurrence of an exception.

try:
    x = 1 / 0  # This will raise an exception
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always be printed.")

# Output:
# Cannot divide by zero!
# This will always be printed.

# --------------------------------------------------------------------------------
# 2. Order of Execution: try -> except -> else -> finally
# --------------------------------------------------------------------------------

try:
    x = 5
    print("Value of x:", x)
except ValueError:
    print("ValueError occurred.")
else:
    print("No exceptions occurred.")
finally:
    print("Cleanup or final tasks here.")

# Output:
# Value of x: 5
# No exceptions occurred.
# Cleanup or final tasks here.

# --------------------------------------------------------------------------------
# 3. Using `finally` for Cleanup Tasks
# --------------------------------------------------------------------------------

# One of the most common use cases for the `finally` block is file handling.

filename = "sample.txt"

try:
    f = open(filename, 'r')
    content = f.read()
    print(content)
except FileNotFoundError:
    print(f"{filename} not found.")
finally:
    f.close()  # Ensuring the file is always closed
    print(f"{filename} has been closed.")

# --------------------------------------------------------------------------------
# 4. Pitfall: Using return inside `finally`
# --------------------------------------------------------------------------------

def faulty_return():
    try:
        return "From try block"
    finally:
        return "From finally block"

result = faulty_return()
print(result)  # This will print "From finally block" - which might not be the expected behavior!

# --------------------------------------------------------------------------------
# 5. Keeping `finally` Clear and Concise
# --------------------------------------------------------------------------------

# Here, we'll use `finally` to reset a variable, ensuring that no matter what happens, the variable is reset.

status = "In Progress"

try:
    # Some operations here
    status = "Completed"
except:
    status = "Failed"
finally:
    status = "Reset after operation"

print(status)  # Output: Reset after operation
