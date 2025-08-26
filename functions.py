import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as my_file:
        pass

def get_todos():
    with open('todos.txt', 'r') as local_file:
        todos = local_file.readlines()
    return todos

def write_todos(new_todos):
    with open('todos.txt', 'w') as local_file:
        local_file.writelines(new_todos)