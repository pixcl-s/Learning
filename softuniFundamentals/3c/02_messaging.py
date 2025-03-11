
# On the first line, you will receive a sequence of numbers separated by a single space.
# On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string.
# Each char the program adds to the message should be found by its index.
# The index you are looking for is the sum of a number's digits from the first sequence.
# If the index is greater than the length of the text, continue counting from the beginning
# (so that you always have a valid index).
# When you find a char, you should add it to the message and remove it from the string.
# It means that for the following index, the text will contain one character less.
# Print the final message.

key = input().split(" ")
sentence = list(input())

final_message = ""

for number in key:
    index = 0
    for i in number:
        index += int(i)

    if index >= len(sentence):
        index -= len(sentence)

    final_message += sentence[index]
    sentence.pop(index)

print(final_message)
