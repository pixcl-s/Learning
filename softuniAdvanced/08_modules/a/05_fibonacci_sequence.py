# Create a module that can create a Fibonacci sequence up to a number (count of numbers in the sequence)
# and print them, separating them with a single space.
# The module should also be able to locate a specific number in the sequence.
# You will be receiving commands until the "Stop" command. The commands are:
# · "Create Sequence {count}".
# Create a series of numbers up to a specific count and print them in the following format: "{n1} {n2} … {n}"
# · "Locate {number}" Check if the sequence contains the number.
# If it finds the number, it should print:
# "The number - {number} is at index {index}"
# And if it doesn't find it:
# "The number {number} is not in the sequence"
# Input
# · You will be receiving commands until the "Stop" command. All inputs will be valid.
# Output
# · Print the output of every command in the format described above.
# input                     output
# Create Sequence 10        0 1 1 2 3 5 8 13 21 34
# Locate 13                 The number - 13 is at index 7
# Create Sequence 3         0 1 1
# Locate 10                 The number 10 is not in the sequence
# Stop

from my_modules import fibonacci

while True:
    command = input().lower().split()
    do = command[0]
    if do == "stop":
        break

    number = int(command[-1])

    if do == "create":
        sequence = fibonacci.create(number)
    elif do == "locate":
        fibonacci.locate(sequence, number)
