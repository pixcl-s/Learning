# You are in the library, looking for words to write down in your notebook.
# Your first task is to store every word with its definition.
# You will receive all the words and definitions, separated by " | ",
# and each word and its definition will be separated by ": ".
# Note: you could receive the same word more than once with different definitions -
# you need to store all of them in your notebook.
# Next, you will receive only words, again separated by " | ".
# These are the words that your teacher will test you on.
# In the end, you will receive one command, which will be either "Test" or "Hand Over":
# ⦁	If the command is "Test", you should find each word that your teacher will test you on
# (if it exists in your notebook) and print all its definitions in the following format:
# "{word}:"
# " -{definition1}"
# " -{definition2}"
# …
# " -{definitionN}"
# ⦁	If the command is "Hand Over", you should print only the words that are in your notebook,
# without the definitions, separated by a space (" ").
# Input
# ⦁	On the first line, you will receive pairs of words and their definition,
# separated by " | ". Within each pair, the word is separated from the definition with ": ".
# ⦁	On the second line, you will receive only words, separated by " | ".
# ⦁	On the third line, you will receive a command - either "Test" or "Hand Over".
# Output
# ⦁	Print the appropriate message after the "Test" or "Hand Over" command.

# care: worry, anxiety, or concern | care: a state of mind in which one is troubled | face: the front part of the head, from the forehead to the chin
# care | kitchen | flower
# Test
# care:
#  -worry, anxiety, or concern
#  -a state of mind in which one is troubled

definitions = input().split(" | ")
teacher_test = input().split(" | ")
command = input().lower()

each_word = {}

for words in definitions:
    word, definition = words.split(": ")
    if word not in each_word:
        each_word[word] = []
    each_word[word].append(definition)

if command == "hand over":
    for keys in each_word:
        print(keys, end=" ")
elif command == "test":
    for test in teacher_test:
        if test in each_word:
            print(f"{test}:")
            for x in each_word[test]:
                print(f"-{x}")
