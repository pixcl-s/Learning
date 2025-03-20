# Having the following code:
#   def even_numbers(function):
#     def wrapper(numbers):
#       TODO: Implement
#   return wrapper
# Complete the code, so it works as expected.

def even_numbers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return [x for x in result if x % 2 == 0]
    return wrapper


# test
@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
# output
# [2, 4]
