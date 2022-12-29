
class BoardPrinter:

    def __init__(self, last_move, board):
        self.board = board
        self.who = last_move

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


class Messenger:
    def __init__(self, who, name):
        self.who = who
        self.name = name

    def win_message(self):  # BoardPrinter a message about the winner
        if self.who == "X":
            print("Congratulations {}! You won with a very sophisticated Artificial Intelligence!\n"
                  "You are going to loose next time.".format(self.name))

        elif self.who == "O":
            print("I WON! {} You looser. Human beings' time is limited on this planet. Haaa haaa!!\n".format(self.name))

        elif self.who == 'draw':
            print("─" * 8, "DRAW!! {}, really?! You can not even afford to bit a computer?".format(self.name), "─" * 8)

