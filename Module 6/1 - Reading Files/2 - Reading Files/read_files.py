# --------------------------------------------------------------------------------
# Module 6: File Handling in Python
# Sections 1.2 - 1.4: Opening, Reading, and Resource Management
# --------------------------------------------------------------------------------

# 1. Introduction
# Python provides a comprehensive suite for file handling operations. 
# This module focuses primarily on reading files.

# --------------------------------------------------------------------------------
# 2. Traditional Method: Manual Open and Close
# --------------------------------------------------------------------------------

# This method involves explicitly opening and closing files.

# Open a file in read mode
file = open('sample.txt', 'r')
content = file.read()
print(content)
file.close()  # Don't forget to close the file!

# --------------------------------------------------------------------------------
# 3. The Modern Way: Using 'with'
# --------------------------------------------------------------------------------

# The 'with' statement automatically closes the file after operations are done.
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

# Note: There's no need to close the file explicitly. It's handled by the 'with' context.

# --------------------------------------------------------------------------------
# 4. File Modes and Focusing on Reading
# --------------------------------------------------------------------------------

# a) Reading the Entire File at Once
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

# b) Reading Line by Line
with open('sample.txt', 'r') as file:
    for line in file:
        print(line)

# c) Reading as a List of Lines
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)

# --------------------------------------------------------------------------------
# 5. Importance of Resource Management
# --------------------------------------------------------------------------------

# The 'with' statement ensures the file is closed, even if an exception occurs within the block.
# This makes resource management more efficient and helps prevent potential data corruption or other issues.

# --------------------------------------------------------------------------------
# Conclusion: 
# File reading in Python is intuitive and efficient. For best practices, always prefer the 'with' statement 
# for its automatic resource management capabilities.
# --------------------------------------------------------------------------------
