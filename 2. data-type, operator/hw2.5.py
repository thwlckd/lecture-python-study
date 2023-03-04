# hw2.5.py
# 터틀 그래픽을 이용한 직사각형 그리기
# Author: 박창협
# Programed on September. 06. 2021

import turtle

vertex = [(-100, 100), (100, 100), (100, -100), (-100, -100)]
t = turtle.Turtle()
t.pensize(3)
t.speed(1)
t.shape("turtle")
t.pencolor("violet")
t.color("green", "orange")
turtle.bgcolor("grey")

t.up()
t.goto(vertex[0])
t.down()
for i in range(len(vertex)):
    t.goto(vertex[i])
    t.dot(10, "red")
    t.write("({}, {})".format(vertex[i][0], vertex[i][1]))
t.goto(vertex[0])
t.done()
