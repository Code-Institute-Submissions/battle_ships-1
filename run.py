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
    board.append(["W"] * 7)
"""
Code to loop through each element in outerlist and join method used to combine the items in the list
"""

def print_board(board):
  for row in board:
    print (" ".join(row))

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
Code to allow the user to guess the location of a battleship
"""

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Column: "))
