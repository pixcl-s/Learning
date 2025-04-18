# Write a program to generate the following matrix of palindromes of 3 letters
# with r rows and c columns like the one in the examples below.
# · Rows define the first and the last letter:
# row 0 -> 'a', row 1 -> 'b', row 2 -> 'c', …
# · Columns + rows define the middle letter:
# o column 0, row 0 -> 'a', column 1, row 0 -> 'b', column 2, row 0 -> 'c', …
# o column 0, row 1 -> 'b', column 1, row 1 -> 'c', column 2, row 1 -> 'd', …
# Input
# · The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
# · r and c are integers in the range [1, 26]
#  input                 output
#   4 6             aaa aba aca ada aea afa
#                   bbb bcb bdb beb bfb bgb
#                   ccc cdc cec cfc cgc chc
#                   ddd ded dfd dgd dhd did

row, col = [int(x) for x in input().split()]

neo = []

for y in range(97, 97 + row):
    neo.append([])
    for z in range(y, y + col):
        neo[-1].append(chr(y)+chr(z)+chr(y))

for o in neo:
    print(*o)

# 100/100
