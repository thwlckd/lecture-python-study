# 윈도우 widget 클래스 기능
# iconify(), deiconify() 윈도우를 아이콘화 (iconify)하여 작게 만들거나, 확장 시킴
# geometry(newGeometry = None)윈도우의 가로 및 세로 크기를 설정하며, 스크린에서의 위치를 설정. 포멧 "{width}x{hight}{±x}{±y}"
# maxsize(width=None, height=None) 윈도우의 최대 크기를 설정
# minsize(width=None, height=None) 윈도우의 최소 크기를 설정
# overrideredirect(flag=None)윈도우 덮어쓰기에 대한 설정. 만약 flag = True이면 윈도우의 이동, 크기 조절, 아이콘화, 숨기기 등이 실행되지 않게 하며, 만약 flag = False이면, 윈도우 이동 및 변경이 가능하게 함.
# resizable(width=None, height=None)윈도우 크기 조절에 대한 설정. 만약 width = False이면 윈도우 가로 크기의 변경 금지. 만약 height = False이면 윈도우의 세로 크기 변경금지
# title(text=None) 윈도우의 제목을 주어진 문자열로 설정
# withdraw() 윈도우를 숨김. 윈도우의 표시는 iconify()와 deiconify()에 의해 제어됨

# widget layout manager
# 압축배치 pack() pack(fill=BOTH, expand=1)
# 격자배치 grid() grid(row=x, column=y, sticky=NSEW)
# 절대위치배치 place() place(x=100, y=100)

# gird(). 메소드 옵션
# column widget을 삽입할 열 (column), 기본값 0으로부터 시작
# row widget을 삽입할 행 (row), 0으로부터 시작, 기본값은 비어있는 첫 행
# columnspan widget이 차지할 열의 개수, 기본값 1
# rowspan widget이 차지할 행의 개수, 기본값 1
# in widget이 놓일 widget, 기본값은 parent
# padx, pady 셀 주위의 패딩 화소, 기본값은 0
# sticky widget을 셀에 어떻게 붙일 것인지 지정. S, N, E, W를 조합하여 지정. 기 본 값은 중앙에 위치, NSEW는 셀의 경계에 붙임

# place(). 메소드 옵션
# anchor widget의 기준 위치, N, E, S, W로 지정. 기본값은 NW, NE, SE, SW, CENTER 등 설정 가능
# bordermode 위젯의 테두리를 INSIDE, OUTSIDE
# x, y widget의 위치
# height, width widget의 가로, 세로의 크기
# relx, rely parent widget의 상대 위치 0.0~1.0
# relheight, relwidth parent widget의 상대 크기 0.0~1.0

# 캔버스 객체 메소드
# after(delay_ms, callback=None, *args) delay_ms 밀리초 후에 callback 함수 호출; callback=None이면 sleep(delay_ms)으로 대기
# bind(sequence=None, func=None, add=None) sequence 이벤트에 대한 핸들러 func바인딩, add='+'이면 기존 핸들러에 추가
# bind_all(sequence=None, func=None, add=None) 응용 프로그램의 모든 위젯에 이벤트 핸들러 바인딩
# bind_class(className, equence=None, func=None, add=None) className 이름의 모든 위젯에 이벤트 핸들러 func 바인딩
# config(option=value, ...), configure(option=value, ...) 옵션 속성변경, w[option] = value
# create_arc(bbox, **options) 원호 (arc) 생성
# create_bitmap(position, **optiion) 비트맵 생성
# create_image() 이미지 생성
# create_line(coords, **options) 선 생성
# create_oval(bbox, **options) 타원 생성
# create_polygon(coords, **options) 다각형 생성
# create_rectangle(bbox, **options) 사각형 생성
# create_text(position, **options) 텍스트 생성


# # tkinter ‐ window configurations (1)
# import tkinter
# from tkinter import *

# window = Tk()
# window.title("tkinter window, LabelFrame, Canvas")
# window.geometry("600x600+200+100")
# # "{w}x{h}{±x}{±y}", +/‐x : from left/right end, +/‐y: from top/bottom
# window.resizable(width=False, height=False) # prohibits window resizing

# frame1 = LabelFrame(window, bg="light green", cursor="heart",\
# bd=5, padx=10, pady=10, text="Frame_1", relief=GROOVE)
# frame1.grid(row=0, column=0)
# frame2 = LabelFrame(window, bg="yellow", cursor="man", bd=5,\
# padx=10, pady=10, text="Frame_2", relief=GROOVE)
# frame2.grid(row=1, column=0)
# frame3 = LabelFrame(window, bg="yellow", cursor="plus", bd=5,\
# padx=10, pady=10, text="Frame_3", relief=GROOVE)
# frame3.grid(row=2, column=0)

# canvas_11 = Canvas(frame1, bg="lime", width=100, height=100)
# canvas_11.grid(row=0, column=0, fill=None, padx=10, pady=10)
# canvas_12 = Canvas(frame1, bg="orange", width=150, height=100)
# canvas_12.grid(row=0, column=1, fill=None, padx=10, pady=10)
# canvas_13 = Canvas(frame1, bg="grey", width=100, height=100)
# canvas_13.grid(row=1, column=1, fill=None, padx=10, pady=10)
# canvas_21 = Canvas(frame2, bg="magenta", width=200, height=50)
# canvas_21.grid(row=0, column=0, fill=None, padx=10, pady=10)
# canvas_22 = Canvas(frame2, bg="brown", width=200, height=50)
# canvas_22.grid(row=0, column=1, fill=None, padx=10, pady=10)
# canvas_23 = Canvas(frame2, bg="sky blue", width=200, height=50)
# canvas_23.grid(row=1, column=0, fill=None, padx=10, pady=10)
# canvas_31 = Canvas(frame3, bg="light green", width=400, height=50)
# canvas_31.grid(row=0, column=0, fill=None, padx=10, pady=10)
# mainloop()


# # tkinter ‐ pack layout
# from tkinter import *
# window = Tk()
# window.title("Testing Pack Layout")
# window.geometry('400x300+100+200')

# # fill option
# label1 = Label(window, text="Label 1", bg="#E74C3C", fg="white")\
# .pack(fill=X, padx=10, pady=10)
# label2 = Label(window, text="Label 2", bg="#2ECC71", fg="black")\
# .pack(fill=X, padx=10, pady=10)
# label3 = Label(window, text="Label 3", bg="#F1C40F", fg="white")\
# .pack(fill=X, padx=10, pady=10)

# # side option
# label4 = Label(window, text="Label 4", bg="#34495E", fg="white")\
# .pack(fill=X, padx=10, pady=10, side=LEFT)
# label5 = Label(window, text="Label 5", bg="#5DADE2", fg="black")\
# .pack(fill=X, padx=10, side=LEFT)
# label6 = Label(window, text="Label 6", bg="#A569BD", fg="white")\
# .pack(fill=X, padx=10, side=LEFT)

# # expand option
# listbox = Listbox(window)
# listbox.pack(fill=BOTH, expand=1)

# L = [100, 200, 300, 400, 500]
# for i in range(len(L)):
#     listbox.insert(END, str(L[i]))
# mainloop()



# # Frame with Label and Entry Objects, using grid()
# from tkinter import*

# def fetch(cells): 
#     print("Input data: ")
#     for i, e in enumerate(cells):
#         print("{0}:{1}".format(fields[i], e.get()))

# def make_form(fields):
#     cells = []
#     for r, field in enumerate(fields):
#         label = Label(window, width=10, text = field)
#         entry = Entry(window) 
#         label.grid(row=r, column=0, sticky=NSEW)
#         entry.grid(row=r, column=1, sticky=NSEW)
#         cells.append(entry)
#     return cells

# if __name__ == "__main__":
#     window = Tk()
#     window.title("Input Dialog with Label and Entry Objects")
#     fields = ("Name", "Age", "Address")
#     cells = make_form(fields)
#     window.bind("<Return>", (lambda event, e=cells: fetch(e)))
#     Button(window, text="Fetch", bg="green", command = (lambda e=cells: fetch(e))).grid(row=3, column=0, sticky=NSEW)
#     Button(window, text="Quit", bg="Red", command = quit).grid(row=3, column=1, sticky=NSEW) 
#     print("grid size: ", window.grid_size())
#     window.grid_columnconfigure(1, weight=1)
#     window.grid_rowconfigure(0, weight=1) 
#     window.mainloop()



# # Testing LabelFrame, bordermode, anchor, relwidth, relheight (1)
# from tkinter import *

# window = Tk()
# window.title("Testing LabelFrame, bordermode, anchor, relwidth, relheight")
# window.geometry("500x300+100+100")

# f1 = LabelFrame(window, borderwidth=20, relief=GROOVE,\
# width=200, height=100, text="Frame_1", bg="yellow")
# f1.grid(row=0, column=0)
# l1 = Label(f1, text="position(10, 10)", bg="light green")
# l1.place(x=10, y=10, bordermode="outside")

# f2 = LabelFrame(window, borderwidth=20, relief=GROOVE,\
# width=200, height=100, text="Frame_2", bg="green")
# f2.grid(row=0, column=1)
# l2 = Label(f2, text="position(10, 10)", bg="white")
# l2.place(x=10, y=10, bordermode="inside")

# f3 = LabelFrame(window, borderwidth=20, relief=GROOVE,\
# width=200, height=100, text="Frame_3", bg="light blue" )
# f3.grid(row=1, column=0)
# l3 = Label(f3, text="Label", bg="red")
# l3.place(bordermode="inside", anchor=NW, relwidth=0.5, relheight=0.5)

# f4 = LabelFrame(window, borderwidth=20, relief=FLAT, width=200, height=100,\
# text="Frame_3" )
# f4.grid(row=1, column=1)
# l4 = Label(f4, text="Label", bg="light green")
# l4.place(bordermode="inside",relwidth=1.0, relheight=1.0)
# window.mainloop()



# # tkinter_GUI - create_rectangle, create_line
# from tkinter import *

# win = Tk()
# win.title("My Turtle GUI Window (800x500+500+300)")
# win.geometry('850x550+500+300') # width, height, position
# print("win.geometry() : ", win.geometry())
# win.resizable(0,0)
# win.wm_attributes("-topmost", 1) # show at topmost (front)
# frame_canvas = LabelFrame(win, text="Frame for Canvas",\
# bg="light blue", bd=5, padx=10, pady=10, relief=GROOVE)
# frame_canvas.pack(expand=YES, fill=BOTH)

# myCanvas = Canvas(frame_canvas, bg="grey40", width=600, height=400) #bg : grey40, yellow
# myCanvas.pack(expand=YES, fill=BOTH)
# myCanvas.create_rectangle(0, 300, 600, 400, fill="red")
# myCanvas.create_rectangle(0, 0, 100, 300, fill="blue")
# myCanvas.create_rectangle(100, 0, 600, 300, fill="green", width=10)
# myCanvas.create_line(100, 300, 600, 0, fill="yellow", width=10)
# mainloop()


# # tkinter_GUI – canvas.create_rectangle, create_line
# from tkinter import *

# win = Tk()
# win.title("My Turtle GUI Window (800x500+500+300)")
# win.geometry("800x500+500+300") # width, height, position
# print(" win.geometry() : ", win.geometry())
# win.resizable(0,0)
# win.wm_attributes("-topmost", 1) # show at topmost (front)
# frame = LabelFrame(win, text="Frame for Canvas")
# frame.pack(side="bottom")
# myCanvas = Canvas(frame, bg="grey70", width=600, height=400) #bg : grey40, yellow
# myCanvas.pack(side="bottom") # myCanvas.pack(side="top")
# myCanvas.create_oval(10, 10, 310, 210, fill="", width=3)
# myCanvas.create_polygon(10, 400, 310, 400, 150, 250,\
# fill="#ff0000", outline="#0000ff", width=5) # fill = ‘red’, outline = ‘blue’
# myCanvas.create_arc(400, 100, 600, 300, start = 0, extent=180, fill="pink", outline="red", width=3)
# myCanvas.create_arc(400, 100, 600, 300, start = 180, extent=90, \
# outline="blue", style=ARC, width=7)
# myCanvas.create_arc(400, 100, 600, 300, start = 45, extent=90,\
# outline="green", style=PIESLICE, width=5)
# mainloop()



# # Simple tkinter GUI for Temperature Converter
# from tkinter import *

# class App:
#     def __init__(self, master):
#         frame = LabelFrame(master, text="Temperature Converter",\
#             bg="light blue", relief=GROOVE) 
#         frame.pack()
#         c_label = Label(frame, text = 'deg C', width=15)
#         c_label.grid(row=0, column=0)
#         self.c_var = DoubleVar()
#         c_entry = Entry(frame, textvariable=self.c_var, width=10, justify=RIGHT)
#         c_entry.grid(row=0, column=1)
#         f_label = Label(frame, text='deg F', width=15)
#         f_label.grid(row=1, column=0)
#         self.f_var = DoubleVar()
#         f_entry = Entry(frame, textvariable=self.f_var, width=10, justify=RIGHT)
#         f_entry.grid(row=1, column=1)
#         button_CF = Button(frame, text='Convert C‐>F', command=self.convert_CF) 
#         button_CF.grid(row=2, column=0)
#         button_FC = Button(frame, text='Convert F‐>C', command=self.convert_FC)
#         button_FC.grid(row=2, column=1)

#     def convert_CF(self):
#         c = self.c_var.get()
#         self.f_var.set(c * 1.8+ 32)

#     def convert_FC(self):
#         f = self.f_var.get()
#         self.c_var.set((f - 32)/1.8)

# win = Tk()
# win.wm_title('Temp Converter') 
# win.geometry("200x100+200+200")
# app = App(win)
# win.mainloop()


# # tkinter ‐ Menu Widget
# from tkinter import *
# from tkinter import messagebox
# def onFileNew():
#     print("select New")
# def onFileExit():
#     result = messagebox.askquestion("Exit Confirm", "Quit ?")
#     if result == "yes":
#         window.destroy()
# def onGraphic():
#     global fr, cv
#     cv.delete("all")
#     DT = drawType.get()
#     print("drawType = ", DT)
#     if DT == 1:
#         print(" (line_slash)")
#         cv.create_line(50, 250, 250, 50, fill='red', width=10)
#     elif DT == 2:
#         print(" (line_back_slash)")
#         cv.create_line(50, 50, 250, 250, fill='red', width=10)
#     elif DT == 3:
#         print(" (Rectangle)")
#         cv.create_rectangle(50, 250, 250, 50, outline='red', fill='blue', width=10)
#     elif DT == 4:
#         print(" (Oval)")
#         cv.create_oval(50, 50, 250, 250, outline='magenta', fill = 'yellow', width=10)
#     else:
#         print(" (Undefined type)")

# def makeMenu(master):
#     menuBar = Menu(master) 
#     master.config(menu = menuBar)
#     filemenu = Menu(menuBar, title = "file") 
#     filemenu.add_command(label="New ...", command=onFileNew) 
#     filemenu.add_command(label="Exit", command=onFileExit) 
#     menuBar.add_cascade(label="File", menu=filemenu)
#     drawing = Menu(menuBar, tearoff=0) 
#     drawing.add_radiobutton(label="Line_slash", variable=drawType, value=1, command=onGraphic) 
#     drawing.add_radiobutton(label="Line_back_slash", variable=drawType, value=2, command=onGraphic) 
#     drawing.add_radiobutton(label="Rectangle", variable=drawType, value=3, command=onGraphic) 
#     drawing.add_radiobutton(label="Oval", variable=drawType, value=4, command=onGraphic) 
#     menuBar.add_cascade(label="Drawings", menu=drawing)

# if __name__ == "__main__": 
#     global fr, cv 
#     window = Tk() 
#     window.title("My GUI with Menu") 
#     window.geometry("400x400+100+100") 
#     drawType = IntVar(); drawType.set(1) 
#     makeMenu(window) 
#     fr = Frame(window, borderwidth=10, relief=RIDGE, width=300, height=300) 
#     fr.pack(expand=YES, fill=BOTH)
#     cv = Canvas(fr, bg="grey40", width=300, height=300) 
#     #cv.pack(expand=True, fill="both") 
#     cv.place(x=40, y=40)
#     window.mainloop()




# # Stop Watch
# import time
# from tkinter import *

# def runTimer():
#     global start_time, elapsed_time, prev_elapsed_time
#     if (running):
#         cur_time = time.time()
#         time_diff = cur_time - start_time
#         elapsed_time = time_diff + prev_elapsed_time
#         timeText.configure(text="{:7.3f}".format(elapsed_time))
#     window.after(10, runTimer)

# def start():
#     global running, start_time, elapsed_time, prev_elapsed_time
#     if (running != True):
#         running = True
#         start_time = time.time()
#         prev_elapsed_time = elapsed_time

# def stop():
#     global running, prev_elapsed_time, elapsed_time
#     running = False
#     prev_elapsed_time = elapsed_time

# def reset():
#     global running, elapsed_time, prev_elapsed_time
#     running = False
#     elapsed_time = 0.0
#     prev_elapsed_time = 0.0
#     timeText.configure(text=str(elapsed_time))

# running = False
# window = Tk()
# timer = 0
# start_time = time.time()
# stop_time = time.time()
# elapsed_time = 0.0
# prev_elapsed_time = 0.0
# window.title("My Simple Stop Watch")
# timeText = Label(window, height = 5, text="0",\
# font=("Arial 40 bold"))
# timeText.pack(side = TOP)
# startButton = Button(window, width=10, text="Start",\
# bg="green", command=start)
# startButton.pack(side = LEFT)
# stopButton = Button(window, width=10, text="Stop",\
# bg="red", command=stop)
# stopButton.pack(side = LEFT)
# resetButton = Button(window, width=10, text="Reset",\
# bg="yellow", command=reset)
# resetButton.pack(side = LEFT)

# if __name__ == '__main__':
#     runTimer()
#     window.mainloop()



# # Handling Keyboard Events (1)
# from tkinter import *

# def keyEvent(event):
#     if len(event.char) == 0:
#         input_char = event.keysym
#     else:
#         input_char = event.char
#     label_ky.configure(text="key input = {}, keycode = {}"\
#         .format(input_char, event.keycode))
#     label_ky.update
#     ky_state = ""
#     if event.state & 0x0001:
#         ky_state += "Shift_L "
#     if event.state & 0x0002:
#         ky_state += "Caps_Lock "
#     if event.state & 0x0004:
#         ky_state += "Ctrl "
#     if event.state & 0x0008:
#         ky_state += "Alt_L "
#     if event.state & 0x0010:
#         ky_state += "Num_Lock "
#     if event.state & 0x0080:
#         ky_state += "Alt_R "
#     label_state.configure(text="key state = {} {}"\
#     .format(event.state, ky_state))
#     label_state.update

# window = Tk()
# window.geometry("400x200+100+100")
# window.title("Showing Keyboard Event")
# frame = Frame(window, bg="light yellow", bd = 5,\
# padx=5, pady=5, relief=GROOVE)
# frame.pack(expand=YES, fill=BOTH)
# label_ky = Label(frame, text="key input = {}".format(""),)
# label_ky.update()
# label_ky.grid(row=0, column=0, sticky=NSEW)
# label_state = Label(frame, text="key state = {}"\
# .format(""), anchor="w")

# label_state.update()
# label_state.grid(row=1, column=0, sticky=NSEW)

# window.bind("<Key>", keyEvent)
# window.mainloop()




# # Handling Mouse Events (1)
# from tkinter import *

# def mouse_enter(event): 
#     label_mouse_enter.configure(text = "Mouse entered into {}".format(event.widget))
#     label_mouse_enter.update()
# def mouse_leave(event):
#     label_mouse_enter.configure(text = "Mouse left from {}".format(event.widget))
#     label_mouse_enter.update()
# def move_position(event):
#     label_pos.configure(text = "Mouse position: ({}, {})".format(event.x, event.y))
#     label_pos.update()
# def button_1_pressed(event): 
#     label_mouse_btn.configure(text = "Mouse button {} is pressed".format(event.num))
#     label_mouse_btn.update()
# def button_1_released(event):
#     label_mouse_btn.configure(text = "Mouse button {} is released".format(event.num))
#     label_mouse_btn.update()

# # main loop
# window = Tk() 
# window.geometry("400x200+100+100")
# window.title("Showing Mouse Events")
# frame = Frame(window, bg="light yellow", bd=5, padx=5, pady=5, relief=RIDGE) 
# frame.bind('<Enter>', mouse_enter)
# frame.bind('<Leave>', mouse_leave)
# frame.bind('<Motion>', move_position) 
# frame.bind('<Button-1>', button_1_pressed)
# frame.bind('<ButtonRelease-1>', button_1_released)
# frame.pack(expand=YES, fill=BOTH)

# mouse_motion = ""
# label_mouse_enter = Label(frame, text = "Mouse motion: ({})".format(mouse_motion)) 
# label_mouse_enter.config(bg='yellow', font=('times', 12, 'italic'))
# label_mouse_enter.pack()
# pos_x = pos_y = 0
# label_pos = Label(frame, text = "Mouse position: ({}, {})".format(pos_x, pos_y))
# label_pos.config(bg='lightgreen', font=('times', 12, 'italic')) 
# label_pos.pack()

# btn_motion = ""
# label_mouse_btn = Label(frame, text = "Mouse Button Motion: ({})".format(btn_motion))
# label_mouse_btn.config(bg='orange', font=('times', 12, 'italic'))
# label_mouse_btn.pack()
# window.mainloop()


# #Python ColorChooser
# from tkinter import *
# import tkinter.colorchooser as cc

# class App:
#     def __init__(self, master):
#         b=Button(master, text='Color', command=self.ask_color).pack()
#     def ask_color(self):
#         (rgb, hx) = cc.askcolor()
#         print("rgb=" + str(rgb) + " hx=" + hx)

# window = Tk()
# app = App(window)
# window.mainloop()




# # Color Control with Slider (1)
# from tkinter import *

# class App:
#     def __init__(self, win):
#         frame = Frame(win)
#         frame.pack()
#         Label(frame, text="Checking RGB Color Combination").grid(row=0, column=0, columnspan=3)
#         Label(frame, text='Red').grid(row=1, column=0)
#         Label(frame, text='Green').grid(row=2, column=0)
#         Label(frame, text='Blue').grid(row=3, column=0)
        
#         scaleRed = Scale(frame, from_=0, to=255,
#         orient=HORIZONTAL, command=self.updateRed)
#         scaleRed.grid(row=1, column=1)
#         scaleGreen = Scale(frame, from_=0, to=255,
#         orient=HORIZONTAL, command=self.updateGreen)
#         scaleGreen.grid(row=2, column=1)
#         scaleBlue = Scale(frame, from_=0, to=255,
#         orient=HORIZONTAL, command=self.updateBlue)
#         scaleBlue.grid(row=3, column=1)
        
#         self.red_var = IntVar()
#         self.green_var = IntVar()
#         self.blue_var = IntVar()
#         self.red = 0
#         self.green = 0
#         self.blue = 0

#         Entry(frame, textvariable=self.red_var, justify='right').grid(row=1, column=2) 
#         Entry(frame, textvariable=self.green_var, justify='right').grid(row=2, column=2) 
#         Entry(frame, textvariable=self.blue_var, justify='right').grid(row=3, column=2)
        
#         self.canvas = Canvas(win, bg="grey70", width=300, height=200) 
#         self.canvas.pack() 
#         self.oval = self.canvas.create_oval(10, 10, 290, 190, fill="white", width=3) 
#         color = "#%02x%02x%02x"%(self.red, self.green, self.blue) 
#         self.canvas.itemconfig(self.oval, fill=color)
        
#     def updateRed(self, duty): 
#         self.red = int(duty) 
#         self.red_var.set(int(duty)) 
#         color = "#%02x%02x%02x"%(self.red, self.green, self.blue) 
#         self.canvas.itemconfig(self.oval, fill=color) 
#     def updateGreen(self, duty): 
#         self.green = int(duty) 
#         self.green_var.set(int(duty)) 
#         color = "#%02x%02x%02x"%(self.red, self.green, self.blue) 
#         self.canvas.itemconfig(self.oval, fill=color) 
#     def updateBlue(self, duty): 
#         self.blue = int(duty) 
#         self.blue_var.set(int(duty)) 
#         color = "#%02x%02x%02x"%(self.red, self.green, self.blue) 
#         self.canvas.itemconfig(self.oval, fill=color)

# if __name__ == "__main__":
#     window = Tk() 
#     window.geometry("400x400") 
#     window.wm_title('Color Selection Sliders') 
#     app = App(window) 
#     window.mainloop()




# # tkinter animation with bouncing ball (1)
# from tkinter import *

# def init():
#     global window, canvas, DX, DY
#     window = Tk()
#     window.title("tkinter animation - bouncing ball")
#     canvas = Canvas(window, width=300, height=200)
#     canvas.pack(expand=YES, fill=BOTH)
#     canvas.create_oval(0, 0, 50, 50, fill="red", tags="myBall")
#     DX = 1 # DX = 5
#     DY = 1 # DY = 5
# def animate():
#     global DX, DY
#     canvas.move("myBall", DX, DY) 
#     pos = canvas.coords("myBall")
#     print("coords of Ball : {}, {}, {}, {}".format(pos[0], pos[1], pos[2], pos[3]))
#     if pos[0] <= 0 :
#         print("bounced by left board ")
#         DX *= -1
#     if pos[2] >= canvas.winfo_width():
#         print("bounced by right board")
#         DX *= -1
#     if pos[1] <= 0 :
#         print("bounced by ceil board")
#         DY *= -1
#     if pos[3] >= canvas.winfo_height():
#         print("bounced by bottom board")
#         DY *= -1
#     canvas.update_idletasks()
#     canvas.update()
#     canvas.after(50, animate)

# if __name__ == '__main__':
#     init()
#     animate()
#     mainloop()




# tkinter animation of bouncing ball
# with direction change control by key input
import tkinter
from tkinter import *
from tkinter import messagebox

def ask_quit():
    result = messagebox.askquestion("Mesage", "Quit")
    if result == "yes":
        window.destroy()

def change_direction(event):
    global DX, DY
    if event.keysym == "Left":
        DX = -STEP; DY = 0
    elif event.keysym == "Right":
        DX = STEP; DY = 0
    elif event.keysym == "Up":
        DX = 0; DY = -STEP
    elif event.keysym == "Down": #if event.keysym == "Down":
        DX = 0; DY = STEP
    elif event.keysym == "Escape":
        DX = STEP; DY = STEP
    else:
        DX = STEP; DY = STEP

def init():
    global window, canvas, DX, DY, STEP
    window = Tk()
    window.title("Bouncing ball with direction change control by key input")
    canvas = Canvas(window, width=600, height=400)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_oval(300, 300, 400, 400, fill="red", tag="Ball")
    STEP = 1
    DX = STEP
    DY = STEP
    window.protocol("WM_DELETE_WINDOW", ask_quit)
    window.bind("<KeyPress-Left>", change_direction)
    window.bind("<KeyPress-Right>", change_direction)
    window.bind("<KeyPress-Up>", change_direction)
    window.bind("<KeyPress-Down>", change_direction)
    window.bind("<KeyPress-Escape>", change_direction)

def animate():
    global DX, DY
    Delay = 10 # in millisecond
    canvas.move("Ball", DX, DY) # move Ball in DX, DY from current position
    pos = canvas.coords("Ball")
    if pos[0] < 0 or pos[2] > canvas.winfo_width():
        DX *= -1
    if pos[1] < 0 or pos[3] > canvas.winfo_height():
        DY *= -1
    canvas.update_idletasks()
    canvas.update()
    canvas.after(Delay, animate)

if __name__ == '__main__':
    init()
    animate()
    mainloop()




