# hw1.5.py
# 입력 데이터의 통계를 분석하는 프로그램
# Author: 박창협
# Programed on August. 30. 2021

NUM_DATA = 10
data = []
sum = 0
print("input {} data".format(NUM_DATA))

for i in range(NUM_DATA):
    i = float(input())
    data.append(i)
    sum += i

avg = sum / NUM_DATA
max = data[0]
min = data[0]
temp = 0

for i in range(NUM_DATA):
    if data[i] > max:
        max = data[i]
    if data[i] < min:
        min = data[i]
    
    temp += (avg - data[i]) * (avg - data[i])

var = temp / NUM_DATA
import math
std_dev = math.sqrt(var)

print("average = {0:.5}, max_num = {1}, min_num = \
{2}, variation = {3:.5}, std_deviation = {4:.5}".format(avg, max, min, var, std_dev))
