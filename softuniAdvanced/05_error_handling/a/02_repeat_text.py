# Write a program that receives a text on the first line and times (to repeat the text) that must be an integer.
# If the user passes a non-integer type for the times variable,
# handle the exception and print a message "Variable times must be an integer".
# input         output
# Hello         Variable times must be an integer
# Bye

text = input()
try:
    amount = int(input())
except ValueError:
    print("Variable times must be an integer")
else:
    print(text * amount)
    