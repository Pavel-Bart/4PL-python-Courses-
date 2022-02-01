# list = array
german_cars = ["bmw", "audi", "porshe", "Vs"]
japan_cars = ["toyota", "nissan", "mazda", "lexus"]

# print(type(german_cars))
# print(len(german_cars))
# print(german_cars[1])
# print(german_cars[len(german_cars) -1])
# print(german_cars[-1]) # start from the end -1 = last index
# print(german_cars[-2])

german_cars.append("opel") # prideda i paskutine vieta
german_cars.insert(1, "Smth")
german_cars.extend(japan_cars)

print(german_cars)

german_cars.remove("toyota") # remove by text
german_cars.pop(1) # remove by index
german_cars.pop()

del german_cars[0]
# del japan_cars
# print(japan_cars)

print(german_cars)

