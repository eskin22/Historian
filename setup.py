import subprocess
import sys

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 12
LINK = ""

def checkPythonVersion():
    major, minor = list(sys.version_info)[:2]
    if major != REQUIRED_MAJOR or minor != REQUIRED_MINOR:
        print(f"This script requires Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}.")
        print(f"You are using Python {major}.{minor}. Please run this script with Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}.")
        print(f"You can download Python {REQUIRED_MAJOR}.{REQUIRED_MINOR} at: {LINK}")
        sys.exit(1)

def installDependencies():
    with open('config/requirements.txt', 'r') as file:
        packages = [line.strip() for line in file if line.strip()]
        file.close()
    
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    

if __name__ == '__main__':
    checkPythonVersion()
    installDependencies()
        