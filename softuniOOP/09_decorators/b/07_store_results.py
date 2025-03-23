# Create a class called store_results.
# It should be used as a decorator and store information about the executed functions in a file called results.txt
# in the format: "Function {func_name} was called. Result: {func_result}"


class store_results:
    def __init__(self, file_name):
        self.file_name = file_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with open(self.file_name, "a") as file:
                file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")
                print(func(*args, **kwargs))
        return wrapper


# test
@store_results("07_store_results.txt")
def add(a, b):
  return a + b

@store_results("07_store_results.txt")
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
# output
# Function 'add' was called. Result: 4
# Function 'mult' was called. Result: 24
