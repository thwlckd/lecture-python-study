# hw8.5.py
# tkinter GUI를 이용한 공튀기기 프로그램
# Author: 박창협
# Programed on November. 2. 2021

from tkinter import *
from tkinter import messagebox

def ask_quit():
    result = messagebox.askquestion("Message", "Quit")
    if result == "yes":
        window.destroy()

def change_direction(event):  # event: <keyPress- >
    global DX, DY
    if event.keysym == "Left":
        DX = -STEP; DY = 0
    elif event.keysym == "Right":
        DX = STEP; DY = 0
    elif event.keysym == "Up":
        DX = 0; DY = -STEP
    elif event.keysym == "Down":
        DX = 0; DY = STEP
    elif event.keysym == "Escape":  # ESC
        DX = STEP; DY = STEP
    else:
        DX = STEP; DY = STEP

def init():  # window창 초기화
    global window, canvas, DX, DY, STEP
    window = Tk()
    window.title("Bouncing ball")
    canvas = Canvas(window, width=600, height=400)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_oval(0, 0, 80, 80, fill="red", tag="Ball")  # 타원 생성, 생성위치 테이블 좌상
    STEP = 1
    DX = STEP
    DY = STEP
    window.protocol("WM_DELETE_WINDOW", ask_quit)  # 윈도우 종료버튼(X) 클릭시 ask_quit 실행
    # bind(sequence, func): sequnce 이벤트에 대한 핸들러 func 바인딩
    window.bind("<KeyPress-Left>", change_direction)
    window.bind("<KeyPress-Right>", change_direction)
    window.bind("<KeyPress-Up>", change_direction)
    window.bind("<KeyPress-Down>", change_direction)
    window.bind("<KeyPress-Escape>", change_direction)  # ESC

def animate():
    global DX, DY
    Delay = 10  # msec
    # move(item, dx, dy): item 객체를 현재 위치로 부터 dx, dy만큼 이동
    canvas.move("Ball", DX, DY)
    pos = canvas.coords("Ball")  # coords(): 현재 객체의 위치
    print("coords of Ball : {}, {}, {}, {}".format(pos[0], pos[1], pos[2], pos[3]))
    if pos[0] <= 0 :
        print("bounced by left board ")
        DX *= -1  # 왼쪽 벽에 닿으면 공의 좌우 이동방향 변경
    if pos[2] >= canvas.winfo_width():  # winfo_width(): 픽셀 단위 가로 크기
        print("bounced by right board")
        DX *= -1  # 오른쪽 벽에 닿으면 공의 좌우 이동방향 변경
    if pos[1] <= 0 :
        print("bounced by ceil board")
        DY *= -1  # 천장에 닿으면 공의 상하 이동방향 변경
    if pos[3] >= canvas.winfo_height():  # winfo_height(): 픽셀 단위 세로 크기
        print("bounced by bottom board")
        DY *= -1  # 바닥에 닿으면 공의 상하 이동방향 변경
    canvas.update_idletasks()  # redrawing, resizing 등의 디스플레이 갱신을 다음 갱신 전 강제 처리
    canvas.update()  # 디스플레이 갱신
    canvas.after(Delay, animate)  # 10msec마다 animate

if __name__ == '__main__':
    init()
    animate()
    mainloop()
