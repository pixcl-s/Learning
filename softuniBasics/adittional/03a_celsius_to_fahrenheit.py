
# Напишете програма, която чете градуси по скалата на Целзий (°C) и
# ги преобразува до градуси по скалата на Фаренхайт (°F).
# Потърсете в Интернет подходяща формула, с която да извършите изчисленията.
# Форматирате изхода до втория знак след десетичната запетая.

celsius = float(input())

print(f"{((celsius * 1.8) + 32):.2f}")
