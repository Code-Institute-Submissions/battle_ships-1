"""Import randint module"""
from random import randint


def create_board():
    """creating the game board"""
    board = []
    for _ in range(0, 7):
        board.append(["O"] * 7)
    return board


def print_board(board):
    """Removing commas and quotations from list"""
    for row in board:
        print(" ".join(row))


def random_row():
    """Hiding the battleship by row"""
    return randint(0, 7)


def random_col():
    """Hiding the battleship by column"""
    return randint(0, 7)


def play_again():
    """To play again after game end."""
    print("\n")
    again_input = input("WANT SOME MORE? Y/N ")
    if again_input == "Y":
        play()
    elif again_input != "N":
        print("YER SPEAKING GIBBERISH")
        play_again()
    print("\n")


def play():
    """The main funtion"""
    ship_row = random_row()
    ship_col = random_col()

    print(
        "CHOOSE A ROW AND COLUMN FROM 0-6, YA SEA DOG or type 'flee' to exit"
        )
    board = create_board()
    print_board(board)

    # iterate through seven turns
    for turn in range(7):
        print("\n")
        print("Turn", turn + 1)

        row_input = input("Guess Row: ")
        try:
            guess_row = int(row_input)
        except ValueError:
            if row_input == "flee":
                print("COWARD!")
                quit()
            else:
                print("THAT'S NOT NUMBER NUMPTY!")
                continue

        col_input = input("Guess Col: ")
        try:
            guess_col = int(col_input)
        except ValueError:
            if col_input == "flee":
                print("COWARD!")
                quit()
            else:
                print("THAT'S NOT NUMBER NUMPTY!")
                continue

        # For guesses and messages trigger after guess
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
            if turn == 6:
                print("GAME OVER MAN, GAME OVER!")
            print_board(board)

    # To replay the game
    play_again()


# Play game
play()
