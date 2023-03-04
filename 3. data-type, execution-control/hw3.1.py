# hw3.1.py
# 서기 1년 1월 1일로 부터 몇 번째 날인지 계산하는 프로그램
# Author: 박창협
# Programed on September. 16. 2021

def leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 월별 일수
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Tursday", "Friday", "Saturday"]


while True:
    year, month, day = map(int, input("input year month day(exit to -1 -1 -1): ").split())
    if year == -1:
        break

    total_days = 0 
    for i in range(1, year):
        if leap_year(i)==True:
            total_days += 366  # leap year
        else:
            total_days += 365

    if month>2 and leap_year(year):
        months[2] = 29 # 입력 받은 날짜가 윤년이면 2월달 29일로 변경
    else:
        months[2] = 28

    for i in range(1, month):
        total_days += months[i]

    total_days += day
    weekday = days[total_days%7]

    print("Day (year({}), month({}), day({})): \
        \n{} days Elapsed from Jan01AD01 \nweek day = {}\n"\
        .format(year, month, day, total_days, weekday))



