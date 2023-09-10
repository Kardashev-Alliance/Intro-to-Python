# Module 4, Section 4.4: Practical Use Cases of Dictionaries

# 1. Data Organization and Storage:
# Representing a student's record using a dictionary
student_record = {
    "name": "John Doe",
    "ID": "S12345",
    "grades": [85, 90, 78, 92]
}
print("Student Record:", student_record)

# ------------------------------------------------------------------------------

# 2. Caching (Memoization):
# Implementing caching for Fibonacci series calculation using a dictionary
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

print("Fibonacci(7) with caching:", fibonacci(7))

# ------------------------------------------------------------------------------

# 3. Counting and Frequency Analysis:
# Counting the frequency of words in a given text
text = "apple orange banana apple orange"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word Frequencies:", word_count)

# ------------------------------------------------------------------------------

# 4. Grouping and Aggregation:
# Grouping people by their professions and counting the number in each profession
people = [
    {"name": "Alice", "profession": "Engineer"},
    {"name": "Bob", "profession": "Doctor"},
    {"name": "Charlie", "profession": "Engineer"},
    {"name": "David", "profession": "Artist"},
]
profession_count = {}
for person in people:
    profession = person["profession"]
    profession_count[profession] = profession_count.get(profession, 0) + 1
print("Profession Frequencies:", profession_count)

# ------------------------------------------------------------------------------

# 5. Implementing Switch/Case Structures:
# Mimicking a switch/case structure to create a basic calculator for arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operation_switch = {
    "add": add,
    "subtract": subtract
}
print("Add 5 and 3:", operation_switch["add"](5, 3))
print("Subtract 5 from 8:", operation_switch["subtract"](8, 5))

# ------------------------------------------------------------------------------
