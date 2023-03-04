# hw3.2.py
# 자정까지 몇 초가 남았는지 계산하는 프로그램
# Author: 박창협
# Programed on September. 16. 2021

while True:
    hour, minute, second = map(int, input("input hour min sec(exit to -1 -1 -1): ").split())
    if hour == -1:
        break
    now_time = 3600*hour + 60*minute + second
    until_midnight = 3600*24 - now_time
    print("Elapsed time from last midnight: {}sec\
        \nRemaining time from next midnight: {}sec\n".format(now_time, until_midnight))

