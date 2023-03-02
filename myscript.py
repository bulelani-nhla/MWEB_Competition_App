import os
import subprocess

# Check if MySQL is installed
mysql_installed = False
if os.path.exists("C:/Program Files/MySQL/MySQL Server 8.0"):
    mysql_installed = True
else:
    print("MySQL is not installed.")


venv_dir = "virtualFolder"
if not os.path.exists(venv_dir):
    try:
        # Create a virtual environment folder in the project directory
        subprocess.call(["python", "-m", "venv", "virtualFolder"])
    except Exception as e:
        print("Error creating virtual environment directory:", e)
        exit()



# Activate virtual environment
activate_script = "virtualFolder/Scripts/Activate.ps1"
subprocess.call(["powershell.exe", "-Command", f"& {activate_script}"])

# Check if required modules are installed
modules = ["mysql-connector-python", "pyfiglet", "pandas"]
for module in modules:
    try:
        __import__(module)
    except ImportError:
        subprocess.call(["pip", "install", module])

# Run application
os.system("python application.py")        