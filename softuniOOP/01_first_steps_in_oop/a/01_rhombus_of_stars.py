# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n
# output        input
#    *          4
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *

def top_part(digit):
    for x in range(1, digit+1):
        print(f"{' '*(digit-x)}{'* '*x}")


def bottom_part(digit):
    for x in range(digit-1, 0, -1):
        print(f"{' '*(digit-x)}{'* '*x}")


def rhombus(largeness):
    top_part(largeness)
    bottom_part(largeness)


size = int(input())
rhombus(size)