
# Write a program that reads an integer number of centuries
# and converts it to years, days, hours, and minutes.
# ⦁	Assume that one year has 365.2422 days on average

century = int(input())

years = century * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
