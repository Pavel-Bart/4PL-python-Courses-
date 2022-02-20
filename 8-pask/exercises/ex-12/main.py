import string

for x in string.ascii_uppercase:
    with open(f"./files/{x}.txt", mode="w") as f:
       f.writelines(x)

