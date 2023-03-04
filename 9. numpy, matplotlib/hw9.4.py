# hw9.4.py
# matplotlib를 이용해 sine 파형 그리기
# Author: 박창협
# Programed on November. . 2021

import numpy as np
import matplotlib.pyplot as plt

def sine_graph(amp, freq, theta, pattern):
    x = np.linspace(-3.1, 3.1, num=41)  # 0~2pi를 41개로 나누도록 배열 생성
    sin_x = np.sin(freq * x + theta)  # sin파 생성
    plt.plot(x, sin_x, "k--", x, sin_x, pattern)
    xmin, xmax, ymin, ymax = x[0], x[-1], -amp, amp
    plt.axis([xmin, xmax, ymin, ymax])  # x, y축 범위
    

##### main #####
PI = np.pi
A, freq = 1, 2
theta = [0, PI/2, PI]
pattern = ["ro", "bo", "go"] 

sine_graph(A, freq, theta[0], pattern[0])
sine_graph(A, freq, theta[1], pattern[1])
sine_graph(A, freq, theta[2], pattern[2])

plt.xlabel("x")
plt.ylabel("sin(freq * x + theta)")
plt.title("Example of matplotlib - sin(freq * x + theta)")
plt.grid(True)
# plt.savefig("matplot_sin(freq*x+theta).png")
plt.show()
