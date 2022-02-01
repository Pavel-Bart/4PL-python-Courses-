numb = int(input("Enter number: "))
number_list = [1, 5, 8, 3, 9, 65, 78, 12]
contains = False

for num in number_list:
    if num == numb:
        print("True")
        contains = True

if contains is False:
    print("False")