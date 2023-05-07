
def collect_name():  # Collect User name
    name = input("Please enter your name. ").upper()
    return name


def who_start():  # Make User to chose who starts a game 'x' or 'o'
    while True:
        start = input("I will play with 'O' figure and you with 'X'.\n"
                      "Please type 'O' or 'X' to select who starts the game and confirm with 'Enter'. ").upper()
        if start not in ("O", "X"):
            print("WRONG INPUT. TRY AGAIN.")
        else:
            return start  # "O" or "X"


def user_move(board):  # Collect user move
    while True:
        move = input("Type field coordinates to put your 'X' (e.g. 'A2') ")
        move = move.upper()
        if len(move) != 2 or move[0] not in ("A", "B", "C") or move[1] not in (
                "1", "2", "3"):  # Check if format is OK
            print("WRONG INPUT. TRY AGAIN.")
        elif board.check_field(move) != " ":  # Check if selected field is empty
            print("There is '{}' in this field. Please try again.".format(board.check_field(move)))
        else:
            return move  # e.g "A2"
