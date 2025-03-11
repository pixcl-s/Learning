# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements,
# separated by a comma and a space ", ".
# You should find the matrix's diagonals, print them, and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
# input             output
# 3                 Primary diagonal: 1, 5, 9. Sum: 15
# 1, 2, 3           Secondary diagonal: 3, 5, 7. Sum: 15
# 4, 5, 6
# 7, 8, 9

matrix = [[int(x) for x in input().split(", ")]for _ in range(int(input()))]

sumage_main = 0
main_number = []
sumage_opposite = 0
opposite_numbers = []

for x in range(len(matrix)):
    sumage_main += matrix[x][x]
    sumage_opposite += matrix[x][len(matrix)-1-x]
    main_number.append(matrix[x][x])
    opposite_numbers.append(matrix[x][len(matrix)-1-x])

print(f"Primary diagonal: {', '.join(str(x) for x in main_number)}. Sum: {sumage_main}")
print(f"Secondary diagonal: {', '.join(str(x) for x in opposite_numbers)}. Sum: {sumage_opposite}")

# 100/100
