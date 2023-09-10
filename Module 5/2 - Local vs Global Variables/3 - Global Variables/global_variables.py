# Module 5, Section 2.3: Global Variables

# ==========================
# Declaring a Global Variable
# ==========================
# A global variable is declared outside of a function. This variable can be accessed from anywhere in the module.
global_variable = "I am a global variable"

def display_global():
    """Function to display the global variable"""
    # Accessing the global variable without the need for the 'global' keyword since we're only reading its value
    print(global_variable)

display_global()

# =====================================
# Modifying Global Variable from Inside
# =====================================
# If you wish to modify a global variable from within a function, you need to use the 'global' keyword.

def modify_global():
    """Function to modify the global variable"""
    global global_variable  # This tells Python that we're referring to the global instance of 'global_variable'
    global_variable = "I am the modified global variable"

print("\nBefore modification from inside the function:", global_variable)
modify_global()
print("After modification from inside the function:", global_variable)

# ======================
# Potential Pitfalls
# ======================
# Modifying global variables without caution can lead to confusing results, as changes can affect other parts of your code.
def another_function():
    """Function that unknowingly depends on the global variable"""
    print("\nValue of global variable inside another_function:", global_variable)

another_function()

# ========================================
# Alternatives to Using Global Variables
# ========================================
# Instead of relying on global variables, you can pass them as function parameters.
def function_with_params(param):
    """Function that uses a parameter instead of a global variable"""
    print("\nThe value received as a parameter:", param)

function_with_params(global_variable)

# Note: It's a good practice to limit the use of global variables. If possible, use function parameters or class attributes to manage and modify data.
