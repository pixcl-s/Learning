
# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive one of the following:
# Opening bracket – "(",
# Closing bracket – ")" or
# Random string
# Your task is to find out if the brackets are balanced.
# That means after every opening bracket should follow a closing one.
# Nested parentheses are not valid, and if, for example,
# two consecutive opening brackets exist, the expression should be marked as unbalanced.
# You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.

how_many = int(input())

brackets = ""
counter = 0

for _ in range(how_many):
    string_input = input()
    if string_input == "(" or string_input == ")":
        brackets += string_input

for character in brackets:
    if character == "(":
        counter += 1
    if character == ")":
        counter -= 1
    if counter == -1:
        break
    if counter == 2:
        break

if counter == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
