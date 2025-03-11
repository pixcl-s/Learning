
# Using comprehension, write a program that receives some text,
# separated by space, and takes only those words whose length is even.
# Print each word on a new line.

words = input().split()

even_words = [x for x in words if len(x) % 2 == 0]

print("\n".join(even_words))