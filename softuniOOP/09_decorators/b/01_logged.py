# Create a decorator called logged. It should return the name of the function that is being called and its parameters.
# It should also return the result of the execution of the function being called.

def logged(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"you called {function.__name__}{args}\nit returned {result}"
    return wrapper


# test
@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
# output
# you called func(4, 4, 4)
# it returned 6
print()
# test
@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
# output
# you called sum_func(1, 4)
# it returned 5
