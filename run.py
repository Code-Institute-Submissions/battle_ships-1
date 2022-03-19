board = []
"""
Setting up board in the traditional 7 by 7 grid for battle ships.
Looping the "W" for "water" 7 times to make columns and rows.
"""
for i in range(0,7):
    board.append(["W"] * 7)
"""
Custom print and loop to go through each element in outerlist.
Join method used to combine the items in the list
"""
def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

