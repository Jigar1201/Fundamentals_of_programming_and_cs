#################################################
# HW1
# Your andrewID: Jigar Patel
#################################################

import cs112_s19_week1_linter
import math 

#################################################

def isEvenPositiveInt(n):
    if(type(n)!=int):
        return False
    else:
        if(n>0 and n%2==0):
            return True
        else:
            return False

def hotdogPurchase(numHotdogs):
    if (numHotdogs%10==0 and numHotdogs%8==0):
        return numHotdogs//10,numHotdogs//8
    elif(numHotdogs%10!=0 and numHotdogs%8==0):
        return numHotdogs//10+1,numHotdogs//8
    elif(numHotdogs%10==0 and numHotdogs%8!=0):
        return numHotdogs//10,numHotdogs//8+1
    else:
        return numHotdogs//10+1,numHotdogs//8+1

def hotdogExcess(numHotdogs):
    franks,buns = hotdogPurchase(numHotdogs)
    return franks*10 - numHotdogs,buns*8 - numHotdogs   
        
def playGuessingGame():
    print("Let's play a guessing game! Think of a type of pet.")
    fur = input("Does it have fur?")
    if fur=="Yes":
        fetch = input("Can you teach it to play fetch?")
        if fetch=="Yes":
            print("It's a dog!")
        else:
            print("It's a cat!")
    else:
        swim = input("Can it swim?")
        if swim=="Yes":
            print("It's a fish!")
        else:
            print("It's a bird!")

#### The following four functions go together ####
# TODO : To be Checked
def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def lineIntersection(m1, b1, m2, b2):
    # This function takes four int or float values representing two lines
    #  and returns the x value of the point of intersection of the two lines.
    # If the lines are parallel, or identical, the function should return None.
    if (m1==m2):
        return None
    return ((b2-b1)/(m1-m2))

def triangleArea(s1, s2, s3):
    s = (s1 + s2 + s3)/2
    return math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    # First find where each pair of lines intersects,
    # then return the area of the triangle formed by connecting these three points of intersection. 
    # If no such triangle exists (if any two of the lines are parallel), return 0.
    if(lineIntersection(m1, b1, m2, b2)!=None and lineIntersection(m1, b1, m3, b3)!=None and lineIntersection(m2, b2, m3, b3)!=None):
        x1 = lineIntersection(m1, b1, m2, b2)
        x2 = lineIntersection(m2, b2, m3, b3)
        x3 = lineIntersection(m1, b1, m3, b3)
        if(x1==None or x2== None  or x3==None):
            return 0
        y1 = m1*x1+b1
        y2 = m2*x2+b2
        y3 = m3*x3+b3
        s1 = distance(x1, y1, x2, y2)
        s2 = distance(x2, y2, x3, y3)
        s3 = distance(x1, y1, x3, y3)
        return triangleArea(s1,s2,s3)
    return 0

#### The following three are COLLABORATIVE problems ####
# Collaborators:
# TODO: check other's method
def getKthDigit(n, k):
    if n<0:
        return (-n%(10**(k+1)))//(10**(k))
    return (n%(10**(k+1)))//(10**(k))

def setKthDigit(n, k, d):
    if n<0:
        return -(-n - (-n%(10**(k+1)))//(10**(k)) * (10**k) + d * (10**k))
    return n - (n%(10**(k+1)))//(10**(k)) * (10**k) + d * (10**k)

def colorBlender(rgb1, rgb2, midpoints, n):
    r1 = rgb1//1000000
    g1 = rgb1%1000000//1000
    b1 = rgb1%1000
    r2 = rgb2//1000000
    g2 = rgb2%1000000//1000
    b2 = rgb2%1000
    r = r1 + (r2-r1)/(midpoints+1)*n
    g = g1 + (g2-g1)/(midpoints+1)*n
    b = b1 + (b2-b1)/(midpoints+1)*n
    if ((r>=0 and r<=255) and (g>=0 and g<=255) and (b>=0 and b<=255)):
        if r-int(r)==0.5: r = int(r)+1
        if g-int(g)==0.5: g = int(g)+1
        if b-int(b)==0.5: b = int(b)+1
        return round(r)*1000000+round(g)*1000+round(b)
    return None

#################################################
# HW1 Test Functions
# ignore_rest
#################################################
def testIsEvenPositiveInt():
    print("Testing isEvenPositiveInt()... ", end="")
    assert(isEvenPositiveInt(4) == True)
    assert(isEvenPositiveInt(7) == False)
    assert(isEvenPositiveInt(-2) == False)
    assert(isEvenPositiveInt("6") == False)
    assert(isEvenPositiveInt(None) == False)
    assert(isEvenPositiveInt(8.0) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt(8) == True)
    assert(isEvenPositiveInt(22) == True)
    print("Passed.")

def testHotdogPurchase():
    print('Testing hotdogPurchase()... ', end='')
    assert(hotdogPurchase(0) == (0,0))
    assert(hotdogPurchase(13) == (2,2))
    assert(hotdogPurchase(26) == (3,4))
    assert(hotdogPurchase(39) == (4,5))
    assert(hotdogPurchase(50) == (5,7))
    assert(hotdogPurchase(61) == (7,8))
    assert(hotdogPurchase(80) == (8,10))
    assert(hotdogPurchase(88) == (9,11))
    print('Passed.')

def testHotdogExcess():
    print('Testing hotdogExcess()... ', end='')
    assert(hotdogExcess(0) == (0,0))
    assert(hotdogExcess(13) == (7,3))
    assert(hotdogExcess(26) == (4,6))
    assert(hotdogExcess(39) == (1,1))
    assert(hotdogExcess(50) == (0,6))
    assert(hotdogExcess(61) == (9,3))
    assert(hotdogExcess(80) == (0,0))
    assert(hotdogExcess(88) == (2,0))
    print('Passed.')

def ioTest(test):
    # This is some semi-complicated code to test the guessing game.
    # Don't worry if you don't know what it does.
    import sys, io
    myOut = io.StringIO()
    myIn = io.StringIO(test)
    sys.stdout = myOut
    sys.stdin = myIn
    playGuessingGame()
    return myOut.getvalue()

def testPlayGuessingGame():
    import sys
    print("Testing playGuessingGame()...", end="")
    tmpOut = sys.stdout
    tmpIn = sys.stdin
    dogTest = ioTest("Yes\nYes\n")
    catTest = ioTest("Yes\nNo\n")
    fishTest = ioTest("No\nYes\n")
    birdTest = ioTest("No\nNo\n")
    sys.stdout = tmpOut
    sys.stdin = tmpIn
    assert(dogTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can you teach it to play fetch?It's a dog!\n")
    assert(catTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can you teach it to play fetch?It's a cat!\n")
    assert(fishTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can it swim?It's a fish!\n")
    assert(birdTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can it swim?It's a bird!\n")
    print("Passed.")

def testDistance():
    print("Testing distance()...", end="")
    assert(math.isclose(distance(0, 0, 1, 1), 2**0.5))
    assert(math.isclose(distance(3, 3, -3, -3), 6*2**0.5))
    assert(math.isclose(distance(20, 20, 23, 24), 5))
    print("Passed. (Add more tests to be more sure!)")
    
def testLineIntersection():
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(math.isclose(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(math.isclose(lineIntersection(10,0,-4,35), 2.5))
    print("Passed. (Add more tests to be more sure!)")

def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert(math.isclose(triangleArea(3,4,5), 6))
    assert(math.isclose(triangleArea(2**0.5, 1, 1), 0.5))
    assert(math.isclose(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed. (Add more tests to be more sure!)")

def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert(math.isclose(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(math.isclose(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(math.isclose(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(math.isclose(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(math.isclose(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed. (Add more tests to be more sure!)")

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

def testAll():
    testIsEvenPositiveInt()
    testHotdogPurchase()
    testHotdogExcess()
    testPlayGuessingGame()
    testDistance()
    testLineIntersection()
    testTriangleArea()
    testThreeLinesArea()
    testGetKthDigit()
    testSetKthDigit()
    testColorBlender()

def main():
    cs112_s19_week1_linter.lint() # check rules
    testAll()

if __name__ == '__main__':
    main()
