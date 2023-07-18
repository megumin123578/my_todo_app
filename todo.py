from function import get_todos, write_todos
import time

now = time.strftime('%B %d, %Y, %H:%M:%S')
print('it is', now)
# get user input and strip space chars from it
while True:
    user_action = input('Add, show, edit, delete or exit ?  ')


    if user_action.startswith('add'):
        todo = user_action[4:] 
        s = f'{todo}\n'

        todos = get_todos()

        todos.append(s)

        #open file and write
        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            print(f"{index + 1}.{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1
            
            todos = get_todos()

            
            new_todo = input('edit the todo you chose: ')
            todos[number] = new_todo +'\n'

            write_todos(todos)
        except ValueError:
            print('your command is not valid ! ')
            continue

    elif user_action.startswith('delete'):
        try:
            number = int(user_action[7:])
            
            todos = get_todos()

            
            index = number -1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_todos(todos)

            mess = f"Todo {todo_to_remove} was removed from the list"
            print(mess)
        except IndexError:
            print('There is no item with that number')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('unknow command')
print('bye')





