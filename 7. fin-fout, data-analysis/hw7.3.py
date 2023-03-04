# hw7.3.py
# Program for using user defined module(myClassMtrx.py)
# Author: 박창협
# Programed on October. 11. 2021

import sys
myPyPackage_dir = "C:/"
sys.path.append(myPyPackage_dir)
from MyPyPackage.myModules import myClassMtrx

if __name__ == "__main__":
    data_1 = [ 
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]
    data_2 = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]]

    m1 = myClassMtrx.Mtrx("M1", 5, 5, data_1)
    print("m1 =\n{}".format(m1))

    m2 = myClassMtrx.Mtrx("M2", 5, 5, data_2)
    print("m2 =\n{}".format(m2))

    m3 = m1 + m2
    print("m3 = m1 + m2 =\n{}".format(m3))

    m4 = m1 - m2
    print("m4 = m1 ‐ m2 =\n{}".format(m4))

    m5 = m1 * m2
    print("m5 = m1 * m2 =\n{}".format(m5))