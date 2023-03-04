# hw9.1.py
# numpy를 사용해 생성한 랜덤 정규분포 배열의 통계 분석
# Author: 박창협
# Programed on November. 12. 2021

import numpy as np
from numpy.lib.shape_base import split

def printListSample(L, size, per_line, sample_lines):
    for i in range(per_line*sample_lines):
        if i % per_line == 0:
            print("")
        print("{:8}".format(round(L[i], 2)), end="")        
    print("\n    . . . .\n")
    for i in range(size-per_line*sample_lines, size):
        if i % per_line == 0:
            print("")
        print("{:8}".format(round(L[i], 2)), end="")
    print("")


##### main #####
while(True):
    mu, sigma = map(float, input("mu and sigma(in float): ").split())
    size = int(input("size of array(exit to -1): "))
    if size == -1:
        break
    print("Sample of G = np.random.normal({}, {}, {}) = ".format(mu, sigma, size))
    G = np.random.normal(mu, sigma, size)  # 랜덤 정규분포 배열 생성
    printListSample(G, size, 10, 3)

    G_mean = np.mean(G)  # 랜덤 정규분포 배열 평균
    G_var = np.var(G)  # 랜덤 정규분포 배열 분산
    G_std = np.std(G)  # 랜덤 정규분포 배열 표준편차
    print("mean of G = ",G_mean)
    print("var of G = ",G_var)
    print("std of G = ",G_std)
    print()
