import pandas as pd
import streamlit as st
import pyperclip
import base64   #Base64 is a group of similar binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation.
import sqlite3  #SQLite is a specific relational database management system (RDBMS) that implements a lightweight, serverless, self-contained, and transactional SQL database engine.
from database import values
from database import add_10th_Details
from database import add_12th_Details


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
    

def add_Graduation_Details():
    print("Graduation Details")

    
        