
import re

emails_to_validate = input()
pattern = r"\b((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"

valid = re.findall(pattern, emails_to_validate)

for x in valid:
    print(x[0])
