
# Габи иска да започне здравословен начин на живот
# и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.
# Напишете програма, която чете от конзолата по колко стъпки изминава
# тя всеки път като излиза през деня и
# когато постигне целта си да се изписва "Goal reached! Good job!" и
# колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките,
# които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си,
# на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."

GOAL = 10000

steps = input().lower()

sum_steps = 0

while steps != "going home":
    sum_steps += int(steps)
    if sum_steps >= GOAL:
        print("Goal reached! Good job!")
        print(f"{sum_steps - GOAL} steps over the goal!")
        exit()
    steps = input().lower()

steps_home = int(input())

if sum_steps + steps_home >= GOAL:
    print("Goal reached! Good job!")
    print(f"{sum_steps + steps_home - GOAL} steps over the goal!")
else:
    print(f"{GOAL - (sum_steps + steps_home)} more steps to reach goal.")
