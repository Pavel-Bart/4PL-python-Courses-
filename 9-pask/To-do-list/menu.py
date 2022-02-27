# cross-file tasks
import os
from pprint import pprint


class Menu:

    def __init__(self):
        self.tasks = []

    def prepare_task(self, task):
        """ Adds task to inprogress file and deletes it from ToDo file"""

        f = open("inprogress.txt", "w")
        f.write(task)
        f.close()

        with open("to-do.txt", "r") as f:
            lines = f.readlines()
        with open("to-do.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != task:
                    f.write(line)

    def report(self):
        print("--To Do left:")
        if os.path.exists("to-do.txt"):
            with open("to-do.txt", "r") as f:
                content = f.read().strip()
                print(content)

        print("--In progress:")
        if os.path.exists("inprogress.txt"):
            with open("inprogress.txt", "r") as f:
                content = f.read().strip()
                print(content)

        print("--Done:")
        if os.path.exists("done.txt"):
            with open("done.txt", "r") as f:
                content = f.read().strip()
                print(content)

