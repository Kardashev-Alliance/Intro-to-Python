# Module 6: File Handling in Python
# Section 2.1: Writing to Files

# --------------------------------------------------------------------------------
# 1. Writing Text to a New File
# --------------------------------------------------------------------------------

# Using 'w' mode creates a new file or overwrites an existing one
with open("sample_write.txt", "w") as file:
    file.write("Hello, Python World!\n")
    file.write("Writing to a file is easy.\n")

# --------------------------------------------------------------------------------
# 2. Appending Text to an Existing File
# --------------------------------------------------------------------------------

# Using 'a' mode appends to an existing file without overwriting its contents
with open("sample_write.txt", "a") as file:
    file.write("This line was appended later.\n")

# --------------------------------------------------------------------------------
# 3. Writing Binary Data (e.g., an Image)
# --------------------------------------------------------------------------------

# First, we'll read binary data from an image file
with open("sample_image.jpg", "rb") as source_file:
    data = source_file.read()

# Then, write this binary data to a new image file
with open("copy_sample_image.jpg", "wb") as dest_file:
    dest_file.write(data)

print("Text and binary writing examples completed.")
