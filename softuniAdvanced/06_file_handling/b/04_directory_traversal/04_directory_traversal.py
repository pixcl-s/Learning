# Write a program that traverses a given directory for all files.
# Search through to the first nested level of the directory (inclusive) and write information about each file you find
# into the report.txt file. The files should be grouped by their extension.
# Extensions should be ordered by name alphabetically.
# The files with extensions should also be sorted by name.
# The report.txt file should be saved in the chosen directory.

import os


def writing(stuff):
    with open("./report.txt", "w") as f:
        for key, value in sorted(stuff.items(), key=lambda a: (a, a)):
            f.write(f".{key}\n")
            for z in value:
                f.write(f"- - - {z}.{key}\n")


def finding_files(the_folder, files=[], how_deep=0):
    looking_in = os.listdir(the_folder)
    if how_deep > 1:
        return

    for x in looking_in:
        file = os.path.join(the_folder, x)
        if os.path.isfile(file):
            files.append(x)
        elif os.path.isdir(file):
            finding_files(file, files, how_deep+1)

    return files


folder = os.path.abspath(input())

found_files = finding_files(folder)

extensions = {}

for y in found_files:
    name, extension = y.split(".")
    if extension not in extensions:
        extensions[extension] = []
    extensions[extension].append(name)

if extensions:
    writing(extensions)
