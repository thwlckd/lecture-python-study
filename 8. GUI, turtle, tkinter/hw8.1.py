# hw8.1.py
# 터틀 객체의 circle()을 사용한 원 및 다각형 그리기
# Author: 박창협
# Programed on November. 2. 2021

import turtle

turtle.setup(600, 500)
turtle.title("Drawing polygons with tutle.circle")
t = turtle.Turtle()
t.pensize(1) 
t.up()
t.shape("turtle")
t.down()
radius = 50

# L_polygons = list(tuple(radius, num_vertices, center_x, center_y, color))
L_polygons = [(radius, 3, -225, 150, "red"), (radius, 4, -75, 150, "blue"), (radius, 5, 75, 150, "green"),\
    (radius, 6, 225, 150, "magenta"), (radius, 7, -225, -50, "brown"), (radius, 8, -75, -50, "chocolate"),\
        (radius, 9, 75, -50, "black"), (radius, 0, 225, -50, "indigo")]

for i in range(len(L_polygons)):
    (radius, num_vertices, center_x, center_y, color) = L_polygons[i]
    t.up()
    t.goto(center_x, center_y-radius)
    t.dot(10, "red")
    t.write("({}, {})".format(center_x, center_y-radius))
    t.color(color)
    t.goto(center_x, center_y)
    t.setheading(180)  # 터틀 머리가 왼쪽을 바라보도록
    t.down()
    if num_vertices > 2:
        t.circle(radius, steps = num_vertices)
    else:
        t.circle(radius)

turtle.done()
