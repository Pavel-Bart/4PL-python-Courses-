string = input("Enter text or smth: ")

if string[0:2] != "Is":
    string = "Is" + string

print(string)
