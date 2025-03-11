
# Напишете програма, която при въведени градуси (реално число) принтира какво е времето,
# като имате предвид следната таблица:
# Градуси	           Време
# 26.00 - 35.00	        Hot
# 20.10 - 25.90	        Warm
# 15.00 - 20.00	        Mild
# 12.00 - 14.90	        Cool
#  5.00 - 11.90	        Cold

temp = float(input())

if 26 <= temp <= 35:
    print("Hot")
elif 20.1 <= temp <= 25.9:
    print("Warm")
elif 15 <= temp <= 20:
    print("Mild")
elif 12 <= temp <= 14.9:
    print("Cool")
elif 5 <= temp <= 11.9:
    print("Cold")
else:
    print("unknown")
