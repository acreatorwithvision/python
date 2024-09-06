import streamlit as st
from C:\Users\DELL\PycharmProjects\python\app2-portfolio\send_email

st.header("Contact Me")

with st.form(key="my_forms"):
    user_email = st.text_input("Your email address")

    message = st.text_area("Your message")
    button=st.form_submit_button()
