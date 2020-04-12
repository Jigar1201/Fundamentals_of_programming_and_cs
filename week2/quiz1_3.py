def pairedNumber(n):
    if((n//10000== ((n//100)%100)) and (n//10000==n%100)):
        return True
    return False
print(pairedNumber(121212))
print(pairedNumber(121312))
print(pairedNumber(1212))
print(pairedNumber(565656))
print(pairedNumber(555))