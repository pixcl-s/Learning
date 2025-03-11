# Write a program that gathers a sum of money using the least possible number of coins.
# This is the range of possible coin values:
# · { 1, 2, 5, 10, 20, 50 }
# You will receive the desired sum. The goal is to reach the sum using as few coins as possible using a greedy approach.
# We'll assume that each coin value and the desired sum are integers.
# Input
# · On the first line, you will receive the coins.
# · On the next line, you will receive the target sum.
# input                 output
# 1, 2, 5, 10, 20, 50   Number of coins to take: 21
# 923                   18 coin(s) with value 50
#                       1 coin(s) with value 20
#                       1 coin(s) with value 2
#                       1 coin(s) with value 1

# 3, 7                  Error
# 11

def change(coin, how_much):
    the_change = {}
    coin.reverse()
    for x in coin:
        coins_amount = how_much // x
        if coins_amount:
            how_much %= x
            the_change[x] = coins_amount
    if how_much:
        return "Error"

    to_return = f"Number of coins to take: {sum(the_change.values())}\n"
    for key, value in the_change.items():
        to_return += f"{value} coin(s) with value {key}\n"

    return to_return


coins = [int(x) for x in input().split(", ")]
change_amount = int(input())
print(change(coins, change_amount))

# 80/100


# def change(coin, how_much):
#     the_change = {}
#     while how_much:
#         if how_much and not coin:
#             print("Error")
#             exit()
#         the_coin = coin.pop()
#         if how_much // the_coin:
#             amount_of_coins = how_much // the_coin
#             the_change[the_coin] = amount_of_coins
#             how_much -= amount_of_coins * the_coin
#     to_return = f"Number of coins to take: {sum(the_change.values())}\n"
#     for key, value in the_change.items():
#         to_return += f"{value} coin(s) with value {key}\n"
#
#     return to_return
#
#
# coins = [int(x) for x in input().split(", ")]
# change_amount = int(input())
# print(change(coins, change_amount))

# 80/100
