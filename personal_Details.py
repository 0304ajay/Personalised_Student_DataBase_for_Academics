import streamlit as st
import pandas as pd
from database import add_My_Details
from database import add_Voter_Details
from database import values
import pyperclip #Pyperclip is a cross-platform python module used to interact with the clipboard.It allows us to copy and paste text to and from the clipboard


#Code for the Error Line :0304

def copy_To_Clipboard():
    data=values('PERSONAL_DETAILS_TABLE_2')
    df=pd.DataFrame(data)
    # Copy data to clipboard
    pyperclip.copy(df.to_csv(index=False)) #Copy the data to the clipboard
    st.success("Data copied to clipboard!")
    



# Code for the Aadhar Details
    
def aadhar_Details():
    st.subheader("Enter Aadhar Details")
    
    column_1,column_2=st.columns(2)
    
    with column_1:
        first_Name=st.text_input(label="First Name",value="",placeholder="Enter Your First Name")
        Aadhar_Number=st.text_input(label="Aadhar Number",value="",placeholder="Enter Your Aadhar Number")
        phone_No=st.text_input(label="Phone Number",value="",placeholder="Enter Your Phone Number")
        address=st.text_input(label="Address",value="",placeholder="Enter Your Address")

    with column_2:
        last_Name=st.text_input(label="Last Name",value="",placeholder="Enter Your Last Name")
        Date_Of_Birth = st.text_input("Date of Birth",value="",placeholder="Enter Your Date of Birth") # 0304 For how I have added  I am Getting the error
        Email_Id=st.text_input(label="Email_Id",value="",placeholder="Enter Your Email Id")

    if st.button("Add Details",on_click=add_My_Details,args=(first_Name,last_Name,Aadhar_Number,Date_Of_Birth,phone_No,Email_Id,address)):
            st.success("Details Added Successfully")
            print("Personal Details")

    if st.button("Show Personal Details",key="Personal details"): # IMPROVISE - 1 Should be able to copy data individually to clipboard
        data=values('PERSONAL_DETAILS_TABLE_2')
        df=pd.DataFrame(data)
        df.rename(columns={0:'First Name',1:'Last Name',2:'Aadhar Number',3:'Date Of Birth',4:'Phone Number',5:'Email',6:'Address'},inplace=True)
        df.set_index('First Name',inplace=True)
        st.dataframe(df)
        st.button("Copy to clipboard",on_click=copy_To_Clipboard)
            


            

# Code for the Voter Id 

def voter_Id_Details():
        st.subheader("Enter Voter Id Details")

        column_1,column_2=st.columns(2)

        with column_1:
            voter_Id=st.text_input(label="Voter Id",value="",placeholder="Enter Your Voter Id")
            father_Name=st.text_input(label="Fathers Name",value="",placeholder="Enter Your Fathers Name")
        
        with column_2:
            mother_Name=st.text_input(label="Mothers Name",value="",placeholder="Enter Your Mothers Name")

        if st.button("Add Details of voter",on_click=add_Voter_Details,args=(voter_Id,father_Name,mother_Name)):
            st.success("Details Added Successfully")
            print("Voter Id Details")
        
        if st.button("Show voter Id Details",key="Voter Id details"):
            data=values('VOTER_ID_TABLE_3')
            df=pd.DataFrame(data)
            df.rename(columns={0:'Voter Id',1:'Fathers Name',2:'Mothers Name'},inplace =True)
            df.set_index('Voter Id',inplace=True)            
            st.dataframe(df)
            st.button("Copy to clipboard",on_click=copy_To_Clipboard)
            



     
        