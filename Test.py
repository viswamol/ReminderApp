# Reminder program
import datetime
import sqlite3

# Defining function for create reminder

def create_data():  
    cursor = db.cursor()  
    date = input("Enter date to be remind (must be specify in order DD/MM/YYYY):")
    time = input("Enter time to be remind(must be specify in order HH:MM AM/PM):")
    message = input("Enter the Message to be remind: ")
    cursor.execute("INSERT INTO REMINDER(DATE,TIME,MESSAGE) VALUES(?,?,?)",(date,time,message))
    cursor.close()
    db.commit()
    print("Reminder fixed successfully")
    return_back()

#Define function for return back to option selection

def return_back():
    ch=input("Do you want to continue:y/n?")  
    if ch=='y':
        display()
    else:
        print("Thank you for using reminder") 
        exit()   

#Define function for display options
        
def display():
    print("1. Create Reminder")
    print("2. Update Reminder")
    print("3. View Reminder")
    n = int(input("Enter your option:"))  
    # storing the choice
    if n == 1:
        create_data()
    elif n == 2:
        update_data()
    elif n==3:
        view_data()
    else:
        print("Invalid choice. Please try again")
        return_back()

#Define function for update data into REMINDER

def update_data():    

    cursor = db.cursor() 
    sno =  input("Enter the Serial no of the reminder to be update:") 
    date = input("Update date to be remind (must be specify in order DD/MM/YYYY):")
    time = input("Update time to be remind (must be specify in order HH:MM AM/PM):")
    message = input("Enter the Message to  update reminder:") 
    cursor.execute("UPDATE REMINDER SET DATE= ?,TIME= ?,MESSAGE= ?  WHERE ID= ?",(date,time,message,sno) )
    cursor.close()
    db.commit()
    print("Reminder updated successfully")
    return_back()


def view_data():
    cursor = db.cursor()
    sql3 = "SELECT * FROM REMINDER"
    cursor.execute(sql3)
    print("******REMINDER DETAILS******")
    for i in cursor.fetchall():
        print("Serial no:" + str(i['id']) + " - "+ i['message'] + " on " + i['date'])  
    cursor.close()


#Open database connection

db = sqlite3.connect("sqlite.db")
db.row_factory = sqlite3.Row

#create table REMINDER if it not exist
cursor = db.cursor()
sql="CREATE TABLE IF NOT EXISTS REMINDER (ID INTEGER PRIMARY KEY AUTOINCREMENT,DATE  VARCHAR(20),TIME VARCHAR(20),MESSAGE  VARCHAR(20))"
cursor.execute(sql)
cursor.close()


#display options towads user
print("Welcome to reminder application")
display()

#Close database connection
db.close()