from modules import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a to-do:")
input_box = gui.InputText(tooltip="Enter todo", key='todo')
add_button = gui.Button("Add")

window = gui.Window("To-Do App",
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 16))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            todo = values['todo'] + "\n"
            todos.append(todo)
            functions.write_todos(todos)
        case gui.WINDOW_CLOSED:
            break



window.close()