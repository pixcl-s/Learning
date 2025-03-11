# You will receive passwords as input on new lines, until the command "Done".
# Your task is to validate if the passwords are strong by applying the following validations:
# · Each password should be at least 8 characters long, otherwise, PasswordTooShortError should be raised.
# · If the password consists of
# only digits, only letters, or only special characters, PasswordTooCommonError should be raised.
# · Each password should have at least 1 special character, otherwise,
# PasswordNoSpecialCharactersError should be raised. The special characters are "@", "*", "&", and "%".
# · If the password contains empty spaces, PasswordContainsSpacesError should be raised.
# When an error is encountered, raise it with an appropriate message:
# · PasswordTooShortError - "Password must contain at least 8 characters"
# · PasswordTooCommonError -"Password must be a combination of digits, letters, and special characters"
# · PasswordNoSpecialCharactersError - "Password must contain at least 1 special character"
# · PasswordContainsSpacesError -"Password must not contain empty spaces"
# If the current password is valid, print "Password is valid" and read the next one.

class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass


symbols = ["@", "*", "&", "%"]

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    if password.isalpha() or password.isnumeric() or all(c in symbols for c in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    if not any(s in password for s in symbols):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    print("Password is valid")

