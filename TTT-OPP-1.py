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
response_no = 0  # Computer moves counter


class Display:

    def __init__(self, who_in=" "):
        self.state = Board.state
        self.who = who_in

    def show(self):
        if self.who == "X":
            self.who = "◀   This is your move. ( X )"
        elif self.who == "O":
            self.who = "◀◀◀◀◀◀   This is my move. ( O )"
        else:
            self.who = "◀◀◀  This is our empty board"

        print("        A   B   C  ".format(self.state))
        print("      ╔═══╤═══╤═══╗")
        print("    1 ║ {0[0]:^{1}} │ {0[3]:^{1}} │ {0[6]:^{1}} ║".format(self.state, 1))
        print("      ╟───┼───┼───╢")
        print("    2 ║ {0[1]:^{1}} │ {0[4]:^{1}} │ {0[7]:^{1}} ║   {2}".format(self.state, 1, self.who))
        print("      ╟───┼───┼───╢")
        print("    3 ║ {0[2]:^{1}} │ {0[5]:^{1}} │ {0[8]:^{1}} ║".format(self.state, 1))
        print("      ╚═══╧═══╧═══╝\n")


class Board:
    state = [" ", "X", " ", " ", " ", " ", " ", " ", " "]  # Keeps current game state
    field_coords = (
    "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")  # Coordinates of files where index is field number
    lines = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # All possible lines

    def __init__(self, who_in):
        self.state = Board.state
        self.who = who_in

    def check_win(self):  # Check if there is a win (row of 3) or draw.

        if self.state.count(" ") == 0:  # Check if there is a 'draw'.
            return "draw"

        for i in self.lines:  # check each possible line
            if self.state[i[0]] == self.state[i[1]] == self.state[i[2]] in ("X", "O"):  # Check if line has 3 equal values
                print("─" * 34, " '{0}' WIN!!! ".format(self.who), "─" * 33)
                return self.who

    def insert(self, coodrs):  # Insert input to a filed
        self.state[self.field_coords.index(coodrs)] = self.who
        return self.state, self.who

    def check_field(self, coodrs):  # Return value of selected field
        field = self.state[self.field_coords.index(coodrs)]
        return field

    def empty_corner(self):  # Return list with empty corners
        corners = (0,8,2,6)
        empty_cor = []
        for i in corners:
            if self.state[i] == " ":
                empty_cor.append(i)
        return empty_cor

    def current_state(self):
        return self.state
    dupa = 2

board = Board(who)
disp = Display(board.current_state())

print(board.check_field("A2"))
print(board.empty_corner())
board = Board("O")
disp.show()
board.insert("C1")
disp.show()
print(board.current_state())


class User_inp:

    def collect_name(self):
        name = input("Please enter your name. ").upper()

    def user_move(self):  # Collect user move
        while True:
            move = ""
            move = input("Type field coordinates to put your 'X' (e.g. 'A2') ")
            move = move.upper()
            if len(move) != 2 or move[0] not in ("A", "B", "C") or move[1] not in ("1", "2", "3"):  # Check if format is OK
                print("WRONG INPUT. TRY AGAIN.")
            elif check_field(move) != " ":  # Check if selected field is empty
                print("There is '{}' in this field. Please try again.".format(check_field(move)))
            else:
                return move

    def who_start(self):  # Make user to chose if he wants to start
        while True:
            start = ""
            start = input("I will play with 'O' figure and you with 'X'.\n"
                          "Please type 'O' or 'X' to select who starts the game and confirm with 'Enter'. ").upper()
            if start not in ("O", "X"):
                print("WRONG INPUT. TRY AGAIN.")
            else:
                return start


class Response:

    def response(self, state):  # Computer move

        o_move= Response.potential_win(self, "O")  # Contains winning computr move

        if type(o_move) == int: # Check if there is a computer win
            state[o_move] = "O"
            return state, "O"

        empty_cor = empty_corner(state)  # Create list of empty corners
        x_move = Response.potential_win(self, "X")  # Check if there is a possibility for use win
        move_X_no = state.count("X")  # Number of user moves
        move_O_no = state.count("O")  # Number of computer moves

        if move_X_no >= 2 and type(x_move) == int:  # If there is a risky line blok it
            state[x_move] = "O"
        elif empty_cor:  # Firsto_movein any corner
            state[choice(empty_cor)] = "O"  # ...select random corner from empty_corner list

        return state, "O"


    def potential_win(self, who):

        potential_fields = []

        # Block lines where 2 Xes are already
        for line in lines:
            line_values = [state[line[0]], state[line[1]], state[line[2]]]

            # ↓ Check if line has 2 'X' or 'O' and 1 ' ' ↓
            if line_values.count(who) == 2 and line_values.count(" ") == 1:
                # ↓↓  Save number of empty field  ↓↓
                potential_fields.append(line[line_values.index(" ")])

        if len(potential_fields) > 0:  # Return first empty field if it exist
            return potential_fields[0]







# while True:
#
#
#     """Single game sequence"""
#
#     print("\n"+"═" * 35, "\n     This is TIC TAC TOE game!     \n" + "═" * 35, "\n")
#
#     start = who_start()
#
#     if start == "O":
#         response(state)
#         display(state, "O")
#     else:
#         display(state, "")  # Display empty board
#
#     while True:  # Single game sequence
#
#         inp = user_inp()  # Collect user move
#
#         state, who = insert("X", inp)  # Insert usero_moveto state array
#         display(state, who)  # Display board after user move
#         win = check_win(who)  # Check if there is user win
#         if win == "X":
#             print("You won with a very sophisticated Artificial Intelligence! Congratulations!!\n"
#                   "You are going to loose next time.")
#             break
#         elif win == "draw":
#             print("─"*8, "DRAW!! {0}, really?! You can not even afford to bit a computer?".format(name), "─"*8)
#             break
#
#         state, who = response(state)  # Computer move
#
#         display(state, who)  # Display board after computer move
#
#         win = check_win(who)  # Check if there is computer win
#         if win == "O":
#             print("I WON! {0} You looser. Human beings' time is limited on this planet. Haaa haaa!!\n".format(name))
#             break
#         elif win == "draw":
#             print("─"*8, "DRAW!! I didn't get crazy too much this time.", "─"*8)
#             break
#
#     print("\nTry again")


