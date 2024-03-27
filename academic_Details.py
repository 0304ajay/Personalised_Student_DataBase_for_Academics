import pandas as pd
import streamlit as st
import pyperclip
import base64   #Base64 is a group of similar binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation.
import sqlite3  #SQLite is a specific relational database management system (RDBMS) that implements a lightweight, serverless, self-contained, and transactional SQL database engine.
from database import values
from database import add_10th_Details
from database import add_12th_Details
from database import add_under_Graduation_Details
from database import get_Latest_Node_Id
from database import add_Notes_Details
#Code To Upload photos and store in the database
# upload_File = st.sidebar.file_uploader(label="Upload Your Graduation Marksheet")
        
# if upload_File is not None:
#             # Process the uploaded file
#             st.write("You uploaded a file.")



# Creating a table to store the 10th class marksheets
def create_table():
    conn=sqlite3.connect('Tenth_Marksheet.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Tenth_Marksheet_TABLE (id INTEGER PRIMARY KEY AUTOINCREMENT,file_Name TEXT,file_data BLOB)''')
    #BLOB -> Binary Large Object
    conn.commit()
    conn.close()



def insert_pdf(file_Name,file_Data):
    conn=sqlite3.connect('Tenth_Marksheet.db')
    c=conn.cursor()
    c.execute(''' INSERT INTO  Tenth_Marksheet_TABLE (file_Name,file_Data) VALUES(?,?)''',(file_Name,file_Data))
    conn.commit()
    conn.close()



def retrieve_Pdf():
    conn=sqlite3.connect("Tenth_Marksheet.db")
    c=conn.cursor()
    c.execute('''SELECT id,file_Name FROM Tenth_Marksheet_TABLE''')
    pdf_File=c.fetchall()
    conn.close()
    return pdf_File



def retrieve_pdf_data(file_Id):
    conn=sqlite3.connect('Tenth_Marksheet.db')
    c=conn.cursor()
    c.execute('''SELECT file_Data FROM TENTH_MARKSHEET_TABLE WHERE id=?''',(file_Id,))
    file_Data=c.fetchone()[0]
    conn.close()
    return file_Data



# To STORE THE 12TH MARKSHEET(rewrite the Code like inheritance)
def create_table_2():
    conn=sqlite3.connect('Twelth_Marksheet.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Twelth_Marksheet_Table(id INTEGER PRIMARY KEY AUTOINCREMENT,file_Name TEXT,file_Data BLOB)''')
    conn.commit()
    conn.close()

def insert_pdf_2(file_Name,file_Data):
    conn=sqlite3.connect('Twelth_Marksheet.db')
    c=conn.cursor()
    c.execute('''INSERT INTO Twelth_Marksheet_Table(file_Name,file_Data) VALUES(?,?)''',(file_Name,file_Data))
    conn.commit()
    conn.close()

def retrieve_Pdf_2():
    conn=sqlite3.connect("Twelth_Marksheet.db")
    c=conn.cursor()
    c.execute('''SELECT id,file_Name FROM Twelth_Marksheet_Table''')
    pdf_File=c.fetchall()
    conn.close()
    return pdf_File

def retrieve_pdf_data_2(file_Id):
    conn=sqlite3.connect('Twelth_Marksheet.db')
    c=conn.cursor()
    c.execute('''SELECT file_Data FROM Twelth_Marksheet_Table WHERE id=?''',(file_Id,))
    file_Data=c.fetchone()[0]
    conn.close()
    return file_Data

def create_table_3():
    conn=sqlite3.connect('Graduation_Marksheet.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Graduation_Marksheet_Table(id INTEGER PRIMARY KEY AUTOINCREMENT,file_Name TEXT,file_Data BLOB)''')
    conn.commit()
    conn.close()

def insert_pdf_3(file_Name,file_Data):
    conn=sqlite3.connect('Graduation_Marksheet.db')
    c=conn.cursor()
    c.execute('''INSERT INTO Graduation_Marksheet_Table(file_Name,file_Data) VALUES(?,?)''',(file_Name,file_Data))
    conn.commit()
    conn.close()

def retrieve_Pdf_3():  
    conn=sqlite3.connect("Graduation_Marksheet.db")
    c=conn.cursor()
    c.execute('''SELECT id,file_Name FROM Graduation_Marksheet_Table''')
    pdf_File=c.fetchall()
    conn.close()
    return pdf_File

def retrieve_pdf_data_3(file_Id):
    conn=sqlite3.connect('Graduation_Marksheet.db')
    c=conn.cursor()
    c.execute('''SELECT file_Data FROM Graduation_Marksheet_Table WHERE id=?''',(file_Id,))
    file_Data=c.fetchone()[0]
    conn.close()
    return file_Data

def create_table_4():
    conn=sqlite3.connect('Under_Graduation_Marksheet.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Under_Graduation_Marksheet_Table(id INTEGER PRIMARY KEY AUTOINCREMENT,file_Name TEXT,file_Data BLOB)''')
    conn.commit()
    conn.close()

def insert_pdf_4(file_Name,file_Data):
    conn=sqlite3.connect('Under_Graduation_Marksheet.db')
    c=conn.cursor()
    c.execute('''INSERT INTO Under_Graduation_Marksheet_Table(file_Name,file_Data) VALUES(?,?)''',(file_Name,file_Data))
    conn.commit()
    conn.close()

def retrieve_Pdf_4():
    conn=sqlite3.connect("Under_Graduation_Marksheet.db")
    c=conn.cursor()
    c.execute('''SELECT id,file_Name FROM Under_Graduation_Marksheet_Table''')
    pdf_File=c.fetchall()
    conn.close()
    return pdf_File

def retrieve_pdf_data_4(file_Id):
    conn=sqlite3.connect('Under_Graduation_Marksheet.db')
    c=conn.cursor()
    c.execute('''SELECT file_Data FROM Under_Graduation_Marksheet_Table WHERE id=?''',(file_Id,))
    file_Data=c.fetchone()[0]
    conn.close()
    return file_Data

def create_table_5():
    conn=sqlite3.connect('photo.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Photo_Table(id INTEGER PRIMARY KEY AUTOINCREMENT,file_Name TEXT,file_Data BLOB)''')
    conn.commit()
    conn.close()

def insert_pdf_5(file_Name,file_Data):
    conn=sqlite3.connect('photo.db')
    c=conn.cursor()
    c.execute('''INSERT INTO Photo_Table(file_Name,file_Data) VALUES(?,?)''',(file_Name,file_Data))
    conn.commit()
    conn.close()

def retrieve_Pdf_5():
    conn=sqlite3.connect("photo.db")
    c=conn.cursor()
    c.execute('''SELECT id,file_Name FROM Photo_Table''')
    pdf_File=c.fetchall()
    conn.close()
    return pdf_File

def retrieve_pdf_data_5(file_Id):
    conn=sqlite3.connect('photo.db')
    c=conn.cursor()
    c.execute('''SELECT file_Data FROM Photo_Table WHERE id=?''',(file_Id,))
    file_Data=c.fetchone()[0]
    conn.close()
    return file_Data

def create_table_6():
    conn=sqlite3.connect('signature.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS signature_Table(id INTEGER PRIMARY KEY AUTOINCREMENT,file_Name TEXT,file_Data BLOB)''')
    conn.commit()
    conn.close()

def insert_pdf_6(file_Name,file_Data):
    conn=sqlite3.connect('signature.db')
    c=conn.cursor()
    c.execute('''INSERT INTO signature_Table(file_Name,file_Data) VALUES(?,?)''',(file_Name,file_Data))
    conn.commit()
    conn.close()

def retrieve_Pdf_6():
    conn=sqlite3.connect("signature.db")
    c=conn.cursor()
    c.execute('''SELECT id,file_Name FROM signature_Table''')
    pdf_File=c.fetchall()
    conn.close()
    return pdf_File

def retrieve_pdf_data_6(file_Id):
    conn=sqlite3.connect('signature.db')
    c=conn.cursor()
    c.execute('''SELECT file_Data FROM signature_Table WHERE id=?''',(file_Id,))
    file_Data=c.fetchone()[0]
    conn.close()
    return file_Data

def copy_To_Clipboard_1():
    data=values("TENTH_DETAILS_TABLE_4")
    df=pd.DataFrame(data)
    pyperclip.copy(df.to_csv(index=False))
    st.success("Data Copied to Clip Board Successfully")


def copy_To_Clipboard_2():
    data=values("TWELTH_DETAILS_TABLE_5")
    df=pd.DataFrame(data)
    pyperclip.copy(df.to_csv(index=False))
    st.success("Data Copied to Clip Board Successfully")

def copy_To_Clipboard_3():
    data=values("GRADUATION_DETAILS_TABLE_6")
    df=pd.DataFrame(data)
    pyperclip.copy(df.to_csv(index=False))
    st.success("Data Copied to Clip Board Successfully")


def store_Photo_Signnature():
    upload_File = st.sidebar.file_uploader(label="Upload Your Photo")
    create_table_5()
    if upload_File is not None:
        file_Data=upload_File.getvalue()
        file_Name=upload_File.name
        insert_pdf_5(file_Name,file_Data)
        st.sidebar.success(f"Successfully Uploaded and Saved {file_Name} to the Database")
    if st.sidebar.button(label="Download Photo"):
        pdf_Files=retrieve_Pdf_5()
        if pdf_Files:
            pdf_File_Itr=pdf_Files[0]
            st.write("Uploaded PDF Files :")
            st.write(pdf_File_Itr[1])
            download_Link=f'<a href="data:application/octet-stream;base64,{base64.b64encode(retrieve_pdf_data_5(pdf_File_Itr[0])).decode()}" download="{pdf_File_Itr[1]}">Click ME to Download⬇️ PHOTO</a>'
            st.sidebar.markdown(download_Link,unsafe_allow_html=True)

    upload_File = st.sidebar.file_uploader(label="Upload Your  Signature")
    create_table_6()
    if upload_File is not None:
        file_Data=upload_File.getvalue()
        file_Name=upload_File.name
        insert_pdf_6(file_Name,file_Data)
        st.sidebar.success(f"Successfully Uploaded and Saved {file_Name} to the Database")
    if st.sidebar.button(label="Download Signature"):
        pdf_Files=retrieve_Pdf_6()
        if pdf_Files:
            pdf_File_Itr=pdf_Files[0]
            st.write("Uploaded PDF Files :")
            st.write(pdf_File_Itr[1])
            download_Link=f'<a href="data:application/octet-stream;base64,{base64.b64encode(retrieve_pdf_data_6(pdf_File_Itr[0])).decode()}" download="{pdf_File_Itr[1]}">Click ME to Download⬇️ Signature</a>'
            st.sidebar.markdown(download_Link,unsafe_allow_html=True)
    st.sidebar.markdown("""
    ## Notes
    - In the First Place Upload Your Photo.
    - In the Second Upload Your Signature.
""")
    

def add_Tenth_Details():
    st.subheader('Enter 10th Details')
    column_1,column_2=st.columns(2)

    with column_1:
        tenth_School_Name=st.selectbox(label="Select School Name",options=["St. John's High School","Mother's International School","Scindia School","Bombay Scottish School","The Doon School","Delhi Public School"])
        tenth_Roll_No=st.text_input(label="Roll Number",value="",placeholder="Enter Your Roll Number")
        tenth_Year_Of_Passing=st.text_input(label="Year of Passing",value="",placeholder="Enter Your Year of Passing")

    with column_2:
        tenth_Board=st.selectbox(label="Select Board",options=["Central Board of Secondary Education (CBSE)","Andhra Pradesh Board of Secondary Education","Assam Board of Secondary Education","Bihar School Examination Board","Chhattisgarh Board of Secondary Education","Goa Board of Secondary & Higher Secondary Education"])        
        tenth_Percentage=st.text_input(label="Percentage/GPA",value="",placeholder="Enter Your Percentage/GPA")
        upload_File=st.file_uploader(label="Upload 10th Marksheet",type=["pdf"])
        create_table()
        if upload_File is not None:
            file_data=upload_File.getvalue()
            file_Name=upload_File.name
            insert_pdf(file_Name,file_data)
            st.success(f"Successfully Uploaded and Saved {file_Name} to the Database")

    if st.button("Add 10th Details",on_click=add_10th_Details,args=(tenth_School_Name,tenth_Roll_No,tenth_Year_Of_Passing,tenth_Board,tenth_Percentage),key="Add 10th Details"):
        st.success("Details Added Successfully")

    if st.button("Show Details",key="Show 10th Details"):
        data=values('TENTH_DETAILS_TABLE_4')
        df=pd.DataFrame(data)
        df.rename(columns={0:'School Name',1:'Tenth Roll Number',2:'Year of Passing',3:'Board of Education',4:'Percentage/GPA'},inplace=True)
        df.set_index('School Name',inplace=True)
        st.dataframe(df)
        pdf_Files=retrieve_Pdf()
        if pdf_Files:
            pdf_File_Itr=pdf_Files[0]
            st.write("Uploaded PDF Files :")
            #for pdf_File_Itr in pdf_Files:
            
            st.write(pdf_File_Itr[1])

            download_Link=f'<a href="data:application/octet-stream;base64,{base64.b64encode(retrieve_pdf_data(pdf_File_Itr[0])).decode()}" download="{pdf_File_Itr[1]}">Click ME to Download⬇️</a>'
            st.markdown(download_Link,unsafe_allow_html=True)
        st.button("Copy to clipboard",on_click=copy_To_Clipboard_1)


def add_Twelth_Details():
    st.subheader('Enter 12th Details')
    column_1,column_2=st.columns(2)

    with column_1:
        twelth_College_Name=st.selectbox(label="Select College Name",options=["NARAYANA IIT ACADEMY","SRI CHAITANYA","RV","FITJEE","ALLEN"])
        twelth_Roll_No=st.text_input(label="12th Roll Number",value="",placeholder="Enter Your Roll Number")
        twelth_Year_Of_Passing=st.text_input(label="12th Year of Passing",value="",placeholder="Enter Your Year of Passing")
    
    with column_2:
        twelth_Board=st.selectbox(label="12th Select Board",options=["Andhra Pradesh Intermediate Board","Telengana Intermediate Board","Karnataka Pre-University Board"])
        twelth_Percentage=st.text_input(label="12th Percentage/GPA",value="",placeholder="Enter Your Percentage/GPA")
        st.warning("Maximu Size of the file should be 100MB")
        upload_File=st.file_uploader(label="Upload Your 12th Marksheet",type=["pdf"])
        create_table_2()
        if upload_File is not None:
            file_Data=upload_File.getvalue()
            file_Name=upload_File.name
            insert_pdf_2(file_Name,file_Data)
            st.success(f"Successfully Uplpoaded and Saved {file_Name} to the Database")
            
        if st.button("Add 12th Details",on_click=add_12th_Details,args=(twelth_College_Name,twelth_Roll_No,twelth_Year_Of_Passing,twelth_Board,twelth_Percentage)):
            st.success("Details Added Successfully")

    if st.button("Show Details",key="Show 12th Details"):
            data=values('TWELTH_DETAILS_TABLE_5')
            df=pd.DataFrame(data)
            df.rename(columns={0:'College Name',1:'12th Roll No',2:'Year Of Passing',3:'Twelth Board',4:'Percentage/GPA'},inplace=True)
            df.set_index('College Name',inplace=True)
            st.dataframe(df)
            pdf_Files=retrieve_Pdf_2()
            if pdf_Files:
                pdf_File_Itr=pdf_Files[0]
                st.write("Uploaded PDF Files :")
                st.write(pdf_File_Itr[1])

                download_Link=f'<a href="data:application/octet-stream;base64,{base64.b64encode(retrieve_pdf_data_2(pdf_File_Itr[0])).decode()}" download="{pdf_File_Itr[1]}">Click ME to Download⬇⬆</a>'
                st.markdown(download_Link,unsafe_allow_html=True)
            st.button("Copy to Clipboard",on_click=copy_To_Clipboard_2)
    


def calulate_Overall_Percentage(sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8):
    return (sem1+sem2+sem3+sem4+sem5+sem6+sem7+sem8)/8


def add_Graduation_Details():
    st.subheader("Enter Graduatioin Details")
    column_1,column_2=st.columns(2)

    with column_1:
        graduation_College_Name=st.selectbox(label="Select College Name",options=["ACHARYA INSTITUTE OF TECHNOLOGY","BMS COLLEGE OF ENGINEERING","RV COLLEGE OF ENGINEERING","PES UNIVERSITY","DAYANANDA SAGAR COLLEGE OF ENGINEERING"])
        graduation_Roll_No=st.text_input(label="Gradution Roll Number",value="",placeholder="Enter Your Roll Number")
        graduation_Year_Of_Passing=st.text_input(label="Graduation Year of Passing",value="",placeholder="Enter Your Year of Passing")
        sem_1_GPA=st.number_input(label="Enter Semester 1 SGPA",value=0.0,step=0.01)
        sem_2_GPA=st.number_input(label="Enter Semester 2 SGPA",value=0.0,step=0.01)
        sem_3_GPA=st.number_input(label="Enter Semester 3 SGPA",value=0.0,step=0.01)
        upload_File=st.file_uploader(label="Upload Your Graduation Marksheet",type=["pdf"])
        create_table_3()
        if upload_File is not None:
            file_Data=upload_File.getvalue()
            file_Name=upload_File.name
            insert_pdf_3(file_Name,file_Data)
            st.success(f"Successfully Uplpoaded and Saved {file_Name} to the Database")

    
    with column_2:
        graduation_Board=st.selectbox(label="Graduation Select Board",options=["Visvesvaraya Technological University","Bangalore University","Mysore University"])
        sem_4_GPA=st.number_input(label="Enter Semester 4 SGPA",value=0.0,step=0.01)
        sem_5_GPA=st.number_input(label="Enter Semester 5 SGPA",value=0.0,step=0.01)
        sem_6_GPA=st.number_input(label="Enter Semester 6 SGPA",value=0.0,step=0.01)
        sem_7_GPA=st.number_input(label="Enter Semester 7 SGPA",value=0.0,step=0.01)
        sem_8_GPA=st.number_input(label="Enter Semester 8 SGPA",value=0.0,step=0.01)
        upload_File=st.file_uploader(label="Upload Your College Certification",type=["pdf"])
        create_table_4()
        if upload_File is not None:
            file_Data=upload_File.getvalue()
            file_Name=upload_File.name
            insert_pdf_4(file_Name,file_Data)
            st.success(f"Successfully Uplpoaded and Saved {file_Name} to the Database")

    overall_GPA=calulate_Overall_Percentage(sem_1_GPA,sem_2_GPA,sem_3_GPA,sem_4_GPA,sem_5_GPA,sem_6_GPA,sem_7_GPA,sem_8_GPA)
    graduation_Percentage=st.number_input(label="OVERALL Percentage/GPA",value=(overall_GPA))        
    
    if st.button("Add Graduation Details",on_click=add_under_Graduation_Details,args=(graduation_College_Name,graduation_Roll_No,graduation_Year_Of_Passing,graduation_Board,sem_1_GPA,sem_2_GPA,sem_3_GPA,sem_4_GPA,sem_5_GPA,sem_6_GPA,sem_7_GPA,sem_8_GPA,graduation_Percentage)):
        st.success("Details Added Successfully")

    if st.button("show Details",key="show Graduation Details"):
        data=values('GRADUATION_DETAILS_TABLE_6')
        df=pd.DataFrame(data)
        df.rename(columns={0:'College Name',1:'Graduation Roll No',2:'Year of Passing',3:'Board',4:'Sem 1 SGPA',5:'Sem 2 SGPA',6:'Sem 3 SGPA',7:'Sem 4 SGPA',8:'Sem 5 SGPA',9:'Sem 6 SGPA',10:'Sem 7 SGPA',11:'Sem 8 SGPA',12:'Overall Percentage/GPA'},inplace=True)
        #df.set_index('College Name',inplace=True)
        st.dataframe(df)
        pdf_Files_1=retrieve_Pdf_3()
        pdf_Files_2=retrieve_Pdf_4()
        if pdf_Files_1:
            pdf_File_Itr=pdf_Files_1[0]
            st.write("Uploaded PDF Files :")
            st.write(pdf_File_Itr[1])
            download_Link=f'<a href="data:application/octet-stream;base64,{base64.b64encode(retrieve_pdf_data_3(pdf_File_Itr[0])).decode()}" download="{pdf_File_Itr[1]}">Click ME to Download⬇️</a>'
            st.markdown(download_Link,unsafe_allow_html=True)
        if pdf_Files_2:
            pdf_File_Itr=pdf_Files_2[0]
            st.write("Uploaded PDF Files :")
            st.write(pdf_File_Itr[1])
            download_Link=f'<a href="data:application/octet-stream;base64,{base64.b64encode(retrieve_pdf_data_4(pdf_File_Itr[0])).decode()}" download="{pdf_File_Itr[1]}">Click ME to Download⬇️</a>'
            st.markdown(download_Link,unsafe_allow_html=True)
        st.button("Copy to Clipboard",on_click=copy_To_Clipboard_3)

def  add_Notes():
    st.subheader("Add Notes")
    note_number=get_Latest_Node_Id()
    note_Id=int(note_number+1)
    st.write("Note Number :",note_number+1)
    note_Title=st.text_input(label="Enter Heading of the Notes :",value="")
    note_Description=st.text_area(label="Enter Your Notes",value="",height=200)
    if st.button("Add Notes",on_click=add_Notes_Details,args=(note_Id,note_Title,note_Description),key="Add Notes"):
        st.success("Notes Added Successfully")

    if st.button("Show Notes",key="Show Notes"):
        data=values('NOTES_TABLE_7')
        if data:
            for row in data:
                st.write(f"Note Id : {row[0]}")
                st.write(f"Note Title : {row[1]}")
                st.write(f"Note Description : {row[2]}")
                if st.button(label="Delete",key=f"Deleting the Key" +str(row[0])):
                    st.write("Deleted Successfully")

                st.write("---------------------------------------------------")

                

def tracker():
        st.write(f"<div style='display:inline;'> Hello <h3>{st.session_state['name']}</h1></div>",unsafe_allow_html=True)
        st.write("Welcome to the Work Tracker")



 