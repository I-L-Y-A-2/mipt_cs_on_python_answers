import turtle
from math import pi

turtle.shape('turtle')
f_rad = 0.1
k = 1 / (2 * pi)
f_deg = f_rad * 180 / pi

for i in range(0, 1000):
    r = k * f_rad
    turtle.forward(r)
    turtle.left(f_deg)
    f_rad += 0.1