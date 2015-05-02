from random import randint

board = []

for ocean in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

def incorrect_guess():
    if guess_row not in range(5) or \
        guess_col not in range(5):
        print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)

for turn in range(4):
    print "Turn", turn + 1
    guess_row = raw_input("Guess Row:")
    guess_col = raw_input("Guess Column:")
    try:
        guess_row = int(guess_row)
        guess_col = int(guess_col)
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sank my battleship!"
            break
        else:
            incorrect_guess()
            if turn == 3:
                print "Game Over"
    except ValueError:
        print "Please enter a valid number."