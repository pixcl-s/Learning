
# Write a program that receives a single string.
# On the first line, print all the digits found in the string,
# on the second – all the letters,
# and on the third – all the other characters.
# There will always be at least one digit, one letter, and one other character.

gibberish = input()

numbers = ""
letters = ""
others = ""

for character in gibberish:
    if character.isdigit():
        numbers += character
    elif character.isalpha():
        letters += character
    else:
        others += character

print(numbers)
print(letters)
print(others)
