# Create a generator function called reverse_text that receives a string and yields all string characters on one line in reversed order.

def reverse_text(word: str):
    huh = list(word)
    while huh:
        yield huh.pop()


# test
for char in reverse_text("step"):
    print(char, end='')
# output
# pets
