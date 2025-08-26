import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state['new_todo']+"\n"
    todos.append(new_todo)
    functions.write_todos(todos)

st.title('My Todos App')
st.subheader('This is my Todo Web App')

for todo in todos:
    st.checkbox(label=todo)

st.text_input(placeholder="Enter your todo...",
              label="",
              label_visibility="hidden",
              on_change=add_todo,
              key="new_todo")