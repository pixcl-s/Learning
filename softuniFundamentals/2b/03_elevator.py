
# Calculate how many courses will be needed to elevate N persons by using an elevator
# with a capacity of P persons. The input holds two lines:
# the number of people N and the capacity P of the elevator.

people = int(input())
cap = int(input())
rides = 0

while people > 0:
    people -= cap
    rides += 1

print(rides)
