
# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print("")

#     # Decide the row count. (above pattern contains 5 rows)
# row = 5
# # start: 1
# # stop: row+1 (range never include stop number in result)
# # step: 1
# # run loop 5 times
# for i in range(1, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")

# ------------------------------------------------------------------------------------------------------------------

# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# number = int(input())
#
# sum = 0
#
# for i in range(number + 1):
#     sum += i
#
# print(sum)

# ---------------------------------------------------------------------------------------------------------------------

# Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be
# 2 4 6 8 10 12 14 16 18 20
#
# number = int(input())
#
# for i in range(1, 11):
#     print(number * i)

# ----------------------------------------------------------------------------------------------------------------------
