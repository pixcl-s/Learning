
# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта.
# Той обаче не знае колко парчета могат да си вземат гостите от нея.
# Вашата задача е да напишете програма, която изчислява броя на парчетата,
# които гостите са взели преди тя да свърши.
# Ще получите размерите на тортата
# (широчина и дължина – цели числа и след това на всеки ред,
# до получаване на командата "STOP" или докато не свърши тортата,
# броят на парчетата, които гостите вземат от нея. Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# ⦁	"{брой парчета} pieces are left." -  ако стигнете до STOP и не са свършили парчетата торта;
# ⦁	"No more cake left! You need {брой недостигащи парчета} pieces more."

length = int(input())
width = int(input())

cake_size = length * width

pieces = input()

while pieces != "STOP":
    cake_size -= int(pieces)
    if cake_size <= 0:
        break
    pieces = input()


if cake_size <= 0:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
else:
    print(f"{cake_size} pieces are left.")
