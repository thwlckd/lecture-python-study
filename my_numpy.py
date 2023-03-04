# # NumPy ndarray
# import numpy as np
# A = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32) #dtype = "i4"
# print("A : \n", A)
# print("A.dtype : ", A.dtype)
# print("A.ndim : ", A.ndim)
# print("A.shape : ", A.shape)  # (행, 열)
# print("A.size : ", A.size)  # element size
# print("A.itemsize : ", A.itemsize)  # element 자료형 크기(byte)
# print("A.data : ", A.data)  # 배열의 버퍼
# A = np.arange(3)  # 1차원 배열 생성
# print("A : ", A)
# print("A.type : ", A.dtype)
# B = np.arange(3.0)
# print("B : ", B)
# print("B.type : ", B.dtype)
# C = np.arange(3, 10)
# print("C : ", C)
# print("C.type : ", C.dtype)
# D = np.arange(3, 10, 2)
# print("D : ", D)
# print("D.type : ", D.dtype)
# A1 = np.zeros(6)  # 요소가 모두 0인 배열 생성
# print("A1 : \n", A1)
# A2 = np.zeros((2, 3))
# print("A2 : \n", A2)
# A3 = np.zeros((2, 3), dtype=np.int32)
# print("A3 : \n", A3)
# A4 = np.zeros((3, 2), dtype=np.int32)
# print("A4 : \n", A4)
# A5 = np.zeros((3, 4), dtype=np.int64, order='C')
# print("A5 : \n", A5)
# B1 = np.ones((2, 3))  # 요소가 모두 1인 배열 생성
# print("B1 : \n", B1)
# B2 = np.zeros((2, 3))
# print("B2 : \n", B2)
# B3 = np.empty((2, 3))
# print("B3 : \n", B3)
# B4 = np.full((2, 3), 10, dtype=None, order='C')
# print("B4 : \n", B4)


# # NumPy ndarray - linspace(), logspace()
# import numpy as np
# E1 = np.linspace(0.0, 10.0, num=5)
# print("E1 : \n", E1)
# E2 = np.linspace(0.0, 10.0, num=5, endpoint=False, retstep=True)
# print("E2 : \n", E2)
# E3 = np.logspace(0.1, 1, num=10)
# print("E3 : \n", E3)
# E4 = np.linspace(0.1, 1, num=10)
# print("E4 : \n", E4)
# E5 = np.power(10, E4).astype('float64')
# print("E5 : \n", E5)


# # NumPy ndarray - linspace(), logspace()
# import numpy as np
# dt = np.dtype('<i4') # < means little endian
# print("dt.byteorder : ", dt.byteorder)
# print("dt.itemsize : ", dt.itemsize)
# print("dt.name : ", dt.name)
# dt2 = np.dtype([('name', np.str_, 16), ('scores', np.float64, (2, ))])
# A = np.array([('Kim', (80.0, 90.0)), ('Lee', (70.0, 80.0))], dtype=dt2)
# print("A : ", A)
# print("A[0] : ", A[0])
# print("A[0]['name'] : ", A[0]['name'])
# print("A[0]['scores'] : ", A[0]['scores'])
# print("type(A[0]) : ", type(A[0]))
# print("type(A[0]['name']) : ", type(A[0]['name']))
# print("type(A[0]['scores']) : ", type(A[0]['scores']))



# # NumPy ndarray - linspace(), logspace()
# import numpy as np
# A = np.array([1, 2, 3])
# B = np.array([4, 5, 6])
# C = np.vstack((A, B))
# print("A : ", A)
# print("B : ", B)
# print("C : ", C)
# D = np.vstack(([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]))
# print("D : \n", D)
# E = np.split(D, 2)   
# print("E : \n", E)
# F = np.split(D, [2, 3])  # 2, 3 -> 분할이 2번째 3번째에서 일어남
# print("F : \n", F)



# # NumPy ndarray - hstack(), hsplit()
# import numpy as np
# A = np.array([1, 2, 3])
# B = np.array([4, 5, 6])
# C = np.hstack((A, B))
# print("A : ", A)
# print("B : ", B)
# print("C : ", C)
# D = np.array([[1], [2], [3]])
# E = np.array([[4], [5], [6]])
# F = np.hstack((D, E))
# print("D : \n", D)
# print("E : \n", E)
# print("F : \n", F)
# G = np.arange(8).reshape(2,4)  # 2행 4열로 reshape
# print("G : \n", G)
# H = np.hsplit(G, 2)
# print("H : \n", H)
# K = np.hsplit(G, [2, 3])
# print("K : \n", K)



# # NumPy ndarray(11) – shape(), reshape()
# import numpy as np
# A = np.arange(10)
# print("A : ", A)
# print("A.ndim : ", A.ndim)
# print("A.shape : ", A.shape)
# B = A.reshape((2, 5))
# print("B : ", B)
# print("B.ndim : ", B.ndim)
# print("B.shape : ", B.shape)
# C = A.reshape((5, -1))
# print("C : \n", C)
# print("A : ", A)
# A.shape = (5, 2)
# print("After A.shape(5, 2) ==> A : \n", A)
# print("B : \n", B)
# D = B.ravel()  # 1차원 배열로 반환
# print("D ( = B.ravel()) : ", D)
# E = B.flatten()  # 1차원 배열로 반환
# print("E ( = B.flatten()): ", E)



# # NumPy ndarray(12) - transpose()
# import numpy as np
# A = np.arange(15).reshape(5, 3)
# print("A : \n", A)
# B = A.T  # 전치행렬
# print("B (A.T) : \n", B)
# C = A.transpose()  # 전치행렬
# print("C (A.transpose()) : \n", C)



# # NumPy ndarray indexing, slicing (1) 
# import numpy as np
# A = np.arange(10)
# print("A : \n", A)
# print("A[0] : ", A[0])
# print("A[-1] : ", A[-1])
# print("A[:5] : ", A[:5])
# print("A[::2] : ", A[::2])
# A[:5] = 10
# print("After A[:5] = 10 ==> A : \n", A)
# B = A[5:]
# print("B (A[5:]) : \n", B)
# B[0] = 20
# print("After B[0]=20 ==> A : \n", A)
# C = A[5:].copy()
# C[0] = 30
# print("After C[0]=30 ==> A : \n", A)
# print("A : \n", A)



# # NumPy 2-Dimensional ndarray indexing, slicing 
# import numpy as np
# A = np.arange(12).reshape((3,4))
# print("A : \n", A)
# print("A[0] : ", A[0])
# print("A[:2] : ", A[:2])
# B = A[:, :1] # from all rows, select 0-th element
# print("B (A[:, :1]) : \n", B)
# C = A[:, 1:3] # from all rows, select 1-st and 2-nd elements
# print("C (A[:, 1:3]) : \n", C)
# D = A[:, 1:3].copy()
# print("D (A[:, 1:3].copy()) : \n", D)
# A[:, 1:3] = -1
# print("After A[:, 1:3] = -1 ==> A : \n", A)
# A[:, 1:3] = D
# print("After A[:, 1:3] = D ==> A : \n", A)



# # NumPy ndarray arithmetic operations (1) - add, sub, mult, div
# import numpy as np
# A = np.arange(10).reshape(2, 5)
# print("A : \n", A)
# B = A+10
# print("B (A+10) : \n", B)
# C = A-10
# print("C (A-10) : \n", C)
# D = A*10
# print("D (A*10) : \n", D)
# E = A/10
# print("E (A/10) : \n", E)
# F = A//2
# print("F (A//2) : \n", F)
# G = A%2
# print("G (A%2) : \n", G)
# H = A**2
# print("H (A**2) : \n", H)
# K = A*10 - 50
# print("K (A*10 - 50) : \n", K)
# M = abs(A*10 - 50)
# print("M (abs(A*10 - 50)) : \n", M)



# # NumPy ndarray arithmetic operations (2) - relational, logical
# import numpy as np
# A = np.arange(10).reshape(2, 5)
# print("A : \n", A)
# B = A<5
# print("B (A<5) : \n", B)
# C = A>5
# print("C (A>5) : \n", C)
# D = (A%2 == 0)
# print("D (A%2 == 0) : \n", D)
# E = (A%2 != 0)
# print("E (A%2 != 0) : \n", E)
# F = (A>5).any()
# print("F ((A>5).any()) : \n", F)
# G = (A>5).all()
# print("G ((A>5).all()) : \n", G)
# H = np.logical_and(A%2==0, A>5)
# print("H (np.logical_and(A%2==0, A>5)) : \n", H)
# K = np.logical_or(A%2==0, A>5)
# print("K (np.logical_or(A%2==0, A>5)) : \n", K)
# M = np.logical_not(A%2==0)
# print("M (np.logical_not(A%2==0)) : \n", M)



# # NumPy 2-Dimensional ndarray - sum(), sum(-1) 
# import numpy as np
# A = np.arange(12).reshape((4, 3))
# print("A = \n", A)
# total_sum = A.sum() # sum all elements
# print("A.sum() = \n", total_sum)
# sum_0 = A.sum(0) # sum along axis=0 (column)
# print("A.sum(0) = \n", sum_0)
# sum_1 = A.sum(1) # sum along axis=1 (row)
# print("A.sum(1) = \n", sum_1)
# rowsum = A.sum(-1) # sum along the last axis (row)
# print("A.sum(-1) = \n", rowsum)



# # NumPy 3-Dimensional ndarray - sum(), sum(-1) 
# import numpy as np
# A = np.arange(27).reshape((3, 3, 3))
# print("A = \n", A)
# total_sum = A.sum() # sum all elements
# print("A.sum() = \n", total_sum)
# sum_0 = A.sum(0) # sum along axis=0 (depth)
# print("A.sum(0) = \n", sum_0)
# sum_1 = A.sum(1) # sum along axis=1 (col)
# print("A.sum(1) = \n", sum_1)
# sum_2 = A.sum(2) # sum along axis=2 (row)
# print("A.sum(2) = \n", sum_2)
# sum_last_axis = A.sum(-1) # sum along the last axis (row)
# print("(A.sum(-1)) = \n", sum_last_axis)



# # universal function – reduce()
# import numpy as np
# A = np.arange(10)
# print("A : \n", A)
# a = np.add.reduce(A)
# print("a = np.add.reduce(A) : ", a)
# B = np.arange(9).reshape((3, 3))
# print("B : \n", B)
# r0 = np.add.reduce(B, 0) # sum axis 0 (column)
# r1 = np.add.reduce(B, 1) # sum axis 1 (row)
# print("r0 :", r0)
# print("r1 :", r1)
# C = np.arange(8).reshape((2,2,2))
# print("C : \n", C)
# s0 = np.add.reduce(C, 0) # axis 0 (depth)
# s1 = np.add.reduce(C, 1) # axis 1 (column)
# s2 = np.add.reduce(C, 2) # axis 2 (row)
# print("s0 :", s0)
# print("s1 :", s1)
# print("s2 :", s2)



# # universal function - add
# import numpy as np
# x1 = np.arange(9.0).reshape((3, 3))
# print("x1 = \n", x1)
# x2 = np.add(x1, x1)
# print("x2 = np.add(x1, x1) : \n", x2)
# np.add(x1, x2, x1)
# print("x1 after np.add(x1, x2, x1) : \n", x1)



# # set (1)
# import numpy as np
# A = np.array([1, 6, 4, 4, 3, 3, 5, 5, 2])
# print("A : ", A)
# B = np.unique(A)
# print("B : ", B)
# u, indx = np.unique(A, return_index=True)
# print("u : ", u)
# print("indx : ", indx)
# print("A[indx] : ", A[indx])




# # set (2) - in, intersect, setdiff, union, setxor
# import numpy as np
# A = np.array([1, 2, 3, 4])
# B = np.array([0, 2, 3])
# print("A : ", A)
# print("B : ", B)
# mask = np.in1d(A, B)
# print("mask : ", mask)
# C = np.intersect1d(A, B)
# print("C : ", C)
# D = np.setdiff1d(A, B)
# print("D : ", D)
# E = np.union1d(A, B)
# print("E : ", E)
# F = np.setxor1d(A, B)
# print("F : ", F)
# from functools import reduce
# G = reduce(np.union1d, (A, B, [0, 5, 6]))
# print("G : ", G)




# # ndarray - text file input and output
# import math
# import numpy as np
# A = np.arange(12).reshape(3,4)
# print("np array A ; \n", A)
# print("Saving np array A ...")
# np.savetxt("npArray_A.txt", A)  # 배열을 텍스트 파일에 저장
# B = np.loadtxt("npArray_A.txt")  # 텍스트 파일로 부터 데이터를 읽음
# print("Loaded B : \n", B)




# # Benchmark Test of myQuickSort and NumPy sort (default quick sort) (1) 
# import time, sys, random
# from array import *
# import numpy as np

# def printArraySample(L, size, per_line = 10, sample_lines = 2):
#     for i in range(per_line*sample_lines):
#         if i % per_line == 0:
#             print("")
#         print("{:8}".format(L[i]), end="")        
#     print("\n    . . . .\n")
#     for i in range(size-per_line*sample_lines, size):
#         if i % per_line == 0:
#             print("")
#         print("{:8}".format(L[i]), end="")
#     print("")

# # def _partition(arr, left, right, pivot):
# #     while left <= right:
# #         while arr[left] < pivot:
# #             left += 1
# #         while arr[right] > pivot:
# #             right -= 1
# #         if left <= right:
# #             arr[left], arr[right] = arr[right], arr[left]
# #             left, right = left + 1, right - 1
# #     return left

# # def quickSort(arr, left, right):
# #     if right <= left:
# #         return

# #     pivot = arr[(left + right) // 2]
# #     mid = _partition(arr, left, right, pivot)
# #     quickSort(arr, left, mid - 1)
# #     quickSort(arr, mid, left)

# #     return quickSort(arr, 0, len(arr) - 1)

# def quick_sort(arr):
#     def sort(low, high):
#         if high <= low:
#             return

#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)

#     def partition(low, high):
#         pivot = arr[(low + high) // 2]
#         while low <= high:
#             while arr[low] < pivot:
#                 low += 1
#             while arr[high] > pivot:
#                 high -= 1
#             if low <= high:
#                 arr[low], arr[high] = arr[high], arr[low]
#                 low, high = low + 1, high - 1
#         return low

#     return sort(0, len(arr) - 1)

# def main():
#     while True :
#         array_size = int(input("array_size = "))
#         if array_size == 0:
#             break

#         # np.sort() for numpy array
#         B = np.arange(array_size)
#         print("\nArray created by numpy : ")
#         np.random.shuffle(B)
#         print("After shuffling by np.random.shuffle, before numpy.sort() : ")
#         printArraySample(B, array_size, 10, 2)
#         t1 = time.time()
#         B_Sorted = np.sort(B)  # 내장함수로 배열 정렬
#         t2 = time.time()
#         elapsedtime = t2 - t1
#         print("\nAfter numpy.sort() : ")
#         printArraySample(B_Sorted, array_size, 10, 2)
#         print('total elapsed time of numpy.sort() for {} integers : {} [sec] '.\
#         format(array_size, elapsedtime))
        
#         # myQuickSorting for numpy array
#         np.random.shuffle(B)
#         print("\nAfter shuffling & before myQuickSorting of array B (NumPy ndarray): ")
#         printArraySample(B, array_size, 10, 2)
#         print('my Quick sorting random integer Array (NumPy ndarray) ....')
        
#         t1 = time.time()
#         # quickSort(B, 0, array_size-1)
#         quick_sort(B)
#         t2 = time.time()
#         elapsedtime = t2 - t1
#         print("\nAfter QuickSorting : ")
#         printArraySample(B, array_size, 10, 2)
#         print('total elapsed time of my Quick Sort to sort {} integers : {} [sec] '.\
#         format(array_size, elapsedtime))
# if __name__ == "__main__":
#     main()



# # universal function for linear algebra - dot(), vdot()
# import numpy as np
# A = np.array([1, 2, 3])
# B = np.array([4, 5, 6])
# C = np.dot(A, B)  # 배열 곱
# print("A = ", A)
# print("B = ", B)
# print("C = np.dot(A, B) = ", C)
# X = np.array([1+2j, 3+4j])
# Y = np.array([5+6j, 7+8j])
# XY = np.vdot(X, Y) # in vdot, X’s conjugate is used
# YX = np.vdot(Y, X) # in vdot Y’s conjugate is used
# print("X = ", X)
# print("Y = ", Y)
# print("np.vdot(X, Y) = ", XY)
# print("np.vdot(Y, X) = ", YX)



# # universal function for linear algebra - inner(), outer()
# import numpy as np
# A = np.array([1, 2, 3])
# B = np.array([4, 5, 6])
# C = np.inner(A, B)  # 내적
# print("A = ", A)
# print("B = ", B)
# print("np.inner(A, B) = ", C)
# D = np.outer(A, B)  # 외적
# print("np.outer(A, B) = \n", D)
# E= np.matmul(A, B)  # 배열의 행렬 곱셈
# print("np.matmul(A, B) = ", E)
# # print("np.dot(A, B) = ", np.dot(A, B))
# X = np.array([[1, 2], [3, 4]])
# Y = np.array([[5, 6], [7, 8]])
# W = np.inner(X, Y)
# print("X = \n", X)
# print("Y = \n", Y)
# print("np.inner(X, Y) = \n", W)
# Z = np.outer(X, Y)
# print("np.outer(X, Y) = \n", Z)
# M= np.matmul(X, Y)
# print("np.matmul(X, Y) = \n", M)



# # linear algebra - inv(), det()
# import numpy as np
# A = np.array([[1,4, 1], [1, 6, -1], [2, -1, 2]])
# print("A : \n", A)
# d = np.linalg.det(A)  # 행렬식 계산
# print("d (determinent of A) : ", d)
# inv_A = np.linalg.inv(A)  # 역행렬 계산
# print("inv_A : \n", inv_A)
# B = np.matmul(A, inv_A)
# print("B : \n", B)



# # universal function for linear algebra - solve()
# import numpy as np
# A = np.array([[1, 1, 1], [2, 3, 1], [1, -1, -1]])
# B = np.array([4, 9, -2])
# X = np.linalg.solve(A, B)  # 선형 방정식 AX=B의 해 X를 구함
# B1 = np.matmul(A, X)
# print("A = \n", A)
# print("B = ", B)
# print("X = np.linalg.solve(A)")
# print("X = ", X)
# print("B1 = np.matmul(A, X) = ", B1)



# # Benchmark of Big Matrix Multiplication with Numpy
# import numpy as np
# import time

# def mtrx_mult_numpy(N, M, L, a, x, y):
#     return np.dot(x*a, y)

# if __name__ =='__main__':
#     np.random.seed(0)
#     N = 5000
#     M = 5000
#     L = 5000
#     a = np.random.random(M) - 0.5
#     x = np.random.random((N, M)) - 0.5
#     y = np.random.random((M, L)) - 0.5
#     print("Matrix multiplication for s[{}][{}] = A[{}] * X[{}][{}] * Y[{}][{}]"\
#         .format(N, L, M, N, M, M, L))
#     ts = time.time()
#     r2 = mtrx_mult_numpy(N, M, L, a, x, y)
#     te = time.time()
#     print("Matrix multiplication by NumPy dot took {:.3f}[ms]".format(1000*(te - ts)))

    


################ matplotlib ###############

# # matplotlib(1) - linear
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(5)
# y = []
# for n in range(len(x)):
#     d = 2.0*x[n] + 1
#     y.append(d)

# plt.plot(x, y, "b-", x, y, "ro")  # 선 그래프
# # plt.plot(x, y, "ro") 
# # plt.plot(x, y, "b-") 
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Example of matplotlib")
# plt.grid(True)
# plt.savefig("matplot_001.png")
# plt.show()



# # matplotlib(2) - squarer
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(start=-1, stop=1, num=51)
# y = x**2
# plt.plot(x, y, "b-", x, y, "ro")
# plt.axis([-1, 1, 0, 1])  # [xmin, xmax, ymin, ymax]

# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Example of matplotlib - y = x**2")
# plt.grid(True)
# plt.savefig("matplot_002_square.png")
# plt.show()



# # matplotlib(3) - sin(x), cos(x)
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 2*np.pi, num=41)  # 0~2pi를 41개로 나누도록 배열 생성
# sin_x, cos_x = np.sin(x), np.cos(x)
# plt.plot(x, sin_x, "k--", x, sin_x, "ro")
# plt.plot(x, cos_x, "b-", x, cos_x, "b*")

# xmin, xmax, ymin, ymax = x[0], x[-1], -1, 1
# plt.axis([xmin, xmax, ymin, ymax])
# plt.xlabel("x")
# plt.ylabel("sin(x), cos(x)")
# plt.title("Example of matplotlib - sin(x), cos(x)")
# plt.grid(True)
# plt.savefig("matplot_003_sin_cos.png")
# plt.show()



# # matplotlib(4) - Normal, Gaussian Distribution
# import numpy as np
# import matplotlib.pyplot as plt

# def gauss(mu, sigma, x):  # 가우시안 분포 PDF 구하는 함수
#     y = 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-((x - mu)**2)/(2*sigma**2))
#     return y

# mu, sigma = 0, 2
# x = np.linspace(-4*sigma, 4*sigma, num=101)
# y1 = gauss(mu, sigma, x)
# plt.plot(x, y1, color="red", label="sigma=2")

# mu, sigma = 0, 1
# y2 = gauss(mu, sigma, x)
# plt.plot(x, y2, color="green", label="sigma=1")

# mu, sigma = 0, 0.5
# y3 = gauss(mu, sigma, x)
# plt.plot(x, y3, color="blue", label="sigma=0.5")

# plt.title("Normal Distribution - sigma 0.5, 1, 2")

# plt.legend(loc="best")  # 그래프에 대한 정보 표시
# plt.grid(True)
# plt.savefig("matplot_004_GaussDist.png")
# plt.show()




# # matplotlib - 3D graphs
# import numpy as np
# import matplotlib.pyplot as plt 
# from matplotlib import cm 
# from mpl_toolkits.mplot3d import Axes3D 

# fig = plt.figure(figsize=(8, 8)) 
# fig.suptitle("$f(x,y) = x^2+y^2$", color='b',\
# fontsize=20)
# x = np.linspace(-5, 5, 7) 
# y = np.linspace(-5, 5, 7) 
# X, Y = np.meshgrid(x, y) 
# Z = X**2 + Y**2
# ax1 = fig.add_subplot(221, projection='3d') 
# surf = ax1.plot_wireframe(X, Y, Z) 
# ax1.set_title("wireframe")
# ax2 = fig.add_subplot(222, projection='3d') 
# surf = ax2.plot_surface(X, Y, Z, rstride=1,\
# cstride=1, cmap=cm.RdPu) 
# fig.colorbar(surf) 
# ax2.set_title("surface")
# ax3 = fig.add_subplot(223, projection='3d') 
# surf = ax3.contour(X, Y, Z)  # countour lines 
# surf = ax3.contourf(X, Y, Z)  #filled contours 
# ax3.set_title("contour")
# ax4 = fig.add_subplot(224, projection='3d') 
# surf = ax4.scatter(X, Y, Z) 
# ax4.set_title("scatter")
# plt.grid(True) 
# plt.savefig("matplot_005_3D graphic.png",\
# bbox_inches='tight') 
# plt.show()




# # matplotlib ‐ 3D graphic
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# PI = np.pi
# x = np.arange(-2*PI, 2*PI, 0.25)
# y = np.arange(-2*PI, 2*PI, 0.25)
# X, Y = np.meshgrid(x, y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# print("X = \n", X)
# print("Y = \n", Y)
# print("Z = \n", Z)
# ax = fig.gca(projection = '3d')
# surf = ax.plot_surface(X, Y, Z, rstride=1,\
# cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# ax.set_zlim(-1.02, 1.02)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title("Z = np.sqrt(X**2 + Y**2)")
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig.colorbar(surf, shrink=0.5, aspect=5) 
# plt.show()



# # Example animation with Matplotlib.animation
# import numpy as np 
# import matplotlib.pyplot as plt 
# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots() 
# xdata, y1data, y2data = [], [], [] 
# ln_1, = plt.plot([], [], 'ro', label="sin(x)") 
# ln_2, = plt.plot([], [], 'bd', label="cos(x)") 
# plt.xlabel("x(radian)") 
# plt.ylabel("sin(x), cos(x)") 
# plt.grid(True) 
# start, end = 0, 4*np.pi 
# num_steps = 256 
# plt.legend(loc="best")

# def init(): 
#     ax.set_xlim(start, end) 
#     ax.set_ylim(-1.2, 1.2) 
#     return ln_1, ln_2,

# def update(xn): 
#     xdata.append(xn) 
#     y1data.append(np.sin(xn)) 
#     y2data.append(np.cos(xn)) 
#     ln_1.set_data(xdata, y1data) 
#     ln_2.set_data(xdata, y2data) 
#     return ln_1, ln_2, 

# xn=np.linspace(start, end, num_steps) 
# ani = FuncAnimation(fig, update, xn, init_func=init, blit=True) 
# plt.show()







