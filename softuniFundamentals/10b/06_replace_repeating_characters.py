
# Write a program that reads a string from the console and
# replaces any sequence of the same letters with a single corresponding letter.

the_string = input()

no_duplicates = ""
duplicate_check = ""

for x in the_string:
    if duplicate_check != x:
        no_duplicates += x
        duplicate_check = x

print(no_duplicates)

