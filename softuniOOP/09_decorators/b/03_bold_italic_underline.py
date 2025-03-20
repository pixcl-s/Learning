# Create three decorators: make_bold, make_italic, and make_underline, which will have to wrap a text returned from
# a function in <b></b>, <i></i> and <u></u> respectively.

def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<u>{result}</u>"
    return wrapper


# test
@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"
print(greet("Peter"))
# output
# <b><i><u>Hello, Peter</u></i></b>
print()
# test
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"
print(greet_all("Peter", "George"))
# output
# <b><i><u>Hello, Peter, George</u></i></b>
