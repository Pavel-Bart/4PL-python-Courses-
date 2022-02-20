with open("data.txt", mode="a") as file:
    file.write("Ex-2 write line.\n")

f = open("data.txt", "r")
print(f.read())
