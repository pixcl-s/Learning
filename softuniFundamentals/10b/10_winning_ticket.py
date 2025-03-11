
# You are given a collection of tickets separated by commas and spaces (one or many).
# You need to check each ticket to see if it has a winning combination of symbols:
# A valid ticket has exactly 20 characters.
# A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^'
# uninterruptedly repeated at least 6 times in both halves of the tickets.
# In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"
# Input
# The input will be read from the console. The input consists of a single line containing all tickets separated by
# commas and one or more white spaces in the format:
# "{ticket}, {ticket}, … {ticket}"
# Output
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# If the ticket is invalid: "invalid ticket"
# If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# If the ticket is valid and winning, but not a Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
# If the ticket hits the Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"

def symbol_check(ticket_half):
    special_symbol = 0
    for character in ticket_half:
        if character == y:
            special_symbol += 1
        elif special_symbol >= 6:
            break
        else:
            special_symbol = 0
    return special_symbol


tickets = [tick.strip() for tick in input().split(", ")]
winning_symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    first_half = ticket[:10]
    second_half = ticket[10:]
    counter = 0
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    for y in winning_symbols:
        if y * 10 in first_half and y * 10 in second_half:
            print(f'ticket "{ticket}" - 10{y} Jackpot!')
            break
        elif y * 6 in first_half and y * 6 in second_half:
            how_many_one = symbol_check(first_half)
            how_many_two = symbol_check(second_half)
            print(f'ticket "{ticket}" - {min(how_many_one,how_many_two)}{y}')
            break
        counter += 1
        if counter == 4:
            print(f'ticket "{ticket}" - no match')


