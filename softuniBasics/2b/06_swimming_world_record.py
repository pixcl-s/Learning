
# Иван решава да подобри Световния рекорд по плуване на дълги разстояния.
# На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,
# разстоянието в метри, което трябва да преплува и времето в секунди,
# за което плува разстояние от 1 м. Да се напише програма, която изчислява дали се е справил със задачата,
# като се има предвид, че:
#
# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
#
# Когато се изчислява колко пъти Иван ще се забави, в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.

import math

world_record = float(input())
meters_to_swim = float(input())
time_to_swim_1m = float(input())

time_taken = meters_to_swim * time_to_swim_1m

if meters_to_swim >= 15:
    meters_slowed = meters_to_swim // 15
    slowed_down_by = meters_slowed * 12.5
    math.floor(slowed_down_by)
    time_taken = time_taken + slowed_down_by

difference = time_taken - world_record

if time_taken < world_record:
    print(f"Yes, he succeeded! The new world record is {time_taken:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")



