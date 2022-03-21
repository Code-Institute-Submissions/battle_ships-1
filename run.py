from random import randint
import pyinputplus as pyip

print("TO PLAY, PLEASE SELECT A ROW AND COLUMN BETWEEN 0-6")
# CREATE THE GAME BOARD
board = []

for x in range(0, 7):
    board.append(["O"] * 7)


def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)


# HIDE THE BATTLE SHIP IN RANDOM LOCATION
def random_row(board):
    return randint(0, 7)


def random_col(board):
    return randint(0, 7)


ship_row = random_row(board)
ship_col = random_col(board)
print()
print()

# ITERATE THROUGH 7 TURNS
for turn in range(7):
    print("Turn", turn + 1)
    guess_row = int(pyip.inputNum("Guess Row: "))
    guess_col = int(pyip.inputNum("Guess Col: "))
# TO ALLOW USER TO GUESS LOCATION OF SHIP AND ACTIONS AFTER GUESS
    if guess_row == ship_row and guess_col == ship_col:
        print("YARRR! YE SUNK MY BATTLESHIP!")
        break
    else:
        if guess_row not in range(7) or guess_col not in range(7):
            print("BE YE BLIND? THAT BE OFF THE MAP!")
        elif board[guess_row][guess_col] == "X":
            print("MEMORY OF A GOLDFISH! YE TRIED THAT ALREADY.")
        else:
            print("MISS! YE BARNACLE BOTTOMED BOZO!")
            board[guess_row][guess_col] = "X"
        if (turn == 7):
            print("GAME OVER MAN, GAME OVER!")
        print_board(board)
