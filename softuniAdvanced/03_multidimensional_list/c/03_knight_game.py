# Chess is the oldest game, but it is still popular these days.
# You will use only one chess piece for this task - the Knight.
# A chess knight has 8 possible moves it can make, as illustrated.
# It can move to the nearest square but not on the same row, column, or diagonal.
# (e.g., it can move two squares horizontally, then one square vertically, or
# it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.)
# The knight game is played on a board with dimensions N x N.
# You will receive a board with a "K" for knights and a "0" for empty cells.
# Your task is to remove knights until no knights that can attack one another with one move are left.
# Always remove the knight who can attack the greatest number of knights.
# If there are two or more knights with the same number of attacks, remove the top-left one.
# Input
# · On the first line, you will receive integer N - the size of the board
# · On the following N lines, you will receive strings with "K" and "0"
# Output
# · Print a single integer with the number of knights that need to be removed.
# Constraints
# · The size of the board will be 0 < N < 30
# · Time limit: 0.3 sec. Memory limit: 16 MB
# input     output
# 5         1
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

knight_movement = [
    [-2, +1], [-2, -1],
    [+2, +1], [+2, -1],
    [+1, -2], [-1, -2],
    [+1, +2], [-1, +2]
]
board_dimensions = int(input())

chess_board = []
knight_location = []

removed_knights = 0

for x in range(board_dimensions):
    board_part = list(input())
    chess_board.append(board_part)
    for y in range(len(board_part)):
        if board_part[y] == "K":
            knight_location.append([x, y])

while True:
    taken_pieces = 0
    taking_knight = None

    for x in range(len(knight_location)):
        pieces_to_take = 0
        knight_row, knight_col = knight_location[x]

        for y in range(len(knight_movement)):
            movement_row, movement_col = knight_movement[y]

            going_to_row = knight_row + movement_row
            going_to_col = knight_col + movement_col

            if going_to_row < 0 or going_to_row >= board_dimensions or going_to_col < 0 or going_to_col >= board_dimensions:
                continue

            if chess_board[going_to_row][going_to_col] == "K":
                pieces_to_take += 1

        if pieces_to_take > taken_pieces:
            taken_pieces = pieces_to_take
            taking_knight = knight_location[x]

    if taking_knight:
        chess_board[taking_knight[0]][taking_knight[1]] = "0"
        knight_location.remove(taking_knight)
        removed_knights += 1
    if taken_pieces == 0:
        break

print(removed_knights)

# 100/100
