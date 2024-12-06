from modules import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a to-do:")
input_box = gui.InputText(tooltip="Enter todo", key='todo')
add_button = gui.Button("Add")

list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")


window = gui.Window("To-Do App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todo = values['todo'] + "\n"
            todos.append(todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            todos[todos.index(todo_to_edit)] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window["todo"].update(value=values['todos'][0])
        case gui.WINDOW_CLOSED:
            break



window.close()