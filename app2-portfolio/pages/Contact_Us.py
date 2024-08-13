import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from send_email import send_email

st.header("Contact Me")

with st.form(key="my_forms"):
    user_email = st.text_input("Your email address")

    message = st.text_area("Your message")
    button=st.form_submit_button()
