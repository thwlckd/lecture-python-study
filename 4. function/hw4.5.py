# hw4.5.py
# 행렬의 덧셈 뺄셈
# Author: 박창협
# Programed on September. 28. 2021

def matrixAdd(A, B, n_row, n_col):
    C = [[x for x in range(n_col)] for x in range(n_row)]
    for i in range(n_row):
        for j in range(n_col):
            C[i][j] = A[i][j] + B[i][j]
    print("C = A + B\n  = {0}".format(C))
    
    return C

def matrixSub(A, B, n_row, n_col):
    D = [[x for x in range(n_col)] for x in range(n_row)]
    for i in range(n_row):
        for j in range(n_col):
            D[i][j] = A[i][j] - B[i][j]
    print("D = A - B\n  = {0}".format(D))
    
    return D

A_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B_list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
print("A :", A_list)
print("B :", B_list)
matrixAdd(A_list, B_list, len(A_list), len(A_list[0]))
matrixSub(A_list, B_list, len(A_list), len(A_list[0]))
