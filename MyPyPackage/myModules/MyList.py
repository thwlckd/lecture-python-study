# MyList.py

import random

def genRandList(L, size):
    L.clear()
    count = 0
    a = list(x for x in range(size))
    while(count<size):
        rand = random.randint(0,size-count-1)
        bigrand = a[rand]
        L.append(bigrand)
        a.pop(rand)
        count += 1
    return L

def printListSample(L, size, per_line, sample_lines):
    for i in range(per_line*sample_lines):
        if i % per_line == 0:
            print("")
        print("{:8}".format(L[i]), end="")        
    print("\n    . . . .\n")
    for i in range(size-per_line*sample_lines, size):
        if i % per_line == 0:
            print("")
        print("{:8}".format(L[i]), end="")
    print("")

def shuffleList(L):
    for i in range(len(L)):
        rand = random.randrange(len(L))
        L[i], L[rand] = L[rand], L[i]
    return L
