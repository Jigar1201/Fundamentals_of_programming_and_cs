# https://www.cs.cmu.edu/~112/notes/notes-tetris/2_1_DesignOverview.html

from tkinter import *   

def gameDimensions():
    rows = 15
    cols = 10
    CellSize = 20
    margin = 25
    return (rows, cols, CellSize, margin)

def drawBoard(canvas, app):
    print(app.board)
    for i in range(app.rows):
        for j in range(app.cols):
            drawCell(app, canvas,i,j)

def drawCell(app, canvas, row, col):
    x1 = app.margin + app.CellSize*col
    y1 = app.margin + app.CellSize*row
    x2 = app.margin + app.CellSize*col + app.CellSize
    y2 = app.margin + app.CellSize*row + app.CellSize
    print(x1, y1, x2, y2)
    canvas.create_rectangle(x1, y1, x2, y2,fill = app.board[row][col] ,width=1)

def redrawAll(canvas, app):
    canvas.create_rectangle(0,0, app.width, app.height,fill = "orange" ,width=1)
    drawBoard(canvas, app)

def runApp(width,height):
    def redrawAllWrapper(canvas, app):
        redrawAll(canvas, app)
        canvas.update()

    # def mousePressedWrapper(event, canvas, data):
    #     mousePressed(event, data)
    #     redrawAllWrapper(canvas, data)

    # def keyPressedWrapper(event, canvas, data):
    #     keyPressed(event, data)
    #     redrawAllWrapper(canvas, data)

    class Struct(object): pass
    app = Struct()
    appStarted(app)
    app.height = height
    app.width = width

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    redrawAllWrapper(canvas, app)
    root.mainloop()  # blocks until window is closed    

def appStarted(app):
    app.rows,app.cols, app.CellSize, app.margin = gameDimensions()
    app.emptyColor = "blue"
    app.board = []
    for i in range(app.rows):
        app.board.append([app.emptyColor]*app.cols)

    # pre-load a few cells with known colors for testing purposes
    app.board[0][0] = "red" # top-left is red
    app.board[0][app.cols-1] = "white" # top-right is white
    app.board[app.rows-1][0] = "green" # bottom-left is green
    app.board[app.rows-1][app.cols-1] = "gray" # bottom-right is gray       
    print(app.board)

def playTetris():
    rows, cols, CellSize, margin = gameDimensions()
    width = cols*CellSize+2*margin
    height = rows*CellSize+2*margin
    runApp(width=width, height=height)

def main():
    playTetris()

if __name__ == '__main__':
    main()