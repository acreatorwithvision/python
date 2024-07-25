import streamlit as st #library used to create web app.install using pip3 install streamlit
import functions
def add_todo():
    todo=st.session_state['new_todo']
    print(todo)

todos=functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is to record or monitor todo app")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo..."
              ,on_change=add_todo,key="new_todo")

print("Hello")