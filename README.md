
# Competitions App

This a competition app that reads data from a csv and then data is imported and saved into a MySQL database, with the competition name/id used to link to the imported data, the program then asks how many winners are needed and randomly selects the winners from csv records, displaying the results in the console. The results are saved in the database and output to a text file that includes competition details, winners, and contact information. Finally, auditing is added to track all procedures
[![asciicast](https://asciinema.org/a/P4RBJlEUdZ3UeMqgp1joEdSk5.svg)](https://asciinema.org/a/P4RBJlEUdZ3UeMqgp1joEdSk5)

## Installation

Requirement before running the app:

•	Make sure a Python Interpreter is installed on the    Host Machine

•	Install MySQL with MySQL Installer


•	Install Python Modules with pip

```bash
pip install mysql-connector-python
pip install pyfiglet
pip install pandas
```
2. Install virtualenv via pip on the Host Machine

```bash
python -m pip install --user virtualenv
python -m virtualenv –help
```

Create a virtual environment folder in the project directory
```bash
python -m venv virtualFolder
```

3. Create a .gitignore file in your repository's root directory [virtualFolder] to tell Git which files and directories to ignore when you make a commit.

-------------------------------------------.

Configure the connection to the database using environment variables for the password and database name
