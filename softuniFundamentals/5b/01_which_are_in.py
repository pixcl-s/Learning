
# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.

random_words = input().split(", ")
other_random_words = input().split(", ")

words_to_print = [x for x in random_words for y in other_random_words if x in y]

print(list(dict.fromkeys(words_to_print)))

