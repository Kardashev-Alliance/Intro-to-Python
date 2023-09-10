# --------------------------------------------------------------------------------
# 1. Installing PIP (Package Installer for Python)
# --------------------------------------------------------------------------------

# PIP is the package installer for Python and is included by default with Python 2 >=2.7.9 or Python 3 >=3.4.
# If it's not installed, you can manually install it.
# First, download `get-pip.py` from the official site (https://bootstrap.pypa.io/get-pip.py).
# Navigate to the directory where the file is located and run:
# python get-pip.py

# Note: Depending on your setup, you might need to use `python3` instead of `python`.

# --------------------------------------------------------------------------------
# 2. Virtual Environments (venv)
# --------------------------------------------------------------------------------

# venv is included in the Python standard library for Python 3.3 and later.
# It's used to create isolated Python environments.
# Navigate to the directory where you want the environment and use:
# python3 -m venv name_of_the_environment

# To activate the virtual environment:
# On Windows:
# name_of_the_environment\Scripts\activate.bat
# On Unix or MacOS:
# source name_of_the_environment/bin/activate

# --------------------------------------------------------------------------------
# 3. Anaconda and Mamba
# --------------------------------------------------------------------------------

# Anaconda is a distribution of Python and R for scientific computing and data science.
# Mamba is a reimplementation of the conda package manager in C++.
# You can use Mamba just like you would use conda after installing it.

# To install Anaconda:
# Visit the Anaconda website (https://www.anaconda.com/products/distribution) and download the appropriate version.

# After installing Anaconda, if you want to switch to Mamba (which is faster than conda):
# conda install mamba -c conda-forge

# Use Mamba in place of Conda for installing packages and managing environments.

# --------------------------------------------------------------------------------
# 4. Docker
# --------------------------------------------------------------------------------

# Docker allows you to create containers, which are like lightweight virtual machines.
# They help ensure consistency across multiple platforms and development environments.

# To install Docker:
# Visit the Docker website (https://docs.docker.com/get-docker/) and follow the installation instructions for your OS.

# After installation, you can pull Python images and run Python inside a container for a consistent development experience.

# --------------------------------------------------------------------------------
# 5. Package Management with pipenv and poetry
# --------------------------------------------------------------------------------

# pipenv and poetry are dependency management tools for Python.

# To install pipenv:
# pip install pipenv

# To start a new project using pipenv:
# pipenv install <package_name>

# To install poetry:
# pip install poetry

# Initialize a new project using poetry:
# poetry new <project_name>

# Both pipenv and poetry provide deterministic builds, meaning they'll always produce the same build from the same input.
