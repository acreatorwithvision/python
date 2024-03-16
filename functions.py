def get_todos(filepath="todos.txt"):
    """ Read a text file and return a list
    of todos items.
    """

    with open(filepath,'r') as file_local:
        todos_local=file_local.readlines()
    return todos_local

print(help(get_todos))


def write_todos(todos_arg, filepath = "todos.txt"):
    """Write the todos item list in the text file."""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
