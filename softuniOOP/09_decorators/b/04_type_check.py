# Create a decorator called type_check. It should receive a type (int/float/str/…), and it should check if the parameter
# passed to the decorated function is of the type given to the decorator.
# If it is, execute the function and return the result, otherwise return "Bad Type".

def type_check(types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if isinstance(*args, types):
                result = func(*args, **kwargs)
                return result
            return "Bad Type"
        return wrapper
    return decorator


# test
@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
# output
# 4
# Bad Type
print()
# test
@type_check(str)
def first_letter(word):
    return word[0]
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
# output
# H
# Bad Type
