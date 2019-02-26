"""
This is my game of Connect-Four.
Written by João Ricardo de Souza, February 25 2019.
"""

# Board Variable
board = [[], [], [], [], [], [], []]


def clear_board():
    """Clears the board for a new match"""
    global board
    board = [[], [], [], [], [], [], []]


def add_spaces(b):
    """Adds spaces to match len(board[i]) == 7"""
    for i in b:
        while len(i) < 6:
            i.append(' ')


def clear_spaces(b):
    """Remove spaces after visualizing the board"""
    for i in b:
        while i.count(' ') != 0:
            i.remove(' ')


def score(b):
    """Returns the image of the board, based on indexes"""
    return f"""
      1   2   3   4   5   6   7  
    -----------------------------
    | {b[0][5]} | {b[1][5]} | {b[2][5]} | {b[3][5]} | {b[4][5]} | {b[5][5]} | {b[6][5]} |
    -----------------------------
    | {b[0][4]} | {b[1][4]} | {b[2][4]} | {b[3][4]} | {b[4][4]} | {b[5][4]} | {b[6][4]} |
    -----------------------------
    | {b[0][3]} | {b[1][3]} | {b[2][3]} | {b[3][3]} | {b[4][3]} | {b[5][3]} | {b[6][3]} |
    -----------------------------
    | {b[0][2]} | {b[1][2]} | {b[2][2]} | {b[3][2]} | {b[4][2]} | {b[5][2]} | {b[6][2]} |
    -----------------------------
    | {b[0][1]} | {b[1][1]} | {b[2][1]} | {b[3][1]} | {b[4][1]} | {b[5][1]} | {b[6][1]} |
    -----------------------------
    | {b[0][0]} | {b[1][0]} | {b[2][0]} | {b[3][0]} | {b[4][0]} | {b[5][0]} | {b[6][0]} |
    -----------------------------
"""


def show_board(b):
    """Prints the present board"""
    add_spaces(b)
    print(score(b))
    clear_spaces(b)


def wins_list(b):
    """Returns a list of possible winning positions"""
    check_list = []
    # Add the columns
    for i in range(0, 7):
        check_list.extend([b[i][0:4], b[i][1:5], b[i][2:6]])
    # Add the rows
    for i in range(0, 6):
        check_list.extend([[b[0][i], b[1][i], b[2][i], b[3][i]],
                           [b[1][i], b[2][i], b[3][i], b[4][i]],
                           [b[2][i], b[3][i], b[4][i], b[5][i]],
                           [b[3][i], b[4][i], b[5][i], b[6][i]]])
    # Add the diagonals
    check_list.extend([
                       # Challenge for Carlo: a function to find all possible len(4) diagonals in a 6x7 matrix!
                       # (This was awfully impossible for me...)
                       # Upper-Left to Bottom-Right Diagonals
                       [b[0][5], b[1][4], b[2][3], b[3][2]],
                       [b[1][5], b[2][4], b[3][3], b[4][2]],
                       [b[2][5], b[3][4], b[4][3], b[5][2]],
                       [b[3][5], b[4][4], b[5][3], b[6][2]],
                       [b[0][4], b[1][3], b[2][2], b[3][1]],
                       [b[1][4], b[2][3], b[3][2], b[4][1]],
                       [b[2][4], b[3][3], b[4][2], b[5][1]],
                       [b[3][4], b[4][3], b[5][2], b[6][1]],
                       [b[0][3], b[1][2], b[2][1], b[3][0]],
                       [b[1][3], b[2][2], b[3][1], b[4][0]],
                       [b[2][3], b[3][2], b[4][1], b[5][0]],
                       [b[3][3], b[4][2], b[5][1], b[6][0]],
                       # Bottom-Left to Upper-Right Diagonals
                       [b[0][0], b[1][1], b[2][2], b[3][3]],
                       [b[1][0], b[2][1], b[3][2], b[4][3]],
                       [b[2][0], b[3][1], b[4][2], b[5][3]],
                       [b[3][0], b[4][1], b[5][2], b[6][3]],
                       [b[0][1], b[1][2], b[2][3], b[3][4]],
                       [b[1][1], b[2][2], b[3][3], b[4][4]],
                       [b[2][1], b[3][2], b[4][3], b[5][4]],
                       [b[3][1], b[4][2], b[5][3], b[6][4]],
                       [b[0][2], b[1][3], b[2][4], b[3][5]],
                       [b[1][2], b[2][3], b[3][4], b[4][5]],
                       [b[2][2], b[3][3], b[4][4], b[5][5]],
                       [b[3][2], b[4][3], b[5][4], b[6][5]]])
    return check_list


class Player:

    def __init__(self, index, marker, bool_start):
        """Class for the creation of the players"""
        self.id = index
        self.name = input(f"Enter name for Player {self.id}: ")
        self.marker = marker
        self.start = bool_start
        self.wins = 0

    def has_won(self):
        """Check if the player has won"""
        match = False
        add_spaces(board)
        for i in wins_list(board):
            if i == [self.marker] * 4:
                match = True
        clear_spaces(board)
        return match

    def play(self, position):
        """Player assignment on the board"""
        board[position].append(self.marker)


def action(player):
    """Player action"""
    while True:
        try:
            pos = int(input(f"{player.name}'s Turn. Enter a column to drop '{player.marker}': "))
            if 1 <= pos <= 7:
                if len(board[pos-1]) <= 5:
                    player.play(pos-1)
                    show_board(board)
                    break
                else:
                    print("This column is full. You must select another one.")
            else:
                print("Enter a valid column (1 to 7)")
        except ValueError:
            print("Enter a valid number from 1 to 7")


def show_score(p1, p2):
    """Return the present Score Board"""
    return f"""
           Score:
       --------------
        {p1.name}:  {p1.wins}
       --------------
        {p2.name}:  {p2.wins}
       --------------
"""


def connect_four(player1, player2):
    """Single match structure"""
    show_board(board)
    count = 0
    while True:
        action(player1)
        count += 1
        if player1.has_won() is True:
            print(f"{player1.name} has won the game.")
            player1.wins += 1
            player1.start = True
            player2.start = False
            break
        elif count == 42:
            break
        action(player2)
        count += 1
        if player2.has_won() is True:
            print(f"{player2.name} has won the game.")
            player2.wins += 1
            player2.start = True
            player1.start = False
            break
        elif count == 42:
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
    print("""
This is a game of Connect-Four.

Players must choose a column to drop their markers.
Whoever gets four sequence markers in a row, column or diagonal wins the game.
""", end="\n")
    player_1 = Player(1, "X", True)
    player_2 = Player(2, "O", False)
    print("\nEnter a column number to drop your marker.")
    while True:
        clear_board()
        if player_1.start is True:
            connect_four(player_1, player_2)
        elif player_2.start is True:
            connect_four(player_2, player_1)
        print(show_score(player_1, player_2))
        rematch()


# Play!
game_on()
