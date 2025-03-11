
import re

demon = input().split(", ")
pattern_letters = r"(?i)[a-z]"
pattern_digits = r"(?i)[^a-z]+"
demon.sort()

for x in demon:
    letters = re.findall(pattern_letters, x)
    digits = re.findall(pattern_digits, x)
    health = 0
    damage = 0

    for y in letters:
        health += ord(y)
    for z in digits:
        divide_multiply = []
        if "*" in z or "/" in z:
            z_list = list(z)
            number = ""
            for p in z_list:
                if p == "*" or p == "/":
                    divide_multiply.append(p)
                else:
                    number += p
            if number:
                damage += float(number)
        else:
            damage += float(z)

        if z is digits[-1]:
            for l in divide_multiply:
                if l == "*":
                    damage = damage * 2
                elif l == "/":
                    damage = damage / 2

    print(f"{x} - {health} health, {damage:.2f} damage")
