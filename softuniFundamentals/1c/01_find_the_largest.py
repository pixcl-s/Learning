
# You will be given a number. Print the largest number that can be formed from the digits of the given number.

# Input	Output
# 213	321
# 7389	9873

number = list(input())

number = [int(i) for i in number]

number.sort(reverse=True)

print(*number, sep="")

