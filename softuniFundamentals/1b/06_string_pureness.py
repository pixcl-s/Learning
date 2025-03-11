
# You will be given the number n. After that, you'll receive different strings n times.
# Your task is to check if the given strings are pure,
# meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
# If a string is pure, print "{string} is pure."
# Otherwise, print "{string} is not pure!

number = int(input())
is_pure = ""

for _ in range(number):
    string_string = input()

    for character in string_string:
        if character == "," or character == "." or character == "_":
            is_pure = "no"
    if is_pure == "no":
        print(f"{string_string} is not pure!")
    else:
        print(f"{string_string} is pure.")

    is_pure = ""
