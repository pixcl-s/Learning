
# First, you will be given two sequences of integer values on different lines.
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the following N lines, you will receive one of the following commands:
# "Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# "Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# "Check Subset" - check if any of the given sequences are a subset of the other.
# If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences,
# separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.
# input                                      output
# 1 2 3 4 5                                 True
# 1 2 3                                     1, 2, 3, 4, 5, 6
# 3                                         1, 2, 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset

from collections import deque

first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    commands = deque(input().split())
    first_part = commands.popleft()

    if first_part == "Add":
        if commands.popleft() == "First":
            while commands:
                first_sequence.add(int(commands.popleft()))
        else:
            while commands:
                second_sequence.add(int(commands.popleft()))

    elif first_part == "Remove":
        if commands.popleft() == "First":
            while commands:
                first_sequence.discard(int(commands.popleft()))
        else:
            while commands:
                second_sequence.discard(int(commands.popleft()))

    else:
        if first_sequence <= second_sequence or second_sequence <= first_sequence:
            print(True)
        else:
            print(False)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")

# 100/100