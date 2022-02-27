from todo import ToDo
from inprogress import InProgress
from menu import Menu


inprogress = InProgress()
todo = ToDo()
menu = Menu()

is_on = True

while is_on:

    options = todo.get_items()
    options = options[:-1]
    choice = input(f"Choose task ({options}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        menu.report()
    elif inprogress.check() is True:
        print("You can't start another task until you finish this one.")
        inprogress.progress_task()
    else:
        task = todo.find_task(choice)

        menu.prepare_task(task)
        inprogress.progress_task()

