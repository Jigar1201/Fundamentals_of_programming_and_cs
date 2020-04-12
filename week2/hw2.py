#################################################
# HW2
# Your andrewID:
#################################################

import cs112_s19_week2_linter
import math
#################################################
# The following problems are COLLABORATIVE
#################################################

def numberLength(x):
    c = 1
    while x//10!=0:
        c+=1
        x=x//10
    return c

def countMatchingDigits(x, y):
    match = 0
    num = y
    while True:
        v1 = x%10 
        x//=10
        while True:
            v2 =num%10 
            num//=10
            if(v1==v2):
                match +=1
            if (num//10==0 and num%10==0):
                break
        num = y
        if (x//10==0 and x%10==0):
            break
    return match

def rotateNumber(x):
    rem = x%10
    num = x 
    c   = -1
    while num!=0:
        num//=10
        c+=1
    x = x//10
    return x+rem*(10**c)

def isPrime(x):
    if x<2:
        return False
    for i in range(2,int((x+1)**0.5)+1):
        if (x%i==0):
            return False
    return True

def isCircularPrime(x):
    num =x
    rot =x
    if not isPrime(x):
        return False
    while num!=0: #It might be having an additional check (after rotating when it comes to the original digit)
        if isPrime(rotateNumber(rot))==False:
            return False
        rot = rotateNumber(rot)
        num//=10
    return True

def nthCircularPrime(n):
    count = -1
    num = 1
    while count!=n:
        if (isCircularPrime(num)):
            count+=1
        num+=1
    return (num-1)

#################################################
# Everything below here is SOLO
#################################################
    
# NOTE: remove the triple-quotes before you start debugging. ###
def countEvenDigits(n):
    if n < 0:
        return countEvenDigits(-n)
    elif n == 0:
        return 1
    count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n = n // 10
    return count

# NOTE: remove the triple-quotes before you start debugging. ###
def factorial(n):
    if n==0:
        return 1
    result=n
    for smallerInteger in range(1,n):
        result=result*smallerInteger
    return result

# NOTE: remove the triple-quotes before you start debugging. ###
def intHasRepeatedDigits(n):
    if n>=0:
        remainingDigits=n
    else:
        n=-n
        remainingDigits=n
    while remainingDigits//10>0:
        firstDigit=remainingDigits%10
        tensDigit=(remainingDigits//10)%10
        if firstDigit==tensDigit:
            print(n,"has repeated digits!")
            return True
        remainingDigits=remainingDigits//10
    print(n,"has no repeated digits...")
    return False

def containsOddDigits(x):
    while x!=0:
        if((x%10)%2!=0):
            return True
        x//=10
    return False

def countMultiplesOfSeven(a, b): #TODO : OPTIMIZE FURTHER
    if b<a: return 0
    c=0
    for i in range(a,b+1):
        if(i%7==0):
            c+=1
    return c

def printNumberTriangle(n):
    for i in range(n):
        num=0
        for j in range(i+1):
            num+=(j+1)*(10**j)
        print(num)

def sumOfSquaresOfDigits(n):
    num=0
    while n!=0:
        num+=(n%10)**2
        n//=10
    return num
    
def isHappyNumber(n):
    if(n<1): return False
    num = sumOfSquaresOfDigits(n)
    while True:
        if (num==1):
            return True
        elif(num==4):
            return False
        else:
            num = sumOfSquaresOfDigits(num)

def nthHappyPrime(n):
    count = -1
    num = 1
    while count!=n:
        if(isPrime(num)==True and isHappyNumber(num)==True):
            count+=1
        num+=1
    return num-1
assert(nthHappyPrime(0) == 7)

#################################################
# HW2 Test Functions
# ignore_rest
#################################################

def testNumberLength():
    print('Testing numberLength()...', end='')
    assert(numberLength(12) == 2)
    assert(numberLength(3) == 1)
    assert(numberLength(89) == 2)
    assert(numberLength(12345) == 5)
    assert(numberLength(120021) == 6)
    assert(numberLength(5000) == 4)
    print('Passed!')

def testCountMatchingDigits():
    print('Testing countMatchingDigits()... ', end='')
    assert(countMatchingDigits(1234, 2071) == 2)
    assert(countMatchingDigits(2203, 1527) == 2)
    assert(countMatchingDigits(5, 1253) == 1)
    assert(countMatchingDigits(18737, 7) == 2)
    assert(countMatchingDigits(1220, 7322) == 4)
    assert(countMatchingDigits(1234, 5678) == 0)
    print('Passed!')

def testRotateNumber():
    print('Testing rotateNumber()... ', end='')
    assert(rotateNumber(1234) == 4123)
    assert(rotateNumber(4123) == 3412)
    assert(rotateNumber(3412) == 2341)
    assert(rotateNumber(2341) == 1234)
    assert(rotateNumber(5) == 5)
    assert(rotateNumber(111) == 111)
    print('Passed!')

def testIsCircularPrime():
    print('Testing isCircularPrime()... ', end='')
    assert(isCircularPrime(2) == True)
    assert(isCircularPrime(11) == True)
    assert(isCircularPrime(13) == True)
    assert(isCircularPrime(79) == True)
    assert(isCircularPrime(197) == True)
    assert(isCircularPrime(1193) == True)
    print('Passed!')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(4) == 11)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(11) == 79)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')

def testCountEvenDigits():
    print("Testing countEvenDigits()...", end="")
    assert(countEvenDigits(5) == 0)
    assert(countEvenDigits(8) == 1)
    assert(countEvenDigits(83) == 1)
    assert(countEvenDigits(94) == 1)
    assert(countEvenDigits(1234567890) == 5)
    assert(countEvenDigits(0) == 1)
    print("Passed! (But I didn't check how many lines you changed...)")

def testFactorial():
    print("Testing factorial()...", end="")
    assert(factorial(2) == 2)
    assert(factorial(4) == 24)
    assert(factorial(6) == 720)
    assert(factorial(0) == 1)
    print("Passed!")

def testIntHasRepeatedDigits():
    print("Testing intHasRepeatedDigits()...", end="")
    assert(intHasRepeatedDigits(0) == False)
    assert(intHasRepeatedDigits(5) == False)
    assert(intHasRepeatedDigits(44) == True)
    assert(intHasRepeatedDigits(-6) == False)
    assert(intHasRepeatedDigits(-33) == True)
    assert(intHasRepeatedDigits(124456) == True)
    assert(intHasRepeatedDigits(-124456) == True)
    assert(intHasRepeatedDigits(124) == False)
    assert(intHasRepeatedDigits(-124) == False)
    print("Passed! (But I didn't check how many lines you changed...)")

def testContainsOddDigits():
    print('Testing containsOddDigits()... ', end='')
    assert(containsOddDigits(1246) == True)
    assert(containsOddDigits(8663) == True)
    assert(containsOddDigits(224) == False)
    assert(containsOddDigits(115) == True)
    assert(containsOddDigits(8) == False)
    assert(containsOddDigits(9) == True)
    print('Passed!')

def testCountMultiplesOfSeven():
    print('Testing countMultiplesOfSeven()... ', end='')
    assert(countMultiplesOfSeven(3, 16) == 2)
    assert(countMultiplesOfSeven(13, 15) == 1)
    assert(countMultiplesOfSeven(7, 22) == 3)
    assert(countMultiplesOfSeven(8, 28) == 3)
    assert(countMultiplesOfSeven(15, 18) == 0)
    assert(countMultiplesOfSeven(15, 6) == 0)
    print('Passed!')

def testPrintNumberTriangle():
    import sys, io
    print('Testing printNumberTriangle()... ', end='')
    tmpOut = sys.stdout

    oneOutput = io.StringIO()
    sys.stdout = oneOutput
    printNumberTriangle(1)
    oneCheck = oneOutput.getvalue()

    fourOutput = io.StringIO()
    sys.stdout = fourOutput
    printNumberTriangle(4)
    fourCheck = fourOutput.getvalue()

    sevenOutput = io.StringIO()
    sys.stdout = sevenOutput
    printNumberTriangle(7)
    sevenCheck = sevenOutput.getvalue()

    sys.stdout = tmpOut

    assert(oneCheck == "1\n")
    assert(fourCheck == "1\n21\n321\n4321\n")
    assert(sevenCheck == "1\n21\n321\n4321\n54321\n654321\n7654321\n")
    print('Passed!')

def testSumOfSquaresOfDigits():
    print('Testing sumOfSquaresOfDigits()... ', end='')
    assert(sumOfSquaresOfDigits(5) == 25)
    assert(sumOfSquaresOfDigits(12) == 5)
    assert(sumOfSquaresOfDigits(234) == 29)
    print('Passed!')

def testIsHappyNumber():
    print('Testing isHappyNumber()... ', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Passed!')

def testNthHappyPrime():
    print('Testing nthHappyPrime()... ', end='')
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(5) == 79)
    assert(nthHappyPrime(6) == 97)
    print('Passed!')

def testAll():
    testNumberLength()
    testCountMatchingDigits()
    testRotateNumber()
    testIsCircularPrime()
    testNthCircularPrime()
    testCountEvenDigits()
    testFactorial()
    testIntHasRepeatedDigits()
    testContainsOddDigits()
    testCountMultiplesOfSeven()
    testPrintNumberTriangle()
    testSumOfSquaresOfDigits()
    testIsHappyNumber()
    testNthHappyPrime()

def main():
    cs112_s19_week2_linter.lint() # check rules
    testAll()

if __name__ == '__main__':
    main()