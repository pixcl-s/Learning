
# Напишете програма която, чете ден от седмицата (текст), на английски език
# - въведен от потребителя.Ако денят е работен отпечатва на конзолата - "Working day",
# ако е почивен - "Weekend". Ако се въведе текст различен от ден от седмицата
# да се отпечата - "Error".

day = input().lower()

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    print("Working day")
elif  day == "saturday" or day == "sunday":
    print("Weekend")
else:
    print("Error")
