
from utils import collect_name, who_start, user_move
from display import Display
from board import Board
from response import Response

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


def main():
    """INITIALISATION"""

    user_name = (collect_name()).upper()
    game_counter = 0  # Keeps no. of games
    score = [0, 0, 0]  # Keeps score of all rounds ["X", "O", DRAWS]
    game_start = [0, 0]  # No. of rounds started by each player ["X", "O"]

    """WHOLE GAME SEQUENCE"""

    while True:
        board = Board()  # create instance of board
        display = Display("", board, user_name)
        game_counter += 1

        def win_score(win):
            display.win_message()
            if win:
                if win == "X":
                    score[0] += 1
                elif win == "O":
                    score[1] += 1
                elif win == "draw":
                    score[2] += 1

        """SINGLE GAME SEQUENCE"""

        print("\n" + "═" * 35, "\n     This is TIC TAC TOE game!     \n" + "═" * 35, "\n")

        start = who_start()

        if start == "O":
            Response.response(board)  # First move by computer
            Display("O", board, user_name)  # Display computer move
            game_start[1] += 1
        else:
            game_start[0] += 1

        while True:

            """USER MOVE"""
            move = user_move()  # Collect user move e.g. "A2"

            board.insert(move, "X")  # Insert user move to state array
            display = Display("X", board, user_name)

            win = board.check_win()
            if win:
                win_score(win)
                board.reset_board()
                break

            """COMP MOVE"""
            Response.response(board)  # Computer move

            display = Display("O", board, user_name)
            win = board.check_win()
            if win:
                win_score(win)
                board.reset_board()
                break

        print("We have played {} rounds and the current result is:".format(game_counter))
        print("           {0:^15}  {1:^15}  {2:^15}".format(user_name, "COMPUTER", "DRAW"))
        print("Wins       {0:^15}  {1:^15}  {2:^15}".format(score[0], score[1], score[2]))
        print("Starts game{0:^15}  {1:^15}\n".format(game_start[0], game_start[1]))

        while not input("Press Enter to continue."):
            break


if __name__ == "__main__":
    main()
