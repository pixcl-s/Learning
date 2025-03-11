# Create a function called age_assignment() that receives a different number of names and
# a different number of key-value pairs.
# The key will be a single letter (the first letter of each name) and the value - a number (age).
# Find its first letter in the key-value pairs for each name and assign the age to the person's name.
# Then, sort the names in ascending order (alphabetically) and return the information for each person on a new line
# in the format: "{name} is {age} years old."
# Submit only the function in the judge system.
# output
# George is 26 years old.
# Peter is 19 years old

def age_assignment(*args, **kwargs):
    final = []
    for x in args:
        for y, z in kwargs.items():
            if x.startswith(y):
                final.append(f"{x} is {z} years old.")
    return "\n".join(sorted(final))

# 100/100

# test
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36,A=22, B=61))
