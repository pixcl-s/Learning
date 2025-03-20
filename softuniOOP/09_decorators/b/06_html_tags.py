# Create a decorator called tags. It should receive an HTML tag as a parameter,
# wrap the result of a function with the given tag, and return the new result.

def tags(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator


# test
@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
# output
# <p>Hello you!</p>
print()
# test
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
# output
# <h1>HELLO</h1>
