# hw3.3.py
# 입력받은 날짜(튜플 리스트)를 오름차순으로 정렬하는 프로그램 
# Author: 박창협
# Programed on September. 17. 2021

dates = []

while True:
    year, month, day = map(int, input("input year month day(exit to 0 0 0): ").split())
    if year == 0:
        break
    date = (year, month, day)
    dates.append(date)
    print("input date: year({}), month({}), day({})".format(year, day, month))
    

print("List of dates: ", dates)

dates.sort(key = lambda x : x[2])
dates.sort(key = lambda x : x[1])
dates.sort(key = lambda x : x[0])

print("Sorted list of dates: ", dates)
