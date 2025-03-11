import re

find_link = input()

while find_link:
    pattern = r"\b(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)\b"

    valid_link = re.findall(pattern, find_link)

    for x in valid_link:
        print(x[0])

    find_link = input()


