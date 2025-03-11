
# You will receive two lines of input:
# ⦁	a list of employees' happiness as a string of numbers separated by a single space
# ⦁	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# ⦁	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# ⦁	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

happiness = [int(num) for num in input().split()]

improvement = int(input())

improved_happiness = [x * improvement for x in happiness]

average_happiness = sum(improved_happiness) / len(improved_happiness)

happy_employees = [y for y in improved_happiness if y >= average_happiness]

if len(improved_happiness) / 2 <= len(happy_employees):
    print(f"Score: {len(happy_employees)}/{len(improved_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(improved_happiness)}. Employees are not happy!")

