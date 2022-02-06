import random

from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["City", "Area", "Population"]
x.add_row(["Sydney", 2058, 43568])
x.add_row(["Brisbane", 5905, 548548])

print(x)

german_cars = ["BMW", "Audi", "MB"]
print(random.randint(0, 100))
print(random.randrange(10, 100, 5)) # from 10 to 100, kas 5

print(random.choice(german_cars))
random.shuffle(german_cars) # change positions in german_cars
print(german_cars)
german_cars.sort()
print(german_cars)


