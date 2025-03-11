# ⦁	"family" – the initial tax for a family car is 50 euros
# ⦁	" heavyDuty" – the initial tax for a heavy-duty is 80 euros
# ⦁	"sports" – the initial tax for a sports car is 100 euros

# ⦁	For a family car, the tax declines by 5 euros for every year in use. Also,
# the tax increases by 12 euros for every 3000 km. traveled.

# ⦁	For a heavyDuty car, the tax declines by 8 euros for every year in use. Also,
# the tax increases by 14 euros for every 9000 km. traveled.

# ⦁	For a sports car, the tax declines by 9 euros for every year in use. Also,
# the tax increase by 18 euros for every 2000 km. Traveled.


def valid_car(checking):
    valid_cars = ["family", "heavyDuty", "sports"]
    if checking not in valid_cars:
        print("Invalid car type.")
        return False
    return True


def tax_calculation(car, years, km):
    final_tax = 0

    if car == "family":
        initial_tax = 50
        tax_discount = int(years) * 5
        tax_increase = (int(km) // 3000) * 12
        final_tax = initial_tax + tax_increase - tax_discount
    elif car == "heavyDuty":
        initial_tax = 80
        tax_discount = int(years) * 8
        tax_increase = (int(km) // 9000) * 14
        final_tax = initial_tax + tax_increase - tax_discount
    elif car == "sports":
        initial_tax = 100
        tax_discount = int(years) * 9
        tax_increase = (int(km) // 2000) * 18
        final_tax = initial_tax + tax_increase - tax_discount
    return final_tax


cars = input().split(">>")
all_the_tax = 0

for x in range(len(cars)):
    individual_car = cars[x].split()
    if valid_car(individual_car[0]):
        tax = tax_calculation(individual_car[0], individual_car[1], individual_car[2])
        all_the_tax += tax
        print(f"A {individual_car[0]} car will pay {tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {all_the_tax:.2f} euros in taxes.")
