# hw5.1.py
# 사용자 정의 패키지, 모듈 테스트 프로그램(MyList.py)
# Author: 박창협
# Programed on October. 04. 2021

import sys

myPyPackage_dir = "C:/"
sys.path.append(myPyPackage_dir)
from MyPyPackage.myModules import MyList

L = []
n = 100
MyList.genRandList(L, n)
MyList.printListSample(L, n, 10, 5)
