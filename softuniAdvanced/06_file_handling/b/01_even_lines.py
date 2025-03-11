# Write a program that reads a text file and prints on the console its even lines.
# Line numbers start from 0.
# Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

replacing = str.maketrans({"-": "@", ",": "@", ".": "@", "!": "@", "?": "@"})

with open("txt_stuff/even_lines.txt") as file:
    lines = file.readlines()

for x in range(0, len(lines), 2):
    symbols_change = lines[x].translate(replacing).strip().split()

    print(" ".join(symbols_change[::-1]))



