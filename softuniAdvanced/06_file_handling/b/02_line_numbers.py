# Write a program that reads a text file, inserts line numbers in front of each line,
# and counts all the letters and punctuation marks. The result should be written in another text file.
# text.txt                                              output.txt
# -I was quick to judge him, but itwasn't his fault.    Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
# -Is this some kind of joke?! Isit?                    Line 2: -Is this some kind of joke?! Is it? (24)(4)
# -Quick, hide here. It is safer.                       Line 3: -Quick, hide here. It is safer. (22)(4)

with open("txt_stuff/to_count.txt") as file:
    stuff = file.readlines()

for x in range(len(stuff)):
    letter_count = 0
    punctuation = 0

    for y in stuff[x].replace(" ", "").strip():
        if y.isalpha():
            letter_count += 1
        elif not y.isalpha():
            punctuation += 1

    with open("txt_stuff/counted.txt", "a") as file:
        file.write(f"Line {x+1}: {stuff[x].strip()} ({letter_count})({punctuation})\n")
