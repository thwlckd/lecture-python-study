# hw2.4.py
# 직육면체의 가로, 세로, 높이를 입력받아 그 표면적과 부피를 구하는 프로그램
# Author: 박창협
# Programed on September. 06. 2021

width = int(input("직육면체의 가로를 입력하세요."))
height = int(input("직육면체의 세로를 입력하세요."))
colume = int(input("직육면체의 높이를 입력하세요."))

surf_area = 2 * width * height + 2 * width * colume + 2 * height * colume
vol = width * height * colume

print("표면적: {0}, 부피: {1}".format(surf_area, vol))
