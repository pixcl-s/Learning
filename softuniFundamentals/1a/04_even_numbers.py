
# Write a program that receives a number n on the first line.
# On the following n lines, it receives different integer numbers.
# If the program receives an odd number, print "{num} is odd!" and end the program.
# Otherwise, if all numbers given are even, print "All numbers are even.".

how_many_numbers = int(input())

for _ in range(how_many_numbers):
    number = int(input())

    if number % 2 == 1:
        print(f"{number} is odd!")
        exit()

print("All numbers are even.")
