
# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.

year = int(input())

while True:
    split = str(year)

    if len(set(split)) == len(split):
        print(year)
        break

    year += 1
