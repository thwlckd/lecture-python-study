# hw5.2.py
# 사용자 정의 패키지, 모듈 테스트 프로그램(MySortings.py)
# Author: 박창협
# Programed on October. 04. 2021

import sys
myPyPackage_dir = "C:/"
sys.path.append(myPyPackage_dir)
from MyPyPackage.myModules import MyList, MySortings
L = []
n = 100
MyList.genRandList(L, n)
print("Before Sorting :")
MyList.printListSample(L, n, 10, 3)
MySortings.selectionSort(L)
print("\nAfter Sorting :")
MyList.printListSample(L, n, 10, 3)
