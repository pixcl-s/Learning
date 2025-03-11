# Create a program that will receive commands until the command "End". The commands can be:
# · "Create-{file_name}" - Creates the given file with empty content.
# If the file already exists, remove the existing text in it (as if the file is created again)
# · "Add-{file_name}-{content}" - Append the content and a new line after it.
# If the file does not exist, create it, and add the content
# · "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string
# with the new string. If the file does not exist, print: "An error occurred"
# · "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
# input
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End
import os

while True:
    commanding = input().split("-")
    if commanding[0] == "End":
        break

    command, file = commanding[:2]

    if command == "Create":
        with open(f"txt_stuff/{file}", "w") as file:
            pass
        continue
    elif command == "Delete":
        try:
            os.remove(f"txt_stuff/{file}")
        except FileNotFoundError:
            print("An error occurred!")
        finally:
            continue

    content = commanding[2]

    if command == "Add":
        with open(f"txt_stuff/{file}", "a") as file:
            file.write(f"{content}\n")
        continue

    a=1
    old, new = commanding[2:]

    if command == "Replace":
        try:
            with open(f"txt_stuff/{file}", "r") as file:
                stuff = file.readlines()
                for x in range(len(stuff)):
                    stuff[x] = stuff[x].replace(old, new)
        except FileNotFoundError:
            print("An error occurred!")
            continue

        with open(f"txt_stuff/{file}", "w") as f:
            f.writelines(stuff)
                # OSError: [Errno 22 Invalid argument: "txt_stuff/<_io.TextIOWrapper name='txt_stuff/file.txt' mode='r' encoding='cp1252'>"
