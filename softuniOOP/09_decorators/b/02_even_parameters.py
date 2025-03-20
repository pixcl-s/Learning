# Create a decorator function called even_parameters. It should check if all parameters passed to a function are
# even numbers and only then execute the function and return the result.
# Otherwise, don't execute the function and return "Please use only even numbers!"

def even_parameters(func):
    def wrapper(*args):
        even_only = [True if isinstance(x, int) and x % 2 == 0 else False for x in args]
        if False not in even_only:
            result = func(*args)
            return result
        return "Please use only even numbers!"
    return wrapper


# test
@even_parameters
def add(a, b):
    return a + b
print(add(2, 4))
print(add("Peter", 1))
# output
# 6
# Please use only even numbers!
print()
# test
@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result
print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
# 384
# Please use only even numbers!
