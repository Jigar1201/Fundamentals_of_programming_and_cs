#################################################
# Hw5
# Your andrewID:
#################################################

# a = [ [0] * cols ] * rows # Error: creates shallow copy
#                           # Creates one unique row, the rest are aliases!

import cs112_s19_week5_linter
import copy

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
    return False

def isLegalRow(board, row):
    return False

def isLegalCol(board, col):
    return False

def isLegalBlock(board, block):
    return False

def isLegalSudoku(board):
    return False 

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

def init(data):
    pass

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def redrawAll(canvas, data):
    pass

def runSudoku(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
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
    print("Testing testNondestructiveRemoveRowAndCol()...", end="")
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
    print("Testing testDestructiveRemoveRowAndCol()...", end="")
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
    print("Testing testDestructiveRemoveRowAndCol()...", end="")
    a = [[ 88,  80, 91 ],
         [ 68, 100, -1 ]]
    assert(bestQuiz(a) == 2)
    print("Passed!")

def testAreLegalValues():
    print("Write your own tests for areLegalValues!")

def testIsLegalRow():
    print("Write your own tests for isLegalRow!")

def testIsLegalCol():
    print("Write your own tests for isLegalCol!")

def testIsLegalBlock():
    print("Write your own tests for isLegalBlock!")

def testIsLegalSudoku():
    print("Write your own tests for isLegalSudoku!")

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
    # testAreLegalValues()
    # testIsLegalRow()
    # testIsLegalCol()
    # testIsLegalBlock()
    # testIsLegalSudoku()
    # testSudokuAnimation()

def main():
    cs112_s19_week5_linter.lint() # check rules
    testAll()

if __name__ == '__main__':
    main()