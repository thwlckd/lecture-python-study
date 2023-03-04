# # hw9.5.py
# # matplotlib를 이용해 가우시안 PDF 그리기
# # Author: 박창협
# # Programed on November. 12. 2021

# import numpy as np
# import matplotlib.pyplot as plt

# def gauss(mu, sigma, x):
#     y = 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-((x - mu)**2)/(2*sigma**2))  # 가우시안 PDF
#     return y

# ##### main #####
# ##### graph1 #####
# mu = 0
# sigma = [0.5, 1, 2]
# color = ["red", "green", "blue"]
# label = ["sigma=0.5", "sigma=1", "sigma=2"]

# X = np.linspace(-8, 8, num=101)  # -8~8 구간을 100개로 나누는 배열 생성
# for i in range(3):  
#     Y = gauss(mu, sigma[i], X)  # Y = 가우시안 PDF
#     plt.plot(X, Y, color=color[i], label=label[i])

# plt.title("Normal Distribution Graph 1 - mu = 0.0, sigma = [0.5, 1, 2]")
# plt.legend(loc="best")
# plt.grid(True)
# # plt.savefig("Normal Distribution Graph 1 - mu = 0.0, sigma = [0.5, 1, 2]")
# plt.show()


# ##### graph2 #####
# mu = [-2, 0, 2]
# sigma = 1
# color = ["red", "green", "blue"]
# label = ["mu=-2.0", "mu=0.0", "mu=2.0"]

# X = np.linspace(-8, 8, num=101)  # -8~8 구간을 100개로 나누는 배열 생성
# for i in range(3):  
#     Y = gauss(mu[i], sigma, X)  # Y = 가우시안 PDF
#     plt.plot(X, Y, color=color[i], label=label[i])

# plt.title("Normal Distribution Graph 2 - mu = [-2.0, 0.0, 2.0], sigma = 1")
# plt.legend(loc="best")
# plt.grid(True)
# # plt.savefig("Normal Distribution Graph 2 - mu = [-2.0, 0.0, 2.0], sigma = 1")
# plt.show()



import numpy as np
import matplotlib.pyplot as plt

def gauss(mu, sigma, x):
    y = 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-((x - mu)**2)/(2*sigma**2))  # 가우시안 PDF
    return y

##### main #####
##### graph1 #####
mu = 19.16
sigma = 7.05
color = "red"
label = "sigma=7.05"

X = np.linspace(4, 33, num=30)  # -8~8 구간을 100개로 나누는 배열 생성
Y = gauss(mu, sigma, X)  # Y = 가우시안 PDF
plt.plot(X, Y, color=color, label=label)

plt.legend(loc="best")
plt.grid(True)
# plt.savefig("Normal Distribution Graph 1 - mu = 0.0, sigma = [0.5, 1, 2]")
plt.show()

