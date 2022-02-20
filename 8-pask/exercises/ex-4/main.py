with open("data.txt") as f:
    data = f.readlines()

variable = ""

for line in data:
    variable += line

print(variable)


