
from pathlib import Path

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth#streamlit auth



st.set_page_config(page_title="Admin Page", page_icon=":tada", layout="wide")


names = ["Admin1"]
usernames = ["adadmin"]
passwords=["admin@test"]



       
        

# load hashed passwords

authenticator = stauth.Authenticate(names, usernames, passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=1)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:   
       
 # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write( )
            st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
