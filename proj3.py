#File: proj3.py
#Author: Hamza Ilyas
#Date: 11/28/2018
#Section: 21
#E-mail: hamza3@umbc.edu
#Description:
#    This program will allow the user to play a game of suduko.


PLAY_SOLVE_MENU = ["play (p)",
                   "solve (s)"]

PLAY_OPTION_MENU = ["play number (p)",
                    "save (s)",
                    "undo (u)",
                    "quit (q)"]

PLAY_OPTION_CHOICES = ["p", "s", "u", "q"]

MINROW = 1
MINCOL = 1
MAXROW = 9
MAXCOL = 9

ROWMSG = "Enter a row number (1-9) : "
COLMSG = "Enter a column number (1-9) : " 
CELLMSG = "Enter the number to place in the cell: "

def prettyPrint(board):

    # print column headings and top border                                                                             
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ")
    print("  +-------+-------+-------+")

    for i in range(len(board)):
        # convert "0" cells to underscores  (DEEP COPY!!!)                                                  
        boardRow = list(board[i])
        for j in range(len(boardRow)):
            if boardRow[j] == "0":
                boardRow[j] = "_"

        # fill in the row with the numbers from the board                                                              
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1,
                boardRow[0], boardRow[1], boardRow[2],
                boardRow[3], boardRow[4], boardRow[5],
                boardRow[6], boardRow[7], boardRow[8]) )

        # the middle and last borders of the board                                                                     
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")


def savePuzzle(board, fileName):

    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file                                                                       
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()

def readFile(fileName):

    boardOP = open(fileName)

    return boardOP


def solveSudoku(listName):

    while "_" in listName:
        for i in range(listName):
            for j in range(listName[i]):
                if listName[i][j] == "_":
                    listName[i][j] == numToPlay

    if "_" in listname:
        solveSudoku(listName)
    else:
        return
    
def playNums(column, row, listName, numToPlay):

    listName[column][row] = numToPlay
    return listName


def undo(listName, previousMove): 

    listName[previousMove[0]previousMove[1]] = "_"
    

def validIntInput(mini, maxi, msg):

    num = int(input(msg))
    while num >= maxi or num <= mini:
        print("Please choose a number in the specified range!")
        num = int(input(msg))

    return num


def playableNums(column, row):

    if board[column][row] == "_":
        return True


def checkWin(board):

    if "_" not in board:
        return True
    else:
        return False



def removeZeroes(boardOP):

    board = []
    for i in range(9):
        line = boardOP.readline()
        newLine = " "
        line = list(line)
        while "," in line:
            line.remove(",")
        board.append(line)
    return board
        




def main():

    print()

    print("Welcome to Suduko!")
    userChoice = input("Enter the filename of the Sudoko puzzle: ")
    fileName = userChoice

    originalBoard = []
    originalBoard = readFile(fileName)
    originalBoard = removeZeroes(originalBoard)
    prettyPrint(originalBoard)
    
    board = []
    boardOP = readFile(fileName)
    board = removeZeroes(boardOP)
    prettyPrint(board)
    print()
    
    print("Please choose from one of the following: ")    
    print(" - - ")
    for i in range(len(PLAY_SOLVE_MENU)):
        print(PLAY_SOLVE_MENU[i])

    print(" - - ")
    playOrSolve = input("Enter a choice: ")
    while playOrSolve != "s" and playOrSolve != "p":
        print("Please choose a proper letter!")
        playOrSolve = input("Please enter choice: ")

    print(" - - ")

    correctnessCheck = input("Would you like to play with correctness "\
                             "checking? (y/n): ")

    
    while correctnessCheck != "y" and correctnessCheck != "n":
        print("Please choose a proper letter!")
        correctnessCheck = input("Please enter choice: ")


    winCheck = checkWin(board)
    
    while winCheck != False:

        if playOrSolve == "p" and correctnessCheck == n:
            
            for i in range(len(PLAY_OPTION_MENU)):
                print(PLAY_OPTION_MENU[i])
            playMoveOption = input("Please enter a valid choice: ")
            while playMoveOption not in PLAY_OPTION_CHOICES:
                print("Invalid option!")
                playMoveOption = input("Enter a valid choice this time: ")

            if playMoveOption == "p":
                row = validIntInput(MINROW, MAXROW, ROWMSG)
                column = validIntInput(MINCOL, MAXCOL, COLMSG)
                print(row)
                print(column)
                numToPlay = validIntInput(MINCOL, MAXCOL, CELLMSG)
                playNums(column, row, board, numToPlay)

            if playMoveOption == "s":
                savePuzzle(board, fileName)

            if playMoveOption == "u":
                undo(board, previousMove)
            
            validIntInput(MINCOL, MAXCOL, CELLMSG)
            playNums(column, row, board, numToPlay)
 
        previousMove = [row, column, numToPlay]
        winCheck = checkWin(board)


main()
