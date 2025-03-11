
# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows:
# multiply str1[0] with str2[0] and add the result to the total sum,
# then continue with the next two characters.
# If one of the strings is longer than the other,
# add the remaining character codes to the total sum without multiplication.

first_sequence, second_sequence = input().split()

total_sum = 0

if len(first_sequence) == len(second_sequence):
    for x in range(len(first_sequence)):
        one = ord(first_sequence[x])
        two = ord(second_sequence[x])

        total_sum += one * two
else:
    leftover = ""
    shorter = ""
    if len(first_sequence) > len(second_sequence):
        leftover = first_sequence[len(second_sequence)::]
        shorter = second_sequence

    elif len(first_sequence) < len(second_sequence):
        leftover = second_sequence[len(first_sequence)::]
        shorter = first_sequence

    for x in range(len(shorter)):
        one = ord(first_sequence[x])
        two = ord(second_sequence[x])
        total_sum += one * two

    for z in leftover:
        total_sum += ord(z)

print(total_sum)

