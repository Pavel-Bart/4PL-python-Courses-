color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open('data.txt', "w") as file:
    for x in color:
        file.write(f"{x}\n")


content = open('data.txt')
print(content.read())
