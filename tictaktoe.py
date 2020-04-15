import random 

def printBoard(board):
    print('   |   |')
    print(' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3]))
    print('   |   |')
    print('-----------')
    print(' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6]))
    print('   |   |')
    print('-----------')
    print(' ' + str(board[7]) + ' | ' + str(board[8]) + ' | ' + str(board[9]))
    print('   |   |')

def letterPicker():
    selection = ''
    while not (selection == 'O' or selection == 'X'):
        print('Select your letter (X or O)')
        selection = input().upper()
    if selection == 'X':
        return ['X' , 'O']
    else:
        return ['O', "X"]

def makeMove(board, letter, moveLocation ):
    board[moveLocation] = letter

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "human"

def playerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not validMove(board,move):
        print('What is your move (1-9)')
        move = input()
    return int(move)

def computerMove(board):
    move = random.randint(1,9)
    while not validMove(board,move):
        move = random.randint(1,9)
    return move

def winCondition(player):
    print('{0} won the game'.format(player))

def validMove(board,move):
    print(move)
    return board[int(move)] == ' '

def playAgain():
    print('Do you wnat to play again yes/no')
    return input().lower().startswith('y')

def checkWin(board, pl):
    return ((board[1] == pl and board[2] == pl and board[3] == pl) or
    (board[4] == pl and board[5] == pl and board[6] == pl) or
    (board[7] == pl and board[8] == pl and board[9] == pl) or
    (board[1] == pl and board[5] == pl and board[9] == pl) or
    (board[3] == pl and board[5] == pl and board[7] == pl) or
    (board[1] == pl and board[4] == pl and board[7] == pl) or
    (board[2] == pl and board[5] == pl and board[8] == pl) or
    (board[3] == pl and board[6] == pl and board[9] == pl))

while True:
    print("Welcome to Tic Tak Toe")
    board = [' '] * 10 
    playerLetters = letterPicker()
    if (whoseTurn := whoGoesFirst()) == 'human':
       print("Its your turn")
    else:
        print("Computer goes first") 
    gameActive = True
    while gameActive == True:
        if whoseTurn == 'human':
            printBoard(board)
            move = playerMove(board)
            makeMove(board, playerLetters[0], move)
            printBoard(board)
            if not checkWin(board, playerLetters[0]):
                whoseTurn = 'computer'
            else:
                winCondition(whoseTurn)
                gameActive = False
        else:
            move = computerMove(board)
            makeMove(board,playerLetters[1], int(move))
            printBoard(board)
            if not checkWin(board, playerLetters[1]):
                whoseTurn = 'human'
            else:
                winCondition(whoseTurn)
                gameActive = False 
    if not playAgain():
        break     





