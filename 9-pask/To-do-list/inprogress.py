import os


class InProgress:

    def __init__(self):
        self.tasks = []

    def check(self):
        """ Checks if file exist. If it's not tha mean that no task is in progress."""
        if os.path.exists("inprogress.txt"):
            return True
        else:
            return False

    def progress_task(self):
        """ Starts .while. you cant start another tasks until you finish this one"""
        f = open("inprogress.txt", "r")
        task = f.read()
        f.close()

        is_on = True

        while is_on:
            choice = input(f"Task {task} is in progress. Finish it(Yes/No/Stop)?")

            if choice == "Yes":
                os.remove("inprogress.txt")

                is_on = False

            elif choice == "Stop":
                os.remove("inprogress.txt")
                with open("to-do.txt", "a") as f:
                    f.write(task)
                is_on = False
            elif choice == "No":
                pass
            else:
                pass


