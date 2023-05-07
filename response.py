from random import choice
from collections import Counter

class Response:

    def __init__(self, board):
        self.board = board
        self.lines = board.LINES
        self.state = board.state
        self.corners = board.CORNERS
        self.out_centers = board.OUT_CENTERS

    def corner_put(self,
                   empty_cor):  # "O" to empty corner or if central field is taken diagonally opposite to that field
        if self.state[4] in ("O", "X"):  # if "O" in center field
            print(444)
            for diagonal in ([0, 8], [2, 6]):  # check corners in two diagonal lines
                for i in range(2):
                    if self.state[diagonal[i]] in ("O", "X"):  # put "O" to opposite corner if other has "O" already
                        self.state[diagonal[i - 1]] = "O"
                        print(3)
                        return
        self.state[choice(empty_cor)] = "O"  # put "O" in random corner from empty_corner list
        print(4)
        return

    def response(self):  # Computer move

        o_move = self.potential_win("O")  # Contains winning computer move

        """Check if "O" wins now"""
        if type(o_move) == int:  # Check if there is a computer win
            self.state[o_move] = "O"
            return

        """Next move"""
        empty_cor = self.board.empty_corner()  # Obtain list of empty corners
        x_move = self.potential_win("X")  # Check if there is a possibility for use win
        move_X_no = self.state.count("X")  # Number of user moves
        move_O_no = self.state.count("O")  # Number of computer moves

        if move_X_no >= 2 and type(x_move) == int:  # If there is a risky line blok it
            self.state[x_move] = "O"
            print(1)
            return

        elif move_X_no == 1 and move_O_no == 0 and self.state[4] == " ":  # if "X" in a center of the outer line...
            self.state[4] = "O"  # ...put "O" in the center
            print(2)
            return

        # If "O" in center and "X" in corner
        elif move_X_no == 2 and move_O_no == 1 and self.state[4] == "O" and \
            "X" in (self.state[self.corners[0]], self.state[self.corners[1]],
                    self.state[self.corners[2]], self.state[self.corners[3]]):
            x_in_center = False  # Flag, True if "X" in center of outer line
            line = ()
            for line in self.lines[0:3]:  # line in outer lines
                if self.state[line[1]] == "X":  # if "X" in center of outer line
                    x_in_center = line
                    break

            if x_in_center:  # if "X" in center of outer line
                self.two_lines("O", 0)  # Find common empty field for several lines
            else:
                self.state[line[1]] = "O"  # Put "O"
                return

        elif move_X_no <= 1 and empty_cor:  # "O"'s first move in any corner and 2nd move in an opposite corner
            print(555)
            self.corner_put(empty_cor)
            return

        elif self.state.count(" ") == 1:  # The last move in empty field
            self.state[self.state.index(" ")] = "O"
            print(5)
            return

        elif self.state.count(" ") == 2:  # Penultimate move
            self.state[self.state.index(" ")] = "O"
            print(6)
            return

        else:
            two = self.two_lines("O", 0)
            print(7777, two)
            if not two:
                self.state[self.state.index(" ")] = "O"
                print(8)
            return

    def two_lines(self, who, level):  # Find empty field where adding "O" would create 2 lines of 2x "O" and
        # 1x " ". It does the same for "X" in recurrent run if there is no two lines for "O".

        empty = []  # Contain list of empty fields with potential to create a line.
        level += 1  # Recursion level
        for line in self.lines:  # Check each line...
            line_values = [self.state[line[0]], self.state[line[1]], self.state[line[2]]]
            if line_values.count(who) == 1 and line_values.count(" ") == 2:  # ...if line has 1x "O" and 2x " "...
                for i in line:
                    if self.state[i] == " ":  # ...add index of each empty field to the 'empty' list.
                        empty.append(i)
        empty_indexes = Counter(empty)  # Find the most common field index in 'empty'
        print(level, empty_indexes)
        if not all(val == 1 for val in empty_indexes.values()):  # If there is empty field appearing more than 1...
            self.state[(empty_indexes.most_common(1)[0][0])] = "O"  # ...put "O" there
            print("222")
            checked = True
            return checked  # True if state was modified by this function
        elif level == 2:  # Return in recursion level is 2
            print("111")
            checked = False
            return checked  # True if state was NOT modified by this function
        print("recursion")
        return self.two_lines("X", level)  # Recursive check for "X"

    def potential_win(self, who_in):

        potential_fields = []  # Keeps indexes of fields that can create lines

        # Find empty fields in a line where 2 equal figures already are
        for line in self.lines:
            line_values = [self.state[line[0]], self.state[line[1]], self.state[line[2]]]

            # ↓ Check if line has 2 'X' or 'O' and 1 ' ' ↓
            if line_values.count(who_in) == 2 and line_values.count(" ") == 1:
                # ↓↓  Save number of empty field in a list  ↓↓
                potential_fields.append(line[line_values.index(" ")])

        if len(potential_fields) > 0:  # Return first empty field if it exists
            return potential_fields[0]  # Field index
