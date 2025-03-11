
# There is a circle road with N petrol pumps.
# The petrol pumps are numbered 0 to (N−1) (both inclusive).
# For each petrol pump, you will receive two pieces of information (separated by a single space):
# The amount of petrol the petrol pump will give you
# The distance from that petrol pump to the next petrol pump (kilometers)
# You are a truck driver, and you want to go all around the circle.
# You know that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
# In the beginning, the tank is empty,
# but you start your journey at a petrol pump so you can fill it with the given amount of petrol.
# Your task is to calculate the first petrol pump from where the truck will be able to complete the circle.
# You never miss filling its tank at a petrol pump.
# Input
# On the first line, you will receive the number of petrol pumps - N
# On the next N lines, you will receive the amount of petrol that each petrol pump will give
# and the distance between that petrol pump and the next petrol pump, separated by a single space
# Output
# An integer which will be the smallest index of a petrol pump from which you can start the tour

from collections import deque

amount_of_pump = int(input())

pumps = []
start = 0
for _ in range(amount_of_pump):
    pumps.append(input())

dequed_pumps = deque(pumps)
visited_pumps = 0

while visited_pumps < amount_of_pump:
    pumps_two = deque(dequed_pumps)
    fuel = 0
    liters, km = dequed_pumps[0].split()
    if int(liters) < int(km):
        dequed_pumps.rotate(-1)
        start += 1
    else:
        while visited_pumps < amount_of_pump:
            visited_pumps += 1
            fuel += int(liters) - int(km)
            pumps_two.rotate(-1)
            liters, km = pumps_two[0].split()
            if fuel + int(liters) < int(km):
                dequed_pumps.rotate(-1)
                start += 1
                visited_pumps = 0
                break
            else:
                continue

print(start)

# 100/100
