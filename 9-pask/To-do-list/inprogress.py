# inprogress file tasks
import os


class InProgress:

    def __init__(self):
        self.tasks = []

    def check(self):
        """ Checks if file exist. If it's not that means that no task is in progress."""
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

                with open("done.txt", "r") as f:
                    lines = f.read().strip()
                with open("done.txt", "w") as f:
                    f.write(lines)
                    f.write(f"\n{task}")

                is_on = False

            elif choice == "Stop":
                os.remove("inprogress.txt")

                with open("to-do.txt", "r") as f:
                    lines = f.readlines()
                with open("to-do.txt", "w") as f:
                    for line in lines:
                        f.write(line)
                    f.write(task)

                is_on = False
            elif choice == "No":
                is_on = False
            else:
                print("There is no such option")


