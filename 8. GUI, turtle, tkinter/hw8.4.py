# hw8.4.py
# tkinter GUI를 이용한 스탑워치
# Author: 박창협
# Programed on November. 2. 2021

import time
from tkinter import *

def runTimer():  # 스탑워치 기능의 총괄
    global start_time, elapsed_time, prev_elapsed_time
    if (running):
        cur_time = time.time()  # 현재 시각 기록
        time_diff = cur_time - start_time  # 현재 시각과 타이머 시작 시각의 차이 -> 타이머를 멈추지 않고 작동시킨 가장 최근의 시간
        elapsed_time = time_diff + prev_elapsed_time  # 타이머 작동 시간 기록
        timeText.configure(text="{:7.3f}".format(elapsed_time))
    window.after(10, runTimer)  # 타이머가 작동중이지 않으면 10ms뒤 재호출

def start():  # start 버튼이 눌리면 실행
    global running, start_time, elapsed_time, prev_elapsed_time
    if (running != True):
        running = True
        start_time = time.time()  # 타이머 시작 시각 기록
        prev_elapsed_time = elapsed_time

def stop():  # stop 버튼이 눌리면 실행
    global running, prev_elapsed_time, elapsed_time
    running = False
    prev_elapsed_time = elapsed_time

def reset():  # reset 버튼이 눌리면 실행
    global running, elapsed_time, prev_elapsed_time
    running = False
    elapsed_time = 0.0  # 타이머 작동 시간 초기화
    prev_elapsed_time = 0.0
    timeText.configure(text=str(elapsed_time))

running = False
window = Tk()
start_time = time.time()
elapsed_time = 0.0
prev_elapsed_time = 0.0
window.title("Stop Watch")
timeText = Label(window, height = 5, text="0", font=("Arial 40 bold"))
timeText.pack(side = TOP)
startButton = Button(window, width=10, text="Start", bg="green", command=start)
startButton.pack(side = LEFT)
stopButton = Button(window, width=10, text="Stop", bg="red", command=stop)
stopButton.pack(side = LEFT)
resetButton = Button(window, width=10, text="Reset", bg="yellow", command=reset)
resetButton.pack(side = LEFT)

if __name__ == '__main__':
    runTimer()
    window.mainloop()