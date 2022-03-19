from random import randint
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
print (ship_row)
print (ship_col)
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
  if guess_row == ship_row and guess_col == ship_col:
    print ("YARRR! YE SUNK MY BATTLESHIP!")
    break
  else:
    if guess_row not in range(7) or guess_col not in range(7):
      print ("BE YE BLIND? THAT BE OFF THE MAP!")
    elif board[guess_row][guess_col] == "X":
      print("MEMORY OF A GOLDFISH! YE TRIED THAT ALREADY.")
    else:
      print("MISS! YE BARNACLE BOTTOMED BOZO!")
      board[guess_row][guess_col] = "X"
    if (turn == 6):
      print ("GAME OVER MAN, GAME OVER!")
    print_board(board)



