# hw8.2.py
# 마우스 클릭 이벤트를 사용한 선 그리기
# Author: 박창협
# Programed on November. 2. 2021

import turtle

board = turtle.Screen()
board.screensize(800, 600, 'light blue')
pointer = turtle.Turtle() 
pointer.color('red')
pointer.pencolor('red')
pointer.speed(0)
pointer.ht()

# 마우스 왼쪽 버튼 클릭시 실행 함수
def teleport_btn1(x,y):
    pointer.pencolor('red') 
    pointer.goto(x,y)
    pointer.write((pointer.xcor(), pointer.ycor()))

# 마우스 오른쪽 버튼 클릭시 실행 함수
def teleport_btn3(x,y):
    pointer.pencolor('blue')
    pointer.goto(x,y)
    pointer.write((pointer.xcor(), pointer.ycor()))

# 키보드 'q' 입력시 실행 함수
def quitThis():
    board.bye()  # 터틀 그래픽 화면 종료

board.onclick(teleport_btn1, btn=1)  # bte=1: 마우스 왼쪽 클릭, 좌표 (x,y)를 함수에 연결
board.onclick(teleport_btn3, btn=3)  # bte=3: 마우스 오른쪽 클릭
board.onkey(quitThis,'q')  # key-press 이벤트를 함수에 바인드

board.listen()  # 키보드 이벤트를 받을 수 있도록 대기시킴
board.mainloop()  # 이벤트 반복 구문 시작
