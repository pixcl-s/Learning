# Write a program that reads a list of words from the file words.txt
# and finds how many times each of the words is contained in another file text.txt.
# Matching should be case-insensitive.
# The results should be written into other text files.
# Sort the words by frequency in descending order.
# words.txt             input.txt                                               output.txt
# quick is fault        -I was quick to judge him, but it wasn't his fault.     is - 3
#                      -Is this some kind of joke?! Is it?                      quick - 2
#                     -Quick, hide here…It is safer.                            fault - 1

import re

with open("txt_files/words.txt", "w") as file:
    file.write(input("word to count:"))

with open("txt_files/input.txt", "w") as file:
    file.write(input("text for counting:"))

file_words = open("txt_files/words.txt")
file_to_look = open("txt_files/input.txt")

words = file_words.read().split()
look_into = file_to_look.read()

counting = {}

for x in words:
    huh = re.findall(fr"(?i)\b{x}\b", look_into)
    counting[x] = len(huh)

with open("txt_files/output.txt", "w") as file:
    for key, value in sorted(counting.items(), key=lambda z: -z[1]):
        file.write(f"{key} - {value}\n")

# -I was quick to judge him, but it wasn't his fault. -Is this some kind of joke?! Is it? -Quick, hide here…It is safer.
