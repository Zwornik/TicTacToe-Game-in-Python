"""Game Tic Toc Toe"""

from random import choice

while True:
    state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Keeps current game state
    temp_state = ["", "", "", "", "", "", "", "", ""]
    who = ""


    def display(state, move):  # Display game result

        if move == "X":
            move = "◀   This is your move"
        elif move == "O":
            move = "◀◀◀   This is my response"
        else:
            move = ""

        print("        A   B   C  ".format(state))
        print("      ╔═══╤═══╤═══╗")
        print("    1 ║ {0[0]:^{1}} │ {0[3]:^{1}} │ {0[6]:^{1}} ║".format(state, 1))
        print("      ╟───┼───┼───╢")
        print("    2 ║ {0[1]:^{1}} │ {0[4]:^{1}} │ {0[7]:^{1}} ║   {2}".format(state, 1, move))
        print("      ╟───┼───┼───╢")
        print("    3 ║ {0[2]:^{1}} │ {0[5]:^{1}} │ {0[8]:^{1}} ║".format(state, 1))
        print("      ╚═══╧═══╧═══╝\n")


    def check_win(state, win):  # Check if there is a win (row of 3)
        if state[0] == state[1] == state[2] in ("X", "O") or \
                state[3] == state[4] == state[5] in ("X", "O") or \
                state[6] == state[7] == state[8] in ("X", "O") or \
                state[0] == state[3] == state[6] in ("X", "O") or \
                state[1] == state[4] == state[7] in ("X", "O") or \
                state[2] == state[5] == state[8] in ("X", "O") or \
                state[0] == state[4] == state[8] in ("X", "O") or \
                state[2] == state[4] == state[6] in ("X", "O"):
            return win


    def user_inp():  # Collect user move
        while True:
            inp = ""
            inp = input("Type field coordinates to put the 'X' (e.g. 'A2') ")
            inp = inp.upper()
            if len(inp) != 2 or inp[0] not in ("A", "B", "C") or inp[1] not in ("1", "2", "3"):  # Check if format is OK
                print("WRONG INPUT. TRY AGAIN.")
            elif check_field(state, inp) != " ":  # Check if selected field is empty
                print("There is '{}' in this field. Please try again.".format(check_field(state, inp)))
            else:
                return inp


    def insert(state, who, inp):  # Insert input to a filed
        if inp == "A1": state[0] = who
        if inp == "A2": state[1] = who
        if inp == "A3": state[2] = who
        if inp == "B1": state[3] = who
        if inp == "B2": state[4] = who
        if inp == "B3": state[5] = who
        if inp == "C1": state[6] = who
        if inp == "C2": state[7] = who
        if inp == "C3": state[8] = who
        return state, who


    def check_field(state, inp):  # Return value of selected field
        field = " "
        if inp == "A1": field = state[0]
        if inp == "A2": field = state[1]
        if inp == "A3": field = state[2]
        if inp == "B1": field = state[3]
        if inp == "B2": field = state[4]
        if inp == "B3": field = state[5]
        if inp == "C1": field = state[6]
        if inp == "C2": field = state[7]
        if inp == "C3": field = state[8]
        return field


    def empty_corner(state):  # Return list with empty corners
        empty_cor = []
        if state[0] == " ":
            empty_cor.append(0)
        elif state[2] == " ":
            empty_cor.append(2)
        elif state[6] == " ":
            empty_cor.append(6)
        elif state[8] == " ":
            empty_cor.append(8)
        return empty_cor


    def response(state):  # Computer move
        empty_cor = empty_corner(state)
        if state[4] == " ":  # First move in the central field
            state[4] = "O"
        elif empty_cor:  # Check if empty_cor has elements
            state[choice(empty_cor)] = "O"  # Select random corner from empty_corner list
        return state, "O"


    def potential_win(state):
        for line in [[state[0], state[1], state[2]],
                     [state[3], state[4], state[5]],
                     [state[6], state[7], state[8]],
                     [state[0], state[3], state[6]],
                     [state[1], state[4], state[7]],
                     [state[2], state[5], state[8]],
                     [state[0], state[4], state[8]],
                     [state[2], state[4], state[6]], ]:

            if line.count("X") == 2 and line.count(" ") == 1:
                print(line.index(" "))



    print("═" * 35, "\n     This is TIC TOC TOE game!     \n" + "═" * 35, "\n")
    if input("Please press 'Enter' to start the game. \n"):
        pass
    display(state, who)  # Display empty board

    while True:  # Single game sequence
        inp = user_inp()  # Collect user move
        state, who = insert(state, "X", inp)  # Insert user move to state array
        display(state, who)  # Display board after user move
        potential_win(state)
        win = check_win(state, who)  # Check if there is a win
        if win == "X":  # message if there is user win
            print("You won with a very sophisticated AI! Congratulations!!\n"
                  "You are going to loose next time.")
            break
        state, who = response(state)
        display(state, who)

        win = check_win(state, who)
        if win == "O":
            print("I won! You looser. Human beings' time is limited on this planet. Haaa, haa, ha !!\n")
            break

    print("\nTry again")
