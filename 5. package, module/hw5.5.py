# hw5.5.py
# 사용자 정의 모듈(MyMatrix.py)을 사용한 행렬 연산 프로그램
# Author: 박창협
# Programed on October. 04. 2021

import sys

myPyPackage_dir = "C:/"
sys.path.append(myPyPackage_dir)
from MyPyPackage.myModules import MyMatrix

A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[1,0,0], [0,1,0], [0,0,1]]

print("A = ", A)
print("B = ", B)

C = MyMatrix.mtrxAdd(A, B)
print("C = A + B = ", C)

D = MyMatrix.mtrxSub(A, B)
print("D = A - B = ", D)

E = MyMatrix.mtrxMul(A, B)
print("E = A * B = ", E)