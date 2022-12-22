from random import choice

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

    def __init__(self, who_in, board):
        self.board = board
        self.who = who_in
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
        print("      ╚═══╧═══╧═══╝\n")

    def win_message(self, name):  # Display a message about the winner
        if self.who == "X":
            print("You won with a very sophisticated Artificial Intelligence! Congratulations!!\n"
                  "You are going to loose next time.")

        elif self.who == "O":
            print("I WON! {0} You looser. Human beings' time is limited on this planet. Haaa haaa!!\n".format(name))

        elif self.who == 'draw':
            print("─" * 8, "DRAW!! {0}, really?! You can not even afford to bit a computer?".format(name), "─" * 8)


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
    STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Keeps current game state
    print("board")
    field_coords = (
            "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")  # Coordinates of fields where index is field number
    lines = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
            (2, 4, 6))  # All possible lines

    def __init__(self):
        self.state = Board.STATE
        pass

    def check_win(self):  # Check if there is a win (row of 3) or draw.

        if self.state.count(" ") == 0:  # Check if there is a 'draw'.
            return "draw"

        for line in self.lines:  # check each possible line
            if self.state[line[0]] == self.state[line[1]] == self.state[line[2]] in (
                    "X", "O"):  # Check if line has 3 equal values
                print("─" * 34, " '{0}' WIN!!! ".format(self.state[line[0]]), "─" * 33)
                return self.state[line[0]]  # Winner figure "X" or "O"

    def insert(self, coodrs, who):  # Insert figure to a filed
        self.state[self.field_coords.index(coodrs)] = who

    def check_field(self, coodrs):  # Return value of selected field
        field = self.state[self.field_coords.index(coodrs)]
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
        self.state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


class Response:

    @staticmethod
    def response(board):  # Computer move

        state = board.state
        o_move = Response.potential_win("O", state)  # Contains winning computer move

        if type(o_move) == int:  # Check if there is a computer win
            state[o_move] = "O"

        empty_cor = board.empty_corner()  # Obtain list of empty corners
        x_move = Response.potential_win("X", state)  # Check if there is a possibility for use win
        move_X_no = state.count("X")  # Number of user moves

        if move_X_no >= 2 and type(x_move) == int:  # If there is a risky line blok it
            state[x_move] = "O"
        # elif move_X_no >= 2 and Board.state[4] == " ":
        #     Board.state[4] = "O"
        elif empty_cor:  # First "O"'s move in any corner
            state[choice(empty_cor)] = "O"  # ...select random corner from empty_corner list
        elif state.index(" "):
            state[state.index(" ")] = "O"

    @staticmethod
    def potential_win(who_in, state):

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
            print(potential_fields)
            return potential_fields[0]  # Field index


def main():

    """INITIALISATION"""

    user_inp = User_inp()  # create instance of user input
    user_name = (user_inp.collect_name()).upper()
    game_counter = 0  # Keeps no. of games
    score = [0, 0]  # Keeps score of all rounds ["X", "O"]
    game_start = [0, 0]  # No. of rounds started by each player ["X", "O"]

    """WHOLE GAME SEQUENCE"""

    while True:
        board = Board()  # create instance of board
        display = Display("", board)
        game_counter += 1

        """SINGLE GAME SEQUENCE"""

        print("\n" + "═" * 35, "\n     This is TIC TAC TOE game!     \n" + "═" * 35, "\n")

        start = user_inp.who_start()

        if start == "O":
            Response.response(board)  # First move by computer
            Display("O")  # Display computer move
            game_start[1] += 1
        else:
            game_start[0] += 1

        while True:

            """USER MOVE"""
            inp = user_inp.user_move()  # Collect user move e.g. "A2"

            board.insert(inp, "X")  # Insert user move to state array
            display = Display("X", board)

            win = board.check_win()
            print("WIN", win)
            if win:
                display.win_message(user_name)
                board.reset_board()
                if win == "X":
                    score[0] += 1
                break

            """COMP MOVE"""
            Response.response(board)  # Computer move
            display = Display("O", board)

            win = board.check_win()
            if win:
                display.win_message("")
                board.reset_board()
                if win == "O":
                    score[1] += 1
                break

        print("\nTry again\n")
        print("We have played {} rounds and the current result is:".format(game_counter))
        print("           {0:^15}  {1:^15}".format(user_name, "COMPUTER"))
        print("Wins       {0:^15}  {1:^15}".format(score[0], score[1]))
        print("Starts game{0:^15}  {1:^15}\n".format(game_start[0], game_start[1]))

        while not input("Press Enter to continue."):
            break


if __name__ == "__main__":
    main()
