def test_range(n):
    if n in range(3, 9):
        print(f"{n} is in the range")
    else:
        print("The number is outside the given range.")


n = int(input("Input a number: "))
test_range(n)