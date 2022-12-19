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

from random import choice
name = input("Please enter your name. ").upper()
field_coords = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")  # Coordinates of files where index is field number
lines = ((0, 1, 2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))  # All possible lines

while True:
    state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Keeps current game state
    who = ""  # Contain info about recent player

    def display(state, who):  # Display game result

        if who == "X":
            who = "◀   This is your move."
        elif who == "O":
            who = "◀◀◀◀◀◀   This is my move."
        else:
            who = "◀◀◀  This is our empty board"

        print("        A   B   C  ".format(state))
        print("      ╔═══╤═══╤═══╗")
        print("    1 ║ {0[0]:^{1}} │ {0[3]:^{1}} │ {0[6]:^{1}} ║".format(state, 1))
        print("      ╟───┼───┼───╢")
        print("    2 ║ {0[1]:^{1}} │ {0[4]:^{1}} │ {0[7]:^{1}} ║   {2}".format(state, 1, who))
        print("      ╟───┼───┼───╢")
        print("    3 ║ {0[2]:^{1}} │ {0[5]:^{1}} │ {0[8]:^{1}} ║".format(state, 1))
        print("      ╚═══╧═══╧═══╝\n")


    def check_win(win):  # Check if there is a win (row of 3) or draw.

        if state.count(" ") == 0:  # Check if there is a 'draw'.
            return "draw"

        for i in lines:  # check each possible line
            if state[i[0]] == state[i[1]] == state[i[2]] in ("X", "O"):  # Check if line has 3 equal values
                print("─"*34, " '{0}' WIN!!! ".format(win), "─"*33)
                return win


    def insert(who, inp):  # Insert input to a filed
        state[field_coords.index(inp)] = who
        return state, who


    def check_field(inp):  # Return value of selected field
        field = state[field_coords.index(inp)]
        return field


    def user_inp():  # Collect user move
        while True:
            inp = ""
            inp = input("Type field coordinates to put your 'X' (e.g. 'A2') ")
            inp = inp.upper()
            if len(inp) != 2 or inp[0] not in ("A", "B", "C") or inp[1] not in ("1", "2", "3"):  # Check if format is OK
                print("WRONG INPUT. TRY AGAIN.")
            elif check_field(inp) != " ":  # Check if selected field is empty
                print("There is '{}' in this field. Please try again.".format(check_field(inp)))
            else:
                return inp


    def who_start():  # Make user to chose if he wants to start
        while True:
            start = ""
            start = input("I will play with 'O' figure and you with 'X'.\n"
                          "Please type 'O' or 'X' to select who starts the game and confirm with 'Enter'. ").upper()
            if start not in ("O", "X"):
                print("WRONG INPUT. TRY AGAIN.")
            else:
                return start


    def empty_corner(state):  # Return list with empty corners
        corners = (0,8,2,6)
        empty_cor = []
        for i in corners:
            if state[i] == " ":
                empty_cor.append(i)
        return empty_cor


    def response(state):  # Computer move

        o_move= potential_win("O")  # Contains winning computr move

        if type(o_move) == int: # Check if there is a computer win
            state[o_move] = "O"
            return state, "O"

        empty_cor = empty_corner(state)  # Create list of empty corners
        x_move = potential_win("X")  # Check if there is a possibility for use win
        move_X_no = state.count("X")  # Number of user moves

        if move_X_no >= 2 and type(x_move) == int:  # If there is a risky line blok it
            state[x_move] = "O"
        elif empty_cor:  # Firsto_movein any corner
            state[choice(empty_cor)] = "O"  # ...select random corner from empty_corner list

        return state, "O"


    def potential_win(who):

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


    """Single game sequence"""

    print("\n"+"═" * 35, "\n     This is TIC TAC TOE game!     \n" + "═" * 35, "\n")

    start = who_start()

    if start == "O":
        response(state)
        display(state, "O")
    else:
        display(state, "")  # Display empty board

    while True:  # Single game sequence

        inp = user_inp()  # Collect user move

        state, who = insert("X", inp)  # Insert user move to state array
        display(state, who)  # Display board after user move
        win = check_win(who)  # Check if there is user win
        if win == "X":
            print("You won with a very sophisticated Artificial Intelligence! Congratulations!!\n"
                  "You are going to loose next time.")
            break
        elif win == "draw":
            print("─"*8, "DRAW!! {0}, really?! You can not even afford to bit a computer?".format(name), "─"*8)
            break

        state, who = response(state)  # Computer move

        display(state, who)  # Display board after computer move

        win = check_win(who)  # Check if there is computer win
        if win == "O":
            print("I WON! {0} You looser. Human beings' time is limited on this planet. Haaa haaa!!\n".format(name))
            break
        elif win == "draw":
            print("─"*8, "DRAW!! I didn't get crazy too much this time.", "─"*8)
            break

    print("\nTry again")


