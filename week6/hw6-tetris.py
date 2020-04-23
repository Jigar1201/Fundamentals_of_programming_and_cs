# https://www.cs.cmu.edu/~112/notes/notes-tetris/2_1_DesignOverview.html
# ONLY DONE TILL STEP 6

from tkinter import *   
import random

def fallingPieceIsLegal(app):
    for i in range(len(app.fallingPiece)):
        for j in range(len(app.fallingPiece[0])):
            row = app.fallingPieceRow + i
            col = app.fallingPieceCol + j
            if app.fallingPiece[i][j]==True:
                if not ((( 0 <=row <app.rows) and (0 <= col < app.cols)) and app.board[row][col]=="blue"):
                    return False
    return True

def removeFullRows(app):
    tempBoard = []
    pass

def rotateFallingPiece(app):
    oldPieceDimensions = (len(app.fallingPiece), len(app.fallingPiece[0]))
    oldPiece = app.fallingPiece
    oldRow, oldCol = app.fallingPieceRow, app.fallingPieceCol
    
    newRotatedPiece = []
    for i in range(len(app.fallingPiece[0])):
        newRotatedPiece.append([False]*len(app.fallingPiece))
    
    for i in range(oldPieceDimensions[1]):
        for j in range(oldPieceDimensions[0]):
            newRotatedPiece[i][j] = app.fallingPiece[j][oldPieceDimensions[1]-1-i]
    
    app.fallingPiece = newRotatedPiece
    app.fallingPieceRows, app.fallingPieceCols = oldPieceDimensions[1], oldPieceDimensions[0]
    app.fallingPieceRow = oldRow + oldPieceDimensions[0]//2 - app.fallingPieceRows//2
    app.fallingPieceCol = oldCol + oldPieceDimensions[1]//2 - app.fallingPieceCols//2
    
    if not fallingPieceIsLegal(app):
        app.fallingPiece = oldPiece
        app.fallingPieceRows, app.fallingPieceCols = oldPieceDimensions[0],oldPieceDimensions[1]
        app.fallingPieceRow, app.fallingPieceCol = oldRow,oldCol

def moveFallingPiece(app, drow, dcol):
    app.fallingPieceRow+=drow
    app.fallingPieceCol+=dcol
    if not (fallingPieceIsLegal(app)):
        app.fallingPieceRow-=drow
        app.fallingPieceCol-=dcol
        return False
    return True

def newFallingPiece(app):
    randomIndex = random.randint(0, len(app.tetrisPieces) - 1)
    app.fallingPiece = app.tetrisPieces[randomIndex]
    app.fallingPieceColor = app.tetrisPieceColors[randomIndex]
    app.fallingPieceRow = 0
    app.fallingPieceCol = app.cols//2 - len(app.fallingPiece[0])//2
    if not (fallingPieceIsLegal(app)):
        app.isGameOver = True

def drawFallingPiece(canvas, app):
    for i in range(len(app.fallingPiece)):
        for j in range(len(app.fallingPiece[0])):
            if app.fallingPiece[i][j] == True:
                row = app.fallingPieceRow + i
                col = app.fallingPieceCol + j
                drawCell(app,canvas,row,col,app.fallingPieceColor)

def drawBoard(canvas, app):
    for i in range(app.rows):
        for j in range(app.cols):
            drawCell(app, canvas,i,j, app.board[i][j])

def drawCell(app, canvas, row, col, color):
    x1 = app.margin + app.CellSize*col
    y1 = app.margin + app.CellSize*row
    x2 = app.margin + app.CellSize*col + app.CellSize
    y2 = app.margin + app.CellSize*row + app.CellSize
    canvas.create_rectangle(x1, y1, x2, y2,fill = color ,width=1)

def drawGameOver(canvas, app):
    # Too lazy to not hardcord the values :P
    canvas.create_rectangle(30,30,20+20*10,20+20*3,fill = "black" ,width=10)
    canvas.create_text(125,50, font=("Purisa", 15),fill = "WHITE", text="GAME OVER!!", width=200)

def redrawAll(canvas, app):
    drawBoard(canvas, app)
    drawFallingPiece(canvas, app)
    if app.isGameOver:
        drawGameOver(canvas, app)

def keyPressed(event, app):
    if not app.isGameOver:
        if (event.keysym == "Up"):
            rotateFallingPiece(app)
        elif (event.keysym == "Down"):
            moveFallingPiece(app,+1,0)
        elif (event.keysym == "Left"):
            moveFallingPiece(app,0,-1)
        elif (event.keysym == "Right"):
            moveFallingPiece(app,0,+1)
        elif (event.keysym == "space"):
            newFallingPiece(app)
    
    if (event.keysym == "r"):
        appStarted(app)

def placeFallingPiece(app):
    for i in range(len(app.fallingPiece)):
        for j in range(len(app.fallingPiece[0])):
            if(app.fallingPiece[i][j]):
                app.board[i+app.fallingPieceRow][j+app.fallingPieceCol] = app.fallingPieceColor
    newFallingPiece(app)

def timerFired(app):
    if not app.isGameOver:
        if not (moveFallingPiece(app, +1, 0)):
            placeFallingPiece(app)
        

def runApp(app,width,height):
    def redrawAllWrapper(canvas, app):
        redrawAll(canvas, app)
        canvas.update()

    def timerFiredWrapper(canvas, app):
        timerFired(app)
        redrawAllWrapper(canvas, app)
        # pause, then call timerFired again
        canvas.after(app.timerDelay, timerFiredWrapper, canvas, app)

    def keyPressedWrapper(event, canvas, app):
        keyPressed(event, app)
        redrawAllWrapper(canvas, app)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.create_rectangle(0,0, app.width, app.height,fill = "orange" ,width=1)
    canvas.pack()
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, app))
    timerFiredWrapper(canvas, app)
    root.mainloop()  # blocks until window is closed    

def appStarted(app):
    app.rows,app.cols, app.CellSize, app.margin = gameDimensions()
    app.emptyColor = "blue"
    app.board = []
    for i in range(app.rows):
        app.board.append([app.emptyColor]*app.cols)
    
    # Seven "standard" pieces (tetrominoes)
    iPiece = [
        [  True,  True,  True,  True ]]
    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]]
    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]]
    oPiece = [
        [  True,  True ],
        [  True,  True ]]
    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]]
    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]]
    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]]

    app.isGameOver = False
    app.tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    app.tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]
    # Define and draw the new falling piece
    newFallingPiece(app)

def gameDimensions():
    rows = 15
    cols = 10
    CellSize = 20
    margin = 25
    return (rows, cols, CellSize, margin)    

def playTetris():
    rows, cols, CellSize, margin = gameDimensions()
    width = cols*CellSize+2*margin
    height = rows*CellSize+2*margin
    class Struct(object): pass
    app = Struct()
    appStarted(app)
    app.height = height
    app.width = width
    app.timerDelay = 1
    runApp(app,width=width, height=height)

def main():
    playTetris()

if __name__ == '__main__':
    main()