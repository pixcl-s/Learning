
# You are given a secret message you should decipher. To do that, you need to know that in each word:
# the second and the last letter are switched (e.g., Holle means Hello)
# the first letter is replaced by its character code (e.g., 72 means H)

code = input().split()
deciphered = []
for x in code:
    numbers = ""
    letters = ""
    for y in x:
        if y.isnumeric():
            numbers += y
        else:
            letters += y
    lettering = list(letters)
    lettering[0], lettering[-1] = lettering[-1], lettering[0]
    back_to_letters = "".join(lettering)
    back_to = "".join(chr(int(numbers)))
    back_back = back_to + back_to_letters
    deciphered.append(back_back)


print(" ".join(deciphered))

