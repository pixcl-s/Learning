import re

dates = input()
pattern = r"\b(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})\b"

valid_dates = re.findall(pattern, dates)

for x in valid_dates:
    day = x[0]
    month = x[2]
    year = x[3]

    print(f"Day: {day}, Month: {month}, Year: {year}")
