import playing
import checks

player_one = checks.name_check(input("Player one choose name: ").upper())
player_two = checks.name_check(player_one, input("Player two choose name: ").upper())

player_one_char = checks.play_piece(input(f"{player_one} choose playing symbol: ").upper())
player_two_char = checks.play_piece(player_one_char, input(f"{player_two} choose playing symbol: ").upper())

player_board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
print()
print("Playing board:")
for row in range(len(player_board)):
    print(f"| {' | '.join(x for x in player_board[row])} |")
    if row < len(player_board) - 1:
        print("- - - - - - -")

print()
print("To place a piece insert one of the numbers!")
print(f"Players:\n{player_one} - {player_one_char}\n{player_two} - {player_two_char}")

playing.play({player_one: player_one_char, player_two: player_two_char})
