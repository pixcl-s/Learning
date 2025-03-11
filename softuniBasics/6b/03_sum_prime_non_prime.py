
# Напишете програма, която чете от конзолата цели числа,
# докато не се получи команда "stop". Да се намери сумата на всички въведени прости и
# сумата на всички въведени непрости числа.
# Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости,
# ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.".
# В този случай въведено число се игнорира и не се прибавя към нито една от двете суми,
# а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.

# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# ⦁	"Sum of all prime numbers is: {prime numbers sum}"
# ⦁	"Sum of all non prime numbers is: {nonprime numbers sum}"

number = input()

prime = 0
non_prime = 0

while number != "stop":

    flag = True

    if int(number) < 0:
        print("Number is negative.")

    for x in range(2, int(number) + 1):
        if int(number) % x != 0:
            flag = False
            break
    if flag:
        prime += int(number)
    else:
        non_prime += int(number)

    number = input()

print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
