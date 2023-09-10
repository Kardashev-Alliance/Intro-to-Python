# --------------------------------------------------------------------------------
# Module 6: File Handling in Python
# Section 2.3: Appending to Files (Extended Examples)
# --------------------------------------------------------------------------------

# Introduction:
# Appending allows us to add data to the end of a file, whether it's text, binary, or structured data.

import csv
import os

# --------------------------------------------------------------------------------
# 1. Appending Text Data
# --------------------------------------------------------------------------------
# Let's start by appending some lines to a text file.

with open("sample.txt", "a") as text_file:
    text_file.write("\nAppended line 1")
    text_file.write("\nAppended line 2")

# After running this, "sample.txt" will have two new lines added to it.

# --------------------------------------------------------------------------------
# 2. Appending Binary Data
# --------------------------------------------------------------------------------
# To append binary data, we open the file in 'ab' mode (append binary). 
# As a simulation, let's append one image to another, creating a collage.

if os.path.exists("image1.jpg") and os.path.exists("image2.jpg"):
    with open("image1.jpg", "ab") as img1, open("image2.jpg", "rb") as img2:
        img1.write(img2.read())

# This will append the content of image2.jpg to image1.jpg.

# --------------------------------------------------------------------------------
# 3. Appending to CSV Files
# --------------------------------------------------------------------------------
# For data collection or analysis, we often add new rows to existing CSV files.

new_data_rows = [
    [5, "Emma", "Engineering"],
    [6, "Lucas", "HR"]
]

with open("employees.csv", "a", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(new_data_rows)

# This appends new rows to the "employees.csv" file.

# --------------------------------------------------------------------------------
# Conclusion:
# Appending is versatile. Whether it's adding new entries to a dataset, merging binary files, or expanding a text document,
# understanding how to append properly is a key skill in file operations.
# --------------------------------------------------------------------------------
