
# You will receive a single input line containing strings, separated by spaces.
# The strings may contain any ASCII character except whitespace.
# Then you will begin receiving commands in one of the following formats:
# merge {startIndex} {endIndex}
# divide {index} {partitions}
# Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex.
# In other words, you should concatenate them.
# Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
# If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
# Every time you receive the divide command, you must divide the element at the given index
# into several small substrings with equal length.
# The count of the substrings should be equal to the given partitions.
# Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
# If the string cannot be exactly divided into the given partitions,
# make all partitions except the last with equal lengths and make the last one - the longest.
# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
# The input ends when you receive the command "3:1".
# At that point, you must print the resulting elements, joined by a space.
# Input
# The first input line will contain the array of data.
# On the next several input lines, you will receive commands in the format specified above.
# The input ends when you receive the command "3:1".
# Output
# As output, you must print a single line containing the elements of the array, joined by a space.
# Constraints
# The strings in the array may contain any ASCII character except whitespace.
# The startIndex and the endIndex will be in the range [-1000…1000].
# The endIndex will always be greater than the startIndex.
# The index in the divide command will always be inside the array.
# The partitions will be in the range [0…100].
# Allowed working time/memory: 100ms / 16MB.

stuff = input().split()

while True:
    commands = input()

    if commands == "3:1":
        break

    operation, index_one, index_two = commands.split()
    index_one, index_two = int(index_one), int(index_two)

    if operation == "merge":
        if index_one < 0:
            index_one = 0
        if index_two >= len(stuff):
            index_two = len(stuff) - 1
        for x in range(index_one, index_two):
            stuff[index_one] += stuff[index_one + 1]
            stuff.pop(index_one + 1)

    elif operation == "divide":
        a_string = stuff[index_one]
        divided = []
        if len(a_string) % index_two == 0:
            separation = len(a_string) // index_two
            while len(a_string) > 0:
                divided.append(a_string[0:separation])
                a_string = a_string.replace(a_string[0:separation], "")
        else:
            separation = len(a_string) // index_two
            for _ in range(len(a_string) % index_two):
                divided.append(a_string[0:separation])
                a_string = a_string.replace(a_string[0:separation], "")
            divided.append(a_string)
        stuff.pop(index_one)
        stuff[index_one:index_one] = divided

print(" ".join(stuff))


# print(10 // 5)
# print(10 / 5)
# print(10 % 5)

# list = "abcd efgh ijkl mnop qrstuvwxyz".split()
# list2 = "qr st uv wx yz".split()
#
# list.pop(4)
# list[1:2] = list2
# print(list)
# print(list2)