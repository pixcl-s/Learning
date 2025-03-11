
# On the first line, you will receive a key (integer).
# On the second line, you will receive n – the number of lines, which will follow.
# On the next n lines – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message.
# In the end, print the decrypted message.

key = int(input())

how_many = int(input())

message = ""

for _ in range(how_many):
    letter = input()
    message += chr(ord(letter) + key)

print(message)
