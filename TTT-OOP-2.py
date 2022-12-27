from random import choice
from collections import Counter

# from utils import method
# from dispaly import Display

"""GAME TIC TAC TOE"""

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


class Display:

    def __init__(self, last_move, board):
        self.board = board
        self.who = last_move
        self.display_board()

    def display_board(self):

        if self.who == "X":  # Select message to display
            message = "◀◀◀  ( X )  This is your move. "
        elif self.who == "O":
            message = "◀◀◀  ( O )  This is my move."
        else:
            message = "◀◀◀  This is our empty board"

        print("        A   B   C  ".format(self.board.state))
        print("      ╔═══╤═══╤═══╗")
        print("    1 ║ {0[0]:^{1}} │ {0[3]:^{1}} │ {0[6]:^{1}} ║".format(self.board.state, 1))
        print("      ╟───┼───┼───╢")
        print("    2 ║ {0[1]:^{1}} │ {0[4]:^{1}} │ {0[7]:^{1}} ║   {2}".format(self.board.state, 1, message))
        print("      ╟───┼───┼───╢")
        print("    3 ║ {0[2]:^{1}} │ {0[5]:^{1}} │ {0[8]:^{1}} ║".format(self.board.state, 1))
        print("      ╚═══╧═══╧═══╝")

    def win_message(self, name, win):  # Display a message about the winner
        if win == "X":
            print("Congratulations {}! You won with a very sophisticated Artificial Intelligence!\n"
                  "You are going to loose next time.".format(name))

        elif win == "O":
            print("I WON! {} You looser. Human beings' time is limited on this planet. Haaa haaa!!\n".format(name))

        elif win == 'draw':
            print("─" * 8, "DRAW!! {}, really?! You can not even afford to bit a computer?".format(name), "─" * 8)


class User_inp:
    def __init__(self):
        self.board = Board()

    @staticmethod
    def collect_name():
        name = input("Please enter your name. ").upper()
        return name

    def user_move(self):  # Collect user move
        while True:
            move = input("Type field coordinates to put your 'X' (e.g. 'A2') ")
            move = move.upper()
            if len(move) != 2 or move[0] not in ("A", "B", "C") or move[1] not in (
                    "1", "2", "3"):  # Check if format is OK
                print("WRONG INPUT. TRY AGAIN.")
            elif self.board.check_field(move) != " ":  # Check if selected field is empty
                print("There is '{}' in this field. Please try again.".format(self.board.check_field(move)))
            else:
                return move  # e.g "A2"

    @staticmethod
    def who_start():  # Make user to chose if he wants to start
        while True:
            start = input("I will play with 'O' figure and you with 'X'.\n"
                          "Please type 'O' or 'X' to select who starts the game and confirm with 'Enter'. ").upper()
            if start not in ("O", "X"):
                print("WRONG INPUT. TRY AGAIN.")
            else:
                return start  # "O" or "X"


class Board:
    STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Keeps initial game state
    FIELD_COORDS = (
            "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")  # Coordinates of fields where index is field number
    LINES = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
            (2, 4, 6))  # All possible LINES

    def __init__(self):
        self.state = Board.STATE

    def check_win(self):  # Check if there is a win (row of 3) or draw.

        def x_or_o():
            for line in self.LINES:  # check each possible line
                if self.state[line[0]] == self.state[line[1]] == self.state[line[2]] in (
                        "X", "O"):  # Check if line has 3 equal values
                    print("─" * 34, " '{0}' WON!!! ".format(self.state[line[0]]), "─" * 33)
                    return self.state[line[0]]  # Winner figure "X" or "O"

        if self.state.count(" ") == 0 and not x_or_o():  # Check if there is a 'draw'.
            return "draw"
        else:
            return x_or_o()

    def insert(self, coodrs, who):  # Insert figure to a filed
        self.state[self.FIELD_COORDS.index(coodrs)] = who

    def check_field(self, coodrs):  # Return value of selected field
        field = self.state[self.FIELD_COORDS.index(coodrs)]
        return field  # "X" or "O" or " "

    def empty_corner(self):  # Return list with empty corners
        corners = (0, 8, 2, 6)
        empty_cor = []
        for i in corners:
            if self.state[i] == " ":
                empty_cor.append(i)
        return empty_cor  # list of empty corners

    def current_state(self):
        return self.state  # List of field states

    def reset_board(self):
        Board.STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


class Response:

    @staticmethod
    def response(board):  # Computer move
        lines = Board.LINES
        state = board.state
        o_move = Response.potential_win("O", state)  # Contains winning computer move

        def two_lines():  # Find empty field where adding "O" would create 2 lines of 2x "O" and 1x " "
            temp = []
            for line in lines:  # Check each line...
                line_values = [state[line[0]], state[line[1]], state[line[2]]]
                if line_values.count("O") == 1 and line_values.count(" ") == 2:  # ...if line has 1x "O" and 2x " "...
                    for i in line:
                        if state[i] == " ":  # ...add index of each empty field to the 'temp' list.
                            temp.append(i)
            data = Counter(temp)  # Find the most common field index in 'temp'
            state[(data.most_common(1)[0][0])] = "O"

        def two_fields():  # Check if "O" in the corner neighbors with "X" is in center of outer lines
            outer_lines = [lines[0], lines[2], lines[3], lines[5], ]
            for line in outer_lines:
                if line[1] == "X" and line[0] == "O" and line[2] == " " or line[0] == " " and line[2] == "X":
                    return True
                else:
                    return False

        """Check if "O" wins now"""
        if type(o_move) == int:  # Check if there is a computer win
            state[o_move] = "O"
            return

        """Next move"""
        empty_cor = board.empty_corner()  # Obtain list of empty corners
        x_move = Response.potential_win("X", state)  # Check if there is a possibility for use win
        move_X_no = state.count("X")  # Number of user moves

        if move_X_no >= 2 and type(x_move) == int:  # If there is a risky line blok it
            state[x_move] = "O"
            print(1)
            return

        elif move_X_no == 1 and state.index("X") in (1, 3, 5, 7):  # if "X" in a center of the outer line...
            state[4] = "O"  # ...put "O" in the center
            print(2)
            return

        elif move_X_no <= 1 and empty_cor:  # "O"'s first move in any corner and 2nd move in an opposite corner
            print(555)
            if state[4] in ("O", "X"):  # if "O" in center field
                print(444)
                for diagonal in ([0, 8], [2, 6]):  # check corners in two diagonal lines
                    for i in range(2):
                        if state[diagonal[i]] in ("O", "X"):  # put "O" to opposite corner if other has "O" already
                            state[diagonal[i - 1]] = "O"
                            print(3)
                            return
                state[choice(empty_cor)] = "O"  # put "O" in random corner from empty_corner list
                print(4)
                return
            state[choice(empty_cor)] = "O"  # put "O" in random corner from empty_corner list
            print(4)
            return

        elif state.count(" ") == 1:  # The last move in empty field
            state[state.index(" ")] = "O"
            print(5)
            return

        elif state.count(" ") == 2:  # Penultimate move
            state[state.index(" ")] = "O"
            print(6)

        else:
            two_lines()
            print(7)
            return

    @staticmethod
    def potential_win(who_in, state):

        LINES = Board.LINES  # Obtain all LINES
        potential_fields = []

        # Find empty fields in a line where 2 equal figures already are
        for line in LINES:
            line_values = [state[line[0]], state[line[1]], state[line[2]]]

            # ↓ Check if line has 2 'X' or 'O' and 1 ' ' ↓
            if line_values.count(who_in) == 2 and line_values.count(" ") == 1:
                # ↓↓  Save number of empty field in a list  ↓↓
                potential_fields.append(line[line_values.index(" ")])

        if len(potential_fields) > 0:  # Return first empty field if it exists
            return potential_fields[0]  # Field index


def main():

    """INITIALISATION"""

    user_name = (User_inp().collect_name()).upper()
    game_counter = 0  # Keeps no. of games
    score = [0, 0, 0]  # Keeps score of all rounds ["X", "O"]
    game_start = [0, 0]  # No. of rounds started by each player ["X", "O"]

    """WHOLE GAME SEQUENCE"""

    while True:
        board = Board()  # create instance of board
        user_inp = User_inp()  # create instance of user input
        display = Display("", board)
        game_counter += 1

        """SINGLE GAME SEQUENCE"""

        print("\n" + "═" * 35, "\n     This is TIC TAC TOE game!     \n" + "═" * 35, "\n")

        start = user_inp.who_start()

        if start == "O":
            Response.response(board)  # First move by computer
            Display("O", board)  # Display computer move
            game_start[1] += 1
        else:
            game_start[0] += 1

        while True:

            """USER MOVE"""
            inp = user_inp.user_move()  # Collect user move e.g. "A2"

            board.insert(inp, "X")  # Insert user move to state array
            display = Display("X", board)

            win = board.check_win()
            if win:
                display.win_message(user_name, win)
                board.reset_board()
                if win == "X":
                    score[0] += 1
                elif win == "draw":
                    score[2] += 1
                break

            """COMP MOVE"""
            Response.response(board)  # Computer move

            win = board.check_win()
            display = Display("O", board)
            if win:
                display.win_message(user_name, win)
                board.reset_board()
                if win == "O":
                    score[1] += 1
                elif win == "draw":
                    score[2] += 1
                break

        print("We have played {} rounds and the current result is:".format(game_counter))
        print("           {0:^15}  {1:^15}  {2:^15}".format(user_name, "COMPUTER", "DRAW"))
        print("Wins       {0:^15}  {1:^15}  {2:^15}".format(score[0], score[1], score[2]))
        print("Starts game{0:^15}  {1:^15}\n".format(game_start[0], game_start[1]))

        while not input("Press Enter to continue."):
            break


if __name__ == "__main__":
    main()
