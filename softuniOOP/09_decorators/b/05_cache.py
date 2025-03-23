# Create a decorator called cache. It should store all the returned values of the recursive function fibonacci.
# You are provided with this code:
#
#   def cache(func):
#       TODO: Implement
#
#   @cache
#   def fibonacci(n):
#       if n < 2:
#           return n
#       else:
#           return fibonacci(n-1) + fibonacci(n-2)
#
# You need to create a dictionary called log that will store all the n's (keys) and
# the returned results (values) and attach that dictionary to the fibonacci function as a variable called log,
# so when you call it, it returns that dictionary.


def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):
            wrapper.log[num] = func(num)
        return wrapper.log[num]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# test
print(fibonacci(3))
print(fibonacci.log)
# output
# {1: 1, 0: 0, 2: 1, 3: 2}
print()
# test
fibonacci(4)
print(fibonacci.log)
# output
# {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
