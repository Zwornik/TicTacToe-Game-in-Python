"""Game Tic Toc Toe"""

from random import choice

state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Keeps current game state


def display(state, first_move):  # Display game result
    whi = who(state, first_move)

    if whi != "":
        whi = "◀◀◀ {0}".format(whi)

    print("        A   B   C  ".format(state))
    print("      ╔═══╤═══╤═══╗")
    print("    1 ║ {0[0]} │ {0[3]} │ {0[6]} ║".format(state))
    print("      ╟───┼───┼───╢")
    print("    2 ║ {0[1]} │ {0[4]} │ {0[7]} ║   {1}".format(state, whi))
    print("      ╟───┼───┼───╢")
    print("    3 ║ {0[2]} │ {0[5]} │ {0[8]} ║".format(state))
    print("      ╚═══╧═══╧═══╝\n")


def who(state, first_move):  # find if move was made by X or O
    global temp_state
    sign = ""
    if first_move == 0:  # assign state to temp_state but only first time
        temp_state = state
        print("first")

    for i in range(len(state)):  # find out whose move was recent
        if len(state[i]) > len(temp_state[i]):
            sign = state[i]
            print(temp_state, "< temp", first_move)
            print(state, "< state")
            temp_state = state
        print(sign, ":::")
        return sign

    return sign

    # znajdź różnicę między temp_state i state





def check(state):  # Check if there is a win (row of 3)
    if state[0] == state[1] == state[2] or \
            state[3] == state[4] == state[5] in ("X", "O") or \
            state[6] == state[7] == state[8] in ("X", "O") or \
            state[0] == state[3] == state[6] in ("X", "O") or \
            state[1] == state[4] == state[7] in ("X", "O") or \
            state[2] == state[5] == state[8] in ("X", "O") or \
            state[0] == state[4] == state[8] in ("X", "O") or \
            state[2] == state[4] == state[6] in ("X", "O"):
        print("{} wins, congratulations!!\n".format("'Z'"))
        print(state)


def user_inp():  # collect user move
    inp = ""
    inp = input("Type field coordinates to put the 'X' (e.g. 'A2')")
    inp = inp.upper()
    if len(inp) != 2 or inp[0] not in ("A", "B", "C") or inp[1] not in ("1", "2", "3"):
        print("WRONG INPUT. TRY AGAIN.")
        user_inp()
    elif read(state, inp) != " ":
        print("There is '{}' in this field. Please try again.".format(read(state, inp)))
    else:
        print("ok")
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
    return state


def read(state, inp):  # Read value of selected field
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


def empty_corner(state):
    empty_corners = []
    if state[0] == " ":
        empty_corners.append(0)
    elif state[2] == " ":
        empty_corners.append(2)
    elif state[6] == " ":
        empty_corners.append(6)
    elif state[8] == " ":
        empty_corners.append(8)
    print(empty_corners)
    return empty_corners


def response(state):
    if state[4] == " ":
        state[4] = "O"
    elif empty_corner(state) != []:
        state[choice(empty_corner(state))] = "O"


print("\n_________________________\nThis is TIC TOC TOE game.\n_________________________\n")
display(state, 0)

while True:
    inp = user_inp()
    insert(state, "X", inp)
    display(state, 1)
    response(state)

    display(state, 1)
    check(state)
