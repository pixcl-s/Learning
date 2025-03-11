
# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това.
# Ако е пристигнал по-рано повече от 30 минути, той е подранил.
# Ако е дошъл след часа на изпита, той е закъснял.
# Напишете програма, която прочита време на изпит и време на пристигане и
# отпечатва дали студентът е дошъл навреме,
# дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.

# Вход
# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# ⦁	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# ⦁	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# ⦁	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# ⦁	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.

# Изход
# На първия ред отпечатайте:
# ⦁	"Late", ако студентът пристига по-късно от часа на изпита;
# ⦁	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# ⦁	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.

# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# ⦁	"mm minutes before the start" за идване по-рано с по-малко от час;
# ⦁	"hh:mm hours before the start" за подраняване с 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:05”;
# ⦁	"mm minutes after the start" за закъснение под час;
# ⦁	"hh:mm hours after the start" за закъснение от 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:03”.

hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

arrival = ""

if (hour_arrival == hour_exam and minute_arrival == minute_exam) or (hour_arrival == hour_exam and 0 < minute_exam - minute_arrival <= 30) or (hour_exam - hour_arrival == 1 and ((minute_exam + 30) <= minute_arrival)):
    arrival = "On Time"
elif (hour_exam == hour_arrival and minute_exam - minute_arrival > 30) or (hour_arrival < hour_exam and 0 < abs(minute_exam - minute_arrival) < 30) or (hour_exam - hour_arrival > 0):
    arrival = "Early"
elif (hour_exam == hour_arrival and minute_exam < minute_arrival) or (hour_exam < hour_arrival):
    arrival = "Late"

print(arrival)

if arrival == "On Time":
    if hour_arrival == hour_exam and minute_arrival == minute_exam:
        exit()
    elif minute_exam == 0:
        print(f"{60 - minute_arrival} minutes before the start")
    elif hour_arrival < hour_exam:
        print(f"{minute_exam + abs(minute_arrival - 60)} minutes before the start")
    else:
        print(f"{abs(minute_exam - minute_arrival)} minutes before the start")
elif arrival == "Early":
    # if hour_exam - hour_arrival == 1 and (abs(minute_arrival - 60) + abs(minute_exam - 60) < 60):
    #     print(f"{(60 - minute_arrival) + (60 - minute_exam)} minutes before the start")
    if hour_exam - hour_arrival == 1 and 60 > (60 - minute_arrival) + minute_exam > 30:
        print(f"{(60 - minute_arrival) + minute_exam} minutes before the start")
    elif hour_exam - hour_arrival > 1:
        if minute_exam < minute_arrival:
            print(f"{(hour_exam - hour_arrival)-1}:{(60 - minute_arrival + minute_exam):02d} hours before the start")
        else:
            print(f"{(hour_exam - hour_arrival)}:{abs(minute_exam - minute_arrival):02d} hours before the start")
    else:
        print(f"{hour_exam - hour_arrival}:{abs(minute_exam - minute_arrival):02d} hours before the start")
elif arrival == "Late":
    if hour_arrival == hour_exam:
        print(f"{minute_arrival - minute_exam} minutes after the start")
    elif hour_exam < hour_arrival:
        if minute_exam > minute_arrival:
            print(f"{60 + minute_arrival - minute_exam} minutes after the start")
        else:
            print(f"{hour_arrival - hour_exam}:{(minute_arrival - minute_exam):02d} hours after the start")
