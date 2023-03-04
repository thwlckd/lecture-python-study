
# PyApp.py - Test Program for PyCppExt
'''
import PyCppExt
print("Testing PyCppExt on Visual Studio 2019")
probe_result = PyCppExt.probe()
print("Result of PyCppExt.probe() = ", probe_result)
'''


# PyApp - Test Program for PyCppExt (1)
import math
import PyCppExt
import numpy as np

print("Testing PyCppExt on Visual Studio 2019")
print("math.pi = ", math.pi)

probe_result = PyCppExt.probe()
print("Result of PyCppExt.probe() = ", probe_result)
add_result = PyCppExt.add(3, 5)
print("PyCppExt.add(3, 5) = ", add_result)

mul_result = PyCppExt.mul(3.1, 5.2)
print("PyCppExt.mul(3.1, 5.2) = ", mul_result)

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
B = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
C = PyCppExt.add_arrays(A, B)
print("A = ", A)
print("B = ", B)
print("PyCppExt.add_arrays(A, B) = ", C)
sorted_B = PyCppExt.sort_array(B)
print("Sorted_B = ", sorted_B)

# PyApp - Test Program for PyCppExt (2)

A = np.arange(0.1, 10.0, 1.1)
B = np.arange(9.9, 0.0, -1.1)
C = PyCppExt.add_arrays(A, B)
print("A = ", A)
print("B = ", B)
print("PyCppExt.add_arrays(A, B) = ", C)
sorted_B = PyCppExt.sort_array(B)
print("Sorted_B = ", sorted_B)



'''
import PyCppExt

a = [9,0,6,7,4,2,8,1,3,5]
print(a)
PyCppExt.merge(a,0,9)
print(a)
'''



