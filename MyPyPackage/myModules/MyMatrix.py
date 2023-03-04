# MyMatrix.py

def mtrxAdd(A, B):
    C = [[x for x in range(len(A[1]))] for x in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[1])):
            C[i][j] = A[i][j] + B[i][j]    
    return C

def mtrxSub(A, B):
    C = [[x for x in range(len(A[1]))] for x in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[1])):
            C[i][j] = A[i][j] - B[i][j]    
    return C

def mtrxMul(A, B):
    C = [[x for x in range(len(B[1]))] for x in range(len(A))]
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] = 0
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]    
    return C
