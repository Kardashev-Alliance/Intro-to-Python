# --------------------------------------------------------------------------------
# Module 6 - File Handling
# --------------------------------------------------------------------------------
# Section 1.1 - Introduction to File Handling
# --------------------------------------------------------------------------------

# The purpose of this file is to demonstrate some basic concepts related to file
# handling in Python. We won't be diving into reading or writing just yet, but we'll
# understand some foundational elements.

# --------------------------------------------------------------------------------
# 1. Open a File
# --------------------------------------------------------------------------------

# We'll just open a file for this demonstration. Ensure you have a file named
# 'sample.txt' in the same directory as this script.

# 'r' denotes that we are opening the file in read mode.
file = open('sample.txt', 'r')

# --------------------------------------------------------------------------------
# 2. Check the File Mode
# --------------------------------------------------------------------------------

# The mode with which the file was opened can be checked using the 'mode' attribute.
print(f"File mode: {file.mode}")

# --------------------------------------------------------------------------------
# 3. Check if the File is Closed
# --------------------------------------------------------------------------------

# The 'closed' attribute tells us if a file is closed or not.
print(f"Is file closed?: {file.closed}")

# --------------------------------------------------------------------------------
# 4. Close the File
# --------------------------------------------------------------------------------

file.close()
print(f"Is file closed after calling close()?: {file.closed}")

# --------------------------------------------------------------------------------
# 5. Using 'with' for File Handling
# --------------------------------------------------------------------------------

# Using 'with' is a best practice when working with files as it automatically
# manages resources and closes the file once operations are done.

with open('sample.txt', 'r') as file_with:
    # For demonstration, we'll just print the mode again.
    print(f"File mode within 'with' block: {file_with.mode}")

print(f"Is file closed after 'with' block?: {file_with.closed}")

# --------------------------------------------------------------------------------
# Note: Actual reading and writing operations will be covered in upcoming sections.
# This is just to get you familiar with the basic operations and checks.
# --------------------------------------------------------------------------------
