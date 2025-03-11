# Write a program that draws the figure below depending on n.
# input     output
# 2         **
#           *
#           #
#           ##

def draw(how_much):
    if how_much == 0:
        return
    print("*"*how_much)

    draw(how_much-1)

    print("#"*how_much)


amount = int(input())
draw(amount)

# 100/100
