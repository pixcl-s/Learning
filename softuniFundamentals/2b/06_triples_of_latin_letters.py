
# Write a program to read an integer N and
# print all triples of the first N small Latin letters, ordered alphabetically:

how_many = int(input())

for a in range(97, 97 + how_many, + 1):
    for b in range(97, 97 + how_many, + 1):
        for c in range(97, 97 + how_many, + 1):
            print(f"{chr(a)}{chr(b)}{chr(c)}")
