"""
This is my game of Tic-Tac-Toe
Built by João Ricardo, February 23 2019
"""

# Dictionary of values for the board
v_dict = {"A1": " ", "A2": " ", "A3": " ",
          "B1": " ", "B2": " ", "B3": " ",
          "C1": " ", "C2": " ", "C3": " "}


def clear_board():
    """Clear the board for a new game"""
    global v_dict
    v_dict = {"A1": " ", "A2": " ", "A3": " ",
              "B1": " ", "B2": " ", "B3": " ",
              "C1": " ", "C2": " ", "C3": " "}


def wins():
    """Generate list for winning possibilities"""
    return [[v_dict["A1"], v_dict["A2"], v_dict["A3"]],
            [v_dict["B1"], v_dict["B2"], v_dict["B3"]],
            [v_dict["C1"], v_dict["C2"], v_dict["C3"]],
            [v_dict["A1"], v_dict["B1"], v_dict["C1"]],
            [v_dict["A2"], v_dict["B2"], v_dict["C2"]],
            [v_dict["A3"], v_dict["B3"], v_dict["C3"]],
            [v_dict["A1"], v_dict["B2"], v_dict["C3"]],
            [v_dict["A3"], v_dict["B2"], v_dict["C1"]]]


def board():
    """Return the present board"""
    return """
          1   2   3
        -------------
     A  | {0} | {1} | {2} |
        -------------
     B  | {3} | {4} | {5} |
        -------------
     C  | {6} | {7} | {8} |
        -------------
        """.format(v_dict["A1"], v_dict["A2"], v_dict["A3"], v_dict["B1"],
                   v_dict["B2"], v_dict["B3"], v_dict["C1"], v_dict["C2"], v_dict["C3"])


class Player:

    def __init__(self, index, marker, bool_start):
        """Class for the creation of the players"""
        self.id = index
        self.name = input("Enter name for Player {0}: ".format(self.id))
        self.marker = marker
        self.wins = 0
        self.start = bool_start

    def has_won(self):
        """Check if the player has won"""
        match = False
        for i in wins():
            if i == [self.marker] * 3:
                match = True
        return match

    def play(self, position):
        """Player assignment on the board"""
        v_dict["{0}".format(position)] = self.marker


def player_play(player):
    """Player action"""
    while True:
        pos = input("{0}'s Turn. Position: ".format(player.name)).upper()
        if pos in v_dict.keys():
            if v_dict[pos] == " ":
                player.play(pos)
                print(board())
                break
            else:
                print("This position has already been assigned. You must choose another one.")
        else:
            print("Input a position on the board (A1, C3, B2, etc.)")


def score(p1, p2):
    """Return the present Score Board"""
    points = """
           Score:
       --------------
        {0}:  {1}
       --------------
        {2}:  {3}
       --------------
    """.format(p1.name, p1.wins, p2.name, p2.wins)
    return points


def tic_tac_toe(player1, player2):
    """Single match structure"""
    print(board())
    count = 0
    while True:
        player_play(player1)
        count += 1
        if player1.has_won() is True:
            print("{0} has won the game.".format(player1.name))
            player1.wins += 1
            player1.start = True
            player2.start = False
            break
        elif count == 9:
            break
        player_play(player2)
        count += 1
        if player2.has_won() is True:
            print("{0} has won the game.".format(player2.name))
            player2.wins += 1
            player2.start = True
            player1.start = False
            break
        elif count == 9:
            break
    if player1.has_won() is False and player2.has_won() is False:
        print("The game finished with a draw.")
        if player1.start is True and player2.start is False:
            player2.start = True
            player1.start = False
        elif player2.start is True and player1.start is False:
            player1.start = True
            player2.start = False


def rematch():
    """Rematch option"""
    print("Do you wish for a rematch?")
    re = input("[y/n]: ").lower()
    while True:
        if re == "y":
            break
        elif re == "n":
            print("\nClosing the game. Goodbye.")
            exit(0)
        else:
            print("Type 'y' for Yes or 'n' for No")
            re = input("[y/n]: ").lower()


def game_on():
    """Game loop"""
    print("\nThis is a classic game of Tic-Tac-Toe.", end="\n\n")
    player_1 = Player(1, "X", True)
    player_2 = Player(2, "O", False)
    print("\nInsert a position on the board to assign your play.")
    while True:
        clear_board()
        if player_1.start is True:
            tic_tac_toe(player_1, player_2)
        elif player_2.start is True:
            tic_tac_toe(player_2, player_1)
        print(score(player_1, player_2))
        rematch()


# Play!
game_on()
