
def food_expenses(people, food, days):
    return (people * food) * days


def accommodation_expanses(people, room, days):
    expanses = (people * room) * days
    if people > 10:
        expanses -= expanses * 0.25
    return expanses


def traveling_expanses(fuel, kilometers):
    return fuel * kilometers


trip_length = int(input())
budget_for_trip = float(input())
group = int(input())
fuel_price = float(input())
food_price_per_person = float(input())
room_price_per_person = float(input())

total_expanses = food_expenses(group, food_price_per_person, trip_length) + accommodation_expanses(group, room_price_per_person, trip_length)

for x in range(1, trip_length + 1):

    traveled_distance = float(input())

    total_expanses += traveling_expanses(fuel_price, traveled_distance)

    if x % 3 == 0 or x % 5 == 0:
        total_expanses += total_expanses * 0.40
    if x % 7 == 0:
        total_expanses -= total_expanses / group

    if total_expanses > budget_for_trip:
        print(f"Not enough money to continue the trip. You need {total_expanses - budget_for_trip:.2f}$ more.")
        exit()


print(f"You have reached the destination. You have {budget_for_trip - total_expanses:.2f}$ budget left.")
