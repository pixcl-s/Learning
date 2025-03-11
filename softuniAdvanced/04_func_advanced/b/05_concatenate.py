# Write a concatenate() function that receives some strings as arguments and
# some named arguments (the key will be a string, and the value will be another string).
# First, you should concatenate all arguments successively.
# Next, take each key successively, and if it is present in the resulting string,
# change all matching parts with the key's value. In the end, return the final string.
# See the examples for more clarification.
# Submit only your function in the judge system.
# test                                                      output
# print(concatenate("Soft", "UNI", "Is", "Grate", "!",      SoftUniIsGreat!
# UNI="Uni", Grate="Great"))

def concatenate(*args, **kwargs):
    word = f"{''.join(args)}"

    for key, value in kwargs.items():
        word = word.replace(key, value)

    return word


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

# 100/100
