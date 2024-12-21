FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH) -> list:
    """
    Read a text file and return the list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """
    Opens a file and writes the to-do items on the file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)

