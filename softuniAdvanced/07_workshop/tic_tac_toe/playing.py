from pyfiglet import figlet_format
import checks

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

locations = {
    "1": [0, 0],
    "2": [0, 1],
    "3": [0, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [2, 0],
    "8": [2, 1],
    "9": [2, 2]
}

winning_condition = {"123": "", "456": "", "789": "",
                     "147": "", "258": "", "369": "",
                     "159": "", "357": ""}


def board_state():
    print()
    for row in range(len(board)):
        print(f"| {' | '.join(x for x in board[row])} |")
        if row < len(board) - 1:
            print("- - - - - - -")
    print()


def placement(pl, pcs):
    print()
    piece_placement = input(f"{pl} place a piece: ")
    piece_placement = checks.check_placement(piece_placement, locations)
    board[locations[piece_placement][0]][locations[piece_placement][1]] = pcs
    del locations[piece_placement]
    board_state()
    for x in winning_condition.keys():
        if piece_placement in x:
            winning_condition[x] += pcs


def win_check(pcs, pl):
    if locations:
        if pcs*3 in winning_condition.values():
            print(f"AND THE WINNER IS\n{figlet_format(pl, font='contessa')}LET'S GOOO")
            exit()
    else:
        print("It's a tie..\nPathetic")
        exit()


def play(players):
    turns = 0
    while True:
        for x, y in players.items():
            placement(x, y)
            turns += 1
            if turns > 4:
                win_check(y, x)

