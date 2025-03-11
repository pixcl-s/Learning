
# Write a function that receives two characters and returns a single string with all the characters
# in between them (according to the ASCII code), separated by a single space.
# Print the result on the console.

def searching(input_one, input_two):
    characters = []
    for i in range(ord(input_one) + 1, ord(input_two)):
        characters.append(chr(i))
    return characters


first_symbol = input()
second_symbol = input()

print(*searching(first_symbol, second_symbol))
