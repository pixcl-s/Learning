
# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

text = list(input())

for x in range(len(text)):
    if text[x] == ":":
        print(text[x] + text[x+1])
