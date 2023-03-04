# hw3.5.py
# dictionary를 활용한 유의어 사전 프로그램
# Author: 박창협
# Programed on September. 17. 2021

Thresaurus_Dict = {}
List_Voca = ["mean", "resume", "gentle", "unique", "evaluate",\
    "eligible", "present", "apparent", "compromise", "deteriorate"]

for i in range(len(List_Voca)):
    words = tuple(input("input theasaurs of {}: ".format(List_Voca[i])).split())
    Thresaurus_Dict[List_Voca[i]] = words   
    print(Thresaurus_Dict.items())
    
while True:
    keyword = input("input keyword to search for theasarus(exit to -1): ")
    if keyword == "-1":
        break
    if keyword not in List_Voca:
        print("input wrong keyword!!")
        continue
    print("Theasaurs of {} = {}".format(keyword, Thresaurus_Dict[keyword]))
