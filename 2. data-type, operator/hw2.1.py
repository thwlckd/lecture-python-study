# hw2.1.py
# 0 ~ 255 사이의 정수를 여러 진법으로 출력하는 프로그램
# Author: 박창협
# Programed on September. 06. 2021

data = int(input("0 ~ 255 사이의 정수를 입력하세요. "))

print("data = {} (10진수)".format(data))
print("data = {} (16진수)".format(hex(data)))
print("data = {} (8진수)".format(oct(data)))
print("data = {} (2진수)".format(bin(data)))
