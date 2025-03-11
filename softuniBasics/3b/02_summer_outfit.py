
# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ.
# Напишете програма, която спрямо времето от денонощието и градусите да препоръча
# на Виктор какви дрехи да облече. Вашият приятел има различни планове за всеки етап от деня,
# които изискват и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# ⦁	Градусите - цяло число;
# ⦁	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".

# 10 <= градуси <= 18

# Morning Outfit = Sweatshirt Shoes = Sneakers
# Afternoon Outfit = Shirt Shoes = Moccasins
# Evening Outfit = Shirt Shoes = Moccasins

# 18 < градуси <= 24

# Morning Outfit = Shirt Shoes = Moccasins
# Afternoon Outfit = T-Shirt Shoes = Sandals
# Evening Outfit = Shirt Shoes = Moccasins

# градуси >= 25

# Morning Outfit = T-Shirt Shoes = Sandals
# Afternoon Outfit = Swim Suit Shoes = Barefoot
# Evening Outfit = Shirt Shoes = Moccasins

# Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."

temperature = int(input())
time_of_day = input().lower()

if 10 <= temperature <= 18:
    if time_of_day == "morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "afternoon" or time_of_day == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"

elif 18 <= temperature <= 24:
    if time_of_day == "morning" or temperature == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"

elif temperature >= 25:
    if time_of_day == "morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_day == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
