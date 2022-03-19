"""
Import randit from random module built in module in python3 to generate random numbers
"""
from random import randint

board = []
"""
Setting up board in the traditional 7 by 7 grid for battle ships.
Looping the "W" for "water" 7 times to make columns and rows.
"""
for i in range(0,7):
    board.append(["O"] * 7)
"""
Code to loop through each element in outerlist and join method used to combine the items in the list
"""

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

"""
Code to hide battleship in a random location
"""

def random_row(board):
  return randint(0, 7)

def random_col(board):
  return randint(0, 7)

ship_row = random_row(board)
ship_col = random_col(board)

print (ship_row)
print (ship_col)

"""
Code to promt and allow the user to guess the location of a battleship. 
"""

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Column: "))


"""
Statments for actions after hit or miss 
"""
if guess_row == ship_row and guess_col == ship_col:                    
  print ("YARRR! YOU SUNK ME BATTLESHIP!")
else:
    if guess_row not in range(7) or guess_col not in range(7):
        print("BE YE BLIND? THAT BE OFF THE MAP!")
    else:
        print("MISS! YE BARNACLE BOTTOMED BOZO!")        
        board[guess_row][guess_col] = "X"
print_board(board)
