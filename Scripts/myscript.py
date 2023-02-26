import os
import subprocess

# Check if MySQL is installed
mysql_installed = False
if os.path.exists("C:/Program Files/MySQL/MySQL Server 8.0"):
    mysql_installed = True
else:
    print("MySQL is not installed.")

# Check if required Python modules are installed
required_modules = ["mysql-connector-python", "pyfiglet", "pandas"]
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{module} module is not installed.")

# Install virtualenv via pip
subprocess.call(["python", "-m", "pip", "install", "--user", "virtualenv"])

# Create a virtual environment folder in the project directory
subprocess.call(["python", "-m", "venv", "virtualFolder"])
