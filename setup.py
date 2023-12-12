"""
Author:     Blake McBride (blakepm2@illinois.edu)
Created:    12/08/2023

Overview:   This file defines a script to install all the dependencies for this project
"""

# import standard modules
import subprocess
import sys

# define system requirements
REQUIRED_MAJOR = 3
REQUIRED_MINOR = 12
LINK = ""

def checkPythonVersion():
    """
    Verifies that the user has the correct version of Python installed
    """
    
    major, minor = list(sys.version_info)[:2]
    if major != REQUIRED_MAJOR or minor != REQUIRED_MINOR:
        print(f"This script requires Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}.")
        print(f"You are using Python {major}.{minor}. Please run this script with Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}.")
        print(f"You can download Python {REQUIRED_MAJOR}.{REQUIRED_MINOR} at: {LINK}")
        sys.exit(1)

def installDependencies():
    """
    Installs all of the dependencies in requirements.txt
    """
    with open('config/requirements.txt', 'r') as file:
        packages = [line.strip() for line in file if line.strip()]
        file.close()
    
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
if __name__ == '__main__':
    checkPythonVersion()
    installDependencies()
        