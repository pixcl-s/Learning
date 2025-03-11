# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.
# Submit only your function in the judge system.
# test                                          output
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))     [2, 4, 6]

def even_odd(*args):

    def even_filter():
        return [int(x) for x in args[:-1] if x % 2 == 0]

    def odd_filter():
        return [int(x) for x in args[:-1] if x % 2 != 0]

    filterage = {
        "even": even_filter,
        "odd": odd_filter
    }

    return filterage[args[-1]]()

print(even_odd(1, 2, 3, 4, 5, 6, "even"))

# 100/100
