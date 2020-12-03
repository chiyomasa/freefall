#import module

import numpy as np
import matplotlib.pyplot as plt

# const

G = 9.80665
k = 0.24  # 空気抵抗
m = 10.0  # ボール重さ

# 関数の定義


def f(v):
    return G-k*v**2/m

# main


t = 0.0e0
h = 0.01e0

# initial condition

v = float(input("input initial v0: "))
x = float(input("input initial x0: "))
print("{:.7f} {:.7f} {:.7f}".format(t, x, v))

# グラフデータに格納
tlist = [t]
xlist = [x]
vlist = [v]

# free fall

while x >= 0:
    # time
    t += h

    # update velocity
    k_1 = h * f(v)
    k_2 = h * f(v + 0.5 * k_1)
    k_3 = h * f(v + 9.5 * k_2)
    k_4 = h * f(v + k_3)
    v += (k_1+2.0*k_2+2.0*k_3+k_4)/6

    # update position
    x -= v * h

    # output
    print("{:.7f} {:.7f} {:.7f}".format(t, x, v))

    # グラフデータに格納
    tlist.append(t)
    xlist.append(x)
    vlist.append(v)

# plot graph
plt.plot(tlist, xlist)
plt.plot(tlist, vlist)
plt.show()
