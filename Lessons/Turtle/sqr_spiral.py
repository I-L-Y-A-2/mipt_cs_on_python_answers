import turtle
from math import pi

turtle.shape('turtle')
f_rad = pi / 2
k = 5
f_deg = 90

for i in range(0, 500):
    r = k * f_rad 
    turtle.forward(r)
    turtle.left(f_deg)
    f_rad += 1