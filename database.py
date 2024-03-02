import mysql.connector #Python applications to MySQL databases,

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
    




    
# def sign_Up(User_Id,password,User_Name):
#     my_Cursor.execute("INSERT INTO ADMINISTRATOR_TABLE_1 (admin_Id,passwrd,admin_Name) VALUES (%s,%s,%s)",(User_Id,password,User_Name))
#     my_Database.commit() #To execute the SQL statements, COMMIT is used to make the changes permanent in the database.

