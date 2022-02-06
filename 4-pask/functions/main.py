
def print_something():
    print("hello world")


def print_something_with_args(text):
    print(f"Hello {text}")


print_something()
print_something_with_args("Sky")


def double_number_with_default_value(number =9):
    result = number * number
    return result


print(double_number_with_default_value(10))


very_important_variable = "Hello"


def get_important_variable():
    global very_important_variable # global changes everywhere not only in function
    very_important_variable = "gggg"
    print(very_important_variable)


get_important_variable()
print(very_important_variable)


def more_arguments(make, model, year, color, engine):
    print(f"Make : {make} | Model: {model} | Year: {year} | Color: {color} | Engine: {engine}")


more_arguments("BMW", "5-ER", 2020, "RED", 3.0)
more_arguments(make="BMW", model="5-er", color="red",year=2020, engine=3.0)


def unknown_arguments(*smth): # when we don't know how many arguments do we need
    """Prints arguments"""
    print(type(smth))
    result = 0
    for num in smth:
        result += num
    print(result)


unknown_arguments(5, 10, 15)


def create_car(**kwargs):
    """ Prints """
    print(type(kwargs))
    print(kwargs)

    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


create_car(make="BMW", model="5-er", color="red",year=2020, engine=3.0)


def chain_function(*args):
    def inner_function(values):
        print(values)

    inner_function(args)


chain_function(1, 2, 3, 4, 5)