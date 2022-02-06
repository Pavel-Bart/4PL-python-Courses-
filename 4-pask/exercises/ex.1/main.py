def find_max(arg1, arg2, arg3):
    if arg1 > arg2 and arg1 > arg3:
        return arg1
    if arg2 > arg1 and arg2 > arg3:
        return arg2
    if arg3 > arg1 and arg3 > arg2:
        return arg3


print(find_max(3, 4, 5))