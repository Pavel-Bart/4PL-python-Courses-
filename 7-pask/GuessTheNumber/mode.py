
class ModeItem:
    """ Models each Mode Item """

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives


class Mode:
    """  """

    def __init__(self):
        self.mode = [
            ModeItem(name="easy", lives=9),
            ModeItem(name="normal", lives=6),
            ModeItem(name="hard", lives=3),
    ]

    def get_items(self):

        options = ""
        for item in self.mode:
            options += f"{item.name}/"
        return options

    def find_level(self, level_name):
        """ Searches the mode for a particular level by name. Returns that item if exists, otherwise return None """
        for item in self.mode:
            if item.name == level_name:
                return item

        print("Sorry that item is not available..")
