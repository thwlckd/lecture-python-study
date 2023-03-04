# hw3.4.py
# 10개국에 대한 정보의 튜플 표현과, 일정 인구수 이상의 국가를 뽑아 출력하기
# Author: 박창협
# Programed on September. 16. 2021

country = [("Korea", 51821669, "Seoul", "Korean", "Asia"), ("Japan", 126050796, "Tokyo", "Japanese", "Asia"),\
    ("China", 1444216102, "Beijing", "Chinese", "Asia"), ("USA", 332915074, "Washington DC", "English", "North Amarica"),\
    ("Canada", 38067913, "Ottawa", "English", "North America"), ("UK", 68207114, "London", "English", "Europe"),\
    ("France", 65426177, "Paris", "French", "Europe"), ("Mexico", 130262220, "Mexicocity", "Spanish", "North America"),\
    ("Germany", 83900471, "Berlin", "Germany", "Europe"), ("India", 1393409033, "New Delhi", "Hindu", "Asia")]

for i in range(len(country)):
    print("countries[{}]: name({:^8}), population({:>11}), capital({:<16}), language({:<9}), continent({:<14})"\
        .format(i, country[i][0], country[i][1], country[i][2], country[i][3], country[i][4]))

population = int(input("input threshold of population: "))
print("Countries whose population is greater than {}: ".format(population))

populous_country = []

for i in range(len(country)):
    if country[i][1] >= population:
        populous_country.append(country[i])

populous_country.sort(key = lambda x : x[1], reverse = True)

for i in range(len(populous_country)):
    print("countries[{}]: name({:^8}), population({:>11}), capital({:<16}), language({:<9}), continent({:<14})"\
    .format(i, populous_country[i][0], populous_country[i][1], populous_country[i][2], populous_country[i][3], populous_country[i][4]))
