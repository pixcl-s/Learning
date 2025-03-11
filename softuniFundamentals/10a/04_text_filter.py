
# Write a program that receives a text and a string of banned words, separated by a comma and space ", ".
# All banned words in the text should be replaced with the number of asterisks "*", equal to the word's length.
# The ban list will be entered on the first input line and the text - on the second input line.

banned_words = input().split(", ")
words_to_ban = input()

for x in banned_words:
    if x in words_to_ban:
        words_to_ban = words_to_ban.replace(x, "*" * len(x))

print(words_to_ban)
