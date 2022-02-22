
class ToDoItem:
    """ Models each ToDo Item """

    def __init__(self, name):
        self.name = name


class ToDo:

    def __init__(self):
        self.tasks = []

    def read_items(self):
        with open("to-do.txt") as file:
            self.tasks = file.readlines()
        self.tasks = [x.strip() for x in self.tasks]

    def get_items(self):
        self.read_items()
        options = ""
        for item in self.tasks:
            options += f"{item}/"
        return options

    def find_task(self, task):
        """ Searches the tasks for a particular task by name. Returns that item if exists, otherwise return None """
        for item in self.tasks:
            if item == task:
                return item

    def start_task(self, task):
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


