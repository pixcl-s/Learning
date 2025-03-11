
class NameTooLong(Exception):
    pass


class NameTaken(Exception):
    pass


class PlacementError(Exception):
    pass


def length(p, how_long):
    while True:
        if how_long != 1:
            try:
                if not 3 <= len(p) <= how_long:
                    raise NameTooLong
                return p
            except NameTooLong:
                print("Invalid name length b-b-buddy. Should be between 3 and 18 characters!")
                p = input("Choose new one...\n").upper()
        else:
            try:
                if len(p) != how_long:
                    raise NameTooLong
                return p
            except NameTooLong:
                print("Play symbol should be 1 character...")
                p = input("Choose again...\n").upper()


def name_check(player1, player2=None):
    len_border = 18
    while True:
        if player2 or player2 == "":
            try:
                player2 = length(player2, len_border)
                if player2 == player1:
                    raise NameTaken
                return player2
            except NameTaken:
                print("The muppet you are playing against claimed this one!")
                player2 = input("Choose new one...\n").upper()
        if not player2:
            player1 = length(player1, len_border)
            if len(player1) <= len_border and not player2:
                return player1


def play_piece(piece1, piece2=None):
    len_border = 1
    while True:
        if piece2 or piece2 == "":
            try:
                piece2 = length(piece2, len_border)
                if piece2 == piece1:
                    raise NameTaken
                return piece2
            except NameTaken:
                print("Player 1 chose this already...")
                piece2 = input("Choose new one...\n").upper()
        if not piece2:
            piece1 = length(piece1, len_border)
            if len(piece1) == len_border and not piece2:
                return piece1


def check_placement(placement, location):
    while True:
        try:
            if not placement.isnumeric():
                raise PlacementError
            elif len(placement) != 1 or placement == "0":
                raise PlacementError
            elif placement not in location:
                raise KeyError
            return placement
        except PlacementError:
            print("Bruh... You should enter digit between 1-9")
            placement = input("Try again: ")
        except KeyError:
            print("Already taken DUMASS")
            placement = input("Try again: ")
