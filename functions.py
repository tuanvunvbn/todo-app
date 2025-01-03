FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the
    list of to-do items"""
    with open(filepath, "r", encoding="UTF-8") as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do item list  in the text file """
    with open(filepath, "w", encoding="UTF-8") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())