board = []
"""
Setting up board in the traditional 7 by 7 grid for battle ships.
Looping the "W" for "water" 7 times to make columns and rows.
"""
for x in range(0,7):
    board.append(["W"] * 7)
    print(["W"] * 7)
