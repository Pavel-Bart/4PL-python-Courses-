from random import randint
from mode import Mode
from number import Number

number = Number()
mode = Mode()

is_on = True

while is_on:
    options = mode.get_items()
    options = options[:-1]
    choice = input(f"Choose level ({options}): ")

    if choice == "off":
        is_on = False
    else:
        level = mode.find_level(choice)

        if level is None:
            print()
        else:
            number.start_game(level)

