import functions  #import functions.py file
import PySimpleGUI as sg  #GUI module in python which needs to be downloaded before working on that.


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")


button_labels=["close","apply"]

complete_button=sg.Button("Complete")


layout=[[label], 
        [input_box, add_button], 
        [list_box, edit_button,complete_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 30))



while True:
    event, values = window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            
        case 'complete':
            todo_to_complete=values['todos'][0]
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

print("Bye")
window.close()

