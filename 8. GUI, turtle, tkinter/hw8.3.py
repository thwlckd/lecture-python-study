# hw8.3.py
# tkinker를 사용한 km, mile 양방향 변환기
# Author: 박창협
# Programed on November. 2. 2021

from tkinter import *

class App:
    def __init__(self, master):
        # LabelFrame(): 테두리와 제목을 가지는 프레임 위젯
        frame = LabelFrame(master, relief=FLAT)
        frame.pack()  # pack(): 위젯 배치 관리자 -> 압축 배치

        self.km_var = DoubleVar()  # DoubleVar(): 실수용 변수
        km_entry = Entry(frame, textvariable=self.km_var, width=20, justify=LEFT)  # Entry(): 문자열 입력 필드
        km_entry.grid(row=0, column=0)  # grid(row, column): 위젯 배치 관리자 -> 격자 배치

        km_label = Label(frame, text = 'Km', width=3)  # Label(): 텍스트 문자열 or 이미지 표시 위젯
        km_label.grid(row=0, column=1)

        self.mile_var = DoubleVar()
        Mile_entry = Entry(frame, textvariable=self.mile_var, width=20, justify=LEFT)
        Mile_entry.grid(row=0, column=2)
        
        Mile_label = Label(frame, text='Mile', width=3)
        Mile_label.grid(row=0, column=3)
        
        # Button(): 버튼 위젯, command: 버튼이 눌려지는 이벤트에서 실행되는 함수 바인딩
        button_KtoM = Button(frame, text='Km ‐> Mile', command=self.convert_KtoM) 
        button_KtoM.grid(row=2, column=0)
        button_MtoK = Button(frame, text='Mile ‐> Km', command=self.convert_MtoK)
        button_MtoK.grid(row=2, column=2)

    def convert_KtoM(self):
        km = self.km_var.get()
        self.mile_var.set(km / 1.60934)

    def convert_MtoK(self):
        mile = self.mile_var.get()
        self.km_var.set(mile * 1.60934)

win = Tk()  # GUI Toolkit, 윈도우 생성
win.wm_title('Km <-> Mile Converter')  # 윈도우 타이틀
win.geometry("350x50+200+200")  # geometry({width}x{hight}+{screen_x_pos}+{screen_y_pos}) 
app = App(win)
win.mainloop()