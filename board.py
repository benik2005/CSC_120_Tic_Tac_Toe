#Tic-Tac_Toe
import sqlite3

#prints the board
def printBoard(s):
    print("Printing the board...")
    for i in s:
        print(i)

#Checks for errors and updates the board with the players move
def placeMarker(r, c, sym):
    if r > 2 or c > 2 or r < 0 or c < 0:
        print("Invalid input: position not on board!")
        makeMove(currentPlayer)
    elif board[r][c] == 'X' or board[r][c] == 'O':
        print("Invalid input: already selected!")
        makeMove(currentPlayer)
    else:
        board[r][c] = sym
        printBoard(board)

#collects player input
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



#returns winner string, game over boolean(False is game still going)
def checkWin(state):
    if state[0][0] == state[0][1] and state[0][1] == state[0][2]:
        if state[0][0] == "X":
            return "Player 1 Wins!", True
        elif state[0][0] == "O":
            return "Player 2 Wins!", True
        else:
            return "No winner yet!", False
    elif state[1][0] == state[1][1] and state[1][1] == state[1][2]:
        if state[1][0] == "X":
            return "Player 1 Wins!", True
        elif state[1][0] == "O":
            return "Player 2 Wins!", True
        else:
            return "No winner yet!", False
    elif state[2][0] == state[2][1] and state[2][1] == state[2][2]:
        if state[2][0] == "X":
            return "Player 1 Wins!", True
        elif state[2][0] == "O":
            return "Player 2 Wins!", True
        else:
            return "No winner yet!", False
    elif state[0][0] == state[1][0] and state[1][0] == state[2][0]:
        if state[0][0] == "X":
            return "Player 1 Wins!", True
        elif state[0][0] == "O":
            return "Player 2 Wins!", True
        else:
            return "No winner yet!", False
    elif state[0][1] == state[1][1] and state[1][1] == state[2][1]:
        if state[0][1] == "X":
            return "Player 1 Wins!", True
        elif state[0][1] == "O":
            return "Player 2 Wins!", True
        else:
            return "No winner yet!", False
    elif state[0][2] == state[1][2] and state[1][2] == state[2][2]:
        if state[0][2] == "X":
            return "Player 1 Wins!", True
        elif state[0][2] == "O":
            return "Player 2 Wins!", True
        else:
            return "No winner yet!", False
    elif state[0][0] == state[1][1] and state[1][1] == state[2][2]:
        if state[0][0] == "X":
            return "Player 1 Wins!", True
        elif state[0][0] == "O":
            return "Player 2 Wins!", True
        else:
            return "No winner yet!", False
    elif state[0][2] == state[1][1] and state[1][1] == state[2][0]:
        if state[0][2] == "X":
            return "Player 1 Wins!", True
        elif state[0][2] == "O":
            return "Player 2 Wins!", True
        else:
            return "No winner yet!", False
    else:
        boardFull = True
        for i in state:
            if i.__contains__('-'):
                boardFull = False
        if boardFull:
            return "Draw.", True
        else:
            return "No winner yet!", False



#game initialization
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
printBoard(board)
currentPlayer = 1

con = sqlite3.connect('tic_tac_toe.db')

#game loop
while not checkWin(board)[1]:
    makeMove(currentPlayer)
    if currentPlayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1

    if checkWin(board)[1]:
        print("Game Over! " + checkWin(board)[0])
        con.execute("INSERT INTO game_records(result, date_played) VALUES('" + checkWin(board)[0]+"', DATE('now'));")
        con.commit()

#print all time results
cur = con.cursor()
cur.execute("SELECT gameID FROM game_records WHERE result = 'Player 1 Wins!';")
player1Wins = cur.fetchall()
cur.execute("SELECT gameID FROM game_records WHERE result = 'Player 2 Wins!';")
player2Wins = cur.fetchall()
cur.execute("SELECT gameID FROM game_records WHERE result = 'Draw.';")
draws = cur.fetchall()

print("All Time Stats: ")
print("Player 1 Wins: " + str(len(player1Wins)))
print("Player 2 Wins: " + str(len(player2Wins)))
print("Draws: " + str(len(draws)))

con.close()

