
# Напишете програма, която изчислява колко решения в
# естествените числа (включително и нулата) има уравнението:
# x1 + x2 + x3 = n
# Числото n е цяло число и се въвежда от конзолата.

number = int(input())

counter = 0

for x in range(number + 1):
    for y in range(number + 1):
        for z in range(number + 1):
            if x + y + z == number:
                counter += 1

print(counter)
