# class MenuItem vienas gerimas
# class Menu gerimu array, viskas kas susije su menu.

class MenuItem:
    """ Models each Menu Item """

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """ Models the Menu with drinks """

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=150, coffee=24, cost=2.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
    ]

    def get_items(self):

        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """ Searches the menu for a particular drink by name. Returns that item if exists, otherwise return None """
        for item in self.menu:
            if item.name == order_name:
                return item

        print("Sorry that item is not available..")
