import streamlit as st
import database as db

def execute():
    commandLine=st.text_input("Enter the Query To Execute")
    if st.button("Execute Query"):
        res=db.execute_Queries(commandLine)
        st.success("Successfully Executed Query")
        if res:
            with st.expander("View Details"):
                st.dataframe(res)