
# Using a list comprehension, write a program that receives numbers,
# separated by comma and space ", ", and prints all the positive,
# negative, even, and odd numbers on separate lines as shown below.

def unlist(lista):
    return ", ".join(str(o) for o in lista)


initial_numbers = [int(num) for num in input().split(", ")]

positive = [x for x in initial_numbers if x >= 0]
negative = [y for y in initial_numbers if y < 0]
even = [z for z in initial_numbers if z % 2 == 0]
odd = [w for w in initial_numbers if w % 2 != 0]


print(f"Positive: {unlist(positive)}")
print(f"Negative: {unlist(negative)}")
print(f"Even: {unlist(even)}")
print(f"Odd: {unlist(odd)}")
