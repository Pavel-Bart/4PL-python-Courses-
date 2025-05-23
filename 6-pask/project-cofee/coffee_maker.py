# class CoffeeMaker
# viskas kas susije su kava, reportu ir resursu
# skaiciavimu

from menu import MenuItem


class CoffeeMaker:
    """ Models the machine that makes the coffee """

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """ Prints a report of all resources """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def export(self):
        """ saves a report of all resources to file """
        file = open("resources.txt", mode="w")

        file.write(f"Water: {self.resources['water']}ml\n")
        file.write(f"Milk: {self.resources['milk']}ml\n")
        file.write(f"Coffee: {self.resources['coffee']}g")

        file.close()
        print("Successfully printed to file!")

    def is_resources_sufficient(self, drink: MenuItem):
        """ Return true when order can be made, False if ingredients are sufficient """
        can_make = True

        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}. Please 'refill' the ingredients")
                can_make = False

        return can_make

    def make_coffee(self, order: MenuItem):
        """ Deduct required ingredients from the resources """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        print(f"Here is your {order.name}! Enjoy!")

    def refill_ingredients(self):

        for item in self.resources:
            self.resources[item] += int(input(f"How much {item} to add:"))

