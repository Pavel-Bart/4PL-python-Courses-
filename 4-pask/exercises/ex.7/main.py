def calculate_upper_lower(str):
    upper = 0
    lower = 0
    for x in str:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
    print("No. of Upper case characters : ", upper)
    print("No. of Lower case characters : ", lower)


calculate_upper_lower("The quick Brow Fox")
