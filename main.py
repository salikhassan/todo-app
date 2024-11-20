from modules import functions
import time
import json

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    if user_action.startswith("add"):

        todo = user_action[3:].title().strip() + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}- {item.strip('\n')}")

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[4:].strip()) - 1
            todos = functions.get_todos()

            todos[number] = input("Enter a new todo: ").title() + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):

        try:
            number = int(user_action[8:].strip()) - 1

            todos = functions.get_todos()

            print(f"Todo {todos[number].strip('\n')} has been removed")
            todos.pop(number)

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("exit"):

        break

    else:
        print("Command is not valid.")

print("bye!")
