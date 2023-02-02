import mysql.connector as msql
from mysql.connector import Error
import logging
import logging
import os
import pyfiglet
import re
import csv

# Database connection function
def create_connection():
        """
        Connects to the database using environment variables for the password and database name
        """
        try:
            connection = msql.connect(host='localhost',
                                    user='root',
                                    password=os.environ.get('DB_PASSWORD'),
                                    database=os.environ.get('DB_NAME'),
                                    port=3306)
            return connection
        except Error as e:
            logging.error(f"Error connecting to database: {e}")


# Home page function
def Home_page():

        header_1 = pyfiglet.figlet_format("WELCOME TO MWEB COMPETITION APP !!!", font = "digital")
        header_2 = pyfiglet.figlet_format("Competition App")
        para_1 = "\n[Verion 1.0.1]\nCopyright (c) [2023] \nAll rights reserved.\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED , WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, \nWHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\n"   
        print(header_1, header_2, para_1)


# Error Handler Function for csv file
def validate_csv(csv_file):
    if not csv_file.endswith('.csv'):
        raise ValueError("Invalid file type. Please enter a CSV filename that ends with .csv ")
    if not os.path.isfile(csv_file):
        raise FileNotFoundError(f"{csv_file} not found.")
    else:
        return csv_file  



# Error Handler Competition Name:
def validate_compname(input_string):
    pattern = r"^[A-Za-z0-9]+$"
    if re.search(pattern, input_string):
        return input_string
    else:
        raise ValueError("Input should contain only letters, numbers and no spacing inbetween")

# Error Handler Function for Winners needed?       
def validate_winners(input_string):
    pattern = r"^\d+$"
    if re.search(pattern, input_string):
        return input_string
    else:
        raise ValueError("Input should contain only numbers")


# Creating Table from csv data save database as competition id number
def create_table_and_insert_data(Final_ID, csv_file, cursor, connection):
    tb_create = "CREATE TABLE {} (first_name varchar(255),last_name varchar(255),phone_number varchar(255),email varchar(255))"
    cursor.execute(tb_create.format(Final_ID))

    with open(csv_file) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            tb_create2 = "INSERT INTO {} (first_name , last_name, phone_number, email) VALUES (%s,%s,%s,%s)"
            cursor.execute(tb_create2.format(Final_ID), row)
            connection.commit()





# Draw machine handle
def PullWinners():
    print('Press enter to pull the winners of the competition!')
    input()

# Winners pool  
prizes = ["1st Prize", "2nd Prize", "3rd Prize","4th Prize", "5th Prize", "6th Prize","7th Prize", "8th Prize", "9th Prize","10th Prize", "11th Prize", "12th Prize"]



# Logging format: global
logging.basicConfig(filename="logfile.log", level=logging.INFO, format='[%(asctime)s]--- [%(message)s]')

def log_csv(type):
    # Logging the csv filename into log file 
    log_message = "File {} Uploaded To Database."
    logging.info(log_message.format(type))

def log_Comp_ID(type):
    # Logging the Competition_ID into log file
    log_message = "Competition_ID : {}"
    logging.info(log_message.format(type))  

def log_entries(type):
 # Logging number of entries into log file
    log_message = "Winners selected: {}"
    logging.info(log_message.format(type))
    

def log_app(type):
    # Logging aoolication exit into log file
    if type == "start":
        return logging.info("***** Application Started. *****")
    elif type == "end":
        return  logging.info("***** Application Ended. *****")
    
def log_winners(type):
    # Logging winners outcome log file
    logging.info(type)




