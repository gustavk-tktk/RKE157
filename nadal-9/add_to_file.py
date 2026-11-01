def add_task_to_file(file_path):

    new_task = "Celebrate birthday."

    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n" + new_task)

add_task_to_file(r"data\todo.txt")