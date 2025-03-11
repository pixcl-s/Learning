
# You will be given strings until you receive the command "End".
# For each string given, you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!

while True:
    word = input()

    if word == "End":
        break
    elif word == "SoftUni":
        continue

    for character in word:
        print(character * 2, end="")

    print("")
