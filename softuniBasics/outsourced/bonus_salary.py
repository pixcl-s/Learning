
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = float(input())
year_of_service = int(input())

if year_of_service > 5:
    bonus = salary * 0.05
    print(bonus)
else:
    print("No Bonus DUMASS")
    