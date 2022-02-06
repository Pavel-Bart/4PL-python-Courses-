import math


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def degree(num1, num2):
    return num1**num2


def root(num1, num2):
    return math.sqrt(num1)


print("Please select operation -\n"
      "1. +\n"
      "2. -\n"
      "3. *\n"
      "4. /\n"
      "5. ^\n"
      "6. root\n")

# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4, 5, 6 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))

elif select == 5:
    print(number_1, "^", number_2, "=",
          degree(number_1, number_2))

elif select == 6:
    print("sqrt", number_1, "=",
          root(number_1, number_2))
else:
    print("Invalid input")
