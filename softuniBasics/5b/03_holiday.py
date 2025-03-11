
# Джеси е решила да събира пари за екскурзия и
# иска от вас да ѝ помогнете да разбере дали ще успее да събере необходимата сума.
# Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има
# и ще ѝ останат 0 лева.

# От конзолата се четат:
# ⦁	Пари, нужни за екскурзията - реално число;
# ⦁	Налични пари - реално число.
# След това многократно се четат по два реда:
# ⦁	Вид действие – текст с две възможности: "spend" или "save";
# ⦁	Сумата, която ще спести/похарчи - реално число.

# Програмата трябва да приключи при следните случаи:
# ⦁	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# ⦁	"You can't save the money."
# ⦁	"{Общ брой изминали дни}"
# ⦁	Ако Джеси събере парите за почивката, на конзолата се изписва:
# ⦁	"You saved the money for {общ брой изминали дни} days."

holiday = int(input())
available_money = int(input())

money_saved = 0
days_in_a_row_spending = 0
days_past = 0

spend_save = input()
how_much = int(input())

while not money_saved + available_money == holiday:

    days_past += 1

    if spend_save == "spend":
        days_in_a_row_spending += 1
        available_money -= how_much
        if days_in_a_row_spending == 5:
            print("You can't save the money.")
            print(f"{days_past}")
            exit()
        elif how_much > available_money:
            how_much == available_money
    elif spend_save == "save":
        days_in_a_row_spending = 0
        money_saved += how_much
    try:
        spend_save = input()
        how_much = int(input())
    except EOFError:
        break

print(f"You saved the money for {days_past} days.")
