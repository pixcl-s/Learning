
# Напишете програма, която отпечатва числата в диапазона от 1 до 1000, които завършват на 7.

for i in range(1, 1001):
    if i % 10 == 7:
        print(i)
