#File: proj2.py
#Author: Hamza Ilyas
#Date: 09/05/2018
#Section: 21
#E-mail: hamza3@umbc.edu
#Description:
#    This program will allow a user (or users) to play a game of connect
#    four. The user may also choose to play against a computer, which will
#    select moves at random.



P1_MOVE = "X"
P2_MOVE = "O"
MIN_BOARD_SIZE = 5
from random import randint


#def makeBoard(height, width) makes the game board, only used once
#in the entirety of the program.
#Input: height and width, 2 integers to recognize the dimensions of the board.
#Output: Returns a list, the game board
def makeBoard(height, width):

    #Copied from slides
    gameBoard = []
    while len(gameBoard) < height:
        boardRow = []
        while len(boardRow) < width:
            boardRow.append("_")
        gameBoard.append(boardRow)

    return gameBoard






#def validateMove(minimum,maximum,msg) makes sure the column the user chooses
#is within the valid ranges.
#Input: minimum and maximum, the constaints. Also the message to show when
#getting input.
#Output: an integer, the valid choice to return.
def validateMove(minimum, maximum, msg):


    #Make sure the chosen column value falls between
    #the constraints.
    toReturn = int(input(msg))
    while toReturn > maximum or toReturn < minimum:
        if toReturn > maximum:
            print("Column choice too large.")
        if toReturn < minimum:
            print("Column choice too small.")

        toReturn = int(input(msg))


    return toReturn






#def displayBoard(gameBoard) is used multiple times to print out the board
#after every move that the user makes.
#Input: a list, the game board.
#Output: none, since it's a print function.
def displayBoard(gameBoard):

    

    #Copied from slides verbatim.
    row = 0
    while row < len(gameBoard):
        col = 0
        while col < len(gameBoard[row]):
            print(gameBoard[row][col], end = " ")
            col += 1
        print()
        row += 1



#def makeMoveP1(column, gameBoard) makes the move for the first player.
#It changes the column the user chooses to an "X."
#Input: an integer; column. a list; gameBoard
#Output: None, since lists are shallow copies.
def makeMoveP1(column, gameBoard):


    #Must be subtracted by 1, because the index starts at 0.
    column -= 1
    lowestRow = len(gameBoard) - 1

    reprompt = "reprompt"
    #If there is already a piece in the chosen column,
    #move onto the next higher row. 
    while (gameBoard[lowestRow][column] == P1_MOVE\
          or gameBoard[lowestRow][column] == P2_MOVE):
        if lowestRow != 0:
            lowestRow -= 1
        if lowestRow <= 0:
            print("This column is at maximum capacity.")
            return
    #then place the "X" in the empty spot.
    if (gameBoard[lowestRow][column] != P1_MOVE\
       or gameBoard[lowestRow][column] != P2_MOVE):
        
        gameBoard[lowestRow][column] = P1_MOVE

#def makeMoveP2 is the same as def makeMoveP2 except that it replaces
#the chosen column to an "O" instead of an "X."
def makeMoveP2(column, gameBoard):

    column -= 1
    lowestRow = len(gameBoard) - 1
    reprompt = "reprompt"
    while (gameBoard[lowestRow][column] == P1_MOVE\
          or gameBoard[lowestRow][column] == P2_MOVE)\
          and lowestRow != 0:
        if lowestRow != 0:
            lowestRow -= 1
        if lowestRow < 0:
            print("This column is at maximum capacity.")
            return
    if (gameBoard[lowestRow][column] != P1_MOVE\
       or gameBoard[lowestRow][column] != P2_MOVE):
        gameBoard[lowestRow][column] = P2_MOVE
    

#def checkWinConditionX(columns, rows, gameBoard) checks to see if a player,
#particularly player 1 has won. It uses mathematical manipulation to check
#if the horizontal, vertical, or diagonal win conditions are met.
#Input: 2 integers (columns and rows), and a list; gameBoard
#Return: a boolean (True), if any of the win conditions are met.
def checkWinConditionX(gameBoard):


    #horizontal win

    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[i])-3):
            if gameBoard[i][j] == "X" and gameBoard[i][j+1] == "X" and\
               gameBoard[i][j+2] == "X" and gameBoard[i][j+3] == "X":
                print("Player 1 wins!")
                return True

    #vertical win
    for i in range(len(gameBoard)-3):
        for j in range(len(gameBoard[i])):
            if gameBoard[i][j] == "X" and gameBoard [i+1][j] == "X" and\
               gameBoard[i+2][j] == "X" and gameBoard[i+3][j] == "X":
                print("Player 1 wins!")
                return True

    #positive ascension win
    for i in range(len(gameBoard)-3):
        for j in range(len(gameBoard[i])-3):
            if gameBoard[i][j] == "X" and gameBoard[i+1][j+1] == "X" and\
               gameBoard[i+2][j+2] and gameBoard[i+3][i+3] == "X":
                print("Player 1 wins!")
                return True

    #negative regression win
    for i in range(len(gameBoard)-3):
        for j in range(len(gameBoard[i])-3):
            if gameBoard[i][j] == "X" and gameBoard[i-1][j+1] == "X" and\
               gameBoard[i-2][j+2] == "X" and gameBoard[i-3][j+3] == "X":
                print("Player 1 wins!")
                return True
            


#def checkWinConditionO does the same thing as checkWinConditionX except
#that it checks whether or not player 2 has made the winning move, instead
#of player 1, which is checked by checkWinConditionX.
def checkWinConditionO(gameBoard):



    #checks for win by 4 next to each other                                                                                                                                       
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[i])-3):
            if gameBoard[i][j] == "O" and gameBoard[i][j+1] == "O" and\
               gameBoard[i][j+2] == "O" and gameBoard[i][j+3] == "O":
                print("Player 2 wins!")
                return True

    #checks for win by 4 on top of each other                                                                                                                                     
    for i in range(len(gameBoard)-3):
        for j in range(len(gameBoard[i])):
            if gameBoard[i][j] == "O" and gameBoard[i+1][j] == "O" and\
               gameBoard[i+2][j] == "O" and gameBoard[i+3][j] == "O":
                print("Player 2 wins!")
                return True

    #checks diagonal ascension
    for i in range(len(gameBoard)-3):
        for j in range(len(gameBoard[i])-3):
            if gameBoard[i][j] == "O" and gameBoard[i+1][j+1] == "O" and\
               gameBoard[i+2][j+2] == "O" and gameBoard[i+3][j+3] == "O":
                print("Player 2 wins!")
                return True

            
    #checks diagonal regression
    for i in range(len(gameBoard)-3):
        for j in range(len(gameBoard[i])-3):
            if gameBoard[i][j] == "O" and gameBoard[i-1][j+1] == "O" and\
               gameBoard[i-2][j+2] == "O" and gameBoard[i-3][j+3] == "O":
                print("Player 2 wins!")
                return True



#def randomMove(width) is used if the player chooses to play against the
#computer, in which case a random column is chosen by the random function.
#Input: an integer; width, so we may know the maximum value that we should
#allow the randint function to take on.
#Output: an integer; the random column move generated by the function.
def randomMove(width):

    #choose width as the upper bound because it's the max.
    randomMove = randint(1, width)
    return randomMove



def main():


    #intro declarations
    print("Welcome to Connect 4!")
    height = int(input("Enter a height: "))
    while height < MIN_BOARD_SIZE:
        height = int(input("Enter a height: "))
    width = int(input("Enter a width: "))
    while width < MIN_BOARD_SIZE:
        width = int(input("Enter a height: "))
    columns = height
    rows = width
    compOrHuman = input("Play against the computer? (y/n): ")
    
    gameBoard = list(makeBoard(height, width))
    displayBoard(gameBoard)


    #someone hasn't won yet.
    someoneHasWon = False


    #keep a loop going until someone has won.
    playerTurn = 1
    while someoneHasWon != True and compOrHuman == "n":

        if playerTurn % 2 != 0:
            #player1's turn
            print("Player 1 what is your choice?")
            print("You may choose between column ( 1 -", width, ")")
            columnChosen = validateMove(1, width, "Please enter a valid column: ")
            makeMoveP1(columnChosen, gameBoard)
            displayBoard(gameBoard)

        if playerTurn % 2 == 0:
            #player2's turn
            print("Player 2 what is your choice?")
            print("You may choose between column ( 1 -", width, ")")
            columnChosen = validateMove(1, width, "Please enter a valid column: ")
            makeMoveP2(columnChosen, gameBoard)
            displayBoard(gameBoard)

        someoneHasWon = checkWinConditionX(gameBoard)
        someoneHasWon = checkWinConditionO(gameBoard)
        
        playerTurn += 1

    playerTurn = 1
    #if user chooses to play with the computer.
    while someoneHasWon != True and compOrHuman == "y":

        if playerTurn % 2 != 0:
            #player1's turn                                                                                                                    
            print("Player 1 what is your choice?")
            print("You may choose between column ( 1 -", width, ")")
            columnChosen = validateMove(1, width, "Please enter a valid column: ")
            makeMoveP1(columnChosen, gameBoard)
            displayBoard(gameBoard)

        if playerTurn % 2 == 0:
            #player2's turn, computer                                                                                                                    
            print("Player 2 what is your choice?")
            print("You may choose between column ( 1 -", width, ")")
            

            columnChosen = randomMove(width)
            print("Please enter a valid column: ", columnChosen)
            makeMoveP2(columnChosen, gameBoard)
            displayBoard(gameBoard)

        someoneHasWon = checkWinConditionX(gameBoard)
        someoneHasWon = checkWinConditionO(gameBoard)
        
        playerTurn += 1

        if "_" not in gameBoard:
            print("Draw!")
        someoneHasWon = True

main()
