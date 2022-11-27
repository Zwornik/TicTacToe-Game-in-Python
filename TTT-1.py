"""Game Tic Toc Toe"""

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
            state[3] == state[4] == state[5] or \
            state[6] == state[7] == state[8] or \
            state[0] == state[3] == state[6] or \
            state[1] == state[4] == state[7] or \
            state[2] == state[5] == state[8] or \
            state[0] == state[4] == state[8] or \
            state[2] == state[4] == state[6]:
        print("{} wins, congratulations!!\n".format("'Z'"))

def user_inp():
    inp = ""
    inp = input("Type field coordinates to put the 'X' (e.g. 'A2')")
    inp = inp.upper()
    if inp[0] not in ("A", "B", "C") or inp[1] not in ("1","2","3"):
        print("WRONG INPUT. TRY AGAIN.")
        user_inp()
    else:
        print("ok")
        return inp

def insert(state, who, inp):
    state[0] = who if inp == "A1" else pass
    state[1] = who if inp == "A2" else pass
    state[2] = who if inp == "A3" else pass
    state[3] = who if inp == "B1" else None
    state[4] = who if inp == "B2" else None
    state[5] = who if inp == "B3" else None
    state[6] = who if inp == "C1" else None
    state[7] = who if inp == "C2" else None
    state[8] = who if inp == "C3" else None
    return state


print("\n_________________________\nThis is TIC TOC TOE game.\n_________________________\n")
display(state)

while True:

    inp = user_inp()
    insert(state, "X", inp)
    display(state)
    check(state)
