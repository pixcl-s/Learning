# Having the following code:
#    def vowel_filter(function):
#       def wrapper():
#           TODO: Implement
#    return wrapper
# Complete the code, so it works as expected:

def vowel_filter(func):
    def wrapper():
        return [x for x in func() if x in "aeoiuy"]
    return wrapper


# test
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())
# output
# ["a", "e"]