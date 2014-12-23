# import pdb; pdb.set_trace()
active = True
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
    ]

board = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', ]

def print_board():
    print board[0]
    print board[1]
    print board[2]

def alt_print_board():
    print board[0:3]
    print board[3:6]
    print board[6:9]

while active:

    move = raw_input("Make your move: ")

    # Do stuff with move
    move = int(move)



    board[move] = 'X' # Something like this.
































    if move == 'exit':
        alt_print_board()
        print "Thanks for playing!"
        active = False
