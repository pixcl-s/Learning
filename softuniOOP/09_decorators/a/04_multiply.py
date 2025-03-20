# Having the following code:
#   def multiply(times):
#       def decorator(function):
#           TODO: Implement
#       return decorator
# Complete the code, so it works as expected.

def multiply(digit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * digit
        return wrapper
    return decorator

# test
@multiply(3)
def add_ten(number):
    return number + 10
print(add_ten(3))
# output
# 39
print()
# test
@multiply(5)
def add_ten(number):
    return number + 10
print(add_ten(6))
# output
# 80
