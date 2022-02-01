numbers = [1, 9, 98, 32, 2, 8, 19, 20, 21, 90, 16]
n = len(numbers)-1

for i in range(n):

    for j in range(n):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
