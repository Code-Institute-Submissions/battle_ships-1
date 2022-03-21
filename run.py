from random import randint
"""
Import randit module
"""

print("WELCOME TO BATTLESHIP TO PLAY PLEASE SELECT A ROW AND COLUMN BETWEEN 0-6")

"""
Code to loop through each element in outerlist and join method used to combine the items in the list
"""
board = []

for x in range(0, 7):
  board.append(["O"] * 7)

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
print ()
print ()
"""
Code to iterate though 7 turns
"""
for turn in range(7):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  """
  Code to promt and allow the user to guess the location of a battleship. And actions after each guess.  
  """
  if guess_row == ship_row and guess_col == ship_col: #triggered is guess is a hit
    print ("YARRR! YE SUNK MY BATTLESHIP!")
    break
  else:
    if guess_row not in range(7) or guess_col not in range(7):  #triggered is guess is off the board
      print ("BE YE BLIND? THAT BE OFF THE MAP!")
    elif board[guess_row][guess_col] == "X":
      print("MEMORY OF A GOLDFISH! YE TRIED THAT ALREADY.") #triggered is guess has already been made
    else:
      print("MISS! YE BARNACLE BOTTOMED BOZO!") #triggered if guess is a miss
      board[guess_row][guess_col] = "X"
    if (turn == 7):
      print ("GAME OVER MAN, GAME OVER!") #triggered on game end
    print_board(board)





