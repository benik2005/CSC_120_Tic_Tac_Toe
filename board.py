#Tic-Tac_Toe

def printBoard(s):
    print("Printing the board...")
    for i in s:
        print(i)

def placeMarker(r, c, sym):
    if r > 2 or c > 2:
        print("Invalid input: position not on board!")
        makeMove(currentPlayer)
    elif board[r][c] == 'X' or board[r][c] == 'O':
        print("Invalid input: already selected!")
        makeMove(currentPlayer)
    else:
        board[r][c] = sym
        printBoard(board)

def makeMove(player):
    if player == 1:
        print("Player 1's turn. Enter an row to place your X.")
        row = int(input())
        print("Player 1's turn. Enter a column to place your X.")
        col = int(input())
        placeMarker(row - 1, col - 1, 'X')
    else:
        print("Player 2's turn. Enter an row to place your O.")
        row = int(input())
        print("Player 2's turn. Enter a column to place your O.")
        col = int(input())
        placeMarker(row - 1, col - 1, 'O')

board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
printBoard(board)
currentPlayer = 1

while True:
    makeMove(currentPlayer)
    if currentPlayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1

