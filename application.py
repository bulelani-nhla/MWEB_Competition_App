import mysql.connector as msql
from mysql.connector import Error
import pandas as pd
import random
from app_modules import *
import datetime





def main():

    # Connect to the database
    connection = create_connection()
    cursor = connection.cursor()

    # Logging aoolication start into log file
    log_app("start")

    # Home page of the console App
    Home_page()
    

    ##### 1. Input name of csv file (Excel/CSV)  ###################################
    class bcolors:
        OK = '\033[92m' #GREEN
        WARNING = '\033[93m' #YELLOW
        FAIL = '\033[91m' #RED
        RESET = '\033[0m' #RESET COLOR


    csv_file = input("Enter the csv filename to be read:   ")
    while True:
        try:
            validated_input = validate_csv(csv_file)                      # Use Error Handler function from app_modules
            print(f"Validated input: {validated_input}")
            break
        except ValueError as e:
            print(e)
            csv_file = input("Enter the csv filename to be read:   ")
        except FileNotFoundError as e1:
            print(e1)
            csv_file = input("Enter the csv filename to be read:   ")       
    print(f"{bcolors.OK}File selected: {csv_file}{bcolors.RESET}\n")             

    # Logging the csv filename into log file 
    log_csv(csv_file)
    

    ####### 2. What is the competition name? #############################################
    
    cpuser_input = input("What is the name of the competition ?:   ")
    while True:
        try:
            validated_input = validate_compname(cpuser_input)       # Use Error Handler function from app_modules
            print(f"Validated input: {validated_input}")
            break
        except ValueError as e:
            print(e)
            cpuser_input = input("What is the name of the competition ?:   ")

    # Generating random competition id number
    rand_num= random.randint(0,10000)
    Competition_ID = 'Comp'+str(rand_num) +'_{}'
    Final_ID = Competition_ID.format(cpuser_input)
    print("Competition_ID :" , Final_ID + "\n")

    # Creating Table from csv data save database as competition id number
    create_table_and_insert_data(Final_ID, csv_file, cursor, connection)

    # Logging the Competition_ID into log file
    log_Comp_ID(Final_ID)


    # Create a text file output *****************************************************
    text_output = "App TextOutput/{}.txt"
    text_file = text_output.format(Final_ID)
    file = open(text_file, "w")

    # Write to text file include datetime
    e = datetime.datetime.now() 
    file.write(e.strftime("%Y-%m-%d %H:%M:%S"))
    file.write('\nCompetition ID : '+Final_ID)
    # *********************************************************************************



   


    ####### 3. How many Winners needed? ###########################################
    
    winners = input("How many Winners needed:")
    while True:
            try:
                validated_input = validate_winners(winners)       # Use Error Handler function from app_modules
                print(f"Validated input: {validated_input}")
                break
            except ValueError as e:
                print(e)
                winners = input("How many Winners needed:")

    ####### 4. Random select winners  ###########################################

    PullWinners()

    # Logging number of entries into log file
    log_entries(winners)

    # Write to text file
    text_display = "Winners selected: {}"
    file.writelines("\n"+ text_display.format(winners)+ "\n") 
            

    with connection:
            with connection.cursor() as cursor:

                # Add placeholders (curly brackets {})
                sql = "SELECT * FROM {} ORDER BY RAND () LIMIT {};" 
                # Use String format()   
                cursor.execute(sql.format(Final_ID, winners))
                result = cursor.fetchall()
                Winner_Display = pd.DataFrame(result, columns=['first_name', 'last_name', 'phone_number', 'email'])
                #Create 'Winners' Column
                Winner_Display['winners'] = pd.DataFrame(prizes)
                            
                print("\n-------- Congratulation !!! The Winners Are --------\n\n",Winner_Display.head())
                print(" ")

                # Logging number of entries into log file
                log_winners(Winner_Display)

                # Write to text file
                file.writelines(str(Winner_Display)) 
                            
                # Exit the database                  
                connection.close()


    # Logging aoolication start into log file
    log_app("end")

    # Close Text File
    file.close()


if __name__== '__main__':
    main()    



