# hw4.3.py
# 터틀 그래픽 기능을 이용한 다각형 그리기
# Author: 박창협
# Programed on September. 28. 2021

import turtle
import math

def drawPolygon(x, y, n, l):
    turtle.setup(500, 500)
    t = turtle.Turtle()
    t.shape("turtle")
    t.pencolor("red")
    t.speed(3)
    t.up()
    t.goto(x, y)
    t.dot(10,"blue")
    t.write("({}, {})".format(x, y))
    inside_angle = 180*(n-2)/n
    start_x = x - length/2
    start_y = y - (math.tan(math.radians(inside_angle/2)) * l/2)
    t.goto(start_x, start_y)
    t.dot(10,'red')
    t.write("{:}, {:}".format(start_x, start_y))
    t.down()
    t.right(180)
    next_x = start_x
    next_y = start_y
    for i in range(n):
         next_x = (next_x*math.cos(math.radians(180-inside_angle)))-(next_y*math.sin(math.radians(180-inside_angle)))
         next_y = (next_x*math.sin(math.radians(180-inside_angle)))+(next_y*math.cos(math.radians(180-inside_angle)))
         t.right(360/n)
         t.forward(length)        
    turtle.done()

center_x, center_y, num, length = map(int, input("input center_x, center_y, num_vertices and line_length: ").split())
drawPolygon(center_x, center_y, num, length)