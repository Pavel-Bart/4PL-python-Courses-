# to-do file tasks
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
        print("! No suh task.")


