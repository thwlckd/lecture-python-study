# # matplotlib(1) - linear
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(5)
# y = []
# for n in range(len(x)):
#     d = 2.0*x[n] + 1
#     y.append(d)

# plt.plot(x, y, "b-", x, y, "ro")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Example of matplotlib")
# plt.grid(True)
# plt.savefig("matplot_001.png")
# plt.show()



# # matplotlib(2) - squarer
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(start=-1, stop=1, num=51)
# y = x**2
# plt.plot(x, y, "b-", x, y, "ro")
# plt.axis([-1, 1, 0, 1])

# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Example of matplotlib - y = x**2")
# plt.grid(True)
# plt.savefig("matplot_002_square.png")
# plt.show()



# # matplotlib(3) - sin(x), cos(x)
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 2*np.pi, num=41)
# sin_x, cos_x = np.sin(x), np.cos(x)
# plt.plot(x, sin_x, "k--", x, sin_x, "ro")
# plt.plot(x, cos_x, "b-", x, cos_x, "b*")

# xmin, xmax, ymin, ymax = x[0], x[-1], -1, 1
# plt.axis([xmin, xmax, ymin, ymax])
# plt.xlabel("x")
# plt.ylabel("sin(x), cos(x)")
# plt.title("Example of matplotlib - sin(x), cos(x)")
# plt.grid(True)
# plt.savefig("matplot_003_sin_cos.png")
# plt.show()



# # matplotlib(4) - Normal, Gaussian Distribution
# import numpy as np
# import matplotlib.pyplot as plt

# def gauss(mu, sigma, x):
#     y = 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-((x - mu)**2)/(2*sigma**2))
#     return y

# mu, sigma = 0, 2
# x = np.linspace(-4*sigma, 4*sigma, num=101)
# y1 = gauss(mu, sigma, x)
# plt.plot(x, y1, color="red", label="sigma=2")

# mu, sigma = 0, 1
# y2 = gauss(mu, sigma, x)
# plt.plot(x, y2, color="green", label="sigma=1")

# mu, sigma = 0, 0.5
# y3 = gauss(mu, sigma, x)
# plt.plot(x, y3, color="blue", label="sigma=0.5")

# plt.title("Normal Distribution - sigma 0.5, 1, 2")

# plt.legend(loc="best")
# plt.grid(True)
# plt.savefig("matplot_004_GaussDist.png")
# plt.show()




# # matplotlib - 3D graphs
# import numpy as np
# import matplotlib.pyplot as plt 
# from matplotlib import cm 
# from mpl_toolkits.mplot3d import Axes3D 
# fig = plt.figure(figsize=(8, 8)) 
# fig.suptitle("$f(x,y) = x^2+y^2$", color='b',\
# fontsize=20)
# x = np.linspace(-5, 5, 7) 
# y = np.linspace(-5, 5, 7) 
# X, Y = np.meshgrid(x, y) 
# Z = X**2 + Y**2
# ax1 = fig.add_subplot(221, projection='3d') 
# surf = ax1.plot_wireframe(X, Y, Z) 
# ax1.set_title("wireframe")
# ax2 = fig.add_subplot(222, projection='3d') 
# surf = ax2.plot_surface(X, Y, Z, rstride=1,\
# cstride=1, cmap=cm.RdPu) 
# fig.colorbar(surf) 
# ax2.set_title("surface")
# ax3 = fig.add_subplot(223, projection='3d') 
# #surf = ax3.contour(X, Y, Z) 
# # # countour lines surf = ax3.contourf(X, Y, Z) 
# # #filled contours ax3.set_title("contour")
# ax4 = fig.add_subplot(224, projection='3d') 
# surf = ax4.scatter(X, Y, Z) 
# ax4.set_title("scatter")
# plt.grid(True) 
# plt.savefig("matplot_005_3D graphic.png",\
# bbox_inches='tight') 
# plt.show()



# # matplotlib ‐ 3D graphic
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# PI = np.pi
# x = np.arange(-2*PI, 2*PI, 0.25)
# y = np.arange(-2*PI, 2*PI, 0.25)
# X, Y = np.meshgrid(x, y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# print("X = \n", X)
# print("Y = \n", Y)
# print("Z = \n", Z)
# ax = fig.gca(projection = '3d')
# surf = ax.plot_surface(X, Y, Z, rstride=1,\
# cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# ax.set_zlim(-1.02, 1.02)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title("Z = np.sqrt(X**2 + Y**2)")
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig.colorbar(surf, shrink=0.5, aspect=5) 
# plt.show()



# Example animation with Matplotlib.animation
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 
xdata, y1data, y2data = [], [], [] 
ln_1, = plt.plot([], [], 'ro', label="sin(x)") 
ln_2, = plt.plot([], [], 'bd', label="cos(x)") 
plt.xlabel("x(radian)") 
plt.ylabel("sin(x), cos(x)") 
plt.grid(True) 
start, end = 0, 4*np.pi 
num_steps = 256 
plt.legend(loc="best")

def init(): 
    ax.set_xlim(start, end) 
    ax.set_ylim(-1.2, 1.2) 
    return ln_1, ln_2,

def update(xn): 
    xdata.append(xn) 
    y1data.append(np.sin(xn)) 
    y2data.append(np.cos(xn)) 
    ln_1.set_data(xdata, y1data) 
    ln_2.set_data(xdata, y2data) 
    return ln_1, ln_2, 

xn=np.linspace(start, end, num_steps) 
ani = FuncAnimation(fig, update, xn, init_func=init, blit=True) 
plt.show()






