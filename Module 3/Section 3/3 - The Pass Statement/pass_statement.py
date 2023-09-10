# Module 3 - Section 3.3: The pass Statement

# -----------------------------
# Introducing the pass statement
# -----------------------------

# The pass statement is essentially a no-op. It does nothing.
# It can be used as a placeholder when code is required syntactically, 
# but you want to skip any action.

# For example, when you define an empty function or class:
def yet_to_implement_function():
    pass

class YetToImplementClass:
    pass

print("Function and class defined with pass executed without any errors!")


# -------------------------------------
# Practical Use Cases of the pass statement
# -------------------------------------

# Scenario: Let's say you're developing a function, but you're unsure about the implementation yet.
# Instead of leaving it empty and causing an error, use the pass statement.

def process_data(data):
    # TODO: Implement this function later.
    pass

# Even though we haven't implemented 'process_data', our program runs error-free.


# ---------------------------------------------------
# Difference between pass, break, and continue in loops
# ---------------------------------------------------

numbers = [1, 2, 3, 4, 5]

print("\nUsing pass inside a loop:")

for num in numbers:
    if num == 3:
        pass
    print(num)

# In the above loop, the pass statement does nothing when num is 3. The loop continues its natural flow.

print("\nUsing continue inside a loop:")

for num in numbers:
    if num == 3:
        continue
    print(num)

# With continue, when num is 3, the loop skips the print statement and continues to the next iteration.

print("\nNote: As seen in the examples, while break and continue alter the flow of loops, pass does nothing and lets the code execute naturally.")


# ----------------
# Real-world Example
# ----------------

# While developing a software, you may want to draft the structure 
# without implementing the actual functionalities. 
# The pass statement allows you to do so without any errors.

class SoftwareModule:
    def feature_one(self):
        pass

    def feature_two(self):
        pass

print("\nSoftware module with features defined using pass executed without any errors!")

