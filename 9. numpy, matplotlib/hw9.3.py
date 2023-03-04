# hw9.3.py
# numpy를 사용한 행렬 계산
# Author: 박창협
# Programed on November. . 2021

import numpy as np

A = np.array([[1,2,3,4,5,6,7],[9,8,7,6,5,4,3],[3,7,5,1,0,1,2],\
    [4,1,0,2,8,3,7],[9,7,3,2,1,6,5],[7,5,3,1,2,4,6],[1,3,5,7,9,8,7]])
np.savetxt("A.txt", A)  # 배열 A를 A.txt로 저장
A = np.loadtxt("A.txt")  # A.txt를 불러옴
print("A =\n", A)

A_det = np.linalg.det(A)  # 행렬 절대값
print("A_det = ", A_det)

A_inv = np.linalg.inv(A)  # 역행렬
print("A_inv = ", A_inv)

E = np.matmul(A, A_inv)  # A*A^(-1) = 단위행렬
print("E = np.matmul(A, A_inv) = ", E)

