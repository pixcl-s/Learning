
# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with the corresponding character
# three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

text = list(input())
encrypted_text = ""

for x in text:
    encrypted_text += chr(ord(x) + 3)

print(encrypted_text)
