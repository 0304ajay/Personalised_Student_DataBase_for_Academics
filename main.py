import streamlit as st
import random
import database as db
import numpy as np
from personal_Details import aadhar_Details #we can keep filename and the function name same
from personal_Details import voter_Id_Details #we can keep filename and the function name same
from academic_Details import add_Tenth_Details
from academic_Details import add_Twelth_Details
from academic_Details import add_Graduation_Details
from academic_Details import store_Photo_Signnature
from academic_Details import add_Notes
from developer import execute
from academic_Details import tracker
from database import quotes
st.set_page_config(layout='wide', page_title='My Web App', page_icon=':smiley:', initial_sidebar_state='auto')

headerSection = st.container()
main_Section = st.container()
login_Section = st.container()


column_1,column_2=st.columns(2)

def personal_Details():
     with main_Section:
          aadhar_details,voter_Id=main_Section.tabs(["Aadhar Details","Voter Id Details"])
          with aadhar_details:
               aadhar_Details()
          with voter_Id:
               voter_Id_Details()
     
def academic_Details():
     with main_Section:
          tenth_Details,twelth_Details,graduation_Details,notes,Work_Tracker,developer_Options=main_Section.tabs(["10th Details","12th Details","Graduation Details","Notes","Work Tracker","Developer Options"])
          with tenth_Details:
               add_Tenth_Details()
          with twelth_Details:
               add_Twelth_Details()
          with graduation_Details:
               add_Graduation_Details()
          with notes:
            add_Notes()
          with Work_Tracker:
            tracker()
          with developer_Options:
            execute()


def show_Main_Page():
    st.title(f"Hi {st.session_state['name']}")
    st.write("Welcome to Personalised Student DataBase for Academics")
    image = open("PROFILE.jpg", "rb").read()
    
    # Display the image
    st.image(image, caption='Your Image', width=150, use_column_width=False,clamp=True)
    st.write("")
    st.write("")
    st.write("")
    data=quotes()
    st.write(f"<h3 style= 'color :green;'>{data[0][2]}</h3>",unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.warning("NOTE:")
    st.write("Click on Personal Details to Store Personal Details")
    st.write("Click on Academic Details to Store Academic Details")

    with column_1:
        personal_Details()              #THE PAGE REFRSHING PROBLEM IS SOLVED BY USING THE FUNCTION CALLING
        store_Photo_Signnature()
        
    with column_2:             
        st.button("Academic Details",key="Academic Details")
        academic_Details()



def loggedIn_Clicked(user_Name, password):
    value,name = db.login(user_Name, password) #calling the login function from the database.py file
    if value:
            st.session_state['loggedIn'] = True
            st.session_state['name'] = name
    else:
            st.session_state['loggedIn'] = False
            st.error("Invalid User Name or Password")



def show_Login_Page():
    with login_Section:
        if st.session_state['loggedIn']==False:
            user_Name=st.text_input (label="User-Id", value="", placeholder="Enter your User Id")
            password =st.text_input(label="Password", value="", placeholder="Enter Your Password", type="password")
            st.button ("Login", on_click=loggedIn_Clicked, args=(user_Name, password))


with headerSection:
    st.title("Personalised Student DataBase for Academics")
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        #show_login_page() 
        show_Login_Page() 
    else:
        if st.session_state['loggedIn']:    
            show_Main_Page()  
        else:
            show_Login_Page()


#               Trailed Data


# def sign_Up_Clicked(user_Id,password,User_Name):
#     db.sign_Up(user_Id,password,User_Name)
#     st.success("User Created Successfully")



# def show_SignUP_Page():
#     with signUp_Section:
#         user_Id=st.text_input(label="Enter Your new User-Id", value="", placeholder="Enter your User new User Id")
#         password =st.text_input(label="Enter Your Password", value="", placeholder="Enter Your new Password", type="password")
#         User_Name=st.text_input(label="Enter Your Name",value="",placeholder="Enter Your Name")
#         st.button("Sign Up",on_click=sign_Up_Clicked,args=(user_Id,password,User_Name))    


# def show_SignUp_Button():
#     if st.button("Sign Up",key="Sign Up"):
#          show_SignUP_Page()


# with header_Section:
#     st.write("Consistency is the true foundation of trust")
#     st.title("Welcome to Personalised Student DataBase for Academics")
#     st.button("Sign Up",on_click=show_SignUP_Page, key="Sign Up")
#     st.button("Login",on_click=show_Login_Page,key="Login")


# col1, col2 = st.columns(2)

# with col1:
#     if st.button("Sign Up", key="Sign Up"):
#         st.write("Sign Up clicked")

# with col2:
#     if st.button("Login", on_click=show_Login_Page, key="Login"):
#         st.write("Login clicked")

# st.markdown("""
# <style>
# .stButton > button {
#     margin-top: 100px;
#     background-color: red;
#     color: white;
# }
# </style>
# """, unsafe_allow_html=True)
