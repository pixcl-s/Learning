
# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която чете времената на състезателите в секунди,
# въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").

contestant_1 = int(input())
contestant_2 = int(input())
contestant_3 = int(input())

sum = contestant_1 + contestant_2 + contestant_3

minutes = sum // 60
seconds = sum - (minutes * 60)

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
