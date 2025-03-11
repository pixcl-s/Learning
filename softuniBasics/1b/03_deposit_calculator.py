
# Напишете програма, която изчислява каква сума ще получите в края на депозитния период
# при определен лихвен процент. Използвайте следната формула:
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit = float(input())
deposit_term = int(input())
yearly_interest = float(input()) / 100

total = deposit + deposit_term * ((deposit * yearly_interest) / 12)

print(total)