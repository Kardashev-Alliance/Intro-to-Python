# --------------------------------------------------------------------------------
# Module 6: File Handling in Python
# Section 2.2: Creating New Files
# --------------------------------------------------------------------------------

# Necessary Library
import os

# --------------------------------------------------------------------------------
# 1. Creating a New Configuration File
# --------------------------------------------------------------------------------
# This example demonstrates the creation of a configuration file.

config_path = "configs/new_config.txt"

# Check if directory exists; if not, create it
if not os.path.exists("configs"):
    os.makedirs("configs")

try:
    with open(config_path, 'x') as file:
        file.write("USER=example_user\n")
        file.write("PASSWORD=example_password\n")
    print(f"Configuration file '{config_path}' created successfully!")
except FileExistsError:
    print(f"'{config_path}' already exists. Avoiding overwrite.")

# --------------------------------------------------------------------------------
# 2. Creating a New Log File
# --------------------------------------------------------------------------------
# This example demonstrates the creation of a daily log file.

from datetime import date

log_path = f"logs/{date.today()}_log.txt"

# Check if directory exists; if not, create it
if not os.path.exists("logs"):
    os.makedirs("logs")

try:
    with open(log_path, 'x') as file:
        file.write(f"Log for {date.today()}:\n")
    print(f"Log file '{log_path}' created successfully!")
except FileExistsError:
    print(f"'{log_path}' already exists. Avoiding overwrite.")

# --------------------------------------------------------------------------------
# 3. Data Collection - New File for Each Session
# --------------------------------------------------------------------------------
# This example demonstrates the creation of a new file for each data collection session.

session_id = input("Enter session ID: ")
data_path = f"data/{session_id}_data.txt"

# Check if directory exists; if not, create it
if not os.path.exists("data"):
    os.makedirs("data")

try:
    with open(data_path, 'x') as file:
        file.write(f"Data for session {session_id}:\n")
    print(f"Data file '{data_path}' created successfully!")
except FileExistsError:
    print(f"'{data_path}' already exists. Avoiding overwrite.")
