
def slow1(lst): # N is the length of the list lst
    assert(len(lst) >= 2)
    a = lst.pop()
    b = lst.pop(0)
    lst.insert(0, a)
    lst.append(b)

def slow2(lst): # N is the length of the list lst
    counter = 0
    for i in range(len(lst)):
        if lst[i] not in lst[:i]:
            counter += 1
    return counter

import string
def slow3(s): # N is the length of the string s
    maxLetter = ""
    maxCount = 0
    for c in s:
        for letter in string.ascii_lowercase:
            if c == letter:
                if s.count(c) > maxCount or \
                   s.count(c) == maxCount and c < maxLetter:
                    maxCount = s.count(c)
                    maxLetter = c
    return maxLetter

def slow4(a, b): # a and b are lists with the same length N
    n = len(a)
    assert(n == len(b))
    result = abs(a[0] - b[0])
    for c in a:
        for d in b:
            delta = abs(c - d)
            if (delta > result):
                result = delta
    return result