# range, sum, max, min, reversed, sorted, list.count, list.sort, list.reverse, str.replace, 
# and str.join should not be used

def alternatingSum(lst):
    if (len(lst) == 0):
        return 0
    elif(len(lst)%2==0):
        return alternatingSum(lst[:-1])-lst[-1]
    else:
        return alternatingSum(lst[:-1])+lst[-1]

class VendingMachine(object):
    def __init__(self, numBottles, moneyOwe):
        self.numBottles = numBottles
        self.moneyOwe = moneyOwe
        self.moneyPaid = 0
        self.costEach = moneyOwe

    def __repr__(self):
        if self.numBottles == 1:
            if self.moneyPaid ==0:
                return ("Vending Machine:<%d bottle; $%0.2f each; $%0.0f paid>"% (self.numBottles, self.costEach/100, self.moneyPaid/100))
            else:
                return ("Vending Machine:<%d bottle; $%0.2f each; $%0.2f paid>"% (self.numBottles, self.costEach/100, self.moneyPaid/100))
        
        if self.moneyPaid ==0:
            return ("Vending Machine:<%d bottles; $%0.2f each; $%0.0f paid>"% (self.numBottles, self.costEach/100, self.moneyPaid/100))
        else:
            return ("Vending Machine:<%d bottles; $%0.2f each; $%0.2f paid>"% (self.numBottles, self.costEach/100, self.moneyPaid/100))
    
    def __eq__(self, other):
        return ((isinstance(other,VendingMachine)) and (self.numBottles==other.numBottles and  self.costEach == other.costEach and self.moneyOwe==other.moneyOwe))

    def __hash__(self):
        return hash((self.numBottles,self.costEach))

    def isEmpty(self):
        return self.numBottles==0

    def getBottleCount(self):
        return self.numBottles

    def stillOwe(self):
        return self.moneyOwe

    def insertMoney(self,insertedMoney):
        if self.numBottles == 0:
            return ("Machine is empty", insertedMoney)

        if(self.moneyOwe - insertedMoney)>0:
            self.moneyOwe -= insertedMoney
            self.moneyPaid += insertedMoney
            if(self.moneyOwe%100==0):
                return ("Still owe $%0.0f"%(self.moneyOwe/100), 0)
            return ("Still owe $%0.2f"%(self.moneyOwe/100), 0)

        else:
            excess = insertedMoney - self.moneyOwe
            self.moneyOwe = self.costEach
            self.numBottles-=1
            self.moneyPaid = 0
            if excess==0:
                return ("Got a bottle!", 0)
            return ("Got a bottle!", excess)

    def stockMachine(self,numBottles):
        self.numBottles += numBottles

def testVendingMachineClass():
    print("Testing Vending Machine class...", end="")
    # Vending machines have three main properties: 
    # how many bottles they contain, the price of a bottle, and
    # how much money has been paid. A new vending machine starts with no
    # money paid.
    vm1 = VendingMachine(100, 125)
    assert(str(vm1) == "Vending Machine:<100 bottles; $1.25 each; $0 paid>")
    assert(vm1.isEmpty() == False)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.stillOwe() == 125)
    
    # When the user inserts money, the machine returns a message about their
    # status and any change they need as a tuple.
    assert(vm1.insertMoney(20) == ("Still owe $1.05", 0))
    assert(str(vm1) == "Vending Machine:<100 bottles; $1.25 each; $0.20 paid>")
    assert(vm1.stillOwe() == 105)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.insertMoney(5) == ("Still owe $1", 0))
    
    # When the user has paid enough money, they get a bottle and 
    # the money owed resets.
    assert(vm1.insertMoney(100) == ("Got a bottle!", 0))
    assert(vm1.getBottleCount() == 99)
    assert(vm1.stillOwe() == 125)
    assert(str(vm1) == "Vending Machine:<99 bottles; $1.25 each; $0 paid>")
    
    # If the user pays too much money, they get their change back with the
    # bottle.
    assert(vm1.insertMoney(500) == ("Got a bottle!", 375))
    assert(vm1.getBottleCount() == 98)
    assert(vm1.stillOwe() == 125)
    
    # Machines can become empty
    vm2 = VendingMachine(1, 120)
    assert(str(vm2) == "Vending Machine:<1 bottle; $1.20 each; $0 paid>")
    assert(vm2.isEmpty() == False)
    assert(vm2.insertMoney(120) == ("Got a bottle!", 0))
    assert(vm2.getBottleCount() == 0)
    assert(vm2.isEmpty() == True)
    
    # Once a machine is empty, it should not accept money until it is restocked.
    assert(str(vm2) == "Vending Machine:<0 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Machine is empty", 25))
    assert(vm2.insertMoney(120) == ("Machine is empty", 120))
    assert(vm2.stillOwe() == 120)
    vm2.stockMachine(20) # Does not return anything
    assert(vm2.getBottleCount() == 20)
    assert(vm2.isEmpty() == False)
    assert(str(vm2) == "Vending Machine:<20 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Still owe $0.95", 0))
    assert(vm2.stillOwe() == 95)
    vm2.stockMachine(20)
    assert(vm2.getBottleCount() == 40)
    
    # We should be able to test machines for basic functionality
    vm3 = VendingMachine(50, 100)
    vm4 = VendingMachine(50, 100)
    vm5 = VendingMachine(20, 100)
    vm6 = VendingMachine(50, 200)
    vm7 = "Vending Machine"
    assert(vm3 == vm4)
    assert(vm3 != vm5)
    assert(vm3 != vm6)
    assert(vm3 != vm7) # should not crash!
    s = set()
    assert(vm3 not in s)
    s.add(vm4)
    assert(vm3 in s)
    s.remove(vm4)
    assert(vm3 not in s)
    assert(vm4.insertMoney(50) == ("Still owe $0.50", 0))
    assert(vm3 != vm4)
    print("Done!")


def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

class Bird(object):
    def __init__(self, birdName):
        self.name = birdName
        self.numEggs = 0

    def fly(self):
        return "I can fly!"

    def __repr__(self):
        if(self.numEggs==1):
            return "%s has %d egg"%(self.name, self. numEggs)
        return "%s has %d eggs"%(self.name, self. numEggs)

    def countEggs(self):
        return self.numEggs
    
    def layEgg(self):
        self.numEggs+=1

class Penguin(Bird):
    def fly(self):
        return "No flying for me."

    def swim(self):
        return "I can swim!"

class MessengerBird(Bird):
    def __init__(self, birdName, message=""):
        # super().__init__(birdName, message="") TODO : Find the reason
        self.name = birdName
        self.message = message
        self.numEggs = 0
    
    def deliverMessage(self):
        return self.message

def testBirdClasses():
    print("Testing Bird classes...", end="")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert(type(bird1) == Bird)
    assert(isinstance(bird1, Bird))
    assert(bird1.fly() == "I can fly!")
    assert(bird1.countEggs() == 0)
    assert(str(bird1) == "Parrot has 0 eggs")
    bird1.layEgg()
    assert(bird1.countEggs() == 1)
    assert(str(bird1) == "Parrot has 1 egg")
    bird1.layEgg()
    assert(bird1.countEggs() == 2)
    assert(str(bird1) == "Parrot has 2 eggs")
    assert(getLocalMethods(Bird) == ['__init__', '__repr__', 'countEggs', 
                                     'fly', 'layEgg'])
    
    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert(type(bird2) == Penguin)
    assert(isinstance(bird2, Penguin))
    assert(isinstance(bird2, Bird))
    assert(bird2.fly() == "No flying for me.")
    assert(bird2.swim() == "I can swim!")
    bird2.layEgg()
    assert(bird2.countEggs() == 1)
    assert(str(bird2) == "Emperor Penguin has 1 egg")
    assert(getLocalMethods(Penguin) == ['fly', 'swim'])
    
    # A MessengerBird is a Bird that can optionally carry a message
    bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
    assert(type(bird3) == MessengerBird)
    assert(isinstance(bird3, MessengerBird))
    assert(isinstance(bird3, Bird))
    assert(not isinstance(bird3, Penguin))
    assert(bird3.deliverMessage() == "Top-Secret Message!")
    assert(str(bird3) == "War Pigeon has 0 eggs")
    assert(bird3.fly() == "I can fly!")

    bird4 = MessengerBird("Homing Pigeon")
    assert(bird4.deliverMessage() == "")
    bird4.layEgg()
    assert(bird4.countEggs() == 1)
    assert(getLocalMethods(MessengerBird) == ['__init__', 'deliverMessage'])
    print("Done!")

def testAlternatingSum():
    print("Testing Alternating Sum...", end="")
    assert(alternatingSum([1])==1)
    assert(alternatingSum([1,2])==-1)
    assert(alternatingSum([1,2,3])==2)
    assert(alternatingSum([1,2,3,4])==-2)
    assert(alternatingSum([1,2,3,4,5])==3)
    print("Passed!")

def testGenerateCharacterString():
    print("Testing Generating charater string...", end="")
    assert(generateCharacterString("af") == "abcdef")
    assert(generateCharacterString("ko") == "klmno")
    assert(generateCharacterString("ME") == "MLKJIHGFE")
    assert(generateCharacterString("22") == "2")
    assert(generateCharacterString("ep") == "efghijklmnop")
    print("Passed!")

def generateCharacterString(string):
    if(len(string)<1):
        return ""
    elif(len(string)==2 and string[0]==string[1]):
        return string[0]
    elif(string[1]>string[0]):
        return string[0]+generateCharacterString(chr(ord(string[0])+1)+string[1])
    else:
        return string[0]+generateCharacterString(chr(ord(string[0])-1)+string[1])

def testPowersOf3ToN():
    print("Testing Powers of 3 to N...", end="")
    print("Printing 1",(powersOf3ToN(1)))
    print("Printing 2",(powersOf3ToN(2)))
    print("Printing 3",(powersOf3ToN(3)))
    print("Printing 4",(powersOf3ToN(4)))
    print("Printing 5",(powersOf3ToN(5)))
    print("Printing 6",(powersOf3ToN(6)))
    print("Printing 10",(powersOf3ToN(10)))
    print("Printing 15",(powersOf3ToN(15)))
    print("Printing 33",(powersOf3ToN(33)))
    assert(powersOf3ToN(2) == [1])
    assert(powersOf3ToN(6) == [1,3])
    assert(powersOf3ToN(10) == [1,3,9])
    assert(powersOf3ToN(11) == [1,3,9])
    assert(powersOf3ToN(29) == [1,3,9,27])
    print("Passed!")

def powersOf3ToN(n):
    if(n<1):
        return []
    elif (n==1) or (n==2):
        return [1]
    else:
        return powersOf3ToN(n//3) + [powersOf3ToN(n//3)[-1]*3]

class Polynomial(object):
    def __init__(self, coeffs):
        self.coeffs = []
        for i in range(len(coeffs)):
            if not (coeffs[i]==0):
                self.coeffs = coeffs[i:]
                break
        self.coeffs = list(self.coeffs)
        
    def __repr__(self):
        string = "Polynomial(coeffs=["
        for i in range(len(self.coeffs)-1):
            string+= "%d, "
        string += "%d])"
        return string%tuple(self.coeffs)

    def __eq__(self, other):
        if(len(self.coeffs)==1):
            return self.coeffs[0] == other
        
        return isinstance(other,Polynomial) and self.coeffs == other.coeffs

    def __hash__(self):
        return hash(tuple(self.coeffs))

    def degree(self):
        return len(self.coeffs)-1

    def coeff(self, n):
        return self.coeffs[-1-n]

    def evalAt(self, x):
        evalVal = 0
        for i in range(len(self.coeffs)):
            evalVal += (self.coeffs[i] * (x**(len(self.coeffs[i+1:]))))
        return evalVal 

    def scaled(self, m):
        return Polynomial([m*i for i in self.coeffs])
    
    def derivative(self): # 4x - 3
        derivateCoeffs = []
        for i in range(len(self.coeffs)-1):
            derivateCoeffs.append(len(self.coeffs[i+1:])*self.coeffs[i])
        return Polynomial(derivateCoeffs)
    
    def addPolynomial(self, other):
        if (type(other)!=Polynomial):
            return None
        if(len(self.coeffs) == len(other.coeffs)):
            return Polynomial([self.coeffs[i]+other.coeffs[i] for i in range(len(self.coeffs))])
        elif(len(self.coeffs) > len(other.coeffs)):
            poly1 = self.coeffs
            poly2 = [0]*(len(self.coeffs)-len(other.coeffs))+other.coeffs
        elif(len(self.coeffs) < len(other.coeffs)):
            poly1 = other.coeffs
            poly2 = [0]*(len(other.coeffs)-len(self.coeffs))+self.coeffs
        return Polynomial([poly1[i]+poly2[i] for i in range(len(poly1))])

    def multiplyPolynomial(self,other):
        multiPoly = [0]*(len(self.coeffs)+len(other.coeffs)-1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                multiPoly[i+j] += self.coeffs[i]*other.coeffs[j]
        return Polynomial(multiPoly)

class Quadratic(Polynomial):
    def __init__(self,coeffs):
        if(len(coeffs)!=3):
            raise("Error")
        self.coeffs = coeffs

    def __repr__(self):
        return "Quadratic(a=%d, b=%d, c=%d)"%(self.coeffs[0], self.coeffs[1], self.coeffs[2])

    def discriminant(self):
        self.disc = self.coeffs[1]**2 - 4 * self.coeffs[0] * self.coeffs[2] 
        return self.disc

    def numberOfRealRoots(self):
        self.discriminant()
        if self.disc < 0:
            return 0
        elif self.disc == 0:
            return 1
        else:
            return 2
    
    def getRealRoots(self):
        import math
        self.discriminant()
        if self.disc < 0:
            return [ ]
        elif self.disc == 0:
            return [(-self.coeffs[1])/(2*self.coeffs[0])]
        else:
            return [(-self.coeffs[1] - math.sqrt(self.disc))/(2*self.coeffs[0]),
                    (-self.coeffs[1] + math.sqrt(self.disc))/(2*self.coeffs[0])]

def testPolynomialBasics():
    # we'll use a very simple str format...
    assert(str(Polynomial([1,2,3])) == "Polynomial(coeffs=[1, 2, 3])")
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
    assert(p1.degree() == 2)

    # p.coeff(i) returns the coefficient for x**i
    assert(p1.coeff(0) == 5)
    assert(p1.coeff(1) == -3)
    assert(p1.coeff(2) == 2)

    # p.evalAt(x) returns the polynomial evaluated at that value of x
    assert(p1.evalAt(0) == 5)
    assert(p1.evalAt(2) == 7)

def testPolynomialEq():
    assert(Polynomial([1,2,3]) == Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,3,0]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,0,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,-2,3]))
    assert(Polynomial([1,2,3]) != 42)
    assert(Polynomial([1,2,3]) != "Wahoo!")
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert(Polynomial([42]) == 42)

def testPolynomialConstructor():
    # If the list is empty, treat it the same as [0]
    assert(Polynomial([]) == Polynomial([0]))
    assert(Polynomial([]) != Polynomial([1]))
    # In fact, disregard all leading 0's in a polynomial
    assert(Polynomial([0,0,0,1,2]) == Polynomial([1,2]))
    assert(Polynomial([0,0,0,1,2]).degree() == 1)

    # Require that the constructor be non-destructive
    coeffs = [0,0,0,1,2]
    assert(Polynomial(coeffs) == Polynomial([1,2]))
    assert(coeffs == [0,0,0,1,2])

    # Require that the constructor also accept tuples of coefficients
    coeffs = (0, 0, 0, 1, 2)
    assert(Polynomial(coeffs) == Polynomial([1,2]))

def testPolynomialInSets():
    s = set()
    assert(Polynomial([1,2,3]) not in s)
    s.add(Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) in s)  
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2]) not in s)

def testPolynomialMath():
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5

    # p.scaled(scale) returns a new polynomial with all the
    # coefficients multiplied by the given scale
    p2 = p1.scaled(10) # 20x**2 - 30x + 50
    assert(isinstance(p2, Polynomial))
    assert(p2.evalAt(0) == 50)
    assert(p2.evalAt(2) == 70)

    # p.derivative() will return a new polynomial that is the derivative
    # of the original, using the power rule: 
    # More info: https://www.mathsisfun.com/calculus/power-rule.html
    p3 = p1.derivative() # 4x - 3
    assert(type(p3) == Polynomial)
    assert(str(p3) == "Polynomial(coeffs=[4, -3])")
    assert(p3.evalAt(0) == -3)
    assert(p3.evalAt(2) == 5)

    # we can add polynomials together, which will add the coefficients
    # of any terms with the same degree, and return a new polynomial
    p4 = p1.addPolynomial(p3) # (2x**2 -3x + 5) + (4x - 3) == (2x**2 + x + 2)
    assert(type(p4) == Polynomial)
    assert(str(p4) == "Polynomial(coeffs=[2, 1, 2])")
    assert(p1 == Polynomial([2, -3, 5]))
    assert(p4.evalAt(2) == 12)
    assert(p4.evalAt(5) == 57)
    # can't add a string and a polynomial!
    assert(p1.addPolynomial("woo") == None)

    # lastly, we can multiple polynomials together, which will multiply the 
    # coefficients of two polynomials and return a new polynomial with the 
    # correct coefficients. 
    # More info: https://www.mathsisfun.com/algebra/polynomials-multiplying.html

    p1 = Polynomial([1, 3])
    p2 = Polynomial([1, -3])
    p3 = Polynomial([1, 0, -9])
    assert(p1.multiplyPolynomial(p2) == p3) # (x + 3)(x - 3) == (x**2 - 9)
    assert(p1 == Polynomial([1, 3]))

    # (x**2 + 2)(x**4 + 3x**2) == (x**6 + 5x**4 + 6x**2)
    p1 = Polynomial([1,0,2])
    p2 = Polynomial([1,0,3,0,0])
    p3 = Polynomial([1,0,5,0,6,0,0])
    assert(p1.multiplyPolynomial(p2) == p3)

def testPolynomialClass():
    print('Testing Polynomial class...', end='')
    testPolynomialBasics()
    testPolynomialEq()
    testPolynomialConstructor()
    testPolynomialInSets()
    testPolynomialMath()
    print('Passed!')

def testQuadraticClass():
    import math
    print("Testing Quadratic class...", end="")
    # Quadratic should inherit properly from Polynomial
    q1 = Quadratic([3,2,1])  # 3x^2 + 2x + 1
    assert(type(q1) == Quadratic)
    assert(isinstance(q1, Quadratic) and isinstance(q1, Polynomial))
    assert(q1.evalAt(10) == 321)
    assert(str(q1) == "Quadratic(a=3, b=2, c=1)")

    # We use the quadratic formula to find the function's roots. 
    # More info: https://www.mathsisfun.com/quadratic-equation-solver.html

    # the discriminant is b**2 - 4ac
    assert(q1.discriminant() == -8)
    # use the discriminant to determine how many real roots (zeroes) exist
    assert(q1.numberOfRealRoots() == 0)
    assert(q1.getRealRoots() == [ ])

    # Once again, with a double root
    q2 = Quadratic([1,-6,9])
    assert(q2.discriminant() == 0)
    assert(q2.numberOfRealRoots() == 1)
    [root] = q2.getRealRoots()
    assert(math.isclose(root, 3))
    assert(str(q2) == "Quadratic(a=1, b=-6, c=9)")

    # And again with two roots
    q3 = Quadratic([1,1,-6])
    assert(q3.discriminant() == 25)
    assert(q3.numberOfRealRoots() == 2)
    [root1, root2] = q3.getRealRoots() # smaller one first
    assert(math.isclose(root1, -3) and math.isclose(root2, 2))

    # Creating a non-quadratic "Quadratic" is an error
    ok = False # the exception turns this to True!
    try: q = Quadratic([1,2,3,4]) # this is cubic, should fail!
    except: ok = True
    assert(ok)
    # one more time, with a line, which is sub-quadratic, so also fails
    ok = False
    try: q = Quadratic([2,3])
    except: ok = True
    assert(ok)

    # And make sure that these methods were defined in the Quadratic class
    # and not in the Polynomial class (we'll just check a couple of them...)
    assert('evalAt' in Polynomial.__dict__)
    assert('evalAt' not in Quadratic.__dict__)
    assert('discriminant' in Quadratic.__dict__)
    assert('discriminant' not in Polynomial.__dict__)
    print("Passed!")

def testEquationClasses():
    testPolynomialClass()
    testQuadraticClass()

def testAll():    
    testAlternatingSum()
    testVendingMachineClass()
    testBirdClasses()
    testGenerateCharacterString()
    testPowersOf3ToN()
    testEquationClasses()

def main():
    testAll()

if __name__ == '__main__':
    main()