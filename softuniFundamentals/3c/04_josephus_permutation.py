
# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
# the list itself - numbers separated by a single space representing the people in the circle
# a number k
# People are standing in a circle waiting to be executed.
# Counting begins from the first one in the circle and proceeds from left to right.
# After a specified number of people are skipped, the k person is executed.
# The procedure is repeated with the remaining people, starting with the next person,
# going in the same direction, and skipping the same number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"

prisoners = input().split()

eeny_meeny_miny_moe = int(input()) - 1

initial_eeny = eeny_meeny_miny_moe

multilpier = 0

order_of_executions = []

while True:

    order_of_executions.append(prisoners[eeny_meeny_miny_moe + multilpier])
    prisoners.pop(eeny_meeny_miny_moe + multilpier)
    multilpier += eeny_meeny_miny_moe

    if len(prisoners) <= eeny_meeny_miny_moe + multilpier:
        eeny_meeny_miny_moe = (eeny_meeny_miny_moe + multilpier) - len(prisoners)
        multilpier = 0

    if eeny_meeny_miny_moe < initial_eeny:
        order_of_executions.append(prisoners[eeny_meeny_miny_moe + multilpier])
        prisoners.pop(eeny_meeny_miny_moe + multilpier)
        eeny_meeny_miny_moe += initial_eeny
