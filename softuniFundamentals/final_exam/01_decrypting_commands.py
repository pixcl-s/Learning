# On the first line, you are going to receive a string.
# You will receive "decrypting" commands on the following lines until you get the "Finish" command.
# There are five possible commands:
# ⦁	"Replace {currentChar} {newChar}"
# ⦁	Replace all occurrences of the current char with the new char, then print the resulting message.
# ⦁	"Cut {startIndex} {endIndex}"
# ⦁	Remove the substring from the start index until the end index (both inclusive), then print the resulting message.
# ⦁	If any of the indexes is not valid, print:  "Invalid indices!".
# ⦁	"Make {Upper/Lower}"
# ⦁	Replace all letters with upper/lower case and print the resulting message.
# ⦁	"Check {string}"
# ⦁	If the message contains the given string, print: "Message contains {string}".
# ⦁	Otherwise, print: "Message doesn't contain {string}".
# ⦁	"Sum {startIndex} {endIndex}"
# ⦁	Get the substring from the start index to the end index (both inclusive)
# and print the sum of the ASCII values of the substring.
# ⦁	If any of the given indices are invalid, print:
# "Invalid indices!".
# An index is valid when it is non-negative and less than the size of the collection.
# Note: At any time, the message will contain at least one character.
# ⦁	Input
# ⦁	On the first line, you are going to receive the string.
# ⦁	On the following lines, until the "Finish" command is received, you will be receiving commands.
# ⦁	Output
# ⦁	Print the output of every command in the format described above.
# ⦁	Constraints
# ⦁	The indexes will be integers in the range [-50…150].

message = input()

while True:
    commands = input().split()
    if commands[0] == "Finish":
        break

    if commands[0] == "Replace":
        old_char, new_char = commands[1], commands[2]
        message = message.replace(old_char, new_char)
        print(message)
    elif commands[0] == "Cut":
        start, end = int(commands[1]), int(commands[2])
        if len(message) > start >= 0 and len(message) > end >= 0:
            message = message.replace(message[start:end+1], "")
            print(message)
        else:
            print("Invalid indices!")
    elif commands[0] == "Make":
        if commands[1] == "Upper":
            message = message.upper()
            print(message)
        elif commands[1] == "Lower":
            message = message.lower()
            print(message)
    elif commands[0] == "Check":
        if commands[1] in message:
            print(f"Message contains {commands[1]}")
        else:
            print(f"Message doesn't contain {commands[1]}")
    elif commands[0] == "Sum":
        start, end = int(commands[1]), int(commands[2])
        if len(message) > start >= 0 and len(message) > end >= 0:
            submessage = message[start:end+1]
            summ = 0
            for x in submessage:
                summ += ord(x)
            print(summ)
        else:
            print("Invalid indices!")

