# hw9.2.py
# numpy를 사용한 선형시스템 해 구하기
# Author: 박창협
# Programed on November. 12. 2021

import numpy as np

# AX = B
A = np.array([[10, 10, 0, 0, 0], [1, -1, -1, 0, 0], \
    [0, 0, 1, -1, -1], [0, 10, -5, -10, 0], [0, 0, 0, 10, -10]])
B = np.array([100, 0, 0, 0, 0])
X = np.linalg.solve(A, B)  # 선형 방정식 AX = B의 해 X 구함
B1 = np.matmul(A, X)  # 두 배열의 행렬 곱셈 

print("A = \n", A)
print("B = ", B)
print("X = ", X)
print("np.matmul(A, X) = ", B1)

