
from math import floor


def biscuits_per_month(produce, humans):
    production = 0
    for x in range(1, 30+1):
        if x % 3 == 0:
            third_day_loss = produce * 0.75
            production += floor(humans * third_day_loss)
        else:
            production += humans * produce
    return production


def difference_in_production(produce, diff):
    how_much = produce - diff
    percent = (abs(how_much) / diff) * 100
    if how_much < 0:
        return f"You produce {percent:.2f} percent less biscuits."
    else:
        return f"You produce {percent:.2f} percent more biscuits."


biscuits = int(input())

workers = int(input())

rivals = int(input())

biscuits_made = biscuits_per_month(biscuits, workers)
difference = difference_in_production(biscuits_made, rivals)

print(f"You have produced {biscuits_made:.0f} biscuits for the past month.")
print(difference)
