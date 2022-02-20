
with open('data1.txt', "r") as file:
    data = file.read()

with open('data2.txt', "w") as file:
    file.write(data)
