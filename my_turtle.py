# # Turtle() 터틀 객체의 생성
# # window_width() 윈도우 넓이 읽기
# # window_height() 윈도우 높이 읽기
# # setup(width, height) 캔버스의 크기를 가로 (width)와 세로(height)로 설정
# # shape() 터틀 객체의 모양을 설정 (classic: 화살 촉, circle: 원, square: 사각형, triangle: 삼각형, arrow: 화살 촉)
# # shapesize() 터틀의 크기를 설정
# # bgcolor(color) 배경색을 설정
# # circle(radius, steps) 주어진 반지름 (radius)의 원을 그림, steps가 주어지면 다각형을 그림
# # color(color) 터틀 객체의 색상을 설정
# # dot(size, color) size 크기의 점을 그림
# # goto(x_coord, y_coord) x좌표와 y좌표로 이동
# # forward(distance) 지정된 거리만큼 현재의 방향으로 전진
# # backward(distance) 지정된 거리만큼 현재의 반대 방향으로 후진
# # left(angle) 왼쪽 (반 시계방향)으로 지정된 각도만큼 회전
# # right(angle) 오른쪽 (시계방향)으로 지정된 각도만큼 회전
# # penup() 터틀의 펜을 위로 들어 이동에 따른 그리기가 나타나지 않게 함
# # pendown() 터틀의 펜을 아래로 내려 이동에 따라 그리기가 나타나게 함
# # setposition(x, y) 터틀의 위치를 지정된 좌표(x, y)로 설정
# # speed() 터틀 이동 속도를 설정: 1:가장느림 ~ 9:빠름, 0: 가장빠름
# # textinput() 입력창을 사용하여 문자열 입력, (title, 내용)
# # wirte(label) 현재의 터틀 위치에 label 문자열을 출력
# # title("name") 거북이 창의 이름 설정
# # done() 거북이 창이 바로 종료되지 않도록
# # distance(a, b) 현재 위치로 부터 (a, b)까지 거리 구함
# # heading() 터틀이 바라보는 방향의 각도
# # clearscreen() clear screen

# # 터틀 이벤트 처리
# # 키 입력 관련
# # listen(xdummy=None, ydummy=None) TurtleScreen에 집중하여 키보드 이벤트를 받을 수 있도록 대기시킴.
# # onkey(func, key), onkeyrelease(func, key) 입력키의 <key-press> 이벤트와 <key- release>이벤트를 함수 func() 에 바인드 시킴. 키는 Tk’의 키 심볼과 동일함
# # onkeypress(func, key=None) 입력키의 <key-press> 이벤트를 함수 func() 에 바인드시킴
# # 마우스 클릭 관련
# # onclick(func, btn=1, add=None) 터틀 객체에 마우스가 클릭되는 것을 함수 func(x, y)에 연결시킴. btn = 1 (left mouse button), btn = 3 (right mouse button)으로 매핑 됨.
# # onscreenclick(func, btn=1, add=None) 터틀을 선택한 후 마우스가 click될 때 발생되는 <mouse-click>이벤트를 함수 func(x, y)에 바인딩시킴
# # onrelease(func, btn=1, add=None) 터틀을 선택한 후 마우스가 release되는 이벤트를 함수 func(x, y)에 매핑시킴
# # ondrag(func, btn=1, add=None) 마우스 드래그 이벤트를 함수 func(x, y)에 매핑시킴

# # 터틀 그래픽 애니메이션
# # textinput(title, prompt) 다이얼로그 박스를 사용하여 문자열을 입력받고, 입력된 문 자열을 반환함
# # numinput(title, prompt, default=None, minval=None, maxval=None) 다이얼로그 박스로 숫자를 입력받고, 입력된 숫자를 반환
# # ontimer(func, t_ms=0) t_ms 밀리초 (millisecondsset) 뒤에 함수 func()가 호출되 도록 타이머를 설정
# # mainloop() 이벤트 반복 구문을 시작하도록 하며, tkinter main-loop() 함수가 실행되도록 함
# # done() 이벤트 반복구문을 종료함
# # getshapes() 사용가능한 터틀 형상을 리스트로 반환
# # register_shape(name, shape=None) 주어진 이름 (name)으로 터틀 형상을 등록. name의 터틀 형상은 gif파일, 문자열 및 형상의 좌표로 등록됨.
# # turtules() 화면 (screen)에 표시되어 있는 터틀의 리스트를 제공
# # delay(delay=None) 애니메이션 제어를 위한 밀리초 단위의 지연을 설정
# # tracer(n=None, delay=None) tracer(False)은 애니메이션을 중지시키며, tracer(True)은 애니메이션을 가동시킴. 만약 n이 양수이면 화면은 매 n-번째 update에서 갱신됨.
# # delay는 update 간격을 설정함
# # update() 사전에 설정된 지연시간 뒤에 화면을 갱신 (update) 시킴
# # bye() 터틀 그래픽 화면을 지움
# # exitonclick() 스크린에서 마우스를 클릭하면 turtle.bye()가 실행되도록 함.



# # turtle graphic ‐ window size, coordinates
# import turtle

# turtle.setup(500, 500, 100, 100) # width, height, start_x, start_y
# turtle.bgcolor("light grey")
# win_width, win_height = turtle.window_width(), turtle.window_height()
# margin = 50
# x_max, y_max = win_width // 2 - margin, win_height // 2 - margin
# t = turtle.Turtle() #t.shape("turtle") #shape can be ‘arrow’, ‘classic’, ‘turtle’, 'triangle', 'square' or ‘circle’
# t.shape('classic')

# #t.penup()
# size = 5
# t.write("({}, {})".format(0, 0))
# t.goto(-x_max, 0)
# t.dot(size, 'red')
# t.write("({}, {})".format(-x_max, 0))
# t.goto(x_max, 0)
# t.dot(size, 'red')
# t.write("({}, {})".format(x_max, 0))
# t.penup(); t.goto(0, y_max)
# t.pendown()
# t.dot(size, 'red')
# t.write("({}, {})".format(0, y_max))
# t.goto(0, -y_max)
# t.dot(size, 'red')
# t.write("({}, {})".format(0, -y_max))
# t.penup(); t.goto(0, 0)
# input("")
# turtle.clearscreen()


# # turtle ‐ drawing of triangle
# import turtle

# turtle.setup(500, 500, 100, 100) # width, height, start_x, start_y
# t = turtle.Turtle()
# t.shape("turtle") #shape can be ‘arrow’, 'classic', 'turtle', 'triangle', 'square' or 'circle'
# t.pensize(10)
# t.pencolor("red") # color can be 'blue', 'green', 'yellow', 'orange', 'white', 'black', and ...
# t.speed(0) # 1: slowest, 9: fast, 0: fastest
# side = 200
# turn_angle = 120
# t.forward(side)
# t.left(turn_angle)
# t.forward(side)
# t.left(turn_angle)
# t.forward(side)
# t.left(turn_angle)
# input("")
# turtle.clearscreen()


# # Simple Python Program to Draw a Circle and Box Cross
# import turtle

# turtle.setup(500, 500) #set width and height of canvas
# t = turtle.Turtle()
# t.shape('turtle')
# t.pencolor('red')
# t.width(5)  # pensize
# t.speed(0)
# side = 50

# t.up(); t.goto(0, -side); t.down()
# t.circle(side)
# t.penup() #pen up to prohibit drawing

# t.goto(0, -side*2) # moving to starting position
# t.pendown() #pen down to draw
# t.pencolor('blue')
# for i in range(4):
#     t.forward(side)
#     t.left(90)
#     t.forward(side)
#     t.right(90)
#     t.forward(side)
#     t.left(90)
#     t.forward(side)
# t.up(); t.goto(0,0); t.down()
# input("")
# turtle.clearscreen()

# # turtle ‐ rectangle of window
# import turtle

# turtle.setup(500, 500, 100, 100) # width, height, start_x, start_y
# turtle.bgcolor("light grey")
# win_width = turtle.window_width()
# win_height = turtle.window_height()
# margin = 30
# x_max = win_width // 2 - margin
# y_max = win_height // 2 - margin

# t = turtle.Turtle()
# t.shape('classic')
# t.color('blue')
# t.speed(0)
# PEN_WIDTH = 10
# t.width(PEN_WIDTH)
# t.penup(); t.goto(-x_max, -y_max); t.pendown()
# t.forward(x_max * 2); t.left(90)
# t.forward(y_max * 2); t.left(90)
# t.forward(x_max * 2); t.left(90)
# t.forward(y_max * 2); t.left(90)
# t.penup(); t.goto(0, 0); t.pendown()
# input("")
# turtle.clearscreen()


# #Simple Python Program for Shape Drawing with Text Inputs
# import turtle

# t = turtle.Turtle()
# t.shape('classic')
# colors = ["red", "green", "blue", "orange", "magenta", "purple", "black"]
# num_vertices = len(colors)
# radius = 50
# t.speed(0)
# t.width(3)
# for i in range(num_vertices):
#     circle_steps = i
#     t.color(colors[i])
#     if i == 0:
#         t.up(); t.setposition(0, -radius//2); t.down()
#         t.circle(radius//2)
#     elif i == 1 or i == 2:
#         t.up(); t.setposition(0, -radius * i); t.down()
#         t.circle(radius * i)
#     else:
#         t.up(); t.setposition(0, -radius * i); t.down()
#         t.circle(radius * i, steps = circle_steps) # steps: 원이 외접하고 있는 다각형을 그림
#     t.up(); t.setposition(0, 0); t.down() # return to the origin
# input("")
# turtle.clearscreen()


# # Simple Python Program to Draw a Star
# import turtle

# turtle.setup(500, 500) #set width and height of canvas
# t = turtle.Turtle()
# t.shape('classic')
# t.pencolor('red')
# t.width(10)
# t.penup() #pen up to prohibit drawing
# t.goto(-125, 50) # moving to starting position
# t.pendown() #pen down to draw
# for i in range(5):
#     t.forward(200)
#     t.right(144)
# input("")
# turtle.clearscreen()


# # Sample program that draws a polygon with input N
# import turtle

# t = turtle.Turtle()
# t.shape('classic')
# t.width(3) # set pen thickness
# t.pencolor("red")
# s = turtle.textinput("", "Number of points in polygon?") 
# n = int(s)
# for i in range(n):
#     t.forward(100)
#     t.left(360/n)
# input("")
# turtle.clearscreen()


# #Simple Python Program for Shape Drawing with Text Inputs
# import turtle
# t = turtle.Turtle()
# t.shape('classic')
# radius = 1
# while radius != 0 :
#     #text input for shape type
#     pos_x_str = turtle.textinput("", "position_x : ")
#     pos_y_str = turtle.textinput("", "position_y : ")
#     radius_str = turtle.textinput("", "radius(0 means stop drawing) : ")
#     circle_steps_str = turtle.textinput("", "circle steps (0 means simple circle) : ")
#     pos_x, pos_y = int(pos_x_str), int(pos_y_str)
#     radius = int(radius_str)
#     circle_steps = int(circle_steps_str)
#     t.up(); t.setposition(pos_x, pos_y); t.down()
#     t.write("Drawing a circle of radius ({}) at position({}, {})".format(radius, pos_x, pos_y))
#     t.dot(10, "red")
#     t.up(); t.setposition(pos_x, pos_y - radius); t.down()
#     if circle_steps == 0:
#         t.circle(radius)
#     else:
#         t.circle(radius, steps = circle_steps)
#     t.up(); t.setposition(0, 0); t.down() # return to the origin
# input("")
# turtle.clearscreen()


# # drawing lines with 89 degrees with turtle
# import turtle

# colors = ["red", "purple", "blue", "green", "yellow", "orange", "cyan", "magenta"]
# num_colors = len(colors)
# t = turtle.Turtle()
# turtle.bgcolor("light grey")
# t.speed(0)
# t.width(3)
# length = 10
# turnAngle = 89 # 사각형이 완전히 닫히지 않는 모양
# while length < 500:
#     t.forward(length)
#     t.pencolor(colors[length % num_colors])
#     t.right(turnAngle)
#     length += 7
# input("")
# turtle.clearscreen()


# #turtle graphic and while‐loop
# import turtle
# colors = ["red", "purple", "blue", "green", "yellow", "orange", "cyan"]
# num_colors = len(colors)
# t = turtle.Turtle()
# turtle.bgcolor("light grey")
# t.speed(0)
# t.width(3)
# length = 10
# while length < 300:
#     t.forward(length)
#     t.pencolor(colors[length % num_colors])
#     t.right(59)
#     length += 5
# input("")
# turtle.clearscreen()

# # drawing with for‐loop
# import turtle
# t = turtle.Turtle()
# t.shape("classic")
# t.speed(0)
# radius = 200
# start_pos = (-250, 0)
# t.up()
# t.goto(start_pos)
# t.down()
# color_list = ["red", "yellow", "blue", "orange", "purple",\
# "green", "white", "black", "pink", "brown"]
# for x in range(len(color_list)):
#     color = color_list[x]
#     t.fillcolor(color)  # color 선택
#     t.begin_fill()  # begin_fill, end_fill 사이에 있는 도형에 대해 색칠
#     t.circle(radius)
#     t.end_fill()
#     radius -= 20
#     t.up(); t.forward(50); t.down()
# input("")
# turtle.clearscreen()


# #turtle graphic and while‐loop
# import turtle
# colors = ["red", "purple", "blue", "green", "yellow", "orange", "cyan"]
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.speed(0)
# t.width(3)
# length = 10
# while length < 200:
#     t.forward(length)
#     t.pencolor(colors[length %6])
#     t.right(59)
#     length += 5
# input("")
# turtle.clearscreen()


# import turtle
# import time
# turtle.setup(500, 500, 200, 200) # window width, height, startx, starty
# turtles = []
# turtle_names = ['square', 'circle', 'triangle', 'turtle', 'arrow', 'classic']
# turtle_colors = ['red', 'green', 'blue', 'orange', 'brown', 'magenta']
# turtle_positions = [(-175, 100), (0, 100), (175, 100),\
# (-175, -100), (0, -100), (175, -100)]
# for i in range(len(turtle_names)):
#     t = turtle.Turtle() # create turtle.Pen()
#     t.shape(name = turtle_names[i])
#     t.color(turtle_colors[i])
#     t.shapesize(5)
#     t.up(); t.setpos(turtle_positions[i]); t.down()
#     turtles.append(t)
# turn_angle = 5 # 5 degree for each rotation
# for i in range(360//turn_angle): # repeat the rotation with given angle
#     for t in turtles:
#         t.up(); t.right(turn_angle); t.down() # turn right by the given angle
#         t.dot(5, 'red')
#     time.sleep(1)
# input("")
# turtle.clearscreen()



# # Turtle ‐ coordinates, grid (1)
# import turtle
# pen = turtle.Turtle()
# pen.shape('turtle')
# pen.color("black", "black") # black line, black fill
# turtle.setup(900, 700)

# c = turtle.Turtle()
# c.shape('circle')
# c.shapesize(5,5,3) # strech_width, strech_height, outline (thickness)
# c.color("red", "white") # red line, white filling
# c.setpos(0, 0)

# width, height, margin = 800, 600, 20
# pen.write((0, 0))
# pen.up(); pen.setpos(-(width/2 + margin), 0); pen.down()
# pen.setpos((width/2 + margin), 0)
# pen.up(); pen.setpos(0, -(height/2 + margin)); pen.down()
# pen.setpos(0, (height/2 + margin))

# axis_ends = [(-width//2, 0), (width//2, 0), (0, height//2), (0, -height//2)]
# for p in range(len(axis_ends)):
#     pen.up(); pen.goto(axis_ends[p]); pen.down()
#     pen.write(axis_ends[p])
# pen.up(); pen.setpos(-width//2, -height//2); pen.down()
# pen.color("blue", "red")

# rectangle_ends = [(-width//2,-height//2), (width//2, -height//2),\
# (width//2, height//2), (-width//2, height//2),\
# (-width//2,-height//2)]
# for p in range(len(rectangle_ends)):
#     pen.goto(rectangle_ends[p])
#     pen.write(rectangle_ends[p])
# pen.up(); pen.home(); pen.down()
# input("")
# turtle.clearscreen()


# #Simple Python Program for Shape Drawing with Text Inputs (1)
# import turtle
# import math
# def draw_rectangle(t, cl="black", width=10, height=10):
#     t.up()
#     t.goto(t.xcor()-width//2,\
#     t.ycor()-height//2); t.down()
#     t.color(cl)
#     t.forward(width); t.left(90)
#     t.forward(height); t.left(90)
#     t.forward(width); t.left(90)
#     t.forward(height); t.left(90)
# def draw_triangle(t, cl="black", side=10):
#     t.up()
#     t.goto(t.xcor()-side//2,\
#     t.ycor()-side*math.sin(math.pi/3)/2); t.down()
#     t.color(cl)
#     t.forward(side); t.left(120)
#     t.forward(side); t.left(120)
#     t.forward(side); t.left(120)
# def draw_circle(t, cl="black", radius=10):
#     t.up(); t.goto(t.xcor(), t.ycor()-radius); t.down()
#     t.color(cl)
#     t.circle(radius)

# turtle.setup(600, 200)
# tt = turtle.Turtle()
# tt.shape('classic')
# tt.pensize(3)

# tt.up(); tt.goto(-200, 0); tt.down()
# draw_rectangle(tt, "red", 100, 87)

# tt.up(); tt.goto(0, 0); tt.down()
# draw_triangle(tt, "blue", 100)

# tt.up(); tt.goto(200, 0); tt.down()
# draw_circle(tt, "green", 50)
# input("")
# turtle.clearscreen()


# # Simple Python Turtle Graphic Program to Draw a Star
# import turtle
# turtle.setup(500, 500) #set width and height of canvas
# t = turtle.Turtle()
# t.shape('classic')
# def draw_star(length = 100, thickness = 3, cl = 'red'):
#     t.pencolor(cl)
#     t.width(thickness)
#     t.penup() #pen up to prohibit drawing
#     t.goto(-length//2, length//6) # moving to starting position
#     t.pendown() #pen down to draw
#     for i in range(5):
#         t.forward(length)
#         t.right((360 * 2)/5)
#     t.penup()
# # ‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
# length = 50
# thickness = 1
# colors = ['red', 'blue', 'green', 'cyan',\
# 'orange', 'red', 'blue', 'black']
# for i in range(len(colors)):
#     draw_star(length, thickness, colors[i])
#     length += 50
#     thickness += 1
# input("")
# turtle.clearscreen()


# # turtle graphic ‐ keyboard input event handling
# import turtle

# screen = turtle.Screen()
# screen.screensize(500, 500, 'light green')
# turtle.setup(500, 500) # set canvas width, height
# t = turtle.Turtle()
# t.shape('turtle')
# t.shapesize(5)

# def turn_left_90():
#     t.left(90)
# def turn_right_90():
#     t.right(90)
# def forward_10():
#     t.forward(10)
# def backward_10():
#     t.backward(10)

# screen.onkey(turn_left_90, "Up")
# screen.onkey(turn_right_90, "Down")
# screen.onkey(forward_10, "Right")
# screen.onkey(backward_10, "Left")

# screen.listen()
# screen.mainloop()


# Turtle mouse event processing
import turtle

board = turtle.Screen()
board.screensize(800, 600, 'light blue')
pointer = turtle.Turtle() 
pointer.color('red')
pointer.pencolor('red')
pointer.ht()

def teleport_btn1(x,y):
    pointer.pencolor('red') 
    pointer.goto(x,y)
    pointer.dot(10, "red")
    pointer.write((pointer.xcor(), pointer.ycor()))

def teleport_btn3(x,y):
    pointer.pencolor('blue')
    pointer.goto(x,y)
    pointer.dot(10, "blue")
    pointer.write((pointer.xcor(), pointer.ycor()))

def quitThis():
    board.bye()

pointer.dot(10, "red")
pointer.write((pointer.xcor(), pointer.ycor())) 
board.onclick(teleport_btn1, btn=1)
board.onclick(teleport_btn3, btn=3)
board.onkey(quitThis,'q')

board.listen()
board.mainloop()


