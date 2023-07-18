def get_todos(filepath = 'todos.txt'):
    with open(filepath,'r') as file:
        todos_local = file.readlines()
    return todos_local #local variable

def write_todos(todos_arg ,filepath ='todos.txt'):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
