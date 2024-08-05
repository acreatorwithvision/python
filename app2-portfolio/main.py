import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
    st.image("images/1.png")

with col2:
    st.title("Suhas G")
    content = "Hi, Myself suhas G and im a programmer trying to learn python"
    st.info(content)

content2="Hello and who are you. You can edit this later in the course."

st.write(content2)