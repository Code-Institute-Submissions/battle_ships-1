"""
randit FOR GENERATION RANDOM INTS
pyinputplus FOR ERROR MESSGAE IF INTS NOT INPUT
"""
from random import randint
import pyinputplus as pyip


print("TO PLAY, PLEASE SELECT A ROW AND COLUMN BETWEEN 0-6")
# CREATE THE GAME BOARD
board = []


def print_board():
    """GAME BOARD CREATION"""
    for row in board:
        print(" ".join(row))


for x in range(0, 7):
    board.append(["O"] * 7)


print_board()


def random_row():
    """HIDE THE BATTLE SHIP IN RANDOM - ROW"""
    return randint(0, 7)


def random_col():
    """HIDE THE BATTLE SHIP IN RANDOM LOCATION - COLUMN"""
    return randint(0, 7)


ship_row = random_row()
ship_col = random_col()
print()
print()

# ITERATE THROUGH 7 TURNS
for turn in range(7):
    print("Turn", turn + 1)
    GUESS_ROW = int(pyip.inputNum("Guess Row: "))
    GUESS_COL = int(pyip.inputNum("Guess Col: "))
# TO ALLOW USER TO GUESS LOCATION OF SHIP AND ACTIONS AFTER GUESS
    if GUESS_ROW == ship_row and GUESS_COL == ship_col:
        print("YARRR! YE SUNK MY BATTLESHIP!")
        break
    else:
        if GUESS_ROW not in range(7) or GUESS_COL not in range(7):
            print("BE YE BLIND? THAT BE OFF THE MAP!")
        elif board[GUESS_ROW][GUESS_COL] == "X":
            print("MEMORY OF A GOLDFISH! YE TRIED THAT ALREADY.")
        else:
            print("MISS! YE BARNACLE BOTTOMED BOZO!")
            board[GUESS_ROW][GUESS_COL] = "X"
        if turn == 7:
            print("GAME OVER MAN, GAME OVER!")
        print_board()
