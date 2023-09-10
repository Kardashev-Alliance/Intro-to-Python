# -----------------------------
# Module 5 - Section 4.2: Importing Modules
# -----------------------------

# Comment: Introduction
# Importing allows us to utilize functions, classes, and variables from external modules. 
# This ability lets us harness the vast ecosystem of Python libraries.

# Basic Import
import math
print("Value of Pi:", math.pi)  # Access attributes using the module name as a prefix.

# Comment: Importing Specific Attributes
# Instead of importing an entire module, we can selectively import specific functions or classes.

from datetime import date
print("Today's Date:", date.today())  # Access directly without module prefix.

# Comment: Alias Import
# Aliasing helps in avoiding naming conflicts and can make code more concise.

import numpy as np
print("Numpy version:", np.__version__)  # Using alias as prefix.

from datetime import timedelta as td
print("One week from today:", date.today() + td(days=7))  # Using alias for attribute.

# Comment: Caution on Importing Everything
# It's generally not recommended due to potential naming conflicts and reduced code clarity.

# This line is for demonstration purposes only:
# from os import *

# Comment: Module Search Path
# Python searches for modules in a specific order: current directory, built-in modules, and paths in sys.path.

import sys
print("Python Module Search Path:", sys.path)

# Comment: Conclusion
# Mastering the art of importing in Python allows us to effectively leverage the functionalities 
# of both built-in and third-party modules, making our code more powerful and efficient.

