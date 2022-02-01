string = input("Enter text: ")

for x in string:
    bool = x.islower()
    if bool:
        print("True")
        break
