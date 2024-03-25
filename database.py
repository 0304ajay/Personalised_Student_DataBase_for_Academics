import mysql.connector #Python applications to MySQL databases,
import random
my_Database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="Personalised_Student_DataBase_for_Academics",
    auth_plugin='mysql_native_password'
) #auth_plugin -> to verify using the password

my_Cursor=my_Database.cursor() #To execute SQL statements in a database session

def login(user_Id,password):
    my_Cursor.execute("SELECT passwrd , admin_Name FROM ADMINISTRATOR_TABLE_1 WHERE admin_Id=%s",(user_Id,))
    data=my_Cursor.fetchall()  #retrieves all rows returned by the SQL query executed using the cursor, and stores them in a list
    if(password==data[0][0]):
        return True,data[0][1]
    else:
        return False,None



# Adding the Aadhar Details
def add_My_Details(first_Name,last_Name,Aadhar_Number,Date_Of_Birth,phone_No,Email_Id,address):
    my_Cursor.execute("INSERT INTO PERSONAL_DETAILS_TABLE_2 (first_Name,last_Name,Aadhar_Number,Date_Of_Birth,phone_No,Email_Id,address) VALUES (%s,%s,%s,%s,%s,%s,%s)",(first_Name,last_Name,Aadhar_Number,Date_Of_Birth,phone_No,Email_Id,address))
    my_Database.commit()

# Adding the Voter Id Details
def add_Voter_Details(voter_Id,father_Name,mother_Name):
    my_Cursor.execute("INSERT INTO VOTER_ID_TABLE_3 (voter_Id,father_Name,mother_Name) VALUES (%s,%s,%s)",(voter_Id,father_Name,mother_Name))
    my_Database.commit()

def values(table_Name): #Function to retrieve the values from the table
    my_Cursor.execute(f"SELECT * FROM {table_Name}")
    data=my_Cursor.fetchall()
    return data

#Adding the Tenth Details
def add_10th_Details(tenth_School_Name,tenth_Roll_No,tenth_Year_Of_Passing,tenth_Board,tenth_Percentage):
    my_Cursor.execute("INSERT INTO TENTH_DETAILS_TABLE_4(tenth_School_Name,tenth_Roll_No,tenth_Year_Of_Passing,tenth_Board,tenth_Percentage) VALUES(%s,%s,%s,%s,%s)",(tenth_School_Name,tenth_Roll_No,tenth_Year_Of_Passing,tenth_Board,tenth_Percentage))
    my_Database.commit()



#Adding the Twelth Details
def add_12th_Details(twelth_College_Name,twelth_Roll_No,twelth_Year_Of_Passing,twelth_Board,twelth_Percentage):
    my_Cursor.execute("INSERT INTO TWELTH_DETAILS_TABLE_5(twelth_College_Name,twelth_Roll_No,twelth_Year_Of_Passing,twelth_Board,twelth_Percentage) VALUES(%s,%s,%s,%s,%s)",(twelth_College_Name,twelth_Roll_No,twelth_Year_Of_Passing,twelth_Board,twelth_Percentage))
    my_Database.commit()


#Adding the Graduation Details
def add_under_Graduation_Details(graduation_College_Name, graduation_Roll_No, graduation_Year_Of_Passing, graduation_Board, sem_1_GPA, sem_2_GPA, sem_3_GPA, sem_4_GPA, sem_5_GPA, sem_6_GPA, sem_7_GPA, sem_8_GPA, graduation_Percentage):
        my_Cursor.execute("INSERT INTO GRADUATION_DETAILS_TABLE_6 (graduation_College_Name, graduation_Roll_No, graduation_Year_Of_Passing, graduation_Board, SEM1_GPA, SEM2_GPA, SEM3_GPA, SEM4_GPA, SEM5_GPA, SEM6_GPA, SEM7_GPA, SEM8_GPA, graduation_Percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                          (graduation_College_Name, graduation_Roll_No, graduation_Year_Of_Passing, graduation_Board, sem_1_GPA, sem_2_GPA, sem_3_GPA, sem_4_GPA, sem_5_GPA, sem_6_GPA, sem_7_GPA, sem_8_GPA, graduation_Percentage))
        my_Database.commit()


#To get Notes Id
def get_Latest_Node_Id():
    my_Cursor.execute("SELECT MAX(note_Id) FROM NOTES_TABLE_7")
    latest_note_Id=my_Cursor.fetchone()[0]
    return latest_note_Id if latest_note_Id else 0

def add_Notes_Details(note_Id,note_Title,note_Description):
    my_Cursor.execute("INSERT INTO NOTES_TABLE_7(note_Id,note_Title,note_Description) VALUES(%s,%s,%s)",(note_Id,note_Title,note_Description))
    my_Database.commit()

def quotes():
    my_Cursor.execute('SELECT * FROM QUOTATIONS_8 WHERE quotation_Id=(%s)',(random.randint(1,10),))
    data=my_Cursor.fetchall()
    return data

def execute_Queries(commandLine):
    my_Cursor.execute(commandLine)
    data=my_Cursor.fetchall()
    return data
    
# def sign_Up(User_Id,password,User_Name):
#     my_Cursor.execute("INSERT INTO ADMINISTRATOR_TABLE_1 (admin_Id,passwrd,admin_Name) VALUES (%s,%s,%s)",(User_Id,password,User_Name))
#     my_Database.commit() #To execute the SQL statements, COMMIT is used to make the changes permanent in the database.

