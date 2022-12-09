"""Game Tic Toc Toe"""

"""Fields numbering
       A   B   C  
      ╔═══╤═══╤═══╗
    1 ║ O │ 3 │ 6 ║
      ╟───┼───┼───╢
    2 ║ 1 │ 4 │ 7 ║
      ╟───┼───┼───╢
    3 ║ 2 │ 5 │ 8 ║
      ╚═══╧═══╧═══╝
"""

from random import choice

while True:
    state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Keeps current game state
    who = ""  # Contain info about recent player
    response_no = 0  # Counter of computer moves


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
        global response_no
        response_no += 1  # Counts computer moves
        print(1, response_no)
        empty_cor = empty_corner(state)  # Create list of empty corners
        if state[4] == " ":  # First move always in the central field
            state[4] = "O"
        elif response_no <= 2 and empty_cor:  # In second move...
            state[choice(empty_cor)] = "O"  # ...select random corner from empty_corner list
            print(2, response_no)
        else:
            print(3)
            move = potential_win(state)
            if type(move) == int:
                state[move] = "O"
            else:
                state = "draw"
                return state, None
        return state, "O"


    def potential_win(state):

        hazard_fields = []
        for line in [[0, 1, 2],  # Iterate through indexes of fields representing potentially winning lines
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 6],
                     [1, 4, 7],
                     [2, 5, 8],
                     [0, 4, 8],
                     [2, 4, 6], ]:

            # ↓ Check if line has 2 'X' and 1 'O' ↓
            if [state[line[0]], state[line[1]], state[line[2]]].count("X") == 2 and \
                    [state[line[0]], state[line[1]], state[line[2]]].count(" ") == 1:

                # ↓↓  Save number of empty field  ↓↓
                hazard_fields.append(line[[state[line[0]], state[line[1]], state[line[2]]].index(" ")])

        # ↓↓  Return number of empty field appearing in 2 lines ↓↓
        if len(hazard_fields) == 2 and hazard_fields[0] == hazard_fields[1]:
            print("2 linie ze wspólnym celem", hazard_fields[0])
            return hazard_fields[0]

        elif len(hazard_fields) == 1:  # Return number of empty field in single line
            print("1 linia", type(hazard_fields[0]))
            return hazard_fields[0]
        elif len(hazard_fields) == 2:
            print("2 linie ze różnymi celami", hazard_fields[0])
            return hazard_fields[0]
        else:
            print("Dupa", hazard_fields)


    """Single game sequence"""

    print("═" * 35, "\n     This is TIC TOC TOE game!     \n" + "═" * 35, "\n")
    if input("Please press 'Enter' to start the game. \n"):
        pass
    display(state, who)  # Display empty board

    while True:  # Single game sequence
        inp = user_inp()  # Collect user move

        state, who = insert(state, "X", inp)  # Insert user move to state array
        display(state, who)  # Display board after user move
        win = check_win(state, who)  # Check if there is user win
        if win == "X":
            print("You won with a very sophisticated AI! Congratulations!!\n"
                  "You are going to loose next time.")
            break

        state, who = response(state)  # Computer move
        if type(state) == str:
            print("DRAW!! I didn't get crazy too much this time.")
            break

        display(state, who)  # Display board after computer move

        win = check_win(state, who)  # Check if there is computer win
        if win == "O":
            print("I won! You looser. Human beings' time is limited on this planet. Haaa, haa, ha !!\n")
            break
    print("\nTry again")
