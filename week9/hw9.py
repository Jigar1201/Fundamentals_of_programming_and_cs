#  range, sum, max, min, reversed, sorted, list.count, list.sort, list.reverse, str.replace, and str.join.

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
            if(self.moneyOwe==0):
                return ("Still owe $%0.0f"%(self.moneyOwe/100), 0)
            elif(self.moneyOwe%100==0):
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

# class Bird(object):
#     def __init__():

#     def 

# def testBirdClasses():
#     print("Testing Bird classes...", end="")
#     # A basic Bird has a species name, can fly, and can lay eggs
#     bird1 = Bird("Parrot")
#     assert(type(bird1) == Bird)
#     assert(isinstance(bird1, Bird))
#     assert(bird1.fly() == "I can fly!")
#     assert(bird1.countEggs() == 0)
#     assert(str(bird1) == "Parrot has 0 eggs")
#     bird1.layEgg()
#     assert(bird1.countEggs() == 1)
#     assert(str(bird1) == "Parrot has 1 egg")
#     bird1.layEgg()
#     assert(bird1.countEggs() == 2)
#     assert(str(bird1) == "Parrot has 2 eggs")
#     assert(getLocalMethods(Bird) == ['__init__', '__repr__', 'countEggs', 
#                                      'fly', 'layEgg'])
    
#     # A Penguin is a Bird that cannot fly, but can swim
#     bird2 = Penguin("Emperor Penguin")
#     assert(type(bird2) == Penguin)
#     assert(isinstance(bird2, Penguin))
#     assert(isinstance(bird2, Bird))
#     assert(bird2.fly() == "No flying for me.")
#     assert(bird2.swim() == "I can swim!")
#     bird2.layEgg()
#     assert(bird2.countEggs() == 1)
#     assert(str(bird2) == "Emperor Penguin has 1 egg")
#     assert(getLocalMethods(Penguin) == ['fly', 'swim'])
    
#     # A MessengerBird is a Bird that can optionally carry a message
#     bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
#     assert(type(bird3) == MessengerBird)
#     assert(isinstance(bird3, MessengerBird))
#     assert(isinstance(bird3, Bird))
#     assert(not isinstance(bird3, Penguin))
#     assert(bird3.deliverMessage() == "Top-Secret Message!")
#     assert(str(bird3) == "War Pigeon has 0 eggs")
#     assert(bird3.fly() == "I can fly!")

#     bird4 = MessengerBird("Homing Pigeon")
#     assert(bird4.deliverMessage() == "")
#     bird4.layEgg()
#     assert(bird4.countEggs() == 1)
#     assert(getLocalMethods(MessengerBird) == ['__init__', 'deliverMessage'])
#     print("Done!")

def testAlternatingSum():
    print("Testing Alternating Sum...", end="")
    assert(alternatingSum([1])==1)
    assert(alternatingSum([1,2])==-1)
    assert(alternatingSum([1,2,3])==2)
    assert(alternatingSum([1,2,3,4])==-2)
    assert(alternatingSum([1,2,3,4,5])==3)
    print("Passed!")

def testAll():    
    testAlternatingSum()
    testVendingMachineClass()

def main():
    testAll()

if __name__ == '__main__':
    main()