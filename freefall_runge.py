#import module
import numpy as np
import matplotlib.pyplot as plt

# const

G = 9.80665

# main

t = 0.0
h = 0.01

# 係数

v = float(input("input initial v0: "))
x = float(input("input initial x0: "))
print("{:.7f} {:.7f} {:.7f}".format(t, x, v))

# put initial position into graph data
tlist = [t]
xlist = [x]


# free fall

while x >= 0:
    # time
    t += h

    # velocity
    l_1 = h * G
    l_2 = h * G
    l_3 = h * G
    l_4 = h * G
    v += l_1 / 6 + l_2 / 3 + l_3 / 3 + l_4 / 6

    # position
    k_1 = h * v
    k_2 = h * (v + l_1 / 2)
    k_3 = h * (v + l_2 / 2)
    k_4 = h * (v + l_3)
    x -= k_1 / 6 + k_2 / 3 + k_3 / 3 + k_4 / 6

    print("{:.7f} {:.7f} {:.7f}".format(t, x, v))
    # put position into graph data
    tlist.append(t)
    xlist.append(x)

# plot graph
plt.plot(tlist, xlist)
plt.show()
