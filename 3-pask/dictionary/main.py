from pprint import pprint # pretty-print
my_mustang = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1969,
    "good_condition": True,
}

my_mercedes = {
    "brand": "Mercedes",
    "model": "S",
    "year": 1969,
    "good_condition": True,
}
print(type(my_mustang))
print(my_mustang)
# pprint(my_mustang)
print(my_mustang["brand"])
print(my_mustang.get("model"))
print(my_mustang.keys())
print(my_mustang.values())

my_mustang["year"] = 2020
my_mustang.update({"year": 1999, "good_condition": False})
# my_mustang["other_cars"] = [my_mercedes, my_mercedes]
pprint(my_mustang)
print()
cars = [my_mustang, my_mercedes]
for item in cars:
    print(item.keys())

