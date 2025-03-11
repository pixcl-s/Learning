
# On the first line, you will receive a number n.
# On the second line, you will receive a word.
# On the following n lines, you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

some_list = []
some_list_filtered = []

how_many = int(input())

word = input()

for _ in range(how_many):
    phrase = input()
    some_list.append(phrase)

    if word in phrase:
        some_list_filtered.append(phrase)

print(some_list)
print(some_list_filtered)
