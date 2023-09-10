# ==============================
# Module 4, Section 2.3: When and Why to Use Tuples
# ==============================

# ----
# Immutability Advantage
# ----

# Example of values that shouldn't change
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# Trying to modify a tuple will result in an error
# Uncommenting the line below will raise a TypeError
# days_of_week[0] = 'MONDAY'

print(days_of_week)

# ----
# Efficiency
# ----

# Simple demonstration of tuple vs list iteration
import time

large_tuple = tuple(range(1000000))
large_list = list(range(1000000))

# Measuring the time taken to iterate over a tuple
start_time = time.time()
for i in large_tuple:
    pass
end_time = time.time()
print(f"Time taken to iterate over tuple: {end_time - start_time:.6f} seconds")

# Measuring the time taken to iterate over a list
start_time = time.time()
for i in large_list:
    pass
end_time = time.time()
print(f"Time taken to iterate over list: {end_time - start_time:.6f} seconds")

# ----
# Using Tuples as Dictionary Keys
# ----

# Dictionary with tuple keys representing coordinates
coordinate_data = {
    (40.7128, 74.0060): 'New York',
    (34.0522, 118.2437): 'Los Angeles',
    (51.5074, 0.1278): 'London'
}

print(coordinate_data[(40.7128, 74.0060)])  # Output: New York

# Lists can't be used as dictionary keys
# Uncommenting the line below will raise a TypeError
# invalid_dict = {[1, 2]: 'This will not work'}

# ----
# Data Integrity
# ----

def process_data(data):
    # This function just prints the data, but the important part is that it can't modify it if it's a tuple
    print(data)

immutable_data = (1, 2, 3, 4, 5)
process_data(immutable_data)

