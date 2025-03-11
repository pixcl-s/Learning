
# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines,
# which will follow. On the following n lines, you will receive liters of water (integers),
# which you should pour into your tank. If the capacity is not enough,
# print "Insufficient capacity!" and continue reading the next line.
# On the last line, print the liters in the tank.

tank = 255
poured = 0

how_many_times = int(input())

for _ in range(how_many_times):
    litres = int(input())
    poured += litres
    if poured > tank:
        print("Insufficient capacity!")
        poured -= litres

print(poured)
