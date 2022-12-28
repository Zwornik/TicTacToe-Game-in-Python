from random import choice
from collections import Counter

from board import Board


class Response:

    @staticmethod
    def response(board):  # Computer move
        lines = board.LINES
        state = board.state
        o_move = Response.potential_win("O", state)  # Contains winning computer move

        def two_lines(who, level):  # Find empty field where adding "O" would create 2 lines of 2x "O" and
                        # 1x " ". It does the same for "X" in recurrent run if there is no two lines for "O".
            empty = []  # Contain list of empty fields with potential to create a line.
            level += 1  # Recursion level
            for line in lines:  # Check each line...
                line_values = [state[line[0]], state[line[1]], state[line[2]]]
                if line_values.count(who) == 1 and line_values.count(" ") == 2:  # ...if line has 1x "O" and 2x " "...
                    for i in line:
                        if state[i] == " ":  # ...add index of each empty field to the 'empty' list.
                            empty.append(i)
            empty_indexes = Counter(empty)  # Find the most common field index in 'empty'
            print(level, empty_indexes)
            if not all(val == 1 for val in empty_indexes.values()):  # If there is empty field appearing more than 1...
                state[(empty_indexes.most_common(1)[0][0])] = "O"  # ...put "O" there
                print("222")
                return True  # True if state was modified by this function
            elif level == 2:  # Return in recursion level is 2
                print("111")
                return False  # True if state was NOT modified by this function
            print("recursion")
            two_lines("X", level)  # Recursive check for "X"

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
            return

        else:
            two = two_lines("O", 0)
            print(7777, two)
            if two != True:
                state[state.index(" ")] = "O"
                print(8)
            return

    @staticmethod
    def potential_win(who_in, state):

        lines = Board.LINES  # Obtain all LINES
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

