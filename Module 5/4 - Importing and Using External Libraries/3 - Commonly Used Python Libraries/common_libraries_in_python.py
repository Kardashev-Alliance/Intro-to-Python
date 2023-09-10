# ===============================================
# Module 5, Section 4.3: Commonly Used Python Libraries
# ===============================================

# ===============================================
# Internal Libraries:
# These libraries are part of the Python Standard Library and do not require additional installation.
# ===============================================

# Importing sys library
import sys

# sys provides access to Python's interpreter-related functionalities.
# Common Use Case: Command line argument parsing
args = sys.argv
print(f"Command line arguments: {args}")
# Note: This will fetch arguments provided during script execution.

# -----------------------------------------------
# Importing os library
import os

# os provides a portable way to interact with the operating system.
# Common Use Case 1: Accessing environment variables
path = os.environ.get('PATH')
print(f"System PATH: {path}")

# Common Use Case 2: Listing files in the current directory
files = os.listdir('.')
print(f"Files in current directory: {files}")

# -----------------------------------------------
# Importing time library
import time

# time offers functionalities related to time.
# Common Use Case: Sleep operations
print("Sleeping for 2 seconds...")
time.sleep(2)  # Pauses the script for 2 seconds
print("Woke up!")

# ===============================================
# External Libraries:
# These libraries require installation. Instructions for installation are provided below.
# ===============================================

# For some of these libraries, PIP (Package Installer for Python) is required.
# If you don't have PIP installed, refer to the following link for installation instructions:
# https://pip.pypa.io/en/stable/installation/

# NumPy (Numerical Python)
# Description: Essential for numerical computations in Python.
# Installation: Uncomment the line below to install using pip.
# pip install numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Array using NumPy: {arr}")

# Pandas
# Description: Provides data structures and data analysis tools.
# Installation: Uncomment the line below to install using pip.
# pip install pandas
import pandas as pd

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}
df = pd.DataFrame(data)
print("Data using Pandas:")
print(df)

# Matplotlib
# Description: Plotting library for Python.
# Installation: Uncomment the line below to install using pip.
# pip install matplotlib
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.title('Sample Plot')
plt.show()

# Requests
# Description: HTTP library for Python.
# Installation: Uncomment the line below to install using pip.
# pip install requests
import requests

response = requests.get('https://api.github.com')
print(f"Response from GitHub API: {response.json()}")

# Note: Ensure to uncomment the pip installation lines if you haven't installed these libraries yet.
