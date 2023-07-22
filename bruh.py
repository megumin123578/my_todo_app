import streamlit as st
import function

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    function.write_todos(todos)

todos = function.get_todos()

st.title('My todo App')
st.subheader('this is subheader')
st.write('this app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label ='', placeholder='Enter a todo', on_change=add_todo, key='new_todo')
# hihi