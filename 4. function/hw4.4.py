# hw4.4.py
# 메모기능을 포함하는 재귀함수 dynFibo(n)를 활용한 피보나치 수열계산
# Author: 박창협
# Programed on September. 28. 2021

memo = dict()
def dynFibo(n):
    if n in memo:
        return memo[n]
    elif n <= 1:
        memo[n] = n
        return n
    else:
        fibo_n = dynFibo(n-1) + dynFibo(n-2)
        memo[n] = fibo_n
        return fibo_n

import time

start, stop, step = map(int, input("input start, stop, step of Fibonacci series: ").split())
for i in range(start, stop+1, step):
    before_t = time.time()
    fibo = dynFibo(i)
    after_t = time.time()
    elaped_t = after_t - before_t
    print("dyFibo({0:3}) = {1:23}, took {2:5}[milli_sec]".format(i, fibo, elaped_t*1000))
    