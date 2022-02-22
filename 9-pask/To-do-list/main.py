from todo import ToDo
from inprogress import InProgress

inprogress = InProgress()
todo = ToDo()

is_on = True

while is_on:
    if inprogress.check() is True:
        inprogress.progress_task()
    else:
        options = todo.get_items()
        options = options[:-1]
        choice = input(f"Choose task ({options}): ")

        if choice == "off":
            is_on = False
        else:
            task = todo.find_task(choice)

            todo.start_task(task)

