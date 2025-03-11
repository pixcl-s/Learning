
# Write a function that checks if a given password is valid. Password validations are:
# It should be 6 - 10 (inclusive) characters long
# It should consist only of letters and digits
# It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# "Password must be between 6 and 10 characters"
# "Password must consist only of letters and digits"
# "Password must have at least 2 digits"

def length(word):
    if 6 <= len(word) <= 10:
        return True
    else:
        return False


def symbols(word):
    for symbol in word:
        if not (48 <= ord(symbol) <= 57 or 97 <= ord(symbol) <= 122):
            return False
    return True


def digits(word):
    counter = 0
    for simbol in word:
        if 48 <= ord(simbol) <= 57:
            counter += 1
    if counter < 2:
        return False
    else:
        return True


def is_password_valid(word):
    incorrect_password = []
    missed_requirements = 0
    if not length(word):
        incorrect_password.append("Password must be between 6 and 10 characters")
        missed_requirements += 1
    if not symbols(word):
        incorrect_password.append("Password must consist only of letters and digits")
        missed_requirements += 1
    if not digits(word):
        incorrect_password.append("Password must have at least 2 digits")
        missed_requirements += 1

    if missed_requirements > 0:
        print("\n".join(incorrect_password))
    else:
        print("Password is valid")


password = input().lower()

is_password_valid(password)
