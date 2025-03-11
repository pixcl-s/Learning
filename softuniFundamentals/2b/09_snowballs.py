
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# ⦁	The weight of the snowball (integer).
# ⦁	The time needed for the snowball to get to its target (integer).
# ⦁	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# Input
# ⦁	On the first input line, you will receive N – the number of snowballs.
# ⦁	On the next N*3 input lines, you will be receiving data about each snowball.
# Output
# ⦁	You need to print the highest calculated snowball's value in the format:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"

snowballs = int(input())

highest_value = 0
best_weight = 0
best_travel_time = 0
best_quality = 0

for _ in range(snowballs):
    weight = int(input())
    travel_time = int(input())
    quality = int(input())

    value = (weight // travel_time) ** quality

    if value > highest_value:
        highest_value = value
        best_weight = weight
        best_travel_time = travel_time
        best_quality = quality

print(f"{best_weight} : {best_travel_time} = {highest_value} ({best_quality})")
