# hw7.4.py
# Program for test json by using matrix from .txt file
# Author: 박창협
# Programed on October. 11. 2021

import json
import os, os.path, sys
sys.path.append("C:/")
from MyPyPackage.myModules import myClassMtrx
import CustomJsonEncoder

def main():
    file_path = "C:/Users/박창협/Desktop/과제/파이썬프로그래밍과응용/py/hw7/matrix_data.txt"
    f = open(file_path, 'r')
    
    n_row1, n_col1 = map(int, f.readline().split())
    matrix1 = []
    for i in range(n_row1):
        matrix1.append(list(float(x) for x in f.readline().split()))
    
    n_row2, n_col2 = map(int, f.readline().split())
    matrix2 = []
    for i in range(n_row2):
        matrix2.append(list(float(x) for x in f.readline().split()))
    f.close()

    mA = myClassMtrx.Mtrx("mA", n_row1, n_col1, matrix1)
    mB = myClassMtrx.Mtrx("mB", n_row2, n_col2, matrix2)
    
    print("n_row = {}, n_col = {}".format(mA.n_row, mA.n_col))
    print("mA =\n{}".format(mA))
    print("n_row = {}, n_col = {}".format(mB.n_row, mB.n_col))
    print("mB =\n{}".format(mB))
    mC = mA + mB
    print("mC = mA + mB =\n{}".format(mC))
    mD = mA - mB
    print("mD = mA ‐ mB =\n{}".format(mD))
    mE = mA * mB
    print("mE = mA * mB =\n{}".format(mE))

    print_file_path = "C:/Users/박창협/Desktop/과제/파이썬프로그래밍과응용/py/hw7/mA_json.txt"
    f_json = open(print_file_path, "w")
    json.dump(mA, f_json, indent=4, cls=CustomJsonEncoder.CustomEncoder)
    f_json.close()

    size_f_json = os.path.getsize(print_file_path)
    print("size of mA_json.txt = ", size_f_json)

if __name__ == "__main__":
    main()
