from modules import functions
import FreeSimpleGUI as gui
import os

# If the todos.txt does not exist, then create it
if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

# GUI Elements
# Input Box for typing in the to-do
input_box = gui.InputText(tooltip="Enter todo", key='todo', background_color="Silver")

# Label displaying the instruction
label = gui.Text("Type in a to-do:", background_color="Black")

# Buttons
add_button = gui.Button("Add", button_color="DarkGrey")            # Add Button
edit_button = gui.Button("Edit", button_color="DarkGrey")                    # Edit Button
complete_button = gui.Button("Complete", button_color="DarkGrey")            # Complete Button
exit_button = gui.Button("Exit", button_color="DarkGrey")                    # Exit Button

# Listbox for displaying the to-dos. Gets the to-to items from todos.txt
list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10),
                       background_color="Silver")

# Setting the theme of the GUI
gui.theme("Black")

# Columns
col1 = gui.Column([[label], [input_box], [list_box], [exit_button]])
col2 = gui.Column([[add_button], [edit_button], [complete_button]])

# The layout of the program. Text rows are separated based on the rows in the GUI
layout = [[col1, col2]]

# The GUI window
window = gui.Window("To-Do App",
                    layout=layout,
                    font=('Helvetica', 16))

# Keep the program running until the user exits.
while True:
    event, values = window.read()
    print(values)
    match event:
        # If the Add Button is pressed
        case "Add":
            todos = functions.get_todos()                        # Get the todolist from todos.txt

            if values['todo'] == '':                             # If the Input Box is empty, don't add it to the list
                continue

            todo = values['todo'] + '\n'                         # Get the new to-do from the input box
            todos.append(todo)                                   # Add the new to-do to the to-do list
            functions.write_todos(todos)                         # Update todos.txt
            window['todos'].update(values=todos)                 # Update the listBox on the GUI
            window["todo"].update(value="")                      # Clear the Input Box

        # If the Edit Button is pressed
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]                # Get the to-do that is selected on the list

                if values['todo'] == '':                         # If the Input Box is empty, don't add it to the list
                    continue

                new_todo = values['todo'] + "\n"                 # Get the new to-do from the input box
                todos = functions.get_todos()                    # Get the to-do list from todos.txt
                todos[todos.index(todo_to_edit)] = new_todo      # Edit the to-do item on the list
                functions.write_todos(todos)                     # Update todos.txt
                window['todos'].update(values=todos)             # Update the listBox on the GUI

            # If no item is selected, display a pop-up
            except IndexError:
                gui.popup("Please select an item first",   # Pop-up to remind user to select a to-do
                          font=("Helvetica", 16))

        # If the Complete Button is pressed
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]           # Get the to-do that is selected on the list
                todos = functions.get_todos()                   # Get the to-do list from todos.txt
                todos.remove(todo_to_complete)                  # Remove the selected to-do from the list
                functions.write_todos(todos)                    # Update todos.txt
                window["todos"].update(values=todos)            # Update the listBox on the GUI
                window["todo"].update(value="")                 # Clear the Input Box

            # If no item is selected, display a pop-up
            except IndexError:
                gui.popup("Please select an item first",      # Pop-up to remind user to select a to-do
                          font=("Helvetica", 16))

        # If the Exit Button is pressed, exit the program
        case "Exit":
            break

        # If the Close Modal is pressed, exit the program
        case gui.WINDOW_CLOSED:
            break

window.close()
