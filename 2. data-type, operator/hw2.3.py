# hw2.3.py
# 원의 반지름을 입력 받아, 원의 넓이, 원둘레를 구하는 프로그램
# Author: 박창협
# Programed on September. 06. 2021


radius = int(input("원의 반지름을 입력하세요."))

import math
area = math.pi * radius * radius
circumference = 2 * math.pi * radius

print("넓이: {0}, 원둘레: {1}".format(area, circumference))
