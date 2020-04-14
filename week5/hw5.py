#################################################
# Hw5
# Your andrewID:
#################################################

# a = [ [0] * cols ] * rows # Error: creates shallow copy
#                           # Creates one unique row, the rest are aliases!

import cs112_s19_week5_linter
import copy
import math

#####################################
# COLLABORATIVE Non-Animation Problems
# Collaborators:
#####################################

def nondestructiveRemoveRowAndCol(lst, row, col):
    lstcopy = copy.deepcopy(lst)
    for i in range(len(lst)):
        lstcopy[i].pop(col)
    lstcopy.pop(row)
    return lstcopy
 
def destructiveRemoveRowAndCol(lst, row, col):    
    for i in range(len(lst)):
        lst[i].pop(col)
    lst.pop(row)
    return lst

def bestQuiz(a):
    # resolve ties in favor of the lower quiz number.
    avg = 0
    for i in range(len(a[0])):
        sum_col = 0
        count = 0
        for j in range(len(a)):
            if a[j][i]!=-1:
                sum_col+=(a[j][i])
                count+=1
        if ((sum_col/count)>avg):
            avg = sum_col/count
            index = i
    return index

#####################################
# Solo Non-Animation Problems
# No collaborators allowed here
#####################################

def areLegalValues(a):
    for i in range(len(a)):
        # Check all values are once
        if (a.count(i+1)) > 1:
            return False
        # Check all values are legal
        if a[i] > len(a) or a[i] < 0:
            return False
    return True

def isLegalRow(board, row):
    return areLegalValues(board[row])

def isLegalCol(board, col):
    return areLegalValues([i[col] for i in board])

def isLegalBlock(board, block):
    vals = [] 
    
    N = int(math.sqrt(len(board)))
    row = (block//N)*N
    col = (block%N)*N
    
    for i in range(row, row+N):
        vals+=board[i][col:col+N]
    return areLegalValues(vals)

def isLegalSudoku(board):
    
    for i in range(len(board)):
        if(isLegalRow(board,i)==False):
            return False
        elif(isLegalCol(board,i)==False):
            return False
        elif(isLegalBlock(board,i)==False):
            return False

    return True 

#################################################
# ignore_rest: The autograder will not look at 
# anything below here.  The graphics problems
# will go below.
#################################################

#####################################
# Solo Animation Problem
# No collaborators allowed here
#####################################

from tkinter import *

#### Sudoku Animation ####
# TODO : Game Won - Message and Ignore other keys after that

def init(data):
    data.highlighted_row = 0
    data.highlighted_col = 0
    data.valuePresent = False
    data.erase_current = False
    data.game_won = False

    data.board = [[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]
    
    # Board to check game won
    # data.board = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
    #         [ 5, 2, 9, 1, 3, 4, 7, 6, 8 ],
    #         [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ],
    #         [ 2, 6, 3, 4, 1, 5, 9, 8, 7 ],
    #         [ 9, 7, 4, 8, 6, 3, 1, 2, 5 ],
    #         [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ],
    #         [ 1, 3, 8, 9, 4, 7, 2, 5, 6 ],
    #         [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ],
    #         [ 7, 4, 5, 2, 8, 6, 3, 1, 0 ]]

    data.margin = 20
    data.rect_dim = (data.width - 2*data.margin)/len(data.board)
    
    # Flag for values present by default
    data.default_values = [[(1 if data.board[j][i]!=0 else 0)  for i in range(len(data.board))] for j in range(len(data.board))]

    
def mousePressed(event, data):
    X = (event.x - data.margin)//data.rect_dim
    Y = (event.y - data.margin)//data.rect_dim
    data.highlighted_row = int(X)
    data.highlighted_col = int(Y)

def keyPressed(event, data):
    if (event.keysym == "Left"):
        data.highlighted_row-=1
    elif (event.keysym == "Right"):
        data.highlighted_row+=1
    elif (event.keysym == "Up"):
        data.highlighted_col-=1
    elif (event.keysym == "Down"):
        data.highlighted_col+=1
    elif ((event.keysym).isnumeric() and int(event.keysym)!=0):
        data.valuePresent = True
        data.value = event.keysym
    elif  ((event.keysym) == "BackSpace"):
        data.erase_current = True

def redrawAll(canvas, data):
    starterBoard(canvas, data)
    update_new_values(canvas, data)

def update_new_values(canvas, data):
    if data.valuePresent and not data.game_won:
        temp_board = copy.deepcopy(data.board)
        temp_board[data.highlighted_col][data.highlighted_row] = int(data.value)
        if(sum([(0 if 0 in j else 1)for j in temp_board]) == len(data.board)):
            print("Game Won")
            canvas.create_text(data.height/2, data.width/2, font=("Purisa", 25),fill = "WHITE", text="GAME WON!!", width=40000)
            data.game_won = True

        if (isLegalSudoku(temp_board) and data.default_values[data.highlighted_col][data.highlighted_row]==0):
            data.board[data.highlighted_col][data.highlighted_row] = int(data.value)
            
            # Creating a white rectangle
            px1 = data.highlighted_row*data.rect_dim+data.margin
            px2 = data.highlighted_col*data.rect_dim+data.margin
            py1 = (data.highlighted_row+1)*data.rect_dim+data.margin
            py2 = (data.highlighted_col+1)*data.rect_dim+data.margin
            canvas.create_rectangle(px1, px2, py1, py2,fill = "white" ,width=1)
            
            # Inputing a text in blue
            center_x = data.highlighted_row*data.rect_dim+data.margin+data.rect_dim/2
            center_y = data.highlighted_col*data.rect_dim+data.rect_dim/2+data.margin
            canvas.create_text(center_x, center_y, font=("Purisa", 25),fill = "dark turquoise",text=data.value, width=40)
            
        data.valuePresent = False
    
    if data.erase_current and not data.game_won:
        data.board[data.highlighted_col][data.highlighted_row] = 0
        data.erase_current = False

        # Creating a white rectangle
        px1 = data.highlighted_row*data.rect_dim+data.margin
        px2 = data.highlighted_col*data.rect_dim+data.margin
        py1 = (data.highlighted_row+1)*data.rect_dim+data.margin
        py2 = (data.highlighted_col+1)*data.rect_dim+data.margin
        canvas.create_rectangle(px1, px2, py1, py2,fill = "white" ,width=1)


def starterBoard(canvas, data):
    board = data.board
    rect_dim = data.rect_dim
    margin = data.margin
    
    colors = ["red","orange","yellow","green","blue","purple","gray","brown","tan"]
    N = int(math.sqrt(len(board)))
    
    if not data.game_won:
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,fill='white', width=0)
        # Colours and thick lines for blocks
        for i in range(N):
            for j in range(N):
                canvas.create_rectangle(i*N*rect_dim+margin, j*N*rect_dim+margin, (i+1)*N*rect_dim+margin, (j+1)*N*rect_dim+margin,fill=colors[(N*i+j)%(N**2)],width=3)

        data.highlighted_row %= len(board)
        data.highlighted_col %= len(board)
    
        # Creating small rectangles
        for i in range(len(board)):
            for j in range(len(board[0])):
                canvas.create_rectangle(j*rect_dim+margin, i*rect_dim+margin, (j+1)*rect_dim+margin, (i+1)*rect_dim+margin, width=1)            

                # Highlighted row and column cell
                if j==data.highlighted_row and i == data.highlighted_col:
                    canvas.create_rectangle(j*rect_dim+margin, i*rect_dim+margin, (j+1)*rect_dim+margin, (i+1)*rect_dim+margin,fill = "white" ,width=1)
                # Fill default values
                if(data.default_values[i][j]==1):
                    canvas.create_text(j*rect_dim+margin+rect_dim/2, i*rect_dim+rect_dim/2+margin, font=("Purisa", 25), text=board[i][j],width=50)
                
                elif(data.board[i][j]!=0):
                    canvas.create_text(j*rect_dim+margin+rect_dim/2, i*rect_dim+rect_dim/2+margin, font=("Purisa", 25), fill = "dark turquoise", text=board[i][j],width=50)

def runSudoku(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed    

#################################################
# Test code is below here
#################################################

def testNondestructiveRemoveRowAndCol():
    print("Testing nondestructiveRemoveRowAndCol()...", end="")
    lst = [ [ 2, 3, 4, 5],
        [ 8, 7, 6, 5],
        [ 0, 1, 2, 3] ]
    lstCopy = copy.deepcopy(lst)
    result = [ [ 2, 3, 5],
            [ 0, 1, 3] ]
    assert(nondestructiveRemoveRowAndCol(lst, 1, 2) == result)
    assert(lst == lstCopy), "input list should not be changed"
    print("Passed!")

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end="")
    # The input list and output list
    lst = [ [ 2, 3, 4, 5],
            [ 8, 7, 6, 5],
            [ 0, 1, 2, 3] ]
    result = [ [ 2, 3, 5],
            [ 0, 1, 3] ]
    # The first test is an ordinary test; the second is a destructive test
    assert(destructiveRemoveRowAndCol(lst, 1, 2) == result)
    assert(lst == result), "input list should be changed"
    print("Passed!")

def testBestQuiz():
    print("Testing destructiveRemoveRowAndCol()...", end="")
    a = [[ 88,  80, 91 ],
         [ 68, 100, -1 ]]
    assert(bestQuiz(a) == 2)
    print("Passed!")

def testAreLegalValues():
    print("Testing areLegalValues()...", end="")
    assert(areLegalValues([1,2,0,0,4,6,0,0,8]) == True)
    assert(areLegalValues([1,2,0,0,4,6,0,7,8]) == True)
    assert(areLegalValues([1,2,0,0,4,6,0,0,10]) == False)
    assert(areLegalValues([1,2,0,0,4,6,0,0,-1]) == False)
    assert(areLegalValues([1,2,0,1,4,6,0,0,3]) == False)
    print("Passed!")

def testIsLegalRow():
    print("Testing isLegalRow()...", end="")
    board = [[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]
    assert(isLegalRow(board, 0) == True)
    assert(isLegalRow(board, 1) == True)
    assert(isLegalRow(board, 2) == True)
    assert(isLegalRow(board, 3) == True)
    assert(isLegalRow(board, 4) == True)
    print("Passed!")

def testIsLegalCol():
    print("Testing isLegalCol()...", end="")
    board = [[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]
    assert(isLegalCol(board, 0) == True)
    assert(isLegalCol(board, 1) == True)
    assert(isLegalCol(board, 2) == True)
    assert(isLegalCol(board, 3) == True)
    assert(isLegalCol(board, 4) == True)
    print("Passed!")

def testIsLegalBlock():
    print("Testing isLegalBlock()...", end="")
    board = [[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]
    assert(isLegalBlock(board, 0) == True)
    assert(isLegalBlock(board, 1) == True)
    assert(isLegalBlock(board, 2) == True)
    assert(isLegalBlock(board, 3) == True)
    assert(isLegalBlock(board, 4) == True)
    print("Passed!")

def testIsLegalSudoku():
    print("Testing isLegalSudoku()...", end="")
    board = [[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]
    assert(isLegalSudoku(board) == True)
    print("Passed!")

def testSudokuAnimation():
    print("Running Sudoku Animation...", end="")
    # Feel free to change the width and height!
    width = 500
    height = 500
    runSudoku(width, height)
    print("Done!")

def testAll():    
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testBestQuiz()
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testIsLegalBlock()
    testIsLegalSudoku()
    testSudokuAnimation()

def main():
    cs112_s19_week5_linter.lint() # check rules
    testAll()

if __name__ == '__main__':
    main()