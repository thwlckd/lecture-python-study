# hw7.1.py
# Program for using demography.txt
# Author: 박창협
# Programed on October. 11. 2021

list_country = []
list_capital = []
list_population = []
list_area = []

file_path = "C:/Users/박창협/Desktop/과제/파이썬프로그래밍과응용/py/hw7/demography.txt"
f = open(file_path, 'r')
for line in f.readlines():
    country, capital, population, area = line.split()
    list_country.append(country)
    list_capital.append(capital)
    list_population.append(int(population))
    list_area.append(int(area))
f.close()

countrys = list(zip(list_country, list_capital, list_population, list_area))
print("List of countries:")
for i in range(len(countrys)):
    print("Country[{}] : {}".format(i, countrys[i]))

print("\nAfter sorting by population:")
countrys.sort(key = lambda x : x[2], reverse = True)
for i in range(len(countrys)):
    print("Country[{}] : {}".format(i, countrys[i]))
