# hw4.2.py
# bigrand 병합정렬을 이용하여 정렬하는 프로그램
# Author: 박창협
# Programed on September. 27. 2021

import random

def genBigRandList(L, n):
    L.clear()
    count = 0
    a = list(x for x in range(n))
    while(count<n):
        rand = random.randint(0,n-count-1)
        bigrand = a[rand]
        L.append(bigrand)
        a.pop(rand)
        count += 1
    return L

def printListSample(L, per_line, sample_lines):
    for i in range(per_line*sample_lines):
        if i % per_line == 0:
            print("")
        print("{:8}".format(L[i]), end="")        
    print("\n    . . . .\n")
    for i in range(len(L)-per_line*sample_lines, len(L)):
        if i % per_line == 0:
            print("")
        print("{:8}".format(L[i]), end="")
    print("")

def merge_sort(L):
    if len(L) < 2:
        return L

    mid = len(L) // 2
    left_L = merge_sort(L[:mid])
    right_L = merge_sort(L[mid:])

    merged_L = []
    left = right = 0
    while left < len(left_L) and right < len(right_L):
        if left_L[left] < right_L[right]:
            merged_L.append(left_L[left])
            left += 1
        else:
            merged_L.append(right_L[right])
            right += 1
    merged_L += left_L[left:]
    merged_L += right_L[right:]
    return merged_L

import time

lst = [0]
while(True):
    num = int(input("input size of random list L(-1 to quit) = "))
    if num == -1:
        break
    lst = genBigRandList(lst, num)
    print("Before mergeSort of L :")
    printListSample(lst, 10, 2)
    print("After mergeSort of L :")
    before_t = time.time()
    lst = merge_sort(lst)
    after_t = time.time()
    printListSample(lst, 10, 2)
    elaped_t = after_t - before_t
    print("mergeSort() for list L (size:{} took {}sec)".format(num, elaped_t))
