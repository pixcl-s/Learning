
# Write a program that receives a list of characters separated by ", ".
# It should create a dictionary with each character as a key and its ASCII value as a value.
# Try solving that problem using comprehension.

characters = input().split(", ")

character_ascii = {x:ord(x) for x in characters}

print(character_ascii)