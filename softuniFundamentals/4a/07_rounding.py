
# Write a program that rounds all the given numbers,
# separated by a single space, and prints the result as a list. Use round().

def rounding(num):
    return round(num)


number = [float(digit) for digit in input().split()]
correct_list = []


for i in number:
    hm = (rounding(i))
    correct_list.append(hm)

print(correct_list)
