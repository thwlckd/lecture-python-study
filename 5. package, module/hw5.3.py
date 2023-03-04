# hw5.2.py
# list와 array를 비교하는 프로그램
# Author: 박창협
# Programed on October. 04. 2021

import time, sys
from array import *

sys.path.append("C:/")
from MyPyPackage.myModules import MyList, MySortings

AR = array('i')
L = []
size = 50000
MyList.genRandList(L, size)

for x in L:
    AR.append(x)

print("Array (size : {}) before sorting : ".format(size))
MyList.printListSample(AR, size, 10, 2)

t1 = time.time()
MySortings.selectionSort(AR)
t2 = time.time()

print("Array (size : {}) after sorting : ".format(size))
MyList.printListSample(AR, size, 10, 2)
print("Selection sorting for array of {} integers took {} sec"\
.format(size, t2-t1))

print("\nList (size : {}) before sorting : ".format(size))
MyList.printListSample(L, size, 10, 2)

t1 = time.time()
MySortings.selectionSort(L)
t2 = time.time()

print("\nList (size : {}) after sorting : ".format(size))
MyList.printListSample(L, size, 10, 2)
print("Selection sorting for list of {} integers took {} sec"\
.format(size, t2-t1))
