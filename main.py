import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state['new_todo']+"\n"
    st.session_state['new_todo'] = None
    todos.append(new_todo)
    functions.write_todos(todos)

st.title('My Todos App')
st.subheader('This is my Todo Web App')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(placeholder="Enter your todo...",
              label="",
              label_visibility="hidden",
              on_change=add_todo,
              key="new_todo")