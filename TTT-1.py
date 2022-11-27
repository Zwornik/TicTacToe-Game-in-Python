"""Game Tic Toc Toe"""

from random import choice

state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print(type(state))


def display(state):
    print("        A   B   C  ".format(state))
    print("      ╔═══╤═══╤═══╗")
    print("    1 ║ {0[0]} │ {0[3]} │ {0[6]} ║".format(state))
    print("      ╟───┼───┼───╢")
    print("    2 ║ {0[1]} │ {0[4]} │ {0[7]} ║".format(state))
    print("      ╟───┼───┼───╢")
    print("    3 ║ {0[2]} │ {0[5]} │ {0[8]} ║".format(state))
    print("      ╚═══╧═══╧═══╝\n")


def check(state):
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


def user_inp():
    inp = ""
    inp = input("Type field coordinates to put the 'X' (e.g. 'A2')")
    inp = inp.upper()
    if len(inp) != 2 or inp[0] not in ("A", "B", "C") or inp[1] not in ("1", "2", "3"):
        print("WRONG INPUT. TRY AGAIN.")
        user_inp()
    elif read(state, inp) != " ":
        print("This filed has '{}'".format(read(state, inp)))
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
    return empty_corners


def response(state):
    if state[4] == " ":
        state[4] = "O"
    elif empty_corner(state) != []:
        state[choice(empty_corner(state))] = "O"


print("\n_________________________\nThis is TIC TOC TOE game.\n_________________________\n")
display(state)

while True:
    inp = user_inp()
    insert(state, "X", inp)
    display(state)
    response(state)

    display(state)
    check(state)
