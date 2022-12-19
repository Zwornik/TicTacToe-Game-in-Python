from random import choice

"""Game Tic Tac Toe"""

"""Fields numbering
       A   B   C  
      ╔═══╤═══╤═══╗
    1 ║ O │ 3 │ 6 ║
      ╟───┼───┼───╢
    2 ║ 1 │ 4 │ 7 ║
      ╟───┼───┼───╢
    3 ║ 2 │ 5 │ 8 ║
      ╚═══╧═══╧═══╝
      
      'X' - User figure
      'O' - Computer figure
"""

who = "X"  # Contain info about recent player


class Display:

    def __init__(self, who_in=" "):
        self.who = who_in  # Recent layer figure "X" or "O"
        self.state = Board.state

        if self.who == "X":  # Select message to display
            message = "◀   This is your move. ( X )"
        elif self.who == "O":
            message = "◀◀◀◀◀◀   This is my move. ( O )"
        else:
            message = "◀◀◀  This is our empty board"

        print("        A   B   C  ".format(self.state))
        print("      ╔═══╤═══╤═══╗")
        print("    1 ║ {0[0]:^{1}} │ {0[3]:^{1}} │ {0[6]:^{1}} ║".format(self.state, 1))
        print("      ╟───┼───┼───╢")
        print("    2 ║ {0[1]:^{1}} │ {0[4]:^{1}} │ {0[7]:^{1}} ║   {2}".format(self.state, 1, message))
        print("      ╟───┼───┼───╢")
        print("    3 ║ {0[2]:^{1}} │ {0[5]:^{1}} │ {0[8]:^{1}} ║".format(self.state, 1))
        print("      ╚═══╧═══╧═══╝\n")

    def win_display(self, name):
        if self.who == "X":
            print("You won with a very sophisticated Artificial Intelligence! Congratulations!!\n"
                  "You are going to loose next time.")

        elif self.who == "O":
            print("I WON! {0} You looser. Human beings' time is limited on this planet. Haaa haaa!!\n".format(name))

        elif self.who == 'draw':
            print("─"*8, "DRAW!! {0}, really?! You can not even afford to bit a computer?".format(name), "─"*8)


class User_inp:

    @staticmethod
    def collect_name():
        name = input("Please enter your name. ").upper()
        return name

    @staticmethod
    def user_move():  # Collect user move
        while True:
            move = ""
            move = input("Type field coordinates to put your 'X' (e.g. 'A2') ")
            move = move.upper()
            if len(move) != 2 or move[0] not in ("A", "B", "C") or move[1] not in (
                    "1", "2", "3"):  # Check if format is OK
                print("WRONG INPUT. TRY AGAIN.")
            elif board.check_field(move) != " ":  # Check if selected field is empty
                print("There is '{}' in this field. Please try again.".format(board.check_field(move)))
            else:
                return move  # e.g "A2"

    @staticmethod
    def who_start():  # Make user to chose if he wants to start
        while True:
            start = ""
            start = input("I will play with 'O' figure and you with 'X'.\n"
                          "Please type 'O' or 'X' to select who starts the game and confirm with 'Enter'. ").upper()
            if start not in ("O", "X"):
                print("WRONG INPUT. TRY AGAIN.")
            else:
                return start  # "O" or "X"


class Board:
    state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Keeps current game state
    field_coords = (
            "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")  # Coordinates of fields where index is field number
    lines = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
            (2, 4, 6))  # All possible lines

    def __init__(self, who_in):
        self.who = who_in

    def check_win(self):  # Check if there is a win (row of 3) or draw.

        if Board.state.count(" ") == 0:  # Check if there is a 'draw'.
            return "draw"

        for line in self.lines:  # check each possible line
            if Board.state[line[0]] == Board.state[line[1]] == Board.state[line[2]] in (
                    "X", "O"):  # Check if line has 3 equal values
                print("─" * 34, " '{0}' WIN!!! ".format(Board.state[line[0]]), "─" * 33)
                return Board.state[line[0]]  # Winner figure "X" or "O"

    def insert(self, coodrs):  # Insert figure to a filed
        Board.state[self.field_coords.index(coodrs)] = self.who

    def check_field(self, coodrs):  # Return value of selected field
        field = Board.state[self.field_coords.index(coodrs)]
        return field  # "X" or "O" or " "

    @staticmethod
    def empty_corner():  # Return list with empty corners
        corners = (0, 8, 2, 6)
        empty_cor = []
        for i in corners:
            if Board.state[i] == " ":
                empty_cor.append(i)
        return empty_cor  # list of empty corners

    @staticmethod
    def current_state():
        return Board.state  # List of field states


class Response:

    @staticmethod
    def response():  # Computer move

        state = Board.state

        o_move = Response.potential_win("O")  # Contains winning computer move

        if type(o_move) == int:  # Check if there is a computer win
            Board.state[o_move] = "O"

        empty_cor = Board.empty_corner()  # Obtain list of empty corners
        x_move = Response.potential_win("X")  # Check if there is a possibility for use win
        move_X_no = state.count("X")  # Number of user moves

        if move_X_no >= 2 and type(x_move) == int:  # If there is a risky line blok it
            Board.state[x_move] = "O"
        elif empty_cor:  # First "O"'s move in any corner
            Board.state[choice(empty_cor)] = "O"  # ...select random corner from empty_corner list

    @staticmethod
    def potential_win(who_in):

        state = Board.state  # Obtain current board state
        lines = Board.lines  # Obtain all lines
        potential_fields = []

        # Find empty fields in a line where 2 equal figures already are
        for line in lines:
            line_values = [state[line[0]], state[line[1]], state[line[2]]]

            # ↓ Check if line has 2 'X' or 'O' and 1 ' ' ↓
            if line_values.count(who_in) == 2 and line_values.count(" ") == 1:
                # ↓↓  Save number of empty field in a list  ↓↓
                potential_fields.append(line[line_values.index(" ")])

        if len(potential_fields) > 0:  # Return first empty field if it exists
            return potential_fields[0]  # Field index


"""Initialisation"""
user_inp = User_inp()  # create instance of user input
user_name = (user_inp.collect_name()).upper()

"""Whole game sequence"""
while True:
    board = Board("O")  # create instance of board
    display = Display("X")

    """Single game sequence"""

    print("\n" + "═" * 35, "\n     This is TIC TAC TOE game!     \n" + "═" * 35, "\n")

    start = user_inp.who_start()

    if start == "O":
        Response.response()  # First move by computer
        Display("O")
    else:
        Display("")  # Display empty board

    while True:  # Single game sequence

        inp = user_inp.user_move()  # Collect user move

        board.insert(inp)  # Insert user move to state array
        display = Display("X")

        win = board.check_win()
        if win in ("X", "O"):
            display.win_display("")
            break

        Response.response()  # Computer move
        display = Display("O")

        win = board.check_win()
        if win in ("X", "O"):
            display.win_display(user_name)
            break

    print("\nTry again")
