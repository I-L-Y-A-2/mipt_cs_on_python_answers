import turtle
import math

turtle.shape('turtle')
pi = math.pi
f = 0
k = 1

for i in range(0, 1000):
    r = k * f
    x = r * math.cos(f)
    y = r * math.sin(f)
    turtle.goto(x, y)
    f += 0.1