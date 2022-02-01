my_tuple = ("Apple", "Samsung", "Huawei", "Xiaomi", "Lg", "Asus")
# tuple is read-only array, can't change, difference in tuple syntax is (), when in list is []


# print(type(my_tuple))
# print(my_tuple[1])
# print(my_tuple[1:5])
# print(my_tuple[:4])

# x = list(my_tuple) # how to change read_only tuple->
# x.append("Dell")
# my_tuple = tuple(x)

# print(my_tuple)


colors = (255, 287, 102)

(red, green, blue) = colors

print(f"Red: {red}, Green: {green}, Blue:{blue}")
