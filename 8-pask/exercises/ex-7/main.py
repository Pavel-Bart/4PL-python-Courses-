line_count = 0

file = open("data.txt", "r")
lines = file.read().split("\n")

for x in lines:
    line_count += 1

print(line_count)

file.close()
