def chain_function(*args):
    def inner_function(values):
        print(values)
    inner_function(args)


chain_function(1, 2, 3, 4, 5)
