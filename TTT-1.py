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
      
      'X' - User figure
      'O' - Computer figure
"""

from random import choice
field_coords = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")  # Coordinates of files where index is field number
lines = ((0, 1, 2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))  # All possible lines

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


    def check_win(win):  # Check if there is a win (row of 3)
        for i in lines:  # check each possible line
            if state[i[0]] == state[i[1]] == state[i[2]] in ("X", "O"):  # Check if line has 3 equal values
                print("WIN!!!")
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
            inp = input("Type field coordinates to put the 'X' (e.g. 'A2') ")
            inp = inp.upper()
            if len(inp) != 2 or inp[0] not in ("A", "B", "C") or inp[1] not in ("1", "2", "3"):  # Check if format is OK
                print("WRONG INPUT. TRY AGAIN.")
            elif check_field(inp) != " ":  # Check if selected field is empty
                print("There is '{}' in this field. Please try again.".format(check_field(inp)))
            else:
                return inp


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

        empty_cor = empty_corner(state)  # Create list of empty corners

        if potential_win("O") == "WIN": # Check if there is a computer win
            return state, "O"
        comp_move = potential_win("X")  # Check if there is a possibility for use win
        move_no = state.count("X")  # Number of user moves
        if state[4] == " ":  # First move always in the central field
            state[4] = "O"
        elif move_no >= 2 and type(comp_move) == int:  # If there is a risky line blok it
            state[comp_move] = "O"
        elif move_no == 1 and empty_cor:  # In second move...
            state[choice(empty_cor)] = "O"  # ...select random corner from empty_corner list
            print(2, response_no)
        else:
            print(3)
            if comp_move == "draw":
                return "draw", None
        return state, "O"


    def potential_win(who):

        hazard_fields = []

        # Block lines where 2 Xes are already
        for line in lines:
            line_values = [state[line[0]], state[line[1]], state[line[2]]]
            print(line_values)
            # ↓ Check if line has 2 'X' or 'O' and 1 ' ' ↓
            if line_values.count(who) == 2 and line_values.count(" ") == 1:
                # ↓↓  Save number of empty field  ↓↓
                hazard_fields.append(line[line_values.index(" ")])
                print("hazard fields:", hazard_fields)

                if who == "O":  # Return index of empty field if there is possible line with 'O's
                    comp_move = line_values.index(" ")
                    state[comp_move] = "O"
                    print("OOOO", comp_move, state)
                    return "WIN"

        if who == "X":
            print("XXX")
            # ↓↓  Return number of empty field appearing in 2 lines ↓↓
            if len(hazard_fields) == 2 and hazard_fields[0] == hazard_fields[1]:
                print("2 lines with common aim", hazard_fields[0])
                return hazard_fields[0]

            elif len(hazard_fields) == 1:  # Return number of empty field in single line
                print("1 line", type(hazard_fields[0]))
                return hazard_fields[0]
            elif len(hazard_fields) == 2:  # return first number in case of two lines not sharing
                print("2 lines with different aims", hazard_fields[0])
                return hazard_fields[0]
            elif state.count(" ") == 0:
                print("No lines")
                return "draw"



    """Single game sequence"""

    print("═" * 35, "\n     This is TIC TOC TOE game!     \n" + "═" * 35, "\n")
    if input("Please press any key and 'Enter' to start the game. "):
        pass
    display(state, who)  # Display empty board

    while True:  # Single game sequence
        inp = user_inp()  # Collect user move

        state, who = insert("X", inp)  # Insert user move to state array
        display(state, who)  # Display board after user move
        win = check_win(who)  # Check if there is user win
        if win == "X":
            print("You won with a very sophisticated AI! Congratulations!!\n"
                  "You are going to loose next time.")
            break

        state, who = response(state)  # Computer move
        if type(state) == str:
            print("DRAW!! I didn't get crazy too much this time.")
            break

        display(state, who)  # Display board after computer move

        win = check_win(who)  # Check if there is computer win
        if win == "O":
            print("I WON! You looser. Human beings' time is limited on this planet. Haaa, haa, ha !!\n")
            break
    print("\nTry again")
