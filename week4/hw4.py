#################################################
# Hw4
# Your andrewID:
#################################################

# NOTE : 
# Function parameters are aliases # Equivalent to passing by reference 
# "is" vs "==" - is is used to check  if the elements are same aliases
# list - append, +, extend, insert
# print("Destructive:")

# NOTE : a+=[value] is not equal to a = a + [value]
# The general answer is that += tries to call the __iadd__ special method, and if that isn't available it tries to use __add__ instead. So the issue is with the difference between these special methods.
# The __iadd__ special method is for an in-place addition, that is it mutates the object that it acts on. The __add__ special method returns a new object and is also used for the standard + operator.
# So when the += operator is used on an object which has an __iadd__ defined the object is modified in place. Otherwise it will instead try to use the plain __add__ and return a new objec
# remove, pop, [:]=[], del -> delete destructively
# a[0],a[1] = a[1],a[0] -> swapping with parallel tuple
# reversed, a.reverse() -> to reverse a list
# sorted, a.sort()      -> to sort a list
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# (42) -> int (42,) -> tuple

# TODO  : Check copy.copy(a)

import cs112_s19_week4_linter

#####################################
# COLLABORATIVE Non-Graphics Problems
# Collaborators:
#####################################
def lookAndSay(a):
    result, l = [] , []
    b = copy.copy(a)
    for i in b:
        if i not in l:
            result.append((b.count(i),i))
            l.append(i)
    return result

def inverseLookAndSay(a):
    res = []
    for (i,j) in a:
        for k in range(i):
            res.append(j)
    return res

#####################################
# Solo Non-Graphics Problems
# No collaborators allowed here
#####################################

def allPossibleList(hand):
    print(hand)
    newhand = copy.copy(hand)
    substrings = []
    for i in range(1,len(hand)+1):
        # Number of times to loop 
        print('i',i)
        for j in range(i):
            for k in hand:
                string = ''
                string +=k
                print("string",string)
        # substrings.append(string)

# def calcPoints:

def bestScrabbleScore(dictionary, letterScores, hand):
    print("dictionary",dictionary, "letterScores",letterScores, "hand",hand)
    allPossibleList(hand)
    print("dictionary",dictionary, "letterScores",letterScores, "hand",hand)
    return ("fortytwo",42)

#################################################
# ignore_rest: The autograder will not look at 
# anything below here.  The graphics problems
# will go below.
#################################################

#####################################
# COLLABORATIVE Graphics Problems
# Collaborators:
#####################################
from tkinter import *
import math
import string

def drawStar(canvas, centerX, centerY, diameter, numPoints, color):
    points = [] 
    theta_increment = 180/numPoints
    theta = 180/numPoints
    for i in range(numPoints):    
        points.append((centerX-(diameter/2)*0.382*math.sin(math.radians(theta)),centerY-(diameter/2)*0.382*math.cos(math.radians(theta))))
        theta+=theta_increment
        points.append((centerX-(diameter/2)*math.sin(math.radians(theta)),centerY-(diameter/2)*math.cos(math.radians(theta))))
        theta+=theta_increment

    canvas.create_polygon(points, fill=color)


def drawQatarFlag(winWidth=760, winHeight=300):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    # --8-- --2-- --18--
    # ||11||

    points = [] 
    numPoints = 9
    points.append((winWidth,0))
    points.append((int((8/28)*winWidth),0))
    for i in range(numPoints):
        points.append((int((10/28)*winWidth), int((winHeight/numPoints)*(i+0.5))))
        points.append((int((8/28)*winWidth), int((winHeight/numPoints)*(i+1))))
    points.append((winWidth,winHeight))
    
    canvas.create_polygon(points, fill="#8d1b3d")
    
    root.mainloop()

#####################################
# Solo Graphics Problems
# No collaborators allowed here
#####################################
def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    # color name
    # move n
    # left n
    # right n
    commands = program.splitlines()
    
    # 10-point font, in gray text, running down the left-hand side of the window (10 pixels from the left edge)
    
    
    color = None
    pos_x = int(winWidth/2)
    pos_y = int(winHeight/2)
    
    angle = 0
    draw = False
    count = 1
    for i in commands:
        canvas.create_text(10, 10*count, text=i, fill="grey", anchor=W)# font="Helvetica 26 bold underline")
        count += 1
        if i in string.whitespace:
            continue
        elif i[0] == "#":
            continue
        else:
            command = i.split()
            if command[0] == "color":
                if command[1] == "none":
                    draw = False
                else:
                    draw = True
                    color = command[1]
                
            elif command[0] == "move":
                new_x = pos_x + int(command[1])*math.cos(math.radians(angle))
                new_y = pos_y - int(command[1])*math.sin(math.radians(angle))
                if draw == False:
                    pass
                else:
                    canvas.create_line(pos_x, pos_y, new_x, new_y, fill=color, width=4)
                print(pos_x, pos_y, new_x, new_y)
                pos_x = new_x
                pos_y = new_y
            elif command[0] == "right":
                angle-=int(command[1])
            elif command[0] == "left":
                angle+=int(command[1])
            
    root.mainloop()
    
#################################################
# Test code is below here
#################################################
import copy

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def drawStarHelper(centerX, centerY, diameter, numPoints, color, 
                   winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    drawStar(canvas, centerX, centerY, diameter, numPoints, color)
    
    root.mainloop()    

def testDrawStar():
    print("Testing drawStar()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawStarHelper(250, 250, 500, 5, "gold")
    drawStarHelper(300, 400, 100, 4, "blue")
    drawStarHelper(300, 200, 300, 9, "red")
    print("Done!")

def testDrawQatarFlag():
    print("Testing drawQatarFlag()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawQatarFlag()
    drawQatarFlag(winWidth=1145, winHeight=450)
    print("Done!")    

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testRunSimpleTortoiseProgram1():
    runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

def testRunSimpleTortoiseProgram2():
    runSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")

def testRunSimpleTortoiseProgram():
    print("Testing runSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    testRunSimpleTortoiseProgram1()
    testRunSimpleTortoiseProgram2()
    print("Done!")

def testAll():
    # Call your tests from here.  If you aren't sure how, look at HW2
    testLookAndSay()
    testInverseLookAndSay()
    # testBestSscrabbleScore() #TODO : Remaining
    testDrawStar() 
    testDrawQatarFlag() 
    testRunSimpleTortoiseProgram()
    return

def main():
    cs112_s19_week4_linter.lint() # check rules
    testAll()

if __name__ == '__main__':
    main()        