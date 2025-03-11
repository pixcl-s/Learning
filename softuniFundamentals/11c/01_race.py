import re

racers = {name: 0 for name in input().split(", ")}
pattern_names = r"[A-Za-z]"
pattern_distance = r"[0-9]"

while True:
    gibberish = input()
    if gibberish == "end of race":
        break
    gibberish_names = re.findall(pattern_names, gibberish)
    gibberish_distance = re.findall(pattern_distance, gibberish)

    name = ""
    distance = 0
    for x in gibberish_names:
        name += x
    for y in gibberish_distance:
        distance += int(y)
    if name in racers:
        racers[name] += distance

sorted_racers = dict(sorted(racers.items(), key=lambda km: km[1], reverse=True))
racer = list(sorted_racers.keys())
print(f"1st place: {racer[0]}")
print(f"2nd place: {racer[1]}")
print(f"3rd place: {racer[2]}")

