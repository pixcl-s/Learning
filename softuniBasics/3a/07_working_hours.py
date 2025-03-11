
# Да се напише програма, която чете час от денонощието(цяло число)
# и ден от седмицата(текст) - въведени от потребителя
# и проверява дали офисът на фирма е отворен,
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително

hour = int(input())
day = input().lower()

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday":
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")
