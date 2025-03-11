import re

sentence = input()
word_to_look_for = input()

pattern = fr"(?i)\b{word_to_look_for}\b"

amount = re.findall(pattern, sentence)

print(len(amount))
