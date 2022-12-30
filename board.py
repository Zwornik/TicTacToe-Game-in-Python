"""GAME TIC TAC TOE

Fields numbering
   A   B   C
  ╔═══╤═══╤═══╗
1 ║ O │ 3 │ 6 ║
  ╟───┼───┼───╢
2 ║ 1 │ 4 │ 7 ║
  ╟───┼───┼───╢
3 ║ 2 │ 5 │ 8 ║
  ╚═══╧═══╧═══╝

'X' - User figure
'O' - Computer figure"""


class Board:
    STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Keeps initial game state
    FIELD_COORDS = (
            "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")  # Coordinates of fields where index is a field number
    LINES = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
            (2, 4, 6))  # All possible LINES

    def __init__(self):
        self.state = self.set_board()

    def set_board(self):
        return Board.STATE.copy()
    
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

    def current_state(self):  # Service method, normally not used
        return self.state  # List of field states

    def reset_board(self):
        # Board.STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.state = self.set_board()

