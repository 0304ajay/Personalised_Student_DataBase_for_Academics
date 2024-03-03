import streamlit as st
import pandas as pd
from database import add_My_Details


#Code for the Error Line :0304


def aadhar_Details():
    st.subheader("Enter Aadhar Details")
    
    column_1,column_2=st.columns(2)
    
    with column_1:
        first_Name=st.text_input(label="First Name",value="",placeholder="Enter Your First Name")
        Aadhar_Number=st.text_input(label="Aadhar Number",value="",placeholder="Enter Your Aadhar Number")
        phone_No=st.text_input(label="Phone Number",value="1234567890",placeholder="Enter Your Phone Number")


    with column_2:
        last_Name=st.text_input(label="Last Name",value="",placeholder="Enter Your Last Name")
        Date_Of_Birth = st.text_input("Date of Birth",value="2021-01-01") # 0304 For how I have added  I am Getting the error
        Email_Id=st.text_input(label="Email_Id",value="example@gmail.com",placeholder="Enter Your Email Id")

    if st.button("Add Details"):
        add_My_Details(first_Name,last_Name,Aadhar_Number,Date_Of_Birth,phone_No,Email_Id)
        st.success("Details Added Successfully")
        print("Personal Details")


def voter_Id_Details():
    print("Voter Id Details")
        