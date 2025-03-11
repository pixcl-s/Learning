
# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
# Print the new text string after removing the vowels.
# The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

vowels = ["a", "o", "u", "e", "i"]

word = input()

word_vowel = [x for x in word if x.lower() not in vowels]

print("".join(word_vowel))
