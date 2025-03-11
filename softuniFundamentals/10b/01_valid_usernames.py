
# Write a program that reads usernames on a single line (separated by ", ")
# and prints all valid usernames on separate lines.
# A valid username:
# has length between 3 and 16 characters inclusive
# can contain only letters, numbers, hyphens, and underscores
# has no redundant symbols before, after, or in between

usernames_to_check = input().split(", ")
valid_usernames = []

for x in usernames_to_check:
    valid_or_not = 0
    if 3 <= len(x) <= 16:
        valid_or_not += 1
    for y in x:
        if not (y.isdigit() or y.isalpha() or y == "-" or y == "_"):
            valid_or_not -= 1
            break
    valid_or_not += 1
    if " " not in x:
        valid_or_not += 1

    if valid_or_not == 3:
        valid_usernames.append(x)

print("\n".join(valid_usernames))
