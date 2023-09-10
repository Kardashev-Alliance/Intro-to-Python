# Module 5, Section 2.1: Understanding Scope

# Example 1: Local Scope
def local_scope_demo():
    local_variable = "I'm local to this function"
    print(local_variable)

# Trying to access the local variable outside the function would result in an error
# Uncommenting the line below would cause an error
# print(local_variable)


# Example 2: Global Scope
global_variable = "I'm a global variable"

def global_scope_demo():
    global global_variable
    global_variable = "Modified inside a function"
    print(global_variable)

print(global_variable)  # This will print the initial value
global_scope_demo()     # This will modify the global variable and print the modified value
print(global_variable)  # This will print the modified value


# Example 3: Nonlocal Scope
def outer_function():
    enclosing_variable = "I'm in the enclosing function"
    
    def inner_function():
        nonlocal enclosing_variable
        enclosing_variable = "Modified inside inner function"
        print(enclosing_variable)

    inner_function()
    print(enclosing_variable)

outer_function()


# Example 4: Enclosing Scope
def enclosing_scope_demo():
    enclosing_variable = "I'm in the enclosing function's local scope"
    
    def nested_function():
        print(enclosing_variable)

    nested_function()

enclosing_scope_demo()


# Example 5: Shadowing
shadow_variable = "I'm a global variable"

def shadow_demo():
    shadow_variable = "I'm local to the function"
    print(shadow_variable)

print(shadow_variable)  # This will print the global variable's value
shadow_demo()           # This will print the local variable's value, shadowing the global one

