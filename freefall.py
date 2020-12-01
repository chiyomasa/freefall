#const

G = 9.80665

#main

t = 0.0
h = 0.01

#係数

v = float(input("input initial v0: "))
x = float(input("input initial x0: "))
print("{:.7f} {:.7f} {:.7f}".format(t, x, v))


#free fall

while x >= 0:
    t += h
    v += G * h
    x -= v * h
    print("{:.7f} {:.7f} {:.7f}".format(t, x, v))
