
content_array = []

with open("data.txt") as f:
    words = f.read().split()

    for x in words:
        content_array.append(x)

print(content_array)


